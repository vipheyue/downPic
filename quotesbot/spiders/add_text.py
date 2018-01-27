# -*- coding:utf-8 -*-
def add_text():
    from PIL import Image, ImageDraw, ImageFont
    # 设置所使用的字体
    font = ImageFont.truetype("/System/Library/Fonts/STHeiti Medium.ttc", 40)

    # 打开图片
    imageFile = "/Users/heyue/Desktop/test.jpg"
    img = Image.open(imageFile)

    # 画图
    draw = ImageDraw.Draw(img)
    draw.text((20, img.size[1]/4*3), "牛工程厉害了", (43, 43, 43), font=font)  # 设置文字位置/内容/颜色/字体
    draw = ImageDraw.Draw(img)  # Just draw it!
    # 另存图片
    img.save("/Users/heyue/Desktop/target.png")

add_text()