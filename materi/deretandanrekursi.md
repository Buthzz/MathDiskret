# Deretan dan Rekursi

## Deretan (Sequence)

- Deretan adalah suatu urutan atau susunan elemen atau objek yang disusun secara teratur berdasarkan suatu aturan tertentu. Elemen dalam deretan biasanya berupa angka, huruf, simbol, atau objek lainnya, dan urutannya dapat didasarkan pada pola, nilai, atau hubungan tertentu
- Definisi: Sebuah deretan adalah fungsi dari subset suatu himpunan bilangan bulat (biasanya N atau P) ke sebuah himpunan S.

N = {1, 2, 3, 4, … } <br>
   S misalnya {2, 4, 6, 8, …},   {1/3, 1/5, 1/7, …},  dsb
- Notasi deretan: {an}

Deretan umumnya dinyatakan dalam suatu formula, misalnya:
```
an = 2 n
an = 1/n
an = 7 – 3n
```

Dalam konteks matematika, deretan sering merujuk pada barisan bilangan, yaitu kumpulan bilangan yang disusun dalam suatu pola tertentu. Misalnya:
1. Deretan bilangan ganjil: 1,3,5,7,…
2. Deretan bilangan genap: 2,4,6,8,…
3. Deretan bilangan yang membentuk deret aritmetika: 3,6,9,12....

**Contoh-contoh deretan dan formulanya:**

### Deret Aritmetika
Deret dengan pola kenaikan atau penurunan tetap.
- Contoh: 2,5,8,11,14,...
- Rumus suku ke-n:
![img.png](img/deretaritmatika.png)

Di mana:
- a: suku pertama 
- b: beda (selisih antar suku
- n: nomor suku yang dicari

### Deret Geometri
Deret dengan pola kelipatan tetap.
- Contoh: 3,6,12,24,48,... 
- Rumus suku ke-n:
![img.png](img/deretgeometri.png)

Di mana:
- a: suku pertama 
- r: rasio (perbandingan antar suku,
- n: nomor suku yang dicari

### Deret Bilangan Kuadrat
Deret dengan pola nilai berupa kuadrat bilangan bulat.
- Contoh: 1,4,9,16,25,...
- Rumus suku ke-n:
![img.png](img/deretkuadrat.png)

### Deret Bilangan Kubik
Deret dengan pola nilai berupa kubik bilangan bulat.
- Contoh: 1,8,27,64,125,...
- Rumus suku ke-n:
![img.png](img/deretkubik.png)

### Deret Fibonacci
Deret dengan pola di mana setiap suku merupakan jumlah dua suku sebelumnya.
- Contoh: 0,1,1,2,3,5,8,...
- Rumus suku ke-n (rekursif):
![img.png](img/deretfibonacci.png)

### String
- String adalah deretan berhingga karakter berbentu a1a2a3a4...an
Panjang string s adalah jumlah karakter di dalam string tersebut
Contoh: Informatika adalah string dengan panjang 11 karakter 10100101 adalah string biner dengan panjang 8 bit
- String kosong dilambangkan dengan $$ \lambda $$ , panjangnya = 0

#### Penjumlahan deretan
Jumlah deretan
am, am+1, am+2,...,an
adalah
am + am+1, + am+2 + ... an
atau dalam notasi sumasi:

$$ \Sigma_{km}^n $$ ak

- k adalah index summasi,
- m adalah batas bawah indeks,
- n adalah batas atas indeks

![img_1.png](img/img_2.png)

[//]: # (Slide 12)
##### Tugas pembuktian dari 3 rumus dibawah
Beberapa sumasi sudah ditemukan rumus penjumlahannya sebagai berikut:

![img_1.png](img/img_1.png)

![img_1.png](img/img_3.png)

### Sumasi ganda
Di dalam algoritma, kita perlu menghitung berapa kali suatu operasi tertentu dilakukan di dalam sebuah kalang bersarang (nested loop)
. Penjumlahan semua operasi di dalam kalang bersarang dinyatakan dalam bentuk sumasi ganda.

Contoh: ![img_1.png](img/img_4.png)

![img_1.png](img/img_145.png)

Contoh penggunaan: Berapa kali operasi + dilakukan didalam algoritma di bawah ini
![img_2.png](img/img_2476.png)

![img_1.png](img/img_123.png)

![img_1.png](img/img_146.png)

## Rekursi

- Sebuah objek dikatakan **rekursi** _(recursive)_ jika ia didefinisikan dalam terminologi dirinya sendiri.
- Proses mendefinisikan objek dalam terminologi dirinya sendiri disebut rekursi (recursion).
- Objek fraktal adalah contoh bentuk rekursif

![img_1.png](img/img_132.png)

### Fungsi rekursif

![img_1.png](img/img_122.png)

![img_1.png](img/img_12.png)

![img_1.png](img/img_23.png)

![img_1.png](img/img_24.png)

Contoh 7: Nyatakan n! dalam definisi rekursif
Solusi: ![img_1.png](img/img_6.png)

Misalkan f(n) = n!, maka
![img_1.png](img/img_7.png)

Menghitung 5! secara rekursif adalah:
![img_1.png](img/img_8.png)