import datetime
import re
import os
import subprocess
import config
import markdown
import webbrowser
from xhtml2pdf import pisa

import markup_parser

def title_to_filename(title, ext):
    return title.lower().replace(" ", "_") + ext

def get_tmp_file(ext):
    return os.path.join("/", "tmp",  time_as_filename() + ext)

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

def html_to_pdf(html_path, pdf_path):
    html = ""
    with open(html_path, "r") as html_file:
        html = html_file.read()

    result_file = open(pdf_path, "w+b")

    pisa_status = pisa.CreatePDF(html, dest=result_file)
    result_file.close()

    if not pisa_status:
        print "Creation of PDF failed"


def compile_markdown_pdf(markdown_path, pdf_path):
    html_path = get_tmp_file(".html")
    compile_markdown_html(markdown_path, html_path)
    html_to_pdf(html_path, pdf_path)


def compile_markdown_html(markdown_path, html_path):
    print "Compiling markdown"
    markdown.markdownFromFile(input=markdown_path, output=html_path)


def postprocess(notename, html):
    p = markup_parser.parse(html)
    if "reminders" in p:
        reminders.save()


def view_file(filename):
    _, ext = os.path.splitext(filename)
    if ext == ".md":
        tmp_path = get_tmp_file(".html")
        compile_markdown_html(filename, tmp_path)
        filename = tmp_path
        print filename
        webbrowser.open(filename)


def edit(filename):
    subprocess.call([config.editor, filename])


