#input from user 
# name=input("enter your name")
#print("welcome ",name)
#age=input("enter age ")
#print(type(age)) #by deafault it will be string
#therefore we need type casting 
#var=float(input("enter your age"))
#print(type(var),var)
#print("Write two numbers to add")
#a=int(input("enter first number"))
#b=int(input("enter second number"))
#print("sum is ", a+b) 

#strings
#escape sequence character used for formatting like \n for next line and \t for tab spaace
str1="hello  \n hello \t word"
print(str1)
#concantentation--to add two strings
str1="bat"
str2="man"
print(" ",str1+" "+str2)

#len-length of string
print(len(str1))
len2=len(str2)
print(len2)

#indexing means every letter hass fixed position like name-0123
str3="super"
x=str3[0]
print(x)
#slicing--acessing part of string str[strating inx:ending inx] 
# if no starting given automatically 0 if no ending it is automatically len(str)
print(str3[0:4])
#negative indexxing name_-4-3-2-1 
print(str3[-3:-1])

#string functions liKe length of string 
str4="supercalifragilisticexpialidocious"
print(str4.endswith("ious")) #to check if string ends with given substring
print(str4.startswith("super")) #to check if string starts with given substring

print(str4.capitalize())
print(str4.replace("s","t"))#to replace s with t
print(str4.find("s3")) #to find the index of substring
print(str4.count("is")) #to count the number of times i is present in string


