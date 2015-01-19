#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_dir", help="The dir to walk and look for files to bundle")
    parser.add_argument("-ojs", help="Resulting js/jsx bundle filename")
    parser.add_argument("-ocss", help="Resulting css bundle filename")
    args = parser.parse_args()

    js_bundle = args.ojs or args.source_dir + "/bundle.js"
    css_bundle = args.ocss

    return args.source_dir, js_bundle, css_bundle


def compile_jsx(file):
    return subprocess.check_output(["jsx", file])


def walk(dir, parse_css):
    # TODO: check if dir exists
    js_bundle = ""
    css_bundle = ""
    for d, dirs, files in os.walk(dir):
        for f in files:
            name, ext = os.path.splitext(f)
            fullpath = d + "/" + f
            if ext.lower() == ".jsx":
                print "jsx>", fullpath
                js_bundle += compile_jsx(fullpath)
                js_bundle += "\n;\n"
            elif ext.lower() == ".js":
                print "js>", fullpath
                js_bundle += open(fullpath, "r").read()
                js_bundle += "\n;\n"
            elif parse_css and ext.lower() == ".css":
                print "css>", fullpath
                css_bundle += open(fullpath, "r").read()
                css_bundle += "\n;\n"
    return js_bundle, css_bundle


def write_file(bundle, filename):
    with open(filename, "w") as f:
        f.write(bundle)


if __name__ == "__main__":
    source_dir, js_bundle_name, css_bundle_name = parse_args()
    parse_css = bool(css_bundle_name)
    js_bundle, css_bundle = walk(source_dir, parse_css)
    write_file(js_bundle, js_bundle_name)
    if parse_css:
        write_file(css_bundle, css_bundle_name)

