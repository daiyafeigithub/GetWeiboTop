import json

import os, random

import base64

import urllib.request

import datetime

HOME ="D:\\images\\"  # user home directory

pic_dir = HOME + "Pictures/Bing"  # default dir


def load_config():  # the load config function

    global HOME

    global pic_dir

    config_dir = HOME + ".config/Bing"

    json_file = config_dir + "/" + "config.json"

    init_config = {'Bing': {'dir': pic_dir, 'delete': 'True', 'time': '30', 'version': '1.0'}}

    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    if not os.path.exists(json_file):
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(init_config, f, ensure_ascii=False, indent=4)

    with open(json_file, 'r', encoding='utf-8') as f:

        config_json = json.load(f)

    pic_dir = config_json['Bing']['dir'] + '/'

    if not os.path.exists(pic_dir):
        os.makedirs(pic_dir)


def download_and_apply():
    global HOME

    global pic_dir

    date = datetime.datetime.now().strftime('%Y%m%d')

    today_picture = pic_dir + date + ".jpg"

    yesterday_pic = pic_dir + str(int(date) - 1) + ".jpg"

    bing_json_file = HOME + ".bing.json"

    json_url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=100"  # where to get the json file

    bing_url = "https://www.bing.com"  # bing.com main domain

    print('当前目录有照片：', os.listdir(pic_dir))

    pic_num = len(os.listdir(pic_dir))

    if not os.path.exists(today_picture):

        if not os.path.exists(yesterday_pic) or pic_num < 7:  # 只有初始化或者最近两天照片都不在或者操作失误删除照片小于7张，才需要一次下载7张

            print('今天是%s,全部初始化！' % date)

            # get the json file and hide the file

            urllib.request.urlretrieve(json_url, bing_json_file)

            # open the file and import json string

            with open(bing_json_file, "r", encoding='utf-8') as f:

                bing_json = json.load(f)

            url_append = bing_json['images']

            for image in url_append:
                imgurl = bing_url + image['url']

                imgname = pic_dir + image['startdate'] + '.jpg'

                # get picture

                urllib.request.urlretrieve(imgurl, imgname)

        else:

            print('今天是%s,今天的图片还没有更新！' % date)

            urllib.request.urlretrieve(json_url, bing_json_file)

            # open the file and import json string

            with open(bing_json_file, "r", encoding='utf-8') as f:

                bing_json = json.load(f)

            url_append = bing_json['images'][0]['url']

            imaurl = bing_url + url_append

            imgname = pic_dir + bing_json['images'][0]['startdate'] + '.jpg'

            print('开始下载【%s】，原地址是：%s' % (imgname, imaurl))

            # get picture

            urllib.request.urlretrieve(imaurl, imgname)
            #transferToBase64(imaurl)

def transferToBase64(imaurl):
    with open(imaurl, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
        print('data:image/jpeg;base64,%s' % s)
if __name__ == '__main__':
    load_config()

    download_and_apply()




