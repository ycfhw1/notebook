#open函数三个参数，文件名，模式，缓冲区大小
#是否有缓冲是由缓冲区大小决定的
import os
f=open(r"C:\Users\xiaofu\Desktop\2 (2).txt",'r',encoding='UTF-8')
#print(f.read())
with open(r"C:\Users\xiaofu\Desktop\2 (2).txt",'r',encoding='UTF-8') as filereader:
    print(filereader.read())
    filereader.close()
with open(r"C:\Users\xiaofu\Desktop\2 (2).txt",'w',encoding='UTF-8') as filewriter:
    filewriter.write("xiaofu")
    filewriter.close()
#1.3.2文件目录和文件
print(os.getcwd())
print(os.listdir(r"D:\\"))
print(os.path.isdir(r"C:\Users\xiaofu\Desktop\2 (2).txt"))
print(os.path.isfile(r"C:\Users\xiaofu\Desktop\2 (2).txt"))
#自动分离文件名和目录
print(os.path.split(r"C:\Users\xiaofu\Desktop\2 (2).txt"))
#输出当前系统的换行符
print(os.linesep)
#输出特定后缀
print(os.path.splitext(r"C:\Users\xiaofu\Desktop\2 (2).txt"))
print(os.stat(r"C:\Users\xiaofu\Desktop\2 (2).txt"))