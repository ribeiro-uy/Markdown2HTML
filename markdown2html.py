#!/usr/bin/python3
"""Convert mardown file to html"""
from sys import argv, exit
import os.path
import re


def createHeading(line):
    """ Parsing Headings Markdown syntax for generating HTML"""
    length = len(line)
    headings = line.lstrip('#')
    headingNum = length - len(headings)
    if 1 <= headingNum <= 6:
        line = '<h{}>'.format(headingNum) + \
            headings.strip() + '</h{}>\n'.format(headingNum)
    return line


def createUl(line):
    """ Parsing Unordered listing syntax for generating HTML """
    ul = line.lstrip('-')
    ulNum = length - len(ul)


def boldface(line):
    """ Bold text """
    bold = '**'
    index = 1
    while(bold in line):
        if index % 2 == 0:
            line = line.replace(bold, '</b>', 1)
        else:
            line = line.replace(bold, '<b>', 1)
        index = index + 1
    return line


def emphasis(line):
    """ Emphasis text """
    emphasis = '__'
    index = 1
    while(emphasis in line):
        if index % 2 == 0:
            line = line.replace(emphasis, '</em>', 1)
        else:
            line = line.replace(emphasis, '<em>', 1)
        index = index + 1
    return line


if __name__ == "__main__":
    if len(argv) < 3:
        exit("Usage: ./markdown2html.py README.md README.html")

    if not os.path.isfile(argv[1]):
        exit('Missing {}'.format(argv[1]))

    with open(argv[1]) as mdFile:
        with open(argv[2], 'w') as htmlFile:
            for line in mdFile:
                if '#' in line:
                    line = createHeading(line)
                    htmlFile.write(line)
                if '-' in line:
                    line = createUl(line)
                    htmlFile.write(line)
                if '**' in line and line.count("**") % 2 == 0:
                    line = boldface(line)
                    htmlFile.write(line)
                if '__' in line and line.count("__") % 2 == 0:
                    line = emphasis(line)
                    htmlFile.write(line)
