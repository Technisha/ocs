from os import system, path, walk

for base, _, files in walk("."):
    if ".git" not in base:
        for file in files:
            system(f"git add '{path.join(base, file)}'")

system("git commit -am 'autocommit';git push")