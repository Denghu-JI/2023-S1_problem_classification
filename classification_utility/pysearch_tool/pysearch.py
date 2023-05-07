# import git
#import subprocess
#(might delete if never used) import pathlib
import os


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

    def search(filename, keyword):
        with open(filename) as file:
            lines = file.readlines()

        results = []
        method = ""
        cofi = ""
        desc = ""

        for line in lines:
            if "Method :" in line:
                method = line.strip()
            elif "CoFI ->" in line:
                parts = line.strip().split(" -> ")
                cofi = {
                    "category": parts[1],
                    "subcategory": parts[2],
                    "library": parts[3],
                    "function": parts[4]
                }
            elif "description:" in line:
                desc = line.strip()

                if keyword.lower() in f"{method.lower()} {cofi.lower()} {desc.lower()}":
                    results.append((method, cofi, desc))

    

                

        for root, dirs, files in os.walk(self._app_path):
            if root == self._app_path:
                for dirr in dirs:
                    if dirr not in ignore:
                        app_path = self._app_path + '/' + dirr + '/' + dirr + '.py'
                        r = open(app_path)
                        if os.path.exists(app_path):
                            app_name = r.readline().strip('\n')[2:]
                            app_tree = r.readline().strip('\n')[2:].split(" -> ")
                            app_des = r.readline().strip('\n')[15:]
                            self._apps.append(App(app_name, app_path, app_tree, app_des))
                            print(app_tree)
            # print(self._apps)
            # print(self._apps)

        
        
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
            


    
