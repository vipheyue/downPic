# -*- coding:utf-8 -*-
def add_text(url, word):
    from PIL import Image, ImageDraw, ImageFont
    # 设置所使用的字体
    font = ImageFont.truetype("/System/Library/Fonts/STHeiti Medium.ttc", 30)

    # 打开图片
    # imageFile = "/Volumes/Untitled/doutupic/full/热门/0a7fbf1780401add4f2a166a073642d6_713_50.jpg"
    import os
    try:
        fileName=os.path.basename(url)
        filePath = str('/Volumes/Untitled/doutupic/full/热门/') + fileName
        imageFile = filePath
        img = Image.open(imageFile)
        # 画图
        draw = ImageDraw.Draw(img)
        draw.text((20, img.size[1] / 8 * 7), word, (43, 43, 43), font=font)  # 设置文字位置/内容/颜色/字体
        draw = ImageDraw.Draw(img)  # Just draw it!
        # 另存图片
        img.save("/Volumes/Untitled/addText/"+fileName)
    except:
            print("add_text 小问题......")

def findFils():
    import os
    dirs = os.listdir('/Volumes/Untitled/doutu/')
    for file in dirs:
        try:
            with open('/Volumes/Untitled/doutu/%s' % file, 'r') as f:
                import json
                data = json.load(f)
                item = data['data']['item']
                url = item['picPath']
                word = item['name']
                add_text(url, word)
                pass
        except:
            print("小问题......")


findFils()
