import time
import pymysql
import base64
import os

mysql_conn = pymysql.connect('localhost', 'root', 'root', 'asusee')
cursor = mysql_conn.cursor()
def  transferToBase64(imaurl):
    with open(imaurl, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s=base64_data.decode()
        return s
def connectmysql(valuelist):
    paramlist="base64,size,imagename,createtime,updatetime,userip,sourceflag,imagetypeid,userid,status"
    insertsql='insert into t_bizhi(' + paramlist + ') values('+ valuelist +')'
    #cursor.execute(insertsql)
if __name__ == "__main__":


  pic_dir = "D:\\images\\Pictures\\Bing"  # default dir
  str_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
  list = os.listdir(pic_dir)  # 列出文件夹下所有的目录与文件
  for file in list:
      imgname = os.path.join(pic_dir, file)
      b64=transferToBase64(imgname);
      print(imgname)

      valuelist="'"+b64+"','1980x1080','"+imgname+"','"+str_time+"','"+str_time+"','localhost','1','21','1','1'"
      connectmysql(valuelist)
  mysql_conn.close()
  cursor.close()
