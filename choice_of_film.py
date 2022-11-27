#!/usr/bin/env python3
import glob
import os
import random
import subprocess
import sys

def choice_of_film():    
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
    folders = {'en': 'Video',
        'uk': 'Відео',
        'ru': 'Видео'}
    folder = folders[os.getenv("LANG")[:2]]
    path = f'{os.getenv("HOME")}/{folder}/' if not args else args[-1]
    film = random.choice(glob.glob(path + '*.*'))
    if not opts:
        print (film.strip(path))
    elif '-v' in opts:
        with subprocess.Popen(['vlc', film], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT):
            pass
    else:
        raise SystemExit(f"Usage: {sys.argv[0]} -v for open to vlc")


if __name__ == '__main__':
    choice_of_film()