#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import subprocess


def parse_args():
    # TODO: add usage
    if len(sys.argv) != 3:
        raise Exception("Bad arguments")
    return sys.argv[1], sys.argv[2]


def compile_jsx(file):
    return subprocess.check_output(["jsx", file])


def walk(dir):
    # TODO: check if dir exists
    jsx_bundle = ""
    for d, dirs, files in os.walk(dir):
        for f in files:
            name, ext = os.path.splitext(f)
            if ext.lower() == ".jsx":
                jsx_bundle += compile_jsx(d + "/" + f)
                jsx_bundle += "\n;\n"
    return jsx_bundle


def write_bundles(jsx_bundle, bundle_file):
    # TODO: check that bundle is not empty
    with open(bundle_file, "w") as f:
        f.write(jsx_bundle)


if __name__ == "__main__":
    project_dir, bundle_file = parse_args()
    jsx_bundle = walk(project_dir)
    write_bundles(jsx_bundle, bundle_file)
    
