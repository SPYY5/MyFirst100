'''here in this code  we want to write a Calculator to learn how to use following this:
first we want to learn about type like integer=1 , -1 / float= 1.5 , -1.5 / string= ' abc 1 1.5 ' 
*for str we must use '' to python underestand we wrote str
and in python we use * for multipication and / for division'''
import time # go to tome lib to use time.time and more
tm_s = time.time()# time to start
num_1 = int(input('num_1 :'))#give first number from user
op = input("Enter operation (+, -, *, /): ")# give secend number from user
num_2 = int(input('num_2 :'))# give secend number from user
if op=='+': # check to user enterd + or not
    print(num_1 + num_2)# show user result
elif op=='-':# check if user don't entered + chekc to he enter -
    print(num_1 - num_2)# show user result
elif op=='*':# check if user don't entered +,- chekc to he enter *
    print(num_1 * num_2)# show user result
elif op == '/':#check if user don't entered +,-,* chekc to he enter /
    if num_2 != 0:# check to second number isn't 0
        print(num_1 / num_2)# show user result
    else:# if upper if isn't correct do this
        print('divide to zero')#we can divide nmuder to zero
tm_e = time.time()#time to finish
print(tm_e - tm_s)#show us to run the code
