import re
import zipfile

unzip = zipfile.ZipFile('python challenge/channel.zip')
# print(unzip.namelist())
nothing = 90052
pattern = re.compile(r'Next nothing is (\d+)')
while True:
    content = unzip.open('{}.txt'.format(nothing)).read().decode()
    print(content)
    nothing = pattern.search(content)
    if nothing == None:
        break
    nothing = nothing.group(1)
#
# while True:
#     file = open('python challenge/channel/{}.txt'.format(nothing)).read()
#     print(file)
#     nothing = pattern.search(file)
#     if nothing == None:
#         break
#     nothing = nothing.group(1)
