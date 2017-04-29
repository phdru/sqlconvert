#! /usr/bin/env python

import os
import sys

for filename in sys.argv[1:]:
    os.unlink(filename)
