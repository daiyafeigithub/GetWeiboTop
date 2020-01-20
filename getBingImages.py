import json

import os, random

import base64
import time

import urllib.request

import datetime
import pymysql

HOME ="D:/images/"  # user home directory

pic_dir = HOME + "Pictures/Bing"  # default dir
str_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
mysql_conn = pymysql.connect('localhost', 'root', 'root', 'asusee')
cursor = mysql_conn.cursor()
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

    bing_json_file = HOME + ".bing.json"

    json_url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=100"  # where to get the json file

    bing_url = "https://www.bing.com"  # bing.com main domain

    print('当前目录有照片：', os.listdir(pic_dir))



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
                    b64str=transferToBase64(imgname);
                    valuelist="'"+b64str+"','1980x1080','"+image['copyright']+"','"+str_time+"','"+str_time+"','localhost','1','21','1','1'"
                    connectmysql(valuelist)
    mysql_conn.close()
    cursor.close()
def connectmysql(valuelist):
  paramlist="base64,size,imagename,createtime,updatetime,userip,sourceflag,imagetypeid,userid,status"
  insertsql='insert into t_bizhi(' + paramlist + ') values('+ valuelist +')'

  #cursor.execute(insertsql)





def  transferToBase64(imaurl):
    with open(imaurl, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
        return s

if __name__ == '__main__':
    load_config()

    download_and_apply()




