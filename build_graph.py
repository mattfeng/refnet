#!/usr/bin/env python

import json
import glob
import tempfile
import argparse

def main(*, out_file):

    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--output-file", default="graph.html")

    args = parser.parse_args()

    main(out_file=args.output_file)
