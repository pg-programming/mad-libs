#!/usr/bin/env python

import os
import languageparts as lp
import re
from random import choice


def build_lib(lib):
    new_lib = []
    for w in lib.strip('\n').split(" "):
        match_obj = re.match("(%[a-zA-Z ]*%)", w, re.I)
        if match_obj:
            token = match_obj.group(1)
            w = w.replace(token, lp.get_word_part(token.replace('%', '')))
        new_lib.append(w)
    return " ".join(new_lib).strip()


def get_random_lib():
    with open("libs.txt") as f:
        return choice([l for l in f.readlines() if l.strip()])


if __name__ == "__main__":
    os.system('clear')
    lib = get_random_lib()
    new_lib = build_lib(lib)
    print("original:", lib.strip())
    print("mad libs:", new_lib.strip())
