#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# myke mk-xx-proj-struct1.py 2016-05-21 1.1
# discover structure of the project and draw diagram
# testign all .sh, .py files

import os, re

outfile = "mk-xx-proj-struct1.gv"

fout = 0
lof = 0

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
    print (f)
    with open(f) as fin:
        for l in fin:
            names = getfilenames (l)
            if names:
                print ("names:", names)
            if "infile" in l:
                print ("infile")
                for name in names:
                    print ('"{}" -> "{}";' .format (name, f), file=fout)
            if "outfile" in l:
                print ("outfile")
                for name in names:
                    print ('"{}" -> "{}";' .format (f, name), file=fout)


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
