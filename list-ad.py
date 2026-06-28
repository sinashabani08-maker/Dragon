#_coded 2t

#_modluse
import os
import sys
import time

#_script
op = input('ENTER NAME ABZAR?')
if op in ['hydra']:
	print("""
	 _____________
	/    KING     \\
	|   Hacker    |
	|    Hydra    |
	\_____________/	
	""")
	os.system('git clone https://github.com/vanhauser-thc/thc-hydra.git')
	os.system('cd thc-hydra')
	os.system('pkg install make')
	os.system('./configure')
	time.sleep(15)
	os.system('make')
	time.sleep(10)
	os.system('make install')
	os.system(10)
	os.system('hydra')
	sys.exit()

