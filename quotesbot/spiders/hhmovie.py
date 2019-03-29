def downJson(index):
    # 全能接口
    url = f'http://api.sg00.xyz/api/videoplay/{index}?uuid=00000000-0000-0000-0000-000000000000&device=1'
    import requests
    r = requests.get(url)
    json = r.json()
    print(json)
    print("\n\n")
    with open(f"/Users/heyue/Desktop/moviepath/{index}.json", "w", encoding='utf-8') as f:
        f.write(str(json))

    # with open("/Users/heyue/Desktop/moviepath/1.json", "r") as f:  # 打开文件
    #     data = f.read()  # 读取文件
    #     json = json.dumps(data)
    #     tb_command = json["rescont"]["videopath"]
        # print(data)

if __name__ == '__main__':
    for num in range(2000, 2001):
        downJson(num)