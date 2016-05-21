#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# myke mk-xx-proj-struct.py 2016-05-21 0.1
# discover structure of the project and draw diagram
# testign all .sh, .py files

import os

outfile = "mk-xx-proj-struct1.txt"

fout = 0
lof = 0

def init():
    """ init io """
    global fout, lof

    fout = open (outfile, "w", encoding="utf8")

    print ("digraf G {", file=fout)

    lof = [x.name for x in os.scandir(".")]
    #~ print (lof)


def makesh():
    """ make .sh files """
    for f in lof:
        if f.endswith(".sh"):
            procsh(f)


def procsh(f):
    """ process 1 .sh file"""
    with open(f) as fin:
        for l in fin:
            pass


def makepy():
    """ make .py files """
    for f in lof:
        if f.endswith(".py"):
            procpy(f)


def procpy(f):
    """ process 1 .py file"""
    with open(f) as fin:
        for l in fin:
            names = getfilenames(l, ".py")
            if "infile" in l:
                for name in names:
                    print ('"{}" -> "{}";' .format (name, f), file=fout)
            if "outfile" in l:
                for name in names:
                    print ('"{}" -> "{}";' .format (f, name), file=fout)


def getfilenames (nomo, ext):
    """ find filenames of type ext in string nomo and give list of them"""
    lout = []
    if ext ne "" and not ext in nomo:
        return lout   # nothign to search, exit

    # re in nomo for filename... ext


def finish():
    """ close all """
    print ("\n}\n", file=fout)
    fout.close()


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
