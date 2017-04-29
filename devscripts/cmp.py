#! /usr/bin/env python
"""cmp.py: compare two files. Portable replacement for cmp."""

import os
import sys

if sys.argv[1] in ("-h", "--help"):
    print("Broytman cmp.py 1.0, Copyright (C) 2003-2017 PhiloSoft Design")
    print("Usage: cmp.py [-h|--help|-V|--version] [-i] file1 file2")
    sys.exit()
elif sys.argv[1] in ("-V", "--version"):
    print("Broytman cmp.py 1.0, Copyright (C) 2003-2017 PhiloSoft Design")
    sys.exit()
elif sys.argv[1] == "-i":
    show_pbar = False
    fname1 = sys.argv[2]
    fname2 = sys.argv[3]
else:
    show_pbar = sys.stderr.isatty()
    fname1 = sys.argv[1]
    fname2 = sys.argv[2]

if show_pbar:
    try:
        from m_lib.pbar.tty_pbar import ttyProgressBar
    except ImportError:
        show_pbar = 0

if show_pbar:
    try:
        size = os.path.getsize(fname1)
    except:
        print(fname1, ": no such file")
        sys.exit(1)

if show_pbar:
    pbar = ttyProgressBar(0, size)

file1 = open(fname1, 'rb')
file2 = open(fname2, 'rb')

M = 1024*1024
diff = False
count = 0


def report():
    if show_pbar:
        global pbar
        del pbar
    sys.stderr.write("Files differ at %d megabayte block\n" % count)
    global diff
    diff = True


while True:
    block1 = file1.read(M)
    block2 = file2.read(M)

    if show_pbar:
        pbar.display(file1.tell())

    if block1 and block2:
        if len(block1) != len(block2):
            report()
            break
    elif block1:
        report()
        break
    elif block2:
        report()
        break
    else:
        break

    if block1 != block2:
        report()
        break

    count += 1

if show_pbar and not diff:
    del pbar

file1.close()
file2.close()

if diff:
    sys.exit(1)
