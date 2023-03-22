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
    def __init__(self, me, children):
        """
        relationship tree for as parsing result

        Parameters
        ----------------
        me : str
            current leaf name
        parent : [hirc_tree]
            current leaf's parent
        child : [hirc_tree]
            current leaf's children
        """
        self._me = me
        self._children = children

    def me(self):
        return self._me
    
    def children(self):
        return self._children
    
    def add_child(self, node):
        self._children.append(node)

def insert(tre, lst):
        if len(lst)!= 1:
            token = lst.pop(0)
            if token == tre.me():
                print(1)
                flag = False
                child = lst[0]
                for token in tre.children():
                    if child == token.me():
                        insert(token, lst)
                        flag = True
                if not flag:
                    node = hirc_tree(child, [])
                    insert(node, lst)
                    tre.add_child(node)
        return tre

def create_monk(tokens1,tokens2):
    id = 0
    for token in tokens2 + tokens1:
        if token not in tokens.values():
            tokens[id] = token
            id += 1
    print(tokens)
tokens1 = ['cofi_simple_newton', 'simple Newton step', 'InLab', 'non-linear', 'optimization', 'parameter estimation', 'CoFI']
tokens2 = ['pygimli_dcip_century_tri_mesh.ipynb', 'Newton conjugate gradient trust-region algorithm (trust-ncg)', 'scipy.optimize.minimize',  'non-linear', 'optimization', 'parameter estimation', 'CoFI']
create_monk(tokens1,tokens2)


tre = hirc_tree('CoFI', [])

t = insert(tre, tokens1[::-1])
print(t.children()[0].children()[0].me())