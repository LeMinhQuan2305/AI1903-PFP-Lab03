import math

n = int(input("Given number: "))
a = 2
sum = 0
#Q1:
while( a <= n+1):
    print(" ".join(str(i) for i in range(1, a)))
    a+=1
for i in range(0,n+1):
    sum+=i
print("Sum is:", sum)
#Q2:
array = list(map(int, input("enter list:" ).split())) # nhập mảng
def numberdisplay(array):               #tạo hàm để lọc số theo điều kiện trong 1 mảng
    result = []
    for i in range(len(array)):
        if array[i] >500:
            break
        elif array[i]>150:
            continue
        elif array[i]%5 ==0:
            result.append(array[i])
    return result
a = numberdisplay(array)
print(a)
#tìm total digit
td = 0
temp = a.copy()
for i in range(len(a)):
    while temp[i] >0:
        td += 1
        temp[i] //= 10
print(td)
#print thứ tự ngược lại
n = len(a)
for i in range(0, len(a)//2):
    a[i], a[n-1] = a[n-1], a[i]
    n-=1
print(a)

#Q3:
def stringinput():
    a = str(input("Original string is: "))
    return a
def middle4(b):
    n = (len(b) -4)//2
    return b[n:n+4]
a = stringinput()
print("Expected output", middle4(a))   #Q3-2 + Q3-3
def inputappendfirstmidlast():
    s1 = str(input("S1:"))
    s2 = str(input("S2:"))
    s3 = s1[0:len(s1)//2] + s2 + s1[len(s1)//2:len(s1)]
    print(s1)
    s4 = s1[0] + s2[0] + s1[len(s1)//2] +s2[len(s2)//2] + s1[len(s1)-1] + s2[len(s2)-1]
    return s3,s4
b = inputappendfirstmidlast()
print(b)
#Q3-4
def lowcasesort():
    str1 = str(input())
    temp = ""
    for i in range(len(str1)):
        if str1[i] == str1[i].lower():
            temp = temp + str1[i]
    for i in range(len(str1)):
        if str1[i] == str1[i].upper():
            temp = temp + str1[i]
    return temp
c = lowcasesort()
print(c)

#Q3-5
def counter():
    string1 = str(input())
    charscount = {'Chars':0, 'Digits':0, 'Symbols':0}
    for i in string1:
        if i.isalpha():
            charscount['Chars']+=1
        elif i.isdigit():
            charscount['Digits'] +=1
        else:
            charscount['Symbols']+=1
    return charscount
a = counter()
print(a)

#Q4-1
def removeexceptdigit():
    string2= str(input("Nhập chuỗi để bỏ chữ còn lại số"))
    for i in string2:
        if not i.isdigit():
            string2 = string2.replace(i, '')
    return string2
b = removeexceptdigit()
print(b)
#Q4-2
def removespecialchar():
    string2 = str(input("Nhập chuỗi để bỏ tất cả các ki hiệu đặc biệt"))
    for i in string2:
        if not i.isalpha() and not i.isdigit() and not i.isspace():
            string2 = string2.replace(i,'')
    return string2
c = removespecialchar()
print(c)
#Q4-3
def removeemptylist():
    a = list(map(str, input().split()))
    print("b4 remove:", a)
    filterlist = [i for i in a if i !=""]
    print("After remove:")
    return a        
d = removeemptylist()
print(d)
#Q4-4
def splitstring():
    a = str(input())
    a = a.replace("-", " ")
    a = a.replace(" ", "\n")
    return a
e = splitstring()
print(e)
