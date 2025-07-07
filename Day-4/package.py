# packages is a list of packages that are used in the project.
# URL: pypi.org
# pip is a package manager for Python packages.
# pip install package_name is used to install a package from PyPI.
# print("Welcome to the Package Example!")

# install pip command
# pip install package_name

import cowsay
import sys

if len(sys.argv) == 3:
    # cowsay.cow("Hello "+ sys.argv[1] +" "+sys.argv[2])
    cowsay.trex("Hello " + sys.argv[1] + " " + sys.argv[2])


