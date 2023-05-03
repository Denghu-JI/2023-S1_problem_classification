from relation_dict import hirc_tree, insert, assign_depth, build_pos, assign_coordinates,dict_package
from pysearch_tool import pysearch
import json
import boto3

#please specify those folder!
methods_path = "pysearch_tool/cofi/src/cofi/tools"
applications_path = "pysearch_tool/espresso/contrib"
problems_path = "pysearch_tool/cofi-examples/examples"
ignore_list = ['__init__.py', '_base_inference_tool.py']

ignore = []





def main():
    p = pysearch.pysearch(methods_path,applications_path,problems_path)
    p.search(ignore)
    method_tree = hirc_tree('CoFI')
    apps_tree = hirc_tree('37 Earth Sciences')

    for i in p.mds():
        method_tree = insert(method_tree,i)
    
    for i in p.aps():
        print(i)
        apps_tree = insert(apps_tree,i)

    cmd = " "
    current_node = apps_tree
    last_node = []

    cmd = " "
    current_node = apps_tree
    last_node = []

    # while cmd != 'exit':
    #     cmd = input('Whats next?: ')
    #     if cmd == 'children?':
    #         if len(current_node.children()) == 0:
    #             print("you have reached a terminal")
    #         for i in current_node.children():
    #             print(i.me())
    #     elif cmd[:2] == 'go':
    #         flag = False
    #         for i in current_node.children():
    #             if i.me() == cmd [3:]:
    #                 last_node.append(current_node)
    #                 current_node = i
    #                 print("now you are on " + i.me() + ", its children are: ", end = '')
    #                 for j in i.children():
    #                     print(j.me() + " | ", end = '')
    #                 print(" ")
    #                 flag = True
    #         if not flag:
    #             print("no such child!")
    #     elif cmd == "reset":
    #         current_node = apps_tree
    #     elif cmd == "back":
    #         if len(last_node) == 0:
    #             print("cannot go back")
    #         else:
    #             current_node = last_node.pop()
    #     elif cmd == "path":
    #         print(current_node.path())
    #     elif cmd == "des":
    #         print(current_node.description())
    #     elif cmd == "me":
    #         print(current_node.me())
    #     elif cmd == "pt":
    #         print(current_node.parent())
    #     else:
    #         print("not a vaild command")

if __name__ == "__main__": 
    main()
    p = pysearch.pysearch(methods_path,applications_path,problems_path)
    p.search(ignore)
    method_tree = hirc_tree('CoFI')
    apps_tree = hirc_tree('37 Earth Sciences')

    for i in p.mds():
        method_tree = insert(method_tree,i)
    
    for i in p.aps():
        apps_tree = insert(apps_tree,i)
    
    assign_coordinates(apps_tree)
    assign_coordinates(method_tree)
    method_dt = dict_package(method_tree)
    app_dt = dict_package(apps_tree)



    method_dt_key = 'data-methods.json'
    app_dt_key = 'data-apps.json'
    with open(method_dt_key, 'w') as fp:
        json.dump(method_dt, fp)

    with open(app_dt_key, 'w') as fp:
        json.dump(app_dt, fp)

    s3 = boto3.client('s3')
    bucket_name = 'jsonofthetree'
    json_key = 'data.json'
    json_methods_dt = json.dumps(method_dt)
    json_apps_dt = json.dumps(app_dt)

    s3.put_object(Bucket=bucket_name, Key=method_dt_key, Body=json_methods_dt, ACL='public-read')
    s3.put_object(Bucket=bucket_name, Key=app_dt_key, Body=json_apps_dt, ACL='public-read')