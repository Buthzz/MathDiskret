# Probabilitas Diskrit & Probabilitas Bayesian
Probabilitas diskret adalah cabang teori probabilitas yang berhubungan dengan peristiwa atau variabel yang memiliki jumlah terbatas atau dapat dihitung. Dalam konteks ini, kita fokus pada perhitungan probabilitas berbasis data terbatas dan diskret.

Rumus probabilitas dasar dinyatakan sebagai:
$P(A) = \frac{\text{Jumlah kasus yang mengandung A}}{\text{Total jumlah kasus}}$

### Bagaimana kemungkinan/probabilitas usia paruh baya tekanan darah sangat tinggi  kemungkinan penyakit Hipertensi (H) atau Tidak (T)

#### Penjelasannya:

| No | Usia       | Tekanan Darah | Penyakit (H/T) |
|---|---|---|---|
| 1  | Muda       | Normal        | T             |
| 2  | Muda       | Tinggi        | T             |
| 3  | Paruh baya | Normal        | T             |
| 4  | Paruh baya | Tinggi        | H             |
| 5  | Tua        | Normal        | H             |
| 6  | Tua        | Sangat Tinggi | H             |
| 7  | Muda       | Normal        | T             |
| 8  | Tua        | Tinggi        | H             |

Berdasarkan informasi yang diberikan dalam tabel, kita dapat menggunakan konsep probabilitas untuk menghitung kemungkinan seseorang menderita penyakit hipertensi (H) atau tidak (T) berdasarkan usia dan tekanan darah.

Secara umum, rumus probabilitas adalah:

$$P(A) = \frac{\text{Jumlah kasus A}}{\text{Total jumlah kasus}}$$

Dalam konteks ini, kita ingin mencari probabilitas:
1. Seseorang menderita penyakit hipertensi (H)
2. Seseorang tidak menderita penyakit hipertensi (T)

Untuk mencari probabilitas penyakit hipertensi (H), kita dapat menggunakan rumus:

$$P(H) = \frac{\text{Jumlah kasus H}}{\text{Total jumlah kasus}}$$

Dari tabel, kita dapat menghitung jumlah kasus H sebagai berikut:
* Baris 4: 1 kasus
* Baris 5: 1 kasus 
* Baris 6: 1 kasus
* Baris 8: 1 kasus

Jadi total kasus H = 4

Sementara total jumlah kasus = 8

Maka probabilitas penyakit hipertensi (H) adalah:

$$P(H) = \frac{4}{8} = 0.5 = 50\%$$

Untuk mencari probabilitas tidak menderita penyakit hipertensi (T), kita dapat menggunakan rumus:

$$P(T) = \frac{\text{Jumlah kasus T}}{\text{Total jumlah kasus}}$$

Dari tabel, kita dapat menghitung jumlah kasus T sebagai berikut:
* Baris 1: 1 kasus
* Baris 2: 1 kasus
* Baris 3: 1 kasus
* Baris 7: 1 kasus

Jadi total kasus T = 4

Maka probabilitas tidak menderita penyakit hipertensi (T) adalah:

$$P(T) = \frac{4}{8} = 0.5 = 50\%$$

Jadi berdasarkan perhitungan probabilitas, seseorang dengan karakteristik usia dan tekanan darah seperti yang tertera dalam tabel memiliki kemungkinan yang sama (50%) untuk menderita penyakit hipertensi (H) atau tidak (T).


## Teorema Bayes

#### Penjelasannya:
Teorema Bayes adalah konsep dasar dalam probabilitas dan statistik yang menggambarkan hubungan antara probabilitas bersyarat. Teorema ini memungkinkan kita untuk memperbarui keyakinan atau probabilitas kita tentang suatu peristiwa berdasarkan bukti atau informasi baru. Teorema ini dapat dinyatakan secara matematis sebagai:

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

Di sini, istilah-istilah utamanya adalah:
##### Komponen Utama:

1. **Probabilitas Posterior** (`P(A|B)`): Ini adalah probabilitas terjadinya peristiwa A, mengingat peristiwa B telah terjadi. Inilah yang ingin kita hitung.
    - Probabilitas A setelah mengamati B
    - Merupakan keyakinan yang diperbarui

2. **Kemungkinan** (`P(B|A)`): Ini adalah probabilitas untuk mengamati peristiwa B, jika peristiwa A benar. Ini merupakan "bukti" atau informasi baru yang kita miliki.
    - Probabilitas mengamati B jika A benar
    - Representasi bukti atau informasi baru

3. **Probabilitas Sebelumnya** (`P(A)`): Ini adalah probabilitas awal yang sudah ada sebelumnya dari terjadinya peristiwa A, sebelum mempertimbangkan bukti baru apa pun.
    - Probabilitas awal A sebelum mempertimbangkan bukti baru
    - Mencerminkan pengetahuan awal

4. **Probabilitas Marjinal** (`P(B)`): Ini adalah probabilitas keseluruhan terjadinya peristiwa B, terlepas dari apakah peristiwa A benar atau tidak.
    - Probabilitas keseluruhan terjadinya B
    
#### Interpretasi Praktis
Teorema Bayes memungkinkan kita:

- Memperbarui keyakinan berdasarkan bukti baru
- Menggabungkan informasi sebelumnya dengan data aktual
- Membuat keputusan yang lebih baik dalam ketidakpastian

Teorema ini memungkinkan kita untuk memperbarui keyakinan kita tentang probabilitas terjadinya peristiwa A, berdasarkan bukti baru yang diwakili oleh peristiwa B. Kita mulai dengan keyakinan sebelumnya tentang A, lalu menggunakan kemungkinan mengamati B jika A, serta probabilitas keseluruhan B, untuk merevisi estimasi kita tentang probabilitas A.

Ini adalah alat yang ampuh untuk bernalar dalam ketidakpastian, karena menyediakan cara sistematis untuk memasukkan informasi baru dan menyesuaikan estimasi kita sebagaimana mestinya. Teorema Bayes memiliki aplikasi dalam berbagai bidang, mulai dari diagnosis medis hingga pembelajaran mesin dan pengambilan keputusan.

## Rumus Naive Bayes
- Hitunglah probabilitas Hipertensi terhadapa usia paruh baya tekanan darah sangat tinggi  
- Hitunglah probabilitas Tidak  Hipertensi terhadap usia paruh baya tekanan darah sangat tinggi
#### Kasus Hipertensi: Analisis Probabilitas Lanjut
#### Penjelasannya:
Skenario: Usia Paruh Baya dengan Tekanan Darah Sangat Tinggi
1. Menghitung Probabilitas Hipertensi (H) pada Usia Paruh Baya dengan Tekanan Darah Sangat Tinggi

Berdasarkan informasi pada tabel, kita dapat melihat bahwa pada baris 6, untuk usia "Tua" (yang dapat diasumsikan mencakup usia paruh baya) dan tekanan darah "Sangat Tinggi", probabilitas penyakit hipertensi (H) adalah 1.

Secara matematis, kita dapat tulis:

$$P(H | \text{Paruh baya, Sangat Tinggi}) = 1$$

Ini berarti, jika seseorang berusia paruh baya dengan tekanan darah sangat tinggi, maka peluang dia menderita hipertensi adalah 100% atau 1.

2. Menghitung Probabilitas Tidak Hipertensi (T) pada Usia Paruh Baya dengan Tekanan Darah Sangat Tinggi

Sebaliknya, untuk probabilitas tidak hipertensi (T) pada usia paruh baya dengan tekanan darah sangat tinggi, kita dapat melihat pada tabel bahwa nilai yang tertera adalah "T".

Secara matematis, kita dapat tulis:

$$P(T | \text{Paruh baya, Sangat Tinggi}) = 0$$

Ini berarti, jika seseorang berusia paruh baya dengan tekanan darah sangat tinggi, maka peluang dia tidak menderita hipertensi adalah 0% atau 0.

Penjelasan secara detail:

Teorema Bayes menyatakan bahwa probabilitas posterior suatu peristiwa A, diberi peristiwa B, dapat dihitung dengan formula:

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

Dalam konteks ini:
- A = Hipertensi (H) atau Tidak Hipertensi (T)
- B = Usia Paruh Baya dengan Tekanan Darah Sangat Tinggi

Untuk menghitung $P(H | \text{Paruh baya, Sangat Tinggi})$:
- $P(B|A) = 1$, karena dari tabel kita tahu bahwa jika usia paruh baya dan tekanan darah sangat tinggi, maka penyakitnya adalah Hipertensi (H).
- $P(A) = P(H)$, karena kita tidak memiliki informasi awal tentang probabilitas Hipertensi.
- $P(B)$ tidak perlu dihitung karena nilainya tidak dibutuhkan untuk menghitung $P(H | \text{Paruh baya, Sangat Tinggi})$.

Sehingga, $P(H | \text{Paruh baya, Sangat Tinggi}) = 1 \times P(H) / P(B) = 1$.

Untuk menghitung $P(T | \text{Paruh baya, Sangat Tinggi})$:
- $P(B|A) = 0$, karena dari tabel kita tahu bahwa jika usia paruh baya dan tekanan darah sangat tinggi, maka penyakitnya adalah Hipertensi (H), bukan Tidak Hipertensi (T).
- $P(A) = P(T)$, karena kita tidak memiliki informasi awal tentang probabilitas Tidak Hipertensi.
- $P(B)$ tidak perlu dihitung.

Sehingga, $P(T | \text{Paruh baya, Sangat Tinggi}) = 0 \times P(T) / P(B) = 0$.

Jadi, dapat disimpulkan bahwa:
- Probabilitas Hipertensi (H) pada usia paruh baya dengan tekanan darah sangat tinggi adalah 100% atau 1.
- Probabilitas Tidak Hipertensi (T) pada usia paruh baya dengan tekanan darah sangat tinggi adalah 0%.

### Catatan Penting dalam Probabilitas
#### Batasan dan Pertimbangan

- Probabilitas selalu bernilai antara 0 dan 1
- Semakin banyak data, semakin akurat estimasi
- Konteks dan kualitas data sangat menentukan

#### Aplikasi Praktis
Probabilitas Bayesian berguna dalam:

- Diagnosis medis
- Prediksi risiko penyakit
- Sistem rekomendasi
- Analisis keputusan berisiko