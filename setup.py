from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup (
    options = {'py2exe': {
	    'bundle_files': 1,
		'optimize': 2,
		'includes': ['Tkinter'],
		'compressed': True,
	}},
	zipfile = None,
	windows = ["pyserial_tester.py"]
)