#exeption_handlling

#error userfriendly ayi mansilakkan ulla mechanisam in python

# try:
#     even_numbers=[2,4,6,8]
#     print(even_numbers[2])
# except ZeroDivisionError:
#     print("denominator cannot be zero")
# except IndexError:
#     print("index out of range")

# try:
#     x=int(input("enter your first number"))
#     y=int(input("enter your second number"))
#     result=x/y
#     print(abs(result))
# # except ZeroDivisionError:
# #     print("denominator cannot be zero")
# except Exception as k:
#     print(k)

# finally:
#     print("program executed")



# #filenotfound error

# try:
#     file1=open("C:/Users/USER/OneDrive/Desktop/ython/python modules/file/example1222.txt","r")
#     count=0
#     for line in file1:
#         count+=1

#     file1.close()
#     print("number of lines",count)

# except FileNotFoundError:
#     print("not found file")


#modulenotfound error
# try:
#     # import abhiram
#     import datetime
    
#     print("kkkkkk")

# except ModuleNotFoundError:
#     print("not found module")


# try:
#     file2=open("C:/Users/USER/OneDrive/Desktop/ython/python modules/file/data.txt","r")
#     data=file2.read()
#     print(data)
#     file2.close()
 

except FileNotFoundError:
    # print("not found")

    file2=open("C:/Users/USER/OneDrive/Desktop/ython/python modules/file/data.txt","w")
    file2.write("file created because file missing")
    file2.close()
    file2=open("C:/Users/USER/OneDrive/Desktop/ython/python modules/file/data.txt","r")
    data2=file2.read()
    print(data2)


#usig Valueerror

try:
    x=int(input("enter frst number"))
    y=int(input("enter second number"))
    result=x/y
    print(result)
# except ValueError:
#     print("enter valid int number")
# except ZeroDivisionError:
#     print("cannot divsion by zero")
except Exception as e:
    print(e)


#underageerror custome

class UnderageException (Exception):
    pass
try:
    age=int(input("enter your age"))
    if age<18:
        raise UnderageException("NOT ELIGIBLE")
    else:
        print("your eligible")
except UnderageException as e:
    print(e)
except ValueError:
    print("write a valid integer number")