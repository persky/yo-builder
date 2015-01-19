#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import subprocess


def parse_args():
    # TODO: add usage, add normal parsing
    if len(sys.argv) != 3:
        raise Exception("Bad arguments")
    return sys.argv[1], sys.argv[2]


def compile_jsx(file):
    return subprocess.check_output(["jsx", file])

def walk(dir):
    # TODO: check if dir exists
    jsx_bundle = ""
    css_bundle = ""
    for d, dirs, files in os.walk(dir):
        for f in files:
            name, ext = os.path.splitext(f)
            fullpath = d + "/" + f
            if ext.lower() == ".jsx":
                print "jsx>", fullpath
                jsx_bundle += compile_jsx(fullpath)
                jsx_bundle += "\n;\n"
            elif ext.lower() == ".css":
                print "css>", fullpath
                css_bundle += open(fullpath, "r").read()
                css_bundle += "\n;\n"
    return jsx_bundle, css_bundle


def write_file(bundle, filename):
    # TODO: check that bundle is not empty
    with open(filename, "w") as f:
        f.write(bundle)


if __name__ == "__main__":
    project_dir, bundle_target_dir = parse_args()
    jsx_bundle, css_bundle = walk(project_dir)
    write_file(jsx_bundle, bundle_target_dir + "/bundle.js")
    write_file(css_bundle, bundle_target_dir + "/bundle.css")
