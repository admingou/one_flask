from confluent_kafka import Producer
from importlib.machinery import SourceFileLoader
from kafka import KafkaProducer
import  threading
import  json
import  time
import random

#配置读取
conf = SourceFileLoader("config","./config.py").load_module()

confs = {
         'bootstrap.servers': conf.kafka_ip_port,
         'client.id': '23a49894'
     }

#创建连接

producer = KafkaProducer(bootstrap_servers=[k for k in conf.kafka_ip_port.split(",")])

def send_kafka(log):
    """处理发送日志到kafka"""
    try:
        """
            log:发送日志
            return：
        """

        producer.send(conf.kafka_topic, json.dumps(log ,ensure_ascii=False).encode())
        # 关闭kafka连接
        # lock.acquire()
        #producer.close()
        # write_json({"nums":int(num)})
        # lock.release()
        #logger.info("记录数据值:%s" % num)
        #print(log)
    except Exception as f:
        #logger.error("数据发送kafka异常,原因:%s" % str(f))
        exit()


p = Producer(**confs)
p.poll(0)
def  new_send_kafka(log):
    try:

      p.produce(conf.kafka_topic, json.dumps(log).encode('utf-8'))
      p.flush()

      # logger.info("记录数据值:%s" % num)
      #print(log)
      # write_json({"nums": int(num)})

    except Exception as f:
        pass
        # logger.error("数据发送kafka异常,原因:%s" % str(f))


def  get_path():
    return random.choice(["c://tutu/efdfdfdfdsfdsfdsfdsfdsf//weweweew//reffgrrvr/tutu.conf",
                           "c://ttgtgt/efefe//acc.txt",
                           "e://hgkjjyjyjy/ddvdvdvdvdvd/test.exe",
                           "f://ty/yuyu/uuiuoi//yuyuyuyu//kkk.docx",
                           "k://fgfvfvfv//vfvfvvvvvvvvvvvvvvv//ioioikiiukkuiu//wqeewrewrere/rgregbfdvdsvdsvd/cdcdcds/mm.yml"])

if  __name__ == "__main__":
    start_time = time.time()
    num = 0
    for  _ in range(100000000):
        end_time = time.time()
        a = end_time -start_time
        if a <=1:
             tu = threading.Thread(target=new_send_kafka, args=({"vendor":"sqlserver","product":"sqlserver","message":str({"name":"gou","age":23,"path":get_path()})},))
             tu.start()
             tu.join()
             num +=1
        else:
            print(a)
            print(num)
            break