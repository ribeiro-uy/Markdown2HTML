#!/usr/bin/python3
"""Convert mardown file to html"""
from sys import argv, exit
import os.path
import re


def replaceHash(line):
    """ Parsing Headings Markdown syntax for generating HTML"""
    length = len(line)
    headings = line.lstrip('#')
    headingNum = length - len(headings)
    if 1 <= headingNum <= 6:
        line = '<h{}>'.format(headingNum) + \
            headings.strip() + '</h{}>\n'.format(headingNum)
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
                    line = replaceHash(line)
                    htmlFile.write(line)
