#!/usr/bin/env python

import os
import languageparts
import re
from random import randint

def get_token(word):
    return re.match("(%[a-zA-Z ]*%)", word, re.I)

def build_lib(lib):
    new_lib = []
    words = lib.strip('\n').split(" ")
    for word in words:
        new_word = None
        match_obj = get_token(word)
        if match_obj:
            token = match_obj.group(1)
            new_word = word.replace(token, languageparts.get_word_part(token.replace('%', '')))
        else:
            new_word = word
        new_lib.append(new_word)
    return " ".join(new_lib).strip()

def get_random_lib():
    libs = []
    with open("libs.txt") as f:
        libs = [ l for l in f.readlines() if l.strip() ]
    return libs[randint(0, len(libs)-1)] 

def main():
    os.system('clear')
    lib = get_random_lib()
    new_lib = build_lib(lib)
    print "original:", lib.strip()
    print "mad libs:", new_lib.strip()

if __name__ == "__main__":
    main()
