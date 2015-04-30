"""
Some of the structure here is borrowed from the vatic video annotation tool:
https://github.com/cvondrick/vatic
"""

import os
import sys
import reminders
import argparse

import notes


handlers = {}


def handler(help = "", inname = None):
    """
    Decorator bind a function as a handler for a cli command.

    help    specifies the help message to display
    inname  specifies the name of the handler, otherwise infer
    """
    def decorator(func):
        if inname is None:
            name = func.__name__.replace("_", "-")
        else:
            name = inname
        handlers[name.lower()] = func, help
        return func
    return decorator


def main(args = None):
    if args is None:
        args = sys.argv[1:]

    if len(args) == 0 or args[0] not in handlers:
        help()
    else:
        handler = handlers[args[0]][0]
        handler(args[1:])


@handler(help = "display this message")
def help(args = None):
    """
    Print the help information.
    """
    for action, (_, help) in sorted(handlers.items()):
        print "{0:>15}   {1:<50}".format(action, help)


@handler(help = "display sample note text")
def sample(args = None):
    """
    Print a sample note for reference.
    """
    with open("sample.md", "r") as sample_note:
        print sample_note.readlines()


@handler(help = "view an existing note")
def view(args = None):
    """
    View a note in the browser.
    """
    parser = argparse.ArgumentParser(description='Create a new note')
    parser.add_argument('filename', help='filename to view')
    args = parser.parse_args(args)
    notes.view_file(args.filename)


@handler(help = "create a new note")
def new(args = None):
    """
    Create a new note.
    """
    parser = argparse.ArgumentParser(description='Create a new note')
    parser.add_argument('--title', help='title for the new note')
    parser.add_argument('--no-edit', action='store_true', help='optional filename for the new note')
    parser.add_argument('--no-view', action='store_true', help='optional filename for the new note')
    args = parser.parse_args(args)

    title = args.title
    if not title:
        title = notes.time_as_filename()

    filename = notes.title_to_filename(title, ".md")
    with open(filename, "w") as new_file:
        new_file.write(notes.get_header(title))

    print "Created new note with name: {0}".format(filename)

    if not args.no_edit:
        notes.edit(filename)

    if not args.no_view:
        notes.view_file(filename)


if __name__ == "__main__":
    main()
