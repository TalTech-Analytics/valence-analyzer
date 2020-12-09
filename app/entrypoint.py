# -*- coding: utf-8 -*-
from __future__ import print_function
import glob
import os
import json
from valence.valencecolor import *


def process_input():
    for filename in glob.iglob("/analyzer/valence-input/" + '**/*.json', recursive=True):
        with open(filename, encoding="utf-8") as json_input:
            print("processing input:", filename)
            data = json.load(json_input)

            try:
                for message in data["messages"]:
                    message["valence"] = getValence(message["content"])
            except Exception:
                print("Failed processing file. Copying initial file")

            write_output(data, filename)


def write_output(data, filename):
    out_file = filename.replace("/analyzer/valence-input", "/analyzer/valence-output")
    try:
        os.remove(out_file)
        print("Deleting file with same name")
    except Exception:
        print("No file with same name exists")
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    print("writing output:", out_file)
    with open(out_file, "w", encoding="utf-8") as json_output:
        json.dump(data, json_output)


def getValence(text):
    """Standalone"""
    load()
    t = mark(text)
    return emotionBayes(t[3], t[1], t[2])


if __name__ == '__main__':
    process_input()
