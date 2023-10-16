#!/usr/bin/env python3

import os

curr_dir = os.path.dirname(__file__)
xkb = "/usr/share/X11/xkb"


def brackets(text):
    res = 0
    slash = 0
    for i in text:
        if i == "/":
            slash += 1
            if slash == 2:
                break
            continue
        if i == "{":
            res += 1
        if i == "}":
            res -= 1
        slash = 0
    return res


def bracket_end(code, pos):
    indent = 0
    while indent := indent + brackets(code[pos]):
        pos += 1
    return pos + 1


with open(f"{xkb}/rules/evdev.extras.xml", "r") as f:
    evdev = f.read().split("\n")
with open(f"{curr_dir}/patches/evdev", "r") as f:
    evdev_patch = f.read().split("\n")
with open(f"{xkb}/symbols/de", "r") as f:
    de = f.read().split("\n")
with open(f"{curr_dir}/patches/de_neo_base") as f:
    de_neo_base_patch = f.read().split("\n")
with open(f"{curr_dir}/patches/de_koy") as f:
    de_koy_patch = f.read().split("\n")
with open(f"{xkb}/symbols/level3", "r") as f:
    level3 = f.read()
with open(f"{curr_dir}/patches/level3") as f:
    level3_patch = f.read().split("\n")

if "vou" not in "\n".join(evdev):
    koy = [i for i in range(len(evdev)) if "koy" in evdev[i]][0] - 2
    vou = koy + 6
    evdev = evdev[:vou] + evdev_patch + evdev[vou:]
    with open(f"{xkb}/rules/evdev.extras.xml", "w") as f:
        f.write("\n".join(evdev))

if "vou" not in "\n".join(de):
    neo_base = ([i for i in range(len(de)) if "\"neo_base\"" in de[i]][0], -1)
    neo_base = (neo_base[0] - 1, bracket_end(de, neo_base[0]))
    de = de[:neo_base[0]] + de_neo_base_patch + de[neo_base[1]:]
    koy = ([i for i in range(len(de)) if "\"koy\"" in de[i]][0], -1)
    koy = (koy[0] - 1, bracket_end(de, koy[0]))
    de = de[:koy[1]] + de_koy_patch + de[koy[1]:]
    with open(f"{xkb}/symbols/de_neo_base", "w") as f:
        f.write("\n".join(de))

if "quote_switch" not in "\n".join(level3):
    level3 = level3.split("\n")
    bksl_switch = ([i for i in range(len(level3)) if "\"bksl_switch\"" in level3[i]][0], -1)
    bksl_switch = (bksl_switch[0] - 1, bracket_end(level3, bksl_switch[0]))
    level3 = level3[:bksl_switch[1]] + level3_patch + level3[bksl_switch[1]:]
    with open(f"{xkb}/symbols/level3", "w") as f:
        f.write("\n".join(level3))
