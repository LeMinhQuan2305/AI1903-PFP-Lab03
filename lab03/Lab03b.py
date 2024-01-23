#Q1:
def anagramcheck():
    str1 = str(input("str1:"))
    str2 = str(input("str2:"))
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    if sorted(str2) == sorted(str1):
        return True
    else:
        return False
a = anagramcheck()
print(a)
#Q2 
def hexachecker(string):
    try:
        giatri10 = int(string, 16)
        return giatri10
    except ValueError:
        print("k phải string thập lục phân")
        return ""
b = str(input("Nhập chuỗi thập lục phân: "))
a = hexachecker(b)
print(a)