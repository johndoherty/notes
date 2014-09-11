import os
import sys
from optparse import OptionParser
from subprocess import call


def new_note(sys_args):
    #parser = OptionParser()
    #(options, args) = parser.parse_args(args=sys_args)

    EDITOR = os.environ.get('EDITOR','vim') #that easy!

    initial_message = "" # if you want to set up the file somehow
    file_name = "test.txt"

    with open(file_name, 'w') as note_file:
        note_file.write(initial_message)

    call([EDITOR, file_name])

FUNCTION_DICT = {
    'new': new_note,
}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in FUNCTION_DICT:
        print "Available options are:"
        for key in FUNCTION_DICT.keys():
            print "  " + key
    else:
        new_args = [sys.argv[0] + " " + sys.argv[1],] + sys.argv[2:]
        FUNCTION_DICT[sys.argv[1]](new_args)
