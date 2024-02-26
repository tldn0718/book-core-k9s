import os
import sys

my_ver = os.environ["MY_VER"]
arg = sys.argv[1]

print(f"Hello, {arg}, my version is {my_ver}")
