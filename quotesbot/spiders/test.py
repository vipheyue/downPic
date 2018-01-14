from quotesbot.spiders.image_item import ImageItem


def down():
    l = ['abc', 'def', 'xyz']
    mydata=list(map(lambda x: 'str_' + x, l))
    print(mydata)

down()