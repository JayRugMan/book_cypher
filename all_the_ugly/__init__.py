""" All of the ugly functions for book.py """


import base64
import sys
import argparse
import secrets
from os.path import exists


def get_generator_args(argv=None):
    '''Uses argparse to get input'''

    the_description='Generate a 10K file of random bits.'
    help_help = '''\
                 Simply supply an quoted string following the command,
                 which will act as a seed for generation. This seed can
                 then be used to generate the same file of random bits
                 using the same script on any other computer.

'''
    seed_help = '''\
                The seed is any string. This uses python's random seed, for
                which there is some uncertainty of the maximum value that
                can be entered. Note that extremely long values may or may
                not be useful, but are not necessary. 
'''

    parser = (argparse.ArgumentParser(
               prog='file_gen.py',
               formatter_class=lambda prog: argparse.RawDescriptionHelpFormatter(
               prog,indent_increment=2,max_help_position=41),
               add_help=False,
               description=the_description,
            )
             )
    parser.add_argument('-h', '--help',
                        action='help',
                        default=argparse.SUPPRESS,
                        help=help_help
                       )
    parser.add_argument('-s', '--seed',
                        required=True,
                        dest='the_seed',
                        type=str,
                        help=seed_help
                       )

    return vars(parser.parse_args(argv))


def get_args(argv=None):
    '''Uses argparse to get input'''

    the_description='Using a file as a "book," a message can ' \
        'be processed into a code or vise-versa.'
    help_help = '''\
                 You get this helpful message before exiting

'''
    book_help = '''\
                 This designates the file that acts as the "book" in the book
                 code by using its base64 encoding. It can be any type of
                 file - .html, .img, .jpg, .mp4, etc. Keep in mind if the
                 file is too small, the entropy will be small; if the file is
                 too big, the process time and performance may be impacted.

'''
    message_help='''\
                 This is the message string to be encoded. It can be a string
                 or a plain-text file. This cannot be used with -c/--code.

'''
    code_help='''\
                 The code goes here. This can also be a file containing the
                 code in plain text. This cannot be used with -m/--message.

'''
    the_epilog='''\

notes:
  Only the following special characters will work unless you add your own to the ursospecial.json file:
 . , ' ? + - = : ; ! @ # $ % ^ & * / ( ) [ ] { } _

  Some special characters will encode better if a message file is \
used instead of a string on the terminal

'''

    parser = (argparse.ArgumentParser(
               prog='book.py',
               formatter_class=lambda prog: argparse.RawDescriptionHelpFormatter(
               prog,indent_increment=2,max_help_position=41),
##JH               formatter_class=lambda prog: argparse.HelpFormatter(
##JH               prog,indent_increment=2,max_help_position=41),
##JH               formatter_class=lambda prog: argparse.RawTextHelpFormatter(
##JH               prog,indent_increment=2,max_help_position=41),
               add_help=False,
               description=the_description,
               epilog=the_epilog
            )
             )
    group = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument('-h', '--help',
                        action='help',
                        default=argparse.SUPPRESS,
                        help=help_help
                       )
    parser.add_argument('-b', '--book',
                        required=True,
                        dest='book_file',
                        type=str,
                        help=book_help
                       )
    group.add_argument('-m', '--message',
                        dest='the_message',
                        type=str,
                        help=message_help
                       )
    group.add_argument('-c', '--code',
                        dest='the_code',
                        type=str,
                        help=code_help
                       )

    return vars(parser.parse_args(argv))


def process_book(book):
    '''Processes the book file to return a list of lines in base64 charset
    with shifted indeces and a line count (hence the "insert")'''

    with open(book, 'rb') as the_book:
        book_lst = [
            i for i in base64.encodebytes(
                the_book.read()
            ).decode('utf-8').split('\n') if len(i) != 0
        ]

    # This makes line 1 move to line 2 to be index 1
    # for later. The string is arbitrary.
    book_lst.insert(0, 'These bits are the book')

    return book_lst


def process_txt_file(txt_file):
    '''turns file into a string for further processing'''

    ex_msg = "doesn't look like any text is in " + \
        txt_file + \
        ". Try one with ascii text next time."

    try:
        with open(txt_file, 'r') as file:
            file_lst = [i for i in file.read().split('\n') if len(i) != 0]
    except UnicodeDecodeError:
        # if this is a non-text file, like an image, etc
        print(ex_msg)
        sys.exit(1)

    return ' '.join(file_lst)


def enrich_message(message_object, specials):
    '''Refines the message to determine if it's a sting or file, then if
    it has any special characters, which are translated to special-character
    strings so the can be encoded with base64 characters'''

    # Returns true or false depending on whether the string provided is a
    # file. Even if the user is trying to specify a file, but does not exist,
    # it will treat it as a string. Harsh, I know.
    if exists(message_object):
        message_object = process_txt_file(message_object)

    enriched_message = ''

    for char in message_object:
        if char in specials.keys():
            enriched_message += specials[char]
        else:
            enriched_message += char

    return enriched_message


def encode_message(message, special_cs, book_f):
    '''takes the book and the message and works some maigic'''

    message_str = enrich_message(message, special_cs)
    book_list = process_book(book_f)
    numb_of_lines = len(book_list)
    code = ''

    for character in message_str:
        timeout = numb_of_lines
        while True:
            rand_line_num = secrets.randbelow(numb_of_lines)
            if character in book_list[rand_line_num] and rand_line_num != 0:
                line = ' {}'.format(book_list[rand_line_num])  # offset index
                idx = line.index(character)
                code += '{} {} '.format(rand_line_num, idx)
                break
            if timeout == 0:  ## breaks infinite loop cause by bad character
                error_out = 'Looks like {} is an invalid character'
                print(error_out.format(character))
                sys.exit(1)
            timeout -= 1

    return code[:-1]  # because the last char is a space


def interpret_specials(message, specials):
    '''takes special characters and raw message to translate, returning them
    to normal for the final string'''

    for new, old in specials.items():
        if old in message:
            message = message.replace(old, new)

    return message


def de_the_code(code_object, book_f, special_cs):
    '''Takes numbers and book, then returns what it all means'''

    # Returns true or false depending on whether the string provided is a
    # file. If the user is trying to specify a file, but does not exist,
    # it will treat it as a string and return nothing. Harsh, I know.
    if exists(code_object):
        code_object = process_txt_file(code_object)

    try:
        int(code_object.split(' ')[0]) + int(code_object.split(' ')[1])
    except ValueError:
        print('ERROR: provided code is invalid')
        sys.exit(1)
    except IndexError:
        print('ERROR: character index needed')
        sys.exit(1)

    book_list = process_book(book_f)
    raw_message = ''
    line_num = None
    char_num = None

    # This loop stores number pairs from a string-turned-to-list to then
    # store corresponding line and character from the book
    for item in code_object.split(' '):
        if not line_num:
            line_num = item
        else:
            char_num = item
        if line_num and char_num:
            try:
                line = ' {}'.format(book_list[ int(line_num) ])  # offset index
                raw_message += line[ int(char_num) ]
            except IndexError:
                print('ERROR: Wacky Numbers!?!')
                sys.exit(1)
            except ValueError:
                print('ERROR: Are those numbers!?!')
                sys.exit(1)
            line_num = None
            char_num = None

    return interpret_specials(raw_message, special_cs)