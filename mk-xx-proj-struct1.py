#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# myke mk-xx-proj-struct1.py 2016-05-21 1.2
# discover structure of the project and draw diagram
# testign all .sh, .py files

import os, re

outfile = "mk-xx-proj-struct1.gv"

fout = 0
lof = 0

ext_run = "py pl par sh csh zsh p".split()
ext_inf = "txt log jpg png gv ini gif mp3 mp4 sql html htm".split()

color_run = "green"
color_inf = "yellow"

all_run = set()
all_inf = set()

def init():
    """ init io """
    global fout, lof
    print ("init")

    fout = open (outfile, "w", encoding="utf8")

    print ("digraph G {\n", file=fout)

    lof = [x.name for x in os.scandir(".")]
    print (lof)


def makesh():
    """ make .sh files """
    pass
    #~ for f in lof:
        #~ if f.endswith(".sh"):
            #~ procsh(f)


def procsh(f):
    """ process 1 .sh file"""
    pass
    #~ print (f)
    #~ with open(f) as fin:
        #~ for l in fin:
            #~ pass


def makepy():
    """ make .py files """
    for f in lof:
        if f.endswith(".py"):
            procpy(f)


def procpy(f):
    """ process 1 .py file"""
    global all_inf, all_run
    print (f)
    all_run |= {f}
    with open(f) as fin:
        for l in fin:
            names = getfilenames (l)
            if names:
                print ("names:", names)
            if "infile" in l:
                print ("infile")
                for name in names:
                    print ('"{}" -> "{}";' .format (name, f), file=fout)
                    all_inf |= {name}
            if "outfile" in l:
                print ("outfile")
                for name in names:
                    print ('"{}" -> "{}";' .format (f, name), file=fout)
                    all_inf |= {name}


def getfilenames (nomo, ext=""):
    """ find filenames of type ext in string nomo and give list of them"""

    res = re.findall (r"([-_a-zA-Z0-9\.]+\.[a-zA-Z0-9]+)", nomo)
    if ext != "":
        res = [x for x in res if ext in x and x != ext and x in lof]
    else:
        res = [x for x in res if x in lof]
    return res


def finish():
    """ close all """

    print ("all_run = ", all_run)
    print ("all_inf = ", all_inf)
    for f in all_run:
        print ('"{}" [style=filled color={}]' .format(f, color_run), file=fout)
    for f in all_inf:
        print ('"{}" [style=filled color={}]' .format(f, color_inf), file=fout)

    print ("\n}\n", file=fout)
    fout.close()
    print ("finish")


def main(args):
    """ main dispatcher """
    init()
    #~ makesh()
    makepy()
    finish()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
