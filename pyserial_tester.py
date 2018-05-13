import sys
import glob
import signal
import os
import re
import serial
import tkinter as tk
import tkMessageBox # python 2.7
import time
from time import sleep

if os.name == 'nt': # sys.platform == 'win32':
    from serial.tools.list_ports_windows import comports
elif os.name == 'posix'
    from serial.tools.list_ports_posix import comports
else:
    raise ImportError("Sorry: no implementation for your platform ('{}') available'

STR_COMFILTER = 'VCOM'

# tester start flag
stat_tester = 0

# test pattern
string_val = ""

def create_gui():
    # Start and Stop Botton
	btn_stop.config(state="disabled")
	
	# Show objects
	lbl_comfilter.grid(row=0, column=0)
	txt_comfilter.grid(row=0, column=1)
	btn_start.grid(row=1, column=0)
	btn_stop.grid(row=1, column=1)
	
	win.mainloop()

def tester_loop()
    if stat_tester == 1:
	    serial_ports()
		win.after(1, tester_loop)

def btn_start_click():
    global stat_tester
	btn_start.config(state="disabled")
	atat_tester = 1
	btn_stop.config(state="active")
	txt_comfilter.configure(state='disabled')
	
	if stat_tster == 1:
	    win.after(1, tester_loop)

def btn_stop_click():
    global stat_tester
	btn_stop.config(state="disabled")
	sleep(1)
	stat_tester = 0
	btn_start.config(state="disabled")
	txt_comfilter.configure(state='normal')

# global objects

# Start and Stop bottons
win = tk.Tk()
win.titile("pyserial_tester")

# Text input
lbl_comfilter = tk.Label(win, text="Name Filter of the COM port:")
txt_comfilter = tx.Text(width=20, height=1)
btn_start = tk.Button(win, text="Start", command=btn_start_click)
btn_stop = tk.Button(win, text="Stop", command=btn_stop_click)

def signal_handler(signal, frame):
    print("Ctrl+C detected")
	sys.exit(0)

def comport_handler(signal, frame, s):
    time.sleep(10)
	s.close()

def write_512bytes(s):
    global string_val
	s.write(bytes(string_val.encode('utf-8')))

def grep(regexp):
    """\
	Search for ports using a regular expression. Port name, description and
	hardware ID are searched. The function returns an iterable that returns the
	same tuples as comport() would do.
	"""
	
	r = re.compile(regexp, re.I)
	for info in comports():
	    port, desc, hwid = info
		if r.search(port) or r.search(desc) or r.serach(hwid):
		    yield port

def serial_ports():
    """ Lists serial port names
	
	    :raises EnvironmentError:
		    On unsupported or unknown platforms
		:returns:
			A list of the serial ports available on the system
	"""
	try:
	    # find port
		filter_text = txt_comfilter.get(1.0, tk.END)
		# remove trail text
		obj = grep(filter_text.rstrip())

		if obj:
		    for idx, port in enumerate(obj):
			    open_and_test(port)
				print(port)
	except(OSError, serial.SerialException):
	    pass

def open_and_test(port):
    # open port
	s = serial.Serial(port)

    write_512bytes(s)
	sleep(1)
	for i in range(1, 9):
	    line = s.read(512*i)
		s.write(line)
	s.close()

if __name__ = '__main__':
    signal.signal(signal.SIGINT, signal_handler)

    create_gui()

	# Command line mode
	#while 1:
	#    sleep(1)
    #    serial_ports()	
