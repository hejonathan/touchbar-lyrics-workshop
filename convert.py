import os, os.path
from posixpath import split

def new_name(old_name):
    name = old_name[:-5]
    name += ".txt"
    return name

def create(SOURCE_DIR,FINAL_DIR,file,debug=False):
    old_path = os.path.join(SOURCE_DIR,file)
    old = open(old_path,"r")
    new_path = os.path.join(FINAL_DIR,new_name(file))
    new = open(new_path,"w")
    lines = old.readlines()
    for line in lines:
        if any(ele in line for ele in skipwords):
            continue
        if(len(line)> 9+1 and line[9]=='0'):
            line = line[0 : 9 : ] + line[9 + 1 : :]
        new.write(line)
        if("[al:" in line):
            new.write("[by:]\n")
    if(debug):
        print(new_name(file)+" successful")

def run():
    SOURCE_DIR = os.path.join(os.path.dirname(__file__),'local/src')
    source_files = [name for name in os.listdir(SOURCE_DIR) if os.path.isfile(os.path.join(SOURCE_DIR, name))]
    FINAL_DIR = os.path.join(os.path.dirname(__file__),'local/final')
    final_files = [name for name in os.listdir(FINAL_DIR) if os.path.isfile(os.path.join(FINAL_DIR, name))]

    for file in source_files:
        if(not final_files.__contains__(new_name(file))):
            create(SOURCE_DIR,FINAL_DIR,file,True)

skipwords = ["[tr:","[length:","词","曲"]
