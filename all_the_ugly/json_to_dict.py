# Categories
'''
This will turn the comma-separated lists in "THE_FILE" into a dictionary
where the first item is the key while the other items become a list as the
value

The json file needs to be in the same directory as the main script that 
references this script
'''

import sys
import json
import os

# For testing (everything with ##JH)
##JH json_file_name  = 'ursospecial.json'
##JH path_2_script = os.path.abspath(sys.argv[0])
##JH path = os.path.dirname(path_2_script)
##JH THE_FILE = path + '/' + json_file_name
##JH output = '''
##JH script: {}
##JH Path to script: {}
##JH Just the path: {}
##JH Path to json file: {}
##JH '''
##JH print(output.format(sys.argv[0], path_2_script ,path, THE_FILE))

try:
    with open(THE_FILE, 'r') as json_file:
        special_chars = json.load(json_file)
except FileNotFoundError:
    exit_msg = '{} not found. Please refer to the README'
    sys.exit(exit_msg.format(THE_FILE))