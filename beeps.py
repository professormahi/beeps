#! /usr/bin/python3
import argparse
import os

def play_music(beep):
   os.system('~/.config/beeps/%s.sh' % (beep)) 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run some musics using beep command.")
    parser.add_argument('music', help="Your lovely music")
    args = parser.parse_args()
    play_music(args.music)
