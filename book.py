#!/usr/bin/env python3
'''This script does stuff'''

import sys
from all_the_ugly import get_args
from all_the_ugly import encode_message
from all_the_ugly import de_the_code
from all_the_ugly import json_to_dict as sc  # Special chars imported here


def main():
    '''The Main Event'''

    options = None

    args = get_args(options)

    if args['the_message']:
        special_characters = sc.load_special_chars()
        final_answer = encode_message(args['the_message'],
                                      special_characters,
                                      args['book_file']
                                     )
    elif args['the_code']:
        special_characters = sc.load_special_chars(is_legacy=args['is_legacy'])
        final_message = de_the_code(args['the_code'],
                                    args['book_file'],
                                    special_characters,
                                    is_legacy=args['is_legacy']
                                   )
        final_answer = '{}'.format(final_message)
    else:
        final_answer = 'Oopsy... how did this happen?'

    print(final_answer)


if __name__ == "__main__":
    sys.exit(main())
