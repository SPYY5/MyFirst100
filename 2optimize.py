'''here in this code  we want to write a calcuter to learn how to use following this:
first we want to learn about type like integer=1 , -1 / float= 1.5 , -1.5 / string= ' abc 1 1.5 ' 
*for str we must use '' to python underestand we wrote str
and in python we use * for multipication and / for division
in hole of code we use short if to make the code faster and elif to if upper IF is true don't read other IFs'''
import time# go to tome lib to use time.time and more
tm_s = time.time()# time to start
num_1 = int(input('num_1 :'))# give first number from user float numder can be -> 1,1.5,-1,-1.5,...
op = input("Enter operation (+, -, *, /): ")# give secend number from user
num_2 = int(input('num_2 :'))# give secend number from user float numder can be -> 1,1.5,-1,-1.5,...
if op=='+': print(num_1 + num_2)# here we use short form of IF to use it for Optimization and make the code faster --> check to user enterd + or not and show user result
elif op=='-':print(num_1 - num_2) # check if user don't entered + chekc to he enter - --> and show user result
elif op=='*':print(num_1 * num_2)# check if user don't entered +,- chekc to he enter * --> 
elif op == '/' and num_2 != 0: print(num_1 / num_2) if num_2 != 0 else print('divide to zero')# check if user don't entered +,-,* chekc to he enter / and check to second number isn't 0 then show user result but IF it isn't true we use else to show we can't do that
# for upper line we use and to put 2 if in one line and use this(if num_2 != 0 else) to don't write the else in other line
tm_e = time.time()# show the time of end 
print(tm_e - tm_s)# show time of run
