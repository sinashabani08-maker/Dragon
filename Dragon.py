#_coded 697892T 《■》KINGHacker《■》

#_modluse
import os
import sys
import time
import subprocess

#_color
red  = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
belu = '\033[1;34m'
reset = '\033[0m'

#_banner
os.system('chmod +x Dragon.py')
os.system("python bannerD.py")

#_menu
text = f"""{green}

[!]S T A R T M E N U_ _ _ _

{reset} """
word = text.split()

for words in word:

    print(words, end=" ", flush=True)
    time.sleep(0.090)
time.sleep(1)
subprocess.run(["python", "menu.py"])

print(" ")
#_script
nyt = f"""{yellow}
  
   ______________({green}KINGHacker{red}@root{yellow})
  /
  \____/\-》{reset}"""
User = input(f"{nyt}")
  
if User in['1', '01']:
  print(f"""
 
   """, f"{green}__________/S T A R T ", f"{red}@","r","o","o","t",f" {green}+ D R A G O N A I ________",f"""
  {reset}
  """)
  subprocess.run(["python", "DRAGON AI.py"])
	
if User in ['2', '02']:
	po = f"""
	
	""",f"{belu}_______","T"," H ","A ","N","K","S","Y","O","U","______","                            "f"{red}________","Teame"," K"," I"," N ","G ","H"," a ","c"," k ","e ","r"," _____","     "f"{yellow}_______","Loading ","A"," N ","D"," move ","in"," T ","E"," R","M","U","X",f"___{reset}"
	
	
	for tor in po:
		print(tor, end=" ", flush=True)
		time.sleep(0.090)
	
	sys.exit()