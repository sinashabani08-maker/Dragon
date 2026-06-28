#coded 9t 《■》KINGHacker《■》

#modluse
import os 
import sys
import subprocess
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#_color 
red  = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
belu = '\033[1;34m'
reset = '\033[0m'

#_banner

subprocess.run(["python", "bannerD.py"])

#_script
nyt = f"""{yellow}
  
   ______________({green}KINGHacker{red}@root{yellow})
  /
  \____/\-》{reset}"""
get = input(f"{nyt}")
if get in ['dragon -in -p -sa']:
	subprocess.run(["python", "list.py"])
	
if get in ['dragon -in -p -ab']:
	subprocess.run(["python", "list-ab.py"])
	
else:
	print(f"""{red}
  _
 / \\
/ ! \  not{reset} dastor{red}
*****{reset}""")
time.sleep(3)
subprocess.run(["python", "Dragon.py"])