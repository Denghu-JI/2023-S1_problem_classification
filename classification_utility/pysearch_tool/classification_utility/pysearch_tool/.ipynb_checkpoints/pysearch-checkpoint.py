<<<<<<< HEAD
#name
#cofi -> balabal -> foo -> bar
# sghdovhs;dugh
import git
import subprocess
import pathlib
import os


#please specify those folder!
methods_path = "cofi/src/cofi/tools"
applications_path = "espresso/contrib"
problems_path = "cofi-examples/examples"

ignore = ['slug_test', 'pumping_test', 'simple_regression', '']



=======
# import git
import subprocess
#(might delete if never used) import pathlib
import os


>>>>>>> 01438a23d38c7bd96f2a621bce9fd1b2f01f0c79
class pysearch:
    def __init__(self, methods_path, app_path,prob_path):
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
        self._methods = []
        self._apps = []

    def mds(self):
        return self._methods
    
    def aps(self):
        return self._apps

<<<<<<< HEAD
    def search(self):
        #inference methods in cofi
        for _, _, files in os.walk(self._method_path):
            for method in files[:-2]:
                r = open(self._method_path + '/' + method)
                #current plan, read the hierarchial information in the first line
                method_name = r.readline().strip('\n')[11:]
                method_path = self._method_path + '/' + method
                method_tree = r.readline().strip('\n')[2:].split(" -> ")
                des = r.readline().strip('\n')[2:]
                self._methods.append(Method(method_name, method_path, method_tree,des))
=======
    def search(self,ignore):
        #inference methods in cofi
        for _, _, files in os.walk(self._method_path):
            for method in files:
                is_next = True
                if method not in ignore:
                    r = open(self._method_path + '/' + method)
                    while is_next:
                        method_name = r.readline().strip('\n')
                        # print(method_name)
                        if method_name[:8] == "# Method":
                            method_name = method_name[11:]
                            method_path = self._method_path + '/' + method
                            method_tree = r.readline().strip('\n')[2:].split(" -> ")
                            des = r.readline().strip('\n')[2:]
                            self._methods.append(Method(method_name, method_path, method_tree,des))
                        else:
                            is_next = False
>>>>>>> 01438a23d38c7bd96f2a621bce9fd1b2f01f0c79
                

        for root, dirs, files in os.walk(self._app_path):
            if root == self._app_path:
                for dirr in dirs:
                    if dirr not in ignore:
<<<<<<< HEAD
                        app_path = self._app_path + '/' + dirr + '/' + dirr + '.py'
                        if os.path.exists(app_path):
                            r = open(app_path)
                            app_name = r.readline().strip('\n')[2:]
                            print(app_name)
                            app_tree = r.readline().strip('\n')[2:].split(" -> ")
                            app_des = r.readline().strip('\n')[15:]
                            print(app_des)
                            # self._apps.append(App(name,y,z,d))
=======
                        print(1)
                        app_path = self._app_path + '/' + dirr + '/' + dirr + '.py'
                        if os.path.exists(app_path):
                            app_name = r.readline().strip('\n')[2:]
                            app_tree = r.readline().strip('\n')[2:].split(" -> ")
                            app_des = r.readline().strip('\n')[15:]
                            self._apps.append(App(app_name,app_path,app_tree,app_des))
>>>>>>> 01438a23d38c7bd96f2a621bce9fd1b2f01f0c79
                            # self._apps.append({'name': app_name, 'path': app_path, 'description': app_des})

        # #applications in espresso
        # for root, dirs, files in os.walk(self._app_path):
        #     if root == self._app_path:
        #         for dir in dirs:
        #             #current plan: read the hierarchial info in a file
        #             r = open(self._app_path + '/' + dir + '/' + app_info_name)
        #             print(r.read())
        
        
class Method:
    def __init__(self, name, path, tree, des):
        """
        A single Method defination.

        Parameters
        -----------
        name : str
            method name
        path : str
            method file path
        tree : list
            tree path of the method
        """
        self._name = name
        self._path = path
        self._tree = tree
        self._des = des
    
    def name(self):
        return self._name
    
    def path(self):
        return self._path
    
    def tree(self):
        return self._tree
    
    def des(self):
        return self._des
    
class App:
    def __init__(self, name, path, tree, des):
        """
        A single Method defination.

        Parameters
        -----------
        name : str
            method name
        path : str
            method file path
        tree : list
            tree path of the method
        """
        self._name = name
        self._path = path
        self._tree = tree
        self._des = des
    
    def name(self):
        return self._name
    
    def path(self):
        return self._path
    
    def tree(self):
        return self._tree
    
    def des(self):
        return self._des
            
<<<<<<< HEAD
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
    
=======

>>>>>>> 01438a23d38c7bd96f2a621bce9fd1b2f01f0c79

    
