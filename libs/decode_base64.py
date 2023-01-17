import base64

def  decode_base(dicts):
    """
    base64解密
    :param dicts: 加密表单数据
    :return: 解密表单数据
    """
    dicts["password"] = base64.b64decode(dicts.get("password")).decode()
    return dicts