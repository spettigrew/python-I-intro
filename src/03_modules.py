"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.

Modules are a colleciton of code where you create different functions that are related. Library must be imported to use. Can import module so you can export the module in the function. ex: sys(system module) and os(operating systems module) 
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line: - gives an array of arguments that you can pass in the command line.
# YOUR CODE HERE
sys.argv[0]
print(sys.argv)

#for arg in sys.argv:
    #print(arg)

# Print out the OS platform you're using: 
# YOUR CODE HERE
#sys.platform
print(sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
#sys.version
print(sys.version)

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
#process_ID = os.getpid
print(os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
#cwd = os.getcwd
print(os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
#login = os.getlogin
print(os.getlogin())