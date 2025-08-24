#modes

#read()

# file=open("C:/Users/USER/OneDrive/Desktop/ython/python modules/package/bbb.txt","r")   #for read show the content
# print(file.read())

#write()

file=open("C:/Users/USER/OneDrive/Desktop/ython/python modules/file/example155.txt","w")  #for edit or write file already include file anel overwritten avum allenkil new filr
file.write("lakshmi is labanese")
print("succes")

append()

file=open("C:/Users/USER/OneDrive/Desktop/ython/python modules/file/example155.txt","a")
file.write("\n new content")
print("succes")

exeption "x"

file=open("C:/Users/USER/OneDrive/Desktop/ython/python modules/file/example1.txt","r")
file.write("\n new content")
print("succes")
data1=file.read()
# print(data1)
list1=data1.split(",")
print(list1)

# if "\njabir" in list1:
#     print("yes")

# else:
#     print("no")

# line1=file.readlines()
# # print(line1)
# filr_contents=[]
# for line in line1:
#     print(line)
#     filr_contents.append(line.strip())
# print(filr_contents)


#lengthh kanan
# file=open("C:/Users/USER/OneDrive/Desktop/ython/python modules/file/example1.txt","r")
# data=file.readlines()
# # print(data)
# d={}
# for line in data:
#     d[line]=len(line)
# print(d)


#count kanan

# count=0
# for line in file:
#     count+=1
# file.close()
# print(count)

# file2=file.readlines()
# # print(file2)
# file_elements=[]
# for line in file2:
#     file_elements.append(line.strip())
# print(file_elements[-1])


#user input aakunnath

# name=input("enter your name")
# place=input("enter your place")
# mobile=input("enter your mobile")

# file=open("C:/Users/USER/OneDrive/Desktop/ython/python modules/file/example1.txt","w")
# file.write(name+"\n")
# file.write(place+"\n")
# file.write(mobile+"\n")
# file.close()
# file=open("C:/Users/USER/OneDrive/Desktop/ython/python modules/file/example1.txt","r")
# data=file.readlines()
# print(data[-1])

#unlimited text using 


# file=open("C:/Users/USER/OneDrive/Desktop/ython/python modules/file/example1.txt","a")
# print("enter lines of text")
# while True:
#     text=input()
#     if text=="":
#         break
#     file.write(text+"\n")
# file.close()

file=open("C:/Users/USER/OneDrive/Desktop/ython/python modules/file/example1.txt","r")
# data2=file.read(20)
# x=tuple(data2)
# y=x.split()
l=file.readlines()
data2=l[0:21]
print(data2)

# print("last lines",data2[-1])

# print("last 20 characters",data2[:20])

