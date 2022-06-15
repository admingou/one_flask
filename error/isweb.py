from flask import request
import re

def is_web_or_api():
    return re.match(r"/api", request.full_path)
