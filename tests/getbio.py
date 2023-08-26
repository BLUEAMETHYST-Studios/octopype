import octopype

github = octopype.OctoPype(open("tests/token.txt").read())

print(github.account.info().bio)