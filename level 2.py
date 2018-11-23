"""Level 2"""
from collections import Counter
import urllib.request
import re

html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()
comments = re.findall("<!--(.*?)-->", html, re.DOTALL)
data = comments[-1]
print(data)
# print(re.findall(r"[A-Za-z]",data))

# print(comments)
#
# count = Counter(data)
# print(count.most_common()[-10:])

# input = "abcdefg"
# result = re.sub(r'(a)(bc)', r'\1', input)
# print(result)
