# Өгөгдсөн тоо эерег тэгш тоо бол true үгүй бол false гэж хэвлэ.
def EeregTegshToo(n):
    if n>0 and n%2==0:
        return True
    else: return False
n = int(input())
print(EeregTegshToo(n))