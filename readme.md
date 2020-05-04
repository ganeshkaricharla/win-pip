#WIN-PIP

A Python to automate the work of "PIP" command in command line interface through Python Programmes for WINDOWS PYTHON INTERPRETER USERS

#USAGE

There are many functions that you can use to manage the pip module commands all at once

1)pip_installed_list()

it is a function that gets the list of all installed pip_modules except "pip" and "setuptools"
it returns the data to a list data structure
it won't take any Parameters

2)pip_outdated_list()

it is a function that gets the list of all OUTDATED Packages that are installed  except "pip"
it returns the data to a list data struucture
it won't take any Parameters

3)install_pip_module()
This function lets you install one pip module at once,only one parameter is allowed 
parameters :: module Name
parameter_type ::string

4)install_pip_modules()
This function lets you install one or more modules at a time ,only one parameter is allowed
parameters :: a list contains all the names of pacakages
parameter_type ::list

5)uninstall_pip_module()
This function lets you uninstall one pip module at once,only one parameter is allowed 
parameters :: module Name
parameter_type ::string

6)uninstall_pip_modules()
This function lets you uninstall one or more modules at a time ,only one parameter is allowed
parameters :: a list contains all the names of pacakages
parameter_type ::list

7)update_pip_module()
This function lets you update one pip module at once,only one parameter is allowed 
parameters :: module Name
parameter_type ::string

8)update_pip_modules()
This function lets you update one or more modules at a time ,only one parameter is allowed
parameters :: a list contains all the names of pacakages
parameter_type ::list
