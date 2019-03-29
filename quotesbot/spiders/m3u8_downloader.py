from urllib.parse import urlparse
import requests
import urllib
import os
import sys


def convertTemp2Real(tempM3u8file, realM3u8File, host):
    try:
        with open(tempM3u8file) as f:
            for line in f:
                print(line)
                if not line.startswith('#') and line != '':
                    with open(realM3u8File, "a") as code:
                        code.write(host+str(line))
                        code.flush()

    except FileNotFoundError:
        print("读取文件出错")

def downmv(realM3u8File):
    try:
        with open(realM3u8File) as f:
            ts_url_list = []
            for line in f:
                print(line)
                # if not line.startswith('#') and line != '':
                #     ts_url_list.append(line)
                #     body = requests.get(host + line[:-1]).content
                #     with open(realM3u8File, "a") as code:
                #         code.write(host+str(body))
                #         code.flush()
            return ts_url_list

    except FileNotFoundError:
        print("读取文件出错")


def downOneTs(someOneMvM3u8):
    with open(someOneMvM3u8) as f:
        for line in f:
            try:
                if not line.startswith('#') and line != '':
                    body = requests.get(line[:-1]).content
                    print(line)

                    # with open(realM3u8file, "ab") as code:
                     #    code.write(body)
            except Exception:
                print(line)

def get_host(url):
    urlgroup = urlparse(url)
    return urlgroup.scheme + '://' + urlgroup.hostname


def downJson(firstM3u8File,index):
    # 全能接口
    url = f'http://api.sg00.xyz/api/videoplay/{index}?uuid=00000000-0000-0000-0000-000000000000&device=1'
    import requests
    r = requests.get(url)
    json = r.json()
    print(json)
    print("\n\n")
    try:
        with open(firstM3u8File, "a", encoding='utf-8') as f:
            f.write(str(json["rescont"]["videopath"] + "\n"))
    except Exception:
        print(json)

    # with open("/Users/heyue/Desktop/moviepath/1.json", "r") as f:  # 打开文件
    #     data = f.read()  # 读取文件
    #     json = json.dumps(data)
    #     tb_command = json["rescont"]["videopath"]
    # print(data)


def getRealm3u8(firstM3u8File, realM3u8file):
    with open(firstM3u8File) as f:
        for line in f:
            print(line)
            try:
                body = requests.get(line[:-1]).content
                with open(realM3u8file, "ab") as code:
                    code.write(body)
            except Exception:
                print(line)


if __name__ == '__main__':

    # 第一步 down json
    firstM3u8File = f"/Users/heyue/Desktop/moviepath/index.txt"
    tempM3u8file = "临时多部待转换地址.txt"
    realM3u8File = f"/Users/heyue/Desktop/moviepath/real.txt"
    host = "https://tdkdzsw.com"
    # for num in range(2000, 4000):
    #     downJson(firstM3u8File,num)

    # 第二步 得到真 m3u8


    # getRealm3u8(firstM3u8File,tempM3u8file)#得到真的m3u8文件 地址  多部放在一起
    # ts_url_list=convertTemp2Real(tempM3u8file, realM3u8File, host)# 提取前个文件中的地址
    # print(ts_url_list)


    # 第三步 下载单个文件的TS 合计
    # downmv(realM3u8File)
# 转换为

# url_m3u8 = 'https://tdkdzsw.com/20190121/7GJdCAkG/index.m3u8'
# path = r'/Users/heyue/Desktop/'
# url = "https://tdkdzsw.com/20190121/7GJdCAkG/index.m3u8"
# url = "https://tdkdzsw.com/ppvod/FETJmbbE.m3u8"
# host = "https://tdkdzsw.com"
#
# body = requests.get(url).content
# with open("BNPML56i.m3u8", "wb") as code:
#     code.write(body)
# ts_url_list = get_url_list(host, "BNPML56i.m3u8")
# print(ts_url_list)
