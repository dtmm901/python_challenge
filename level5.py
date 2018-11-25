from urllib.request import urlopen
import pickle
import zipfile

raw = urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
pickle_in = pickle.load(raw)
print(pickle_in)

for i in pickle_in:
    final = [x * y for x,y in i]
    print(''.join(final))
