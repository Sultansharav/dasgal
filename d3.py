# Өгөгдсөн тоо 7т хуваагдаж байвал тоог гарга үгүй бол тоог 7д хувааж үлдэгдлийг хэвлэ.
def doloodHuvaagdah(n):
    if n%7 == 0: return n
    else: return n%7
n=int(input())
print(doloodHuvaagdah(n))