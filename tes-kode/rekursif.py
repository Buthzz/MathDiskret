
def rekursi(n):
    hasil =0
    if n <= 1 :
        return 3
    else :
        hasil = 2*rekursi(n-2)+4
        return hasil

n= int(input("masukkan angka: "))
print(rekursi(n))