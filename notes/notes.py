import datetime
import re
import os
import subprocess
import config
import markdown
import webbrowser

import markup_parser

def title_to_filename(title, ext):
    return title.replace(" ", "_") + ext

def get_header(title):
    header = config.header.strip()
    header = header.replace("%d", datetime.datetime.now().strftime(config.dateformat))
    header = header.replace("%a", config.author)
    header = header.replace("%t", title)
    header += "\n\n"
    return header

def time_as_filename():
    now = datetime.datetime.now()
    filename = now.replace(microsecond=0).isoformat()
    return re.sub(":", ".", filename)


def compile_markdown(markdown_path, html_path):
    markdown.markdownFromFile(input=markdown_path, output=html_path)
    return "Compiled markdown"


def postprocess(notename, html):
    p = parse(html)
    if "reminders" in p:
        reminders.save()


def view_file(filename):
    _, ext = os.path.splitext(filename)
    if ext == ".md":
        tmp_path = os.path.join("/", "tmp", time_as_filename() + ".html")
        compile_markdown(filename, tmp_path)
        filename = tmp_path
        webbrowser.open(filename, new=1)


def edit(filename):
    subprocess.call([config.editor, filename])


