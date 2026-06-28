#_coded 7t

#_modluse
import os

#_color 
red  = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
belu = '\033[1;34m'
reset = '\033[0m'

list = 'libsearpc','v2ray','vulkan-loader-             generic','vulkan-loader','vulkan-tools','vulkan-utility-libraries','vulkan-validation-layers','vulkan-volk','w3m-img','w3m','wakatime-cli','wine-stable','woff2','wren','wuzz','wxwidgets','x11-repo','xorg-xcursorgen','xorg-xdpyinfo','xorg-xev','xorg-xhost','xorg-xkbcomp','xorg-xlsfonts','xorg-xmessage','xorg-xprop','xorg-xrandr','xorg-xsetroot','xorg-xwininfo','xorgproto','xorriso','xournalpp','xpdf','xrdp-static','xrdp','xsel','xsettingsd','xsltproc','xtrans','xvidcore-static','xvidcore','xvkbd','xwallpaper','xwayland','xxd','xxhash-static','xxhash','xz-utils','yad','yadm','yajl-static','yajl','yara-static','yara','yarn','yasm-static','yasm','yazi','yoga','yosys','youtubedr','yq','yt-dlp-ejs','ytfzf','ytui-music','yuma123-static','yuma123','z-push','z3','zbar-static','zbar','zeal','zellij','zen-browser','zeronet','zig','zile','zip','zipios','zk','zlib-static','zlib','zls','znc','zola','zopfli','zoxide','zpaq','zrok','zsh-completions','zsh','zssh','zstd','zsync','zziplib','zzuf-static','zzuf'

def user():
  print("""
  pkg zk ---》False
  zk -------》True
  
  """)
  op = input(f"""{green}
  ____________({red}name {yellow}PKG{green})
 /
 \______/-----》{reset}""")
  if op in list:
  		os.system(f"pkg install {op}")
  else:
  	print(f"""{red}
  _
 / \\
/ ! \  not{reset} pkg in list{red}
*****
  	{reset}	""")
user()