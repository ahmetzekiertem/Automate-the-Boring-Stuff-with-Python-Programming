import shutil
import os



#os.chdir('C:\\Windows\\System32')
#os.getcwd()
#shutil.copy("/Users/mac/Desktop/hello.txt", "/Users/mac/Desktop/MOOCS/Udemy/spammmmm.txt")


#shutil.copytree("/Users/mac/Desktop/hello.txt", "/Users/mac/Desktop/MOOCS/Udemy/spammmmmm.txt")

#shutil.move("/Users/mac/Desktop/hello.txt","/Users/mac/Desktop/MOOCS")

#shutil.copy("/Users/mac/Desktop/MOOCS/Udemy/spammmmm.txt","/Users/mac/Desktop/hello.txt")


#shutil.move('/Users/mac/Desktop/Automate the Boring Stuff with Python Programming',"/Users/mac/Desktop/MOOCS/Udemy")

'''Your programs can create new folders (directories) with the os.makedirs() function.
 Enter the following into the interactive shell:'''

print("*********")
os.path.abspath('.')
os.path.isabs('.')
print("****************")

path = '/Users/mac/Desktop/delicious'
print(os.path.basename(path))
#'calc.exe'
print(os.path.dirname(path))
#'C:\\Windows\\System32'
##os.makedirs('C:\\delicious\\walnut\\waffles')
#### DELETING FILES
print(path.split(os.path.sep))
#os.unlink('hello.txt')
print("**********")
print(os.path.getsize(path)) #file size
print("**********")
print(os.listdir(path+"/cat"))
#os.rmdir()

#shutil.rmtree("/Users/mac/Desktop/MOOCS/Udemy/spammmmm.txt")

for folderName, subfolders,filesname in os.walk("/Users/mac/Desktop/delicious"):
    print("Print folder is " + folderName)
    print("Print subfolders" + folderName +"SADASDADASD"+ str(subfolders))
    print("Print filesname" + folderName +"ASDASDSADASD"+ str(subfolders))
    print()
