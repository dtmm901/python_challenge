from urllib.request import urlopen
import re


url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'
nothing = 72758
pattern = re.compile(r'and the next nothing is (\d+)')

while True:
    html = urlopen(url.format(nothing)).read().decode()
    print(html)
    nothing = pattern.search(html)
    if nothing == None:
        break
    nothing = nothing.group(1)

# """
# 16044, message is "Yes. Divide by two and keep going."
# """
