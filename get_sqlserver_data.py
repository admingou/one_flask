from confluent_kafka import Producer
from importlib.machinery import SourceFileLoader
from threading import Lock
import pymssql
import json
import os
import time
import logging
import datetime
import   decimal
from datetime  import date
import  threading

num = 0
lock=Lock()

#配置读取
conf = SourceFileLoader("config","./config.py").load_module()



confs = {
         'bootstrap.servers': conf.kafka_ip_port,
         'client.id': 'ezaccurs'
     }

p = Producer(**confs)
p.poll(0)



#日志写入配置
logger = logging.getLogger('get_sqlserver_date')
logger.setLevel(logging.INFO)
logs = logging.Formatter("%(asctime)s %(name)s %(levelname)s:%(message)s")
basedir = os.path.abspath(".") #返回脚本所在的绝对路径
log_dir = os.path.join(basedir, 'logs')  # 日志文件所在目录,即‘脚本路径/logs'
if not os.path.isdir(log_dir):
        os.mkdir(log_dir)
filename = time.strftime('%Y-%m', time.localtime(time.time())) + '.log'
log_file = logging.FileHandler(os.path.join(log_dir, filename), encoding='utf-8')
log_file.setFormatter(logs)
logger.addHandler(log_file)

#数据存储位置
date_path = "save_date.json"


#处理数据类型异常
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        if isinstance(o, datetime.datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, o)
        super(DecimalEncoder, self).default(o)

def   write_json(data):
        """
        写入数据
        :param data: 写入数据（json格式）
        :return:
        """
        try:
           with  open(date_path,"w+",encoding='utf8') as fp:
                   fp.write(json.dumps(data, indent=4, ensure_ascii=False))
        except Exception as f:
                logger.error("数据写入失败,原因:%s"%str(f))
                exit()


#读取数据
def  read_json():
        """
        读取数据
        :return: da (json格式)
        """
        if not os.path.isfile(date_path):
                write_json({"nums": int(conf.init_index)})
        try:
                with open(date_path,"r") as fp:
                         da = json.load(fp)
                return da
        except Exception as f:
                logger.error("数据读取失败,原因:%s"% str(f))
                exit()

try:
   conn = pymssql.connect(conf.sqlserver_host, conf.sqlserver_user, conf.sqlserver_password, conf.sqlserver_db)
   cursor = conn.cursor()
except Exception as f:
        logger.error("数据库连接失败，原因:%s"%str(f))
        exit()



def  send_kafka(log):
        """处理发送日志到kafka"""
        try:
                """
                    log:发送日志
                    return：
                """
                #producer = KafkaProducer(bootstrap_servers=[k for k in conf.kafka_ip_port.split(",")])
                #producer.send(conf.kafka_topic, json.dumps(log , cls=DecimalEncoder, ensure_ascii=False).encode())
                #关闭kafka连接
               # producer.close()
                #lock.acquire()
               # write_json({"nums":int(num)})
                #lock.release()
                logger.info("记录数据值:%s"%num)
                print(log)
        except Exception as f:
                logger.error("数据发送kafka异常,原因:%s"%str(f))
                exit()



def  new_send_kafka(log):
    try:
      p.produce(conf.kafka_topic, json.dumps(log).encode('utf-8'))
      p.flush()
      logger.info("记录数据值:%s" % num)
      print(log)
      write_json({"nums": int(num)})
    except Exception as f:
        logger.error("数据发送kafka异常,原因:%s" % str(f))


def   get_date(id):
        """
        获取数据
        :param id:
        :return:
        """
        sql = "SELECT * FROM %s where %s > %s and %s < %s"% (conf.sqlserver_table,conf.show_id_key,id,conf.show_id_key,int(id) + conf.count)
        cursor.execute(sql)
        return cursor.fetchall(),cursor.description





def  show_date():
    while True:
           global num
           start_time = time.time()
           data,keys = get_date(read_json()["nums"])
           if len(data) > 0:
                for k in  data:
                    dicts = {}
                    n = 0
                    for m in keys:
                        if m[0] == conf.show_id_key:
                             num = k[n]
                        da = k[n]
                        if not da:
                           da = ""
                        dicts[m[0]] = da
                        n += 1
                    #添加标签
                    tu = threading.Thread(target=new_send_kafka, args=({"vendor":conf.vert,"product":conf.pros,"hostIP":conf.sqlserver_host,"message":json.dumps(dicts, cls=DecimalEncoder, ensure_ascii=False)},))
                    #send_kafka({"vendor":conf.vert,"product":conf.pros,"hostIP":conf.sqlserver_host,"message":json.dumps(dicts, cls=DecimalEncoder, ensure_ascii=False)})
                    tu.start()
                    tu.join()
           end_time = time.time()
           logger.info("读取数据:%s条--------发送kafka耗时:%s秒"%(len(data), (end_time - start_time)))
           if len(data) != conf.count:
                 logger.info("单次获取数据小于预设数据量%s,进入等待---------------->%s秒" % (conf.count, conf.sleep_time))
                 time.sleep(conf.sleep_time)


if __name__ == "__main__":
        logger.info("#####################获取SQLserver服务开启####################")
        try:
           start_time = time.time()
           show_date()
           end_time = time.time()
           print(end_time - start_time)
        except Exception as f:
           logger.error("程序异常退出,原因:%s"%str(f))
           exit()
