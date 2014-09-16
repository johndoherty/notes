import datetime
import os
import os.path
import re
import shutil
import sys
import yaml
from optparse import OptionParser
from subprocess import call


DEFAULT_NOTE_PATH = ".default_note.txt"
DEFAULT_NOTE_TEXT = """TITLE
#TAGS, ...


todos:
- Write todos here
"""

def edit_file(file_path):
    EDITOR = os.environ.get('EDITOR','vim')
    call([EDITOR, file_path])

def new_note(sys_args, config_dict):
    if len(sys_args) != 2:
        print "Incorrect usage"
        return
 
    category = sys_args[1]
    if not os.path.isdir(category):
        print "creating directory for {0}".format(category)
        os.mkdir(category)

    now = datetime.datetime.now()
    file_name = now.replace(microsecond=0).isoformat() + ".txt"
    file_name = re.sub(":", ".", file_name)
    file_path = os.path.join(category, file_name)
 
    if not os.path.isfile(DEFAULT_NOTE_PATH):
        with open(DEFAULT_NOTE_PATH, "w") as default_note:
            default_note.write(DEFAULT_NOTE_TEXT)

    shutil.copy(DEFAULT_NOTE_PATH, file_path)
    edit_file(file_path)

def find_note(sys_args):
    # find by note text
    # find notes within date range
    # find notes by tags
    return

FUNCTION_DICT = {
    'new': new_note,
    'find': find_note,
    #'random': random,
}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in FUNCTION_DICT:
        print "Available options are:"
        for key in FUNCTION_DICT.keys():
            print "  " + key
    else:
        with open("config.yaml", "r") as config_file:
            config_dict = yaml.load(config_file)

        note_dir = os.path.expanduser(config_dict['directory'])

        with open(".storage.yaml", "r") as storage:
            storage_dict = yaml.load(storage)

        if storage_dict.get('first_time', False):
            # First time using note 
            edit_file("config.yaml")
            storage_dict['first_time'] = True
            with open(".storage.yaml", "w") as storage:
                storage.write(yaml.dump(storage_dict))

        os.chdir(note_dir)
        FUNCTION_DICT[sys.argv[1]](sys.argv[1:], config_dict)

