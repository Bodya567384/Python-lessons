# https://github.com/PDUTeacher/python-lessons.git

# Приклади застосування функції print

print("Hello, World!")

print('---- start ----')
print('Work')
print('One', "Two")
print('tutorial','on','python','print','function')
#
print('tutorial' + 'on' + 'python' + 'print' + 'function')
print('tutorial','on','python','print','function',sep='\n')
print('tutorial','on','python','print','function',sep=',+')

print('One', "Two", sep="\n")
print("Int: %d, Str: %s, Fraction number: %d" %(12, 'text', 45.55))

print('----- end -----')


#
a = 2
b = "Datacamp"
print(a,"is an integer while",b,"is a string.")
print("%d is an integer while %s is a string." %(a,b))

print(f"{a} is an integer while {b} is a string.")
print("{0} is an integer while {1} is a string.".format(a,b))
