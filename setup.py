from cx_Freeze import setup,Executable
import sys
import os

import cx_Freeze 

if sys.platform == 'win32':
    base = 'Win32GUI'

os.environ[''] = r''
os.environ[''] = r''

executables = [cx_Freeze("login.py",base=base, icon="logo_castillo_grande.ico")]


# cx_Freeze.setup(
#     name ='Software Topicos de Operaciones',
#     options  = 
# )





