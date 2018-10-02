from time import sleep
#from aiy.voicehat import *
import subprocess

def main():
    subprocess.Popen(["vlc", "radiostream.pls"], shell = True)
    
if (__name__ == '__main__'):
    main()