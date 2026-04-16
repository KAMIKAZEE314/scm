#!/usr/bin/env python3
import os
import sys
import pathlib as pth

def main():
	if len(sys.argv) < 2:
		print("Usage: scm [action] [arguments]")
		sys.exit()
	else:
		action = sys.argv[1]

	if action == "init":
		pth.Path(".scm").mkdir()
	elif action == "add":
		pass

if __name__ == "__main__":
	main()
