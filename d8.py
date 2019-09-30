# 4оронтой тооны зуутын орны тоо тэгш бол true үгүй бол false гэж хэвлэ.
def ZuutynOront(n):
    if n//100%10%2 == 0:
        return True
    else:
        return False

n = int(input())
print(ZuutynOront(n))