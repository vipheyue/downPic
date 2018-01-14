import json
import re
import urllib
from pprint import pprint

import os


def readJsonFromFile():
    # Reading data back
    os.chdir('/Volumes/Untitled/doutu/')
    with open('/Volumes/Untitled/doutu/', 'r') as f:
        data = json.load(f)
        # pprint(data)
        # pprint(data['data'])

        reg = r"(http\S+(png|gif|jpg$))"
        # reg = r"(^http\S+(png|gif|jpg$))"
        # reg = r"(http.*?\.(jpg|png|gif))"
        resultList = re.findall(re.compile(reg), str(data))
        j = 1
        for result in resultList:
            print(result)
            # print(result[0])
            print("----" * 40)
            # urllib.request.urlretrieve(result, './%d.jpg' % j)
            j += 1
        pass


# readJsonFromFile()

def readMyFile():
    dirs = os.listdir('/Users/heyue/Downloads/第12天视频/第12天-网络爬虫/02-视频爬虫/')
    for dirc in dirs:
        print(dirc)


readMyFile()
