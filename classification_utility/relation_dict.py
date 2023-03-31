# An example labelling for CoFI methods

#     cofi_simple_newton <- simple Newton step <- InLab <- non-linear <- optimization <- parameter estimation <- CoFI



# An example labelling for Espresso problems

#     magnetotelluric_1D <- magnetotelluric <- 370602 Electrical and electromanetic methods in geophysics <- 3706 Geophysics <- 37 Earth Sciences



# An example labelling for CoFI examples: pygimli_dcip_century_tri_mesh.ipynb

#     Application domain: pygimli_dcip_century_tri_mesh.ipynb <- DCIP <- 370602 Electrical and electromanetic methods in geophysics <- 3706 Geophysics <- 37 Earth Sciences
#     Methods domain: pygimli_dcip_century_tri_mesh.ipynb <- Newton conjugate gradient trust-region algorithm (trust-ncg) <- scipy.optimize.minimize <- non-linear <- optimization <- parameter estimation <- CoFI



# Another example labelling for CoFI examples

#     Application domain: pygimli_dcip.ipynb <- DCIP <- 370602 Electrical and electromanetic methods in geophysics <- 3706 Geophysics <- 37 Earth Sciences
#     Methods domain:
#         pygimli_dcip.ipynb <- Newton conjugate gradient trust-region algorithm (trust-ncg) <- scipy.optimize.minimize <- non-linear <- optimization <- parameter estimation <- CoFI
#         pygimli_dcip.ipynb <- RAdam <- torch.optim <- non-linear <- optimization <- parameter estimation <- CoFI

tokens = {} #key: token id


class hirc_tree:
    def __init__(self, me):
        """
        relationship tree for as parsing result

        Parameters
        ----------------
        me : str
            current leaf name
       
        child : [hirc_tree]
            current leaf's children
        """
        self._me = me
        self._children = []
        self._parent = None
        self._path = None
        self._description = None

    def me(self):
        return self._me
    
    def children(self):
        return self._children
    
    def parent(self):
        return self._parent
    
    def add_child(self, node):
        self._children.append(node)

    def add_parent(self, node):
        self._parent = node
    
    def add_description(self, des):
        self._description = des
    
    def add_path(self, path):
        self._path = path
    
    def description(self):
        return self._description
    
    def path(self):
        return self._path

def insert(tre, method):
        lst = method.tree()
        if len(lst)!= 1:
            token = lst.pop(0)
            if token == tre.me():
                flag = False
                child = lst[0]
                for tok in tre.children():
                    if child == tok.me():
                        insert(tok, method)
                        flag = True
                if not flag:
                    node = hirc_tree(child)
                    node.add_parent(token)
                    insert(node, method)
                    tre.add_child(node)
        else:
            tre.add_description(method.des())
            tre.add_path(method.path())
            
        return tre



#----------------------test

# tokens1 = ['cofi_simple_newton', 'simple Newton step', 'InLab', 'non-linear', 'optimization', 'parameter estimation', 'CoFI']
# tokens2 = ['pygimli_dcip_century_tri_mesh.ipynb', 'Newton conjugate gradient trust-region algorithm (trust-ncg)', 'scipy.optimize.minimize',  'non-linear', 'optimization', 'parameter estimation', 'CoFI']

# tre = hirc_tree('CoFI', [])

# t = insert(tre, tokens1[::-1])
# t1 = insert(t, tokens1[::-1])


# print(t1.children()[0].children()[0].me())