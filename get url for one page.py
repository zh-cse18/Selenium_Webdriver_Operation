
with open('urls.txt', 'r') as fobj:
    hospitals = fobj.readlines()


new =["\""+i+"\"," for i in hospitals[0:100]]

for i in new:
    print(i)
