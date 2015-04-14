from setuptools import setup
from setuptools import Extension

setup(
    name = "notes",
    author = "John Doherty",
    author_email = "doherty1@stanford.edu",
    description = "A simple note taking framework",
    version = "0.1",
    packages = ["notes"],
    scripts = ['scripts/notes'],
    package_dir = {"notes": "notes"},
    install_requires = ["setuptools"]
)
