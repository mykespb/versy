#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# myke mk-xx-proj-struct.py 2016-05-21 0.1
# discover structure of the project and draw diagram
# testign all .sh, .py files

import os

outfile = "mk-xx-proj-struct1.txt"
logfile = "mk-xx-proj-struct1.log"

fout = 0
flog = 0
lof = 0

def init():
    """ init io """
    global fout, flog, lof

    fout = open (outfile, "w", encoding="utf8")
    flog = open (logfile, "w", encoding="utf8")

    print ("started init", file=flog)
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
    print (f, file=flog)
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
    print (f, file=flog)
    with open(f) as fin:
        for l in fin:
            if "infile" in l:
                names = getfilenames(l, ".py")
                for name in names:
                    print ('"{}" -> "{}";' .format (name, f))
            if "outfile" in l:
                names = getfilenames(l, ".py")
                for name in names:
                    print ('"{}" -> "{}";' .format (f, name))


def getfilenames (nomo, ext):
    """ find filenames of type ext in string nomo and give list of them"""
    lout = []
    if ext ne "" and not ext in nomo:
        return lout   # nothign to search, exit

    # re in nomo for filename... ext


def finish():
    """ close all """
    print ("\n}\n", file=fout)
    print ("finished.", file=flog)
    fout.close()
    flog.close()


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
