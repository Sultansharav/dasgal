# Өгөгдсөн тоо тэгш бол 3т хувааж үлдэгдлийг гарга үгүй бол 3т хувааж бүхлийг хэвлэ.
def tegshToo(n):
    if n%2 == 0:
        return n%3
    else: return n//3
n = int(input())
print(tegshToo(n))