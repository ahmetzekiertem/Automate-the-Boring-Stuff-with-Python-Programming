import os



hellofile = open("/Users/mac/Desktop/hello.txt")

content = hellofile.read()
print(content)
hellofile.close()





hellofilew = open("/Users/mac/Desktop/hello.txt", 'a')

hellofilew.write("hellloooooo!!!!")



hellofilew.write("hellloooooo!!!!\n")

hellofilew.write("hellloooooo!!!!\n")

hellofilew.write("hellloooooo!!!!\n")


hellofilew.close()

print(os.getcwd())


import shelve

shelfFile = shelve.open('mydata')

shelfFile['cats'] = ['Zophie','Pooka','Simon','Fat-tail','Cleo']

shelfFile.close()

shelfFile = shelve.open('mydata')

print(shelfFile['cats'])


shelfFile.close()
