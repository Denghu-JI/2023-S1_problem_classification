#pysearch Python 3.10
import git
import subprocess
import pathlib
import os


#please specify cofi methods folder!
methods_path = "cofi/src/cofi/tools"
applications_path = "espresso/contrib"
problems_path = "cofi-examples/..."

app_info_name = 'README.md'


class pysearch:
    def __init__(self, method_path, app_path,prob_path):
        """
        search earch repository in given path, extract the
        first line.

        Parameters
        ----------------
        method_path : str
            the folder that contains inference methods in CoFI
        app_path : str
            the folder that contains applications in espresso
        prob_path : str
            the folder that contains example problems in CoFI
            examples
        """
        self._method_path = methods_path
        self._app_path = app_path
        self._prob_path = prob_path

    def search(self):
        print('loading methods!')
        #inference methods in cofi
        for _, _, files in os.walk(self._method_path):
            for method in files[:-2]:
                r = open(methods_path + '/' + method)
                #current plan, read the hierarchial information in the first line
                print(method)
                print(r.readline().strip('\n'))

        #applications in espresso
        for root, dirs, files in os.walk(self._app_path):
            if root == self._app_path:
                for dir in dirs:
                    #current plan: read the hierarchial info in a file
                    r = open(self._app_path + '/' + dir + '/' + app_info_name)
                    print(r.read())
        
        

            



# #----git sync-------------------------
# # path : current path 
# # git_path : root project git path
# path = pathlib.Path().resolve()
# git_path = '/'.join(str(path).split('/')[:-2])
# repo = git.Repo(git_path)
# for submodule in repo.submodules:
#     submodule.update(init=True)
#---------------------------------------

#path to methods. applications and problems
methods_prefix = methods_path
#ToDO: create other two prefix

# for _, _, files in os.walk(methods_path):
#     for method in files[:-2]:
#         r = open(methods_path + '/' + method)
#         print(method)
#         print(r.readline().strip('\n'))
#         print("this is it!")

p = pysearch(methods_path,applications_path,problems_path)
p.search()
    

    
