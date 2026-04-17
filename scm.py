#!/usr/bin/env python3
import os
import sys
import pathlib as pth

def search_directory(path):
	return [p for p in path.iterdir()]

def main():
	if len(sys.argv) < 2:
		print("Usage: scm [action] [arguments]")
		sys.exit()
	else:
		action = sys.argv[1]

	if action == "init":
		pth.Path(".scm").mkdir()
	elif action == "add":
		if len(sys.argv) < 3:
			print("Usage: scm add [file | Directory]")
			sys.exit()
		else:
			path = pth.Path(sys.argv[2])
			
			# .scmignore lesen
			try:
				with open(".scmignore") as file:
					ignores = file.readlines() + [".scm"]
			except FileNotFoundError:
				ignores = [".scm"]
			
			recheck = True
			while recheck:
				recheck = False
				content = search_directory(path)
				for p in content:
					for ignore in ignores:
						if p.match(ignore):
							del p
							break

					if any(p is x for x in content):
						if p.is_dir():
							content.insert(search_path(path / p)

if __name__ == "__main__":
	main()
