try:
  from cx_Freeze import *
  from tkinter import *
  import sys
  import requests
except Exception as e:
  print('Modules are Missing! \n\n {}'.format(e))

base = None
if sys.platform == 'win32':
  base = 'Win32GUI'