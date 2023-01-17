import time, hashlib


def create_id():
    m = hashlib.md5(str(time.perf_counter()).encode("utf-8"))
    return m.hexdigest()