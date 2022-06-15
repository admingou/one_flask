from one_all_web.error.codes import Error
import re

def  check_from(dicts):
    """
    表单验证
    :param dicts:
    :return:
    """
    for k,v in dicts.items():
          if k == "email":
              emails = re.search(r"\w+\@\w+\.\S",v)
              if not emails:
                  raise Error(msg="请输入正确的邮箱")
    return dicts
