"""
    items清洗工具
"""

def unicode_item(res):
    return res.text.encode('utf8').decode('unicode_escape')