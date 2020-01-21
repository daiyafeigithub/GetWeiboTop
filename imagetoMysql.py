import time
import pymysql
import base64
import os
import uuid as uid

mysql_conn = pymysql.connect('localhost', 'root', 'root', 'asusee')
cursor = mysql_conn.cursor()


def transferToBase64(imaurl):
    with open(imaurl, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
        return s


def connectmysql(valuelist):
    paramlist = "imagecontent,size,imagename,createtime,updatetime,userip,sourceflag,imagetypeid,userid,status,imagetitle"
    insertsql = 'insert into t_bizhi(' + paramlist + ') values(' + valuelist + ')'
    print("开始执行--->"+insertsql)
    cursor.execute(insertsql)
    print("结束")

if __name__ == "__main__":

    pic_dir = "D:\\gallery"  # default dir
    str_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    list = os.listdir(pic_dir)  # 列出文件夹下所有的目录与文件
    namelist = []
    with open('D://bingpicnames.txt', 'r', encoding="utf-8") as f:
        namelist = f.readlines()
    for i in range(len(list)):

        imgname = os.path.join(pic_dir, str(i + 1) + ".jpg")
        b64 = transferToBase64(imgname);
        imgname = str(uid.uuid1()).replace("-", "") + "_" + str(i + 1) + ".jpg"
        if namelist[i].count("'") > 0:
            str1 = namelist[i].replace("'", "\\'")
            print(str1)
            valuelist = "'" + b64 + "','1980x1080','" + imgname + "','" + str_time + "','" + str_time + "','localhost','1','21','1','1','" + str1 + "'"
        else:
            valuelist = "'" + b64 + "','1980x1080','" + imgname + "','" + str_time + "','" + str_time + "','localhost','1','21','1','1','" + str(namelist[i]) + "'"
        connectmysql(valuelist)
    cursor.close()
    mysql_conn.commit();
    mysql_conn.close()

