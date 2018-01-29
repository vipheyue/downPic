# encoding='utf-8'
import json
import os


def readDir(root_path):
    file_list = list()
    root_dir = os.listdir(root_path)
    for file_or_dir in root_dir:
        realPath = os.path.join(root_path, file_or_dir)
        if os.path.isdir(realPath):
            print("---我是文件夹  " + realPath)
            my_child_list = readDir(realPath)
            print(my_child_list)
            write_data(file_or_dir, my_child_list)

        else:
            # print("-----我是文件   " + realPath)
            file_list.append(file_or_dir)
    return file_list


def write_data(dir_name, file_list):
    try:
        # parent_path = os.path.dirname(realPath)
        # print("parent_path   "+ parent_path)
        # with open('/Volumes/Untitled/doutuCategory/trim/%s.json' % dir_name, 'w') as b:
        #     b.close()

        with open('/Volumes/Untitled/doutuCategory/trim/pic1/%s.json' % dir_name, 'w') as f:
        # with open('/Volumes/Untitled/doutuCategory/trim/pic2/%s.json' % dir_name, 'w') as f:
            # 构造字典
            python2json = {}
            # 构造list
            python2json["title"] = str(dir_name)
            python2json["host"] = "https://gitee.com/heyue/pic1/raw/master/" + str(dir_name) + "/"
            # python2json["host"] = "https://gitee.com/heyue/pic2/raw/master/" + str(dir_name) + "/"
            python2json["listData"] = file_list
            # 转换成json字符串
            json_str = json.dumps(python2json)
            f.write(json_str)
    except TypeError:
        print("小问题......")


root_path = '/Volumes/Untitled/doutuCategory/pic1/'
# root_path = '/Volumes/Untitled/doutuCategory/pic2/'
# root_path = '/Volumes/Untitled/doutuCategory/test/'
readDir(root_path)
