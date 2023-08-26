import octopype
import sys

github = octopype.OctoPype(sys.argv[1])

print(github.account.info().bio)