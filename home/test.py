import json
import   decimal
from datetime  import date
import  datetime


result = [
            {'name': '小红', 'age': datetime.datetime(2015,12,18,15,56,29), 'balance': decimal.Decimal(21.56)},
            {'name': '小明', 'age': datetime.datetime(2015,12,18,15,56,29), 'balance': decimal.Decimal(31.23)},
          ]
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


# jsonData是结合上下文自己定义的
# ensure_ascii=False，显示中文
result = json.dumps(result, cls=DecimalEncoder, ensure_ascii=False)
print(result)


# print(json.dumps({"name":"gou","time":}))