exercise 1
def function(s,i):
    if(i==0):
        return " "
    else:
        reversed = s[::-1]
        for a in range(i):
            print(reversed,end="")

function("mah", 3)


exercise 2
def function_2(s):
    a=""
    b=""
    for i in s:
        if i.isupper():
            a += i
        else:
            i.islower()
            b += i
    return print(a+b)


function_2("aaBBa")


exercise 3

def function_3(s1,s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False
print(function_3("bdc", "cab"))



exercise 4


def function_4(l):
    max=0
    min=0
    for i in l:
        if i>max:
            max=i
        else:
            if i<min:
                min = i

    print("“the highest value in the list is",max  ,"at index",l.index(max),"”")
    print("“the lowest value in the list is",min, "at index", l.index(min),"”")

function_4(l = [5,6,3,2,7,2,0,1,6],)




exercise 5

def function_5():
    a=input("input=")
    print(len(a))

function_5()

