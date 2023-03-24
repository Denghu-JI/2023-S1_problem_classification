from relation_dict import hirc_tree, insert
from tqdm import tqdm

def main():
    print("Now you are on example testing")
    print("-----the first example------Method")
    print("tokens1 = ['cofi_simple_newton', 'simple Newton step', 'InLab', 'non-linear', 'optimization', 'parameter estimation', 'CoFI']")
    print("-----the second example------Application")
    print("tokens2 = ['pygimli_dcip_century_tri_mesh.ipynb', 'Newton conjugate gradient trust-region algorithm (trust-ncg)', 'scipy.optimize.minimize',  'non-linear', 'optimization', 'parameter estimation', 'CoFI']")
    print("Loading the tree!")
    #---------------------------------
    tre = hirc_tree('CoFI', [])
    atre = hirc_tree('37 Earth Sciences', [])

    with tqdm(total=50) as pbar:
        #Method1
        tokens1 = ['Method: cofi_simple_newton', 'simple Newton step', 'InLab', 'non-linear', 'optimization', 'parameter estimation', 'CoFI']
        pbar.update(10)
        #Method2
        tokens2 = ['Application: pygimli_dcip_century_tri_mesh.ipynb', 'Newton conjugate gradient trust-region algorithm (trust-ncg)', 'scipy.optimize.minimize',  'non-linear', 'optimization', 'parameter estimation', 'CoFI']
        pbar.update(10)

        pbar.update(10)
        tre = insert(tre, tokens1[::-1])
        pbar.update(10)
        tre = insert(tre, tokens2[::-1])
        pbar.update(10)

        tokens3 = ["pygimli_dcip_century_tri_mesh.ipynb, DCIP, 370602 Electrical and electromanetic methods in geophysics, 3706 Geophysics, 37 Earth Sciences"]
        atre = atre.insert(atre.token3[::-1])

    cmd = " "
    current_node = tre
    last_node = []

    while cmd != 'exit':
        cmd = input('Whats next?: ')
        if cmd == 'children?':
            if len(current_node.children()) == 0:
                print("you have reached a terminal")
            for i in current_node.children():
                print(i.me())
        elif cmd[:2] == 'go':
            flag = False
            for i in current_node.children():
                if i.me() == cmd [3:]:
                    last_node.append(current_node)
                    current_node = i
                    print("now you are on " + i.me() + ", its children are: ", end = '')
                    for j in i.children():
                        print(j.me() + " | ", end = '')
                    print(" ")
                    flag = True
            if not flag:
                print("no such child!")
        elif cmd == "reset":
            current_node = tre
        elif cmd == "back":
            if len(last_node) == 0:
                print("cannot go back")
            else:
                current_node = last_node.pop()
        else:
            print("not a vaild command")

        
            


if __name__ == "__main__": 
    main()
