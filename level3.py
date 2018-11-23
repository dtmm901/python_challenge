import re
import urllib.request

"""extract html comments from url and find the characters with the following pattern
One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
"""
#Get the html comments
response = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
html = response.read().decode()
comment = re.findall('<!--(.*?)-->', html, re.DOTALL)[0]
# print(text)

#compile the pattern
pattern = re.compile(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]')
matches = pattern.findall(comment)
print(''.join(matches))
