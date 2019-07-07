#This code is required to use ease_import

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from misc.ease_import import *

sys.path.insert(0, currentdir)

import_file("pairs")
