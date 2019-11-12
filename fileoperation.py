
# write some text to file
# you can write more than one time after opening the file
import csv
import os
import pickle

with open('zahid1.txt','w', encoding='UTF-8') as fobj:
    fobj.write('\nBismillahir Rahamanir rahim')
    fobj.write('\nBismillahir Rahamanir rahim')
    fobj.write('\nBismillahir Rahamanir rahim')
    fobj.write('\nBismillahir Rahamanir rahim')
    fobj.write('\nBismillahir Rahamanir rahim')

# You can read only one time after opening the file
with open('zahid1.txt') as fobj:
    print(fobj.read())


# read file data as list
# a file can read or writ only one time for one open
with open('zahid.txt') as readfile:

    # print(readfile.read())
    print(readfile.readlines())
    print(type(readfile.read()))
    print(type(readfile.readline()))
    print(type(readfile.readlines()))

# read file data as enumarate
with open('zahid.txt') as enumarateobj:
    for lineno,content in enumerate(enumarateobj):
        print(str(lineno+1) +"."+ content)

# file pathe check existence
if os.path.exists('zahid2.txt'):
    print("yes")


    # serialize dictionary data using pickle
dict_data = {'name':'Zahid Hassan', 'Country':'Bangladesh'}
with open('serialize', 'wb')as fobj:
    encode = pickle.dump(dict_data, fobj)
    # print(encode)


# Show real dictionary data using load method
with open('serialize', 'rb')as fobj:
    print(pickle.load(fobj))

with open('zahid.csv','a') as fobj:
    fobj.write('\nmy Name is Zahid Hassan')


        # write in csv file
list_items = [['name','age', 'country'],
              ['zahid', 28,'Bangladesh'],
              ['Ayesha', 22, 'Australia']
              ]
with open('write.csv','w') as wcsv:
    fcsv = csv.writer(wcsv)
    fcsv.writerows(list_items)

    # read csv file
with open('write.csv', 'r') as fobj:
    fcsv = csv.reader(fobj)
    for line, content in enumerate(fcsv):
       print(line + 1, content)
