#/usr/bin/env python3
import argparse
import os

parser = argparse.ArgumentParser(description="scm")
parser.add_argument("action", type=str, help="Die Aktion von scm")

args = parser.parse_args()

if args.action == "init":
	os.system("mkdir .scm")
