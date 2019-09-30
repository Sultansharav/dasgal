# 2 оронтой тоо өгөгдөв. Цифрийдүүн нийлбэр ол. 
def hoerOront(n):
    return sum(int(i) for i in str(n))
n=int(input())
print(hoerOront(n))