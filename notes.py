from optparse import OptionParser
import sys

def new_note(sys_args, name):
    parser = OptionParser()
    parser.add_option("-")
    (options, args) = parser.parse_args(args=sys_args)
    
    # Create note in notes directory
    # Open up default editor





