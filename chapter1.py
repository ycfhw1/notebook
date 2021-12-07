#open函数三个参数，文件名，模式，缓冲区大小
#是否有缓冲是由缓冲区大小决定的
import pickle
import os
from multiprocessing import Process,Pool
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
#序列化主要使用cpickle和pickle模块
a=dict(url="index.html",title='首页')
print(pickle.dumps(a))
# def run_proc(name):
#     print("child process(%s) %s running"%(name,os.getpid()))
# #join：主进程等，等待子进程结束
# if __name__=='__main__':
#     print("parent process %s"%os.getpid())
#     for i in range(5):
#         p=Process(target=run_proc,args=(str(i),))
#         print("Process will begin soon")
#         p.start()
#     p.join()
#     # print(os.getpid())
#     # pid=os.fork()
#     # if pid<0:
#     #     print("error")
#     # elif pid==0:
#     #     print("i am the child"+os.getpid())
#     #     print("myfather is "+os.getppid())
#     # else:
#     #     print(os.getpid()+"created"+pid)
import time,random
#池化进程
def run_task(name):
    print("Task %s(pid=%s) is running "%(name,os.getpid()))
    time.sleep(random()*3)
    print("task %s end"%name)
if __name__=="__main__":
    print("current_process"+str(os.getpid()))
    p=Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task,args=(i))
    #在资源池join操作之前必须close(),相当于上锁操作
    p.close()
    p.join()
    print("all is well")