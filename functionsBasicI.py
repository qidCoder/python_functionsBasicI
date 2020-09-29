#Created by Shelley Ophir
#Coding Dojo Sep. 29, 2020
#practice using a T-diagram by predicting the outputs

#1
def a():
    return 5
print(a())
#prediction
#5

#2
def a():
    return 5
print(a()+a())
#prediction
#10

#3
def a():
    return 5
    return 10
print(a())
#prediction
#5

#4
def a():
    return 5
    print(10)
print(a())
#prediction
#5

#5
def a():
    print(5)
x = a()
print(x)
#prediction
#5, none
#none because there is no return statement

#6
# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))
#prediction
#3, 5, undefined

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
#prediction
#25

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
#prediction
#100, 10

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
#prediction
#7, 14, 21

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
#prediction
#8