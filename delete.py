from touchbar_lyric.utility import get_info
import os,os.path
from pathlib import Path

media_info = get_info("Spotify")
file_name = media_info.name + " - " + media_info.artists
file_name = file_name.replace("  "," ")
dir = os.path.join(os.path.join(os.path.dirname(__file__),"local/final"),file_name+".txt")
if(Path(dir).exists()):
    os.remove(dir)
    print(str(file_name)+" removed from final")
else:
    print(str(file_name)+" does not exist")
dir = os.path.join(os.path.join(os.path.dirname(__file__),"local/src"),file_name+".lrcx")
if(Path(dir).exists()):
    os.remove(dir)
    print(str(file_name)+"removed from src")
else:
    print(str(file_name)+" does not exist")