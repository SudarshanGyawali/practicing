import sys
sys.set_int_max_str_digits(50000)

file_obj = open("sample.txt") #'file_obj' is a file object not a variable that stores the file's content
file_content = file_obj.read() #'content' is a variable that stores the information in the file

a =  file_content #the content is "copied" into different variable 'a'

period_pos = a.rfind(".")  #gives information on the postion of the period

a1 = a.replace(" ","")   #replaces the spaces from the number
a2 = a1.replace(".","")  #replaces the decimal point from the number. 
                         #to get the original number, just divide the a2 number by 10^(period_pos).


c = len(a2)

b = int(a2) #makes the decimal number into an integer for reliable calculation

pi_squared = b*b

sol_txt = str(pi_squared)

# print(sol_txt)

new_file = open("pi_squared.txt", "x")
file_answer = new_file.write(sol_txt)