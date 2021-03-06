import subprocess
import re

    
def pip_installed_list():
    result =subprocess.run("pip list" ,stdout =subprocess.PIPE)
    file_pip_list=result.stdout.decode('utf-8')
    pip_list=[]
    result_list=re.findall(r"[\w\-]+",file_pip_list)
    for word in result_list:
        if not word.isnumeric():
            pip_list.append(word)
        else:
            continue
    pip_list=pip_list[4:]
    pip_list.remove("pip")
    pip_list.remove("setuptools")
    return pip_list
    
def pip_outdated_list():
    result =subprocess.run("pip list --outdated" ,stdout =subprocess.PIPE)
    file_pip_list=result.stdout.decode('utf-8')
    pip_list=[]
    result_list=re.findall(r"[\w\-]+",file_pip_list)
    for word in result_list:
        if not word.isnumeric():
            pip_list.append(word)
        else:
            continue
    pip_list=pip_list[8:]
    count=len(pip_list)
    for i in range(0,count//2):
        pip_list.remove('wheel')
    
    return pip_list
    
    
def uninstall_pip_module(pip_module_name):
    result=subprocess.run("pip uninstall "+pip_module_name+" -y")

    
def install_pip_module(pip_module_name):
    result=subprocess.run("pip install "+pip_module_name +" --user")
    

def update_pip_module(pip_module_name):
    result=subprocess.run("pip install --upgrade "+ pip_module_name)
    
def uninstall_pip_modules(pip_list):
    for module in pip_list:
        uninstall_pip_module(module)

def install_pip_modules(pip_list):
    for module in pip_list:
        install_pip_module(module)

def update_pip_modules(pip_list):
    for module in pip_list:
        update_pip_module(module)

