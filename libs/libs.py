import os
import hashlib

def get_FileSize(filePath):
      """
      计算文件大小
      :param filePath:
      :return:
      """
      fsize = os.path.getsize(filePath)
      fsize = fsize/float(1024*1024)
      return round(fsize,2)


def  get_md5(filepath):
      """
      计算文件md5
      :param filepath:
      :return:
      """
      m = hashlib.md5()
      with open(filepath, "rb") as f:
         m.update(f.read())
         f.close()
      return m.hexdigest()