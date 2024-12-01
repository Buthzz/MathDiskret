# Centrality Graph

* **Social Network** Analysis merupakan bidang kajian yang mengekplorasitentang hubungan manusia dengan menggunakan teori graf. Implementasi Social Network Analysis dapat menjelaskan relasi atau hubungan antar aktor melalui visualisasi berbentuk graf. Relasi dalam analisis jaringan sosial dapat diproses dalam bentuk perhitungan yang disebut centrality dalam sebuah jaringan sosial sesuai dengan posisi masing-masing aktor di dalam struktur jaringan tersebut

* **Social network** terdapat node yang mewakili orang atau individu atau aktor. Relasi  antar objek  dapat dinyatakan dengan link atau edges yang terjadi antara aktor tersebut. _Social network_ terdiri dari banyak aktor yang mempunyai relasi satu sama lain hingga membentuk peta jaringan sosial yang dinyatakan dengan graph.

[//]: # (![Social Network]&#40;https://hackmd-prod-images.s3-ap-northeast-1.amazonaws.com/uploads/upload_b315e164df83a9222e26a1d4ad9ea347.png?AWSAccessKeyId=AKIA3XSAAW6AWSKNINWO&Expires=1733052421&Signature=BP5nM46CUYtf4Hk9rH841z0s%2FH8%3D "Social Network"&#41;)
![img_1.png](img/img_29.png)

[//]: # (![Adjacency Matriks]&#40;https://hackmd-prod-images.s3-ap-northeast-1.amazonaws.com/uploads/upload_6e81c5920c231962284d00687cd9d9c8.png?AWSAccessKeyId=AKIA3XSAAW6AWSKNINWO&Expires=1733052677&Signature=siOTKDcJPHTpf1uV4UMpVrfAuPY%3D "Adjacency Matriks"&#41;)

- Tidak semua node dalam jaringan adalah penting  (aktor)
- Mencari node yang paling penting dalam suatu jaringan
- Centrality adalah penentuan aktor menggunakan ukuran pada Social Network - Centrality dalam teori graf dan social network .Dibagi menjadi empat jenis:
  - degree centrality, 
  - betweeness centrality, 
  - closeness centrality 
  - eigenvector centrality

## Degree Centrality

- Degree centrality adalah jumlah edge yang terkoneksi pada suatu node yang mewakili interaksi.
- Pentingnya node ditentukan oleh jumlah node yang berdekatan dengan node tersebut
    - Lebih besar derajatnya (degree), maka lebih penting node itu dalam suatu jaringan 
    - Hanya sebagian kecil node yang memiliki derajat tinggi dalam jaringan

- Degree Centrality
$$ C_D(v_i) = d_i = \sum_{j} A_{ij} $$



- Normalisasi  Degree Centrality: 
$$ C'_D(v_i) = d_i / (n - 1) $$

Untuk  node 1, degree centrality adalah 3;
Normalisasi degree centrality adalah 3/(9-1)=3/8.

![Normalisasi  Degree Centrality](https://hackmd-prod-images.s3-ap-northeast-1.amazonaws.com/uploads/upload_b315e164df83a9222e26a1d4ad9ea347.png?AWSAccessKeyId=AKIA3XSAAW6AWSKNINWO&Expires=1733052421&Signature=BP5nM46CUYtf4Hk9rH841z0s%2FH8%3D "Normalisasi Degree Centrality")

## Closeness Centrality
- **Closenes centrality** adalah nilai kedekatan antara satu node dengan node lain dalam jaringan dengan menghitung rata-rata dari jarak relasi node-node tersebut. Skor closeness centrality mewakili kecepatan dalam penyebaran informasi.

- Average Distance:
$$ D_{avg}(v_i) = \frac{1}{n-1} \sum_{j \neq i}^n g(v_i, v_j) $$

- Closeness Centrality:
$$ C_C(v_i) = \left[\frac{1}{n-1} \sum_{j \neq i}^n g(v_i, v_j)\right]^{-1} = \frac{n - 1}{\sum_{j \neq i}^n g(v_i, v_j)} $$

### Contoh Closeness Centrality
![image](https://hackmd-prod-images.s3-ap-northeast-1.amazonaws.com/uploads/upload_b315e164df83a9222e26a1d4ad9ea347.png?AWSAccessKeyId=AKIA3XSAAW6AWSKNINWO&Expires=1733052421&Signature=BP5nM46CUYtf4Hk9rH841z0s%2FH8%3D "Social network)
![image](https://hackmd-prod-images.s3-ap-northeast-1.amazonaws.com/uploads/upload_616754a8735a944abc01a477c63992fa.png?AWSAccessKeyId=AKIA3XSAAW6AWSKNINWO&Expires=1733052036&Signature=pQhYluns%2Bh00MounGehX9kZJx14%3D)

$$C_C(3) = \frac{9-1}{1+1+1+2+2+3+3+4} = 8/17 = 0.47, \\
C_C(4) = \frac{9-1}{1+2+1+1+1+2+2+3} = 8/13 = 0.62. $$
**Node 4  lebih central  dari node 3**

## Betweenness Centrality
- _Skor betweeness Centrality_ mewakili seberapa besar informasi yang tersebar dari suatu aktor. Semakin besar skor, artinya aktor tersebut semakin berperan dalam penyebaran informasi 

- Semakin banyak lintasan yang harus melewati persimpangan itu (misal tidak ada jalan alternatif), maka semakin penting arti persimpangan tersebut. Hal ini menandakan seberapa besar suatu node diperlukan sebagai penghubung dalam penyebaran informasi di dalam jaringan
- Ukuran ini juga dapat digunakan untuk mengidentifikasi boundary spanners, yaitu orang atau node yang berperan sebagai penghubung (jembatan) antara dua komunitas
- Menghitung jumlah lintasan terpendek yang melewati suatu node
- Node dengan  betweenness  tinggi  adalah  penting dalam komunikasi dan penyebaran informasi
- Betweenness Centrality:
$$ C_B(v_i) = \sum_{v_s \neq v_i \neq v_t \in V, s < t} \frac{\sigma_{st}(v_i)}{\sigma_{st}} $$

- $$ \sigma_{st} \text{ Jumlah lintasan terpendek antara } s \text{ dan } t $$

- $$ \sigma_{st}(v_i) \text{ Jumlah lintasan terpendek antara } s \text{ dan } t \text{ yang melewati } v_i $$


![image](https://hackmd-prod-images.s3-ap-northeast-1.amazonaws.com/uploads/upload_b315e164df83a9222e26a1d4ad9ea347.png?AWSAccessKeyId=AKIA3XSAAW6AWSKNINWO&Expires=1733052421&Signature=BP5nM46CUYtf4Hk9rH841z0s%2FH8%3D)
![image](https://hackmd-prod-images.s3-ap-northeast-1.amazonaws.com/uploads/upload_7f42bae3b14ac2159ed4046bbd494c17.png?AWSAccessKeyId=AKIA3XSAAW6AWSKNINWO&Expires=1733052359&Signature=cCYasZQ0z3gvsIFN%2Bjw5rMpt4k8%3D)
$$ C_B (4) = 15 $$

- betweenness centrality  untuk node 5?

$$ \sigma_{st} \text{ Jumlah lintasan terpendek antara } s \text{ dan } t $$
$$ \sigma_{st}(v_i) \text{ Jumlah lintasan terpendek antara } s \text{ dan } t \text{ yang melewati } v_i $$

$$ C_B(v_i) = \sum_{\substack{v_s \neq v_i \neq v_t \in V \\ s < t}} \frac{\sigma_{st}(v_i)}{\sigma_{st}} $$

#### Normalisasi Betweenness Centrality
$$ C'_B(i) = \frac{C_B(i)}{(n-1)(n-2)/2}. $$
