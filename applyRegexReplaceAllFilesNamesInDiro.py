from os import *
from os.path import *
import sys
import re

VERBOSE = False

def verbose(msg):
    if(VERBOSE):
        print(msg)

i = 0
# argument control related variable
DIRO_PROVIDED = False
SEARCH_REPLACE_NOREGEX = False
REGEX_PROVIDED = False
REPLACE_PROVIDED = False
FILES_ONLY = False

# the variable we will work with
diroPath = None
searchKeyword = None
replaceKeyword = None
regex = None


for arg in sys.argv :
    if arg == "-f":
        DIRO_PROVIDED = True
        diroPath = sys.argv[i+1]
    elif arg == "-s" : # searchKeyWord
        SEARCH_REPLACE_NOREGEX = True
        searchKeyword = sys.argv[i+1]
    elif arg == "-r":
        replaceKeyword = sys.argv[i+1]
        REPLACE_PROVIDED = True
    elif arg == "-x" or  arg == "--regx":
        REGEX_PROVIDED = True
        regex = sys.argv[i + 1]
    elif arg == "-v" :
        VERBOSE = True
    elif arg == "-fo" or arg == "--fileOnly" :
        FILES_ONLY = True
    i+=1

if(not DIRO_PROVIDED) :
    diroPath = getcwd()
elif(not isdir(diroPath)) :
    diroPath = input("the diro you entred doesn't exist! so please reenter a diro here >")
    while  not isdir(diroPath):
        diroPath = input("the diro you entred doesn't exist! so please reenter a diro here >")

if REGEX_PROVIDED: 
    if SEARCH_REPLACE_NOREGEX:
        print("you choosed both regex and simple matching search which one do you want :")
        print("enter 'r' =for> regex")
        print("and 's' =for> simple search")
        answer = input()
        while(answer != 'r' and answer != 's' ) :
            print("wrong value, enter 'r' =for> regex |or|  's' =for> simple search:")
            answer = input() 
        if(answer =='r'):
            SEARCH_REPLACE_NOREGEX = False
        else :
            REGEX_PROVIDED = False
elif not SEARCH_REPLACE_NOREGEX:
    method = input("you didn't provide any methode of search, input r =for> by regex match, or s =for> for simple matching")
    while(method != 'r' and method != 's' ) :
            print("wrong value, enter 'r' =for> regex |or|  's' =for> simple search:")
            method = input() 
    if(method == 'r'):
        REGEX_PROVIDED = True
        regex = input("enter your regex pattern here put it between \"\":")
    else:
        SEARCH_REPLACE_NOREGEX = True
        searchKeyword = input("enter your search matching synthese:")


if(not REPLACE_PROVIDED):
    replaceKeyword = input("please Enter the replacement synthese:") 

if(REGEX_PROVIDED and not SEARCH_REPLACE_NOREGEX):
    currentWorkingDiro = getcwd();
    chdir(diroPath)
    verbose("diroPath chdir to : "+getcwd())
    for num, filename in enumerate(listdir(getcwd()),start = 1):
        if(not isfile(filename) and FILES_ONLY):
            continue
        verbose(str(num)+"- fileName : "+filename)
        newFileName = re.sub(regex,replaceKeyword,filename)
        verbose("regex applied, and replacement:")
        verbose("newFileName=> "+newFileName)
        verbose("renaming!")
        rename(filename,newFileName)
        verbose("renameDone")
        if(VERBOSE):
            verbose("here the tree of the diro")
            for fname in listdir(getcwd()):
                verbose("--- "+fname)
                verbose("|")
        verbose("")

else:
    currentWorkingDiro = getcwd()
    chdir(diroPath)
    verbose("diroPath chdir to : " + getcwd())
    for num, filename in enumerate(listdir(getcwd()), start=1):
        if(not isfile(filename) and FILES_ONLY):
            continue
        verbose(str(num) + "- fileName : " + filename)
        newFileName = filename.replace(searchKeyword,replaceKeyword)
        verbose("regex applied, and replacement:")
        verbose("newFileName=> " + newFileName)
        verbose("renaming!")
        rename(filename, newFileName)
        verbose("renameDone")
        if(VERBOSE):
            verbose("here the tree of the diro")
            for fname in listdir(getcwd()):
                verbose("--- " + fname)
                verbose("|")
        verbose("")

verbose("regex = "+ str(regex))
verbose('searchKey = '+str(searchKeyword))
verbose("replaceKey = "+str(replaceKeyword))
verbose("pathEntred = "+str(diroPath))


