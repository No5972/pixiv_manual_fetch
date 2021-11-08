import requests
import re
import os
import sys

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'referer': 'https://www.pixiv.net/ranking.php?mode=daily&content=illust',
}

path = './'
repeat = 1
repeat_user_name = 1
artwork_id = '93990138' # Specify this in the file directly
# artwork_id = sys.argv[1]


def getSinglePic(url):
    global repeat
    global repeat_user_name
    response = requests.get(url, headers=headers)
    # 提取图片名称
    name = re.search('"illustTitle":"(.+?)"', response.text)
    name = name.group(1)
    illust_id = re.search('"illustId":"(.+?)"', response.text)
    illust_id = illust_id.group(1)
    user_name = re.search('"userName":"(.+?)"', response.text)
    user_name = user_name.group(1)
    if re.search('[\\\ \/ \* \? \" \: \< \> \|]', name) != None:
        name = re.sub('[\\\ \/ \* \? \" \: \< \> \|]', str(repeat), name)
        repeat += 1
    if re.search('[\\\ \/ \* \? \" \: \< \> \|]', user_name) != None:
        user_name = re.sub('[\\\ \/ \* \? \" \: \< \> \|]', str(repeat_user_name), user_name)
        repeat_user_name += 1
    # 提取图片原图地址
    picture = re.search('"original":"(.+?)"},"tags"', response.text)
    pic = requests.get(picture.group(1), headers=headers)
    f = open(path + '%s_%s-by-%s.%s' % (illust_id, name, user_name, picture.group(1)[-3:]), 'wb')
    f.write(pic.content)
    f.close()

getSinglePic('https://www.pixiv.net/artworks/' + artwork_id)
