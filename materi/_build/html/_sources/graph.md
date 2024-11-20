# Centrality Graph

* **Social Network** Analysis merupakan bidang kajian yang mengekplorasitentang hubungan manusia dengan menggunakan teori graf. Implementasi Social Network Analysis dapat menjelaskan relasi atau hubungan antar aktor melalui visualisasi berbentuk graf. Relasi dalam analisis jaringan sosial dapat diproses dalam bentuk perhitungan yang disebut centrality dalam sebuah jaringan sosial sesuai dengan posisi masing-masing aktor di dalam struktur jaringan tersebut

* **Social network** ​terdapat node yang mewakili ​orang atau individu atau aktor. ​Relasi  antar objek  dapat dinyatakan dengan link ​atau edges yang terjadi antara aktor tersebut. _Social network_ terdiri dari banyak aktor ​yang mempunyai relasi satu sama lain hingga​ membentuk peta jaringan sosial yang dinyatakan dengan ​graph​.

![Social Network](https://hackmd.io/_uploads/ByTPnvPzye.png "Social Network")
![Adjacency Matriks](https://hackmd.io/_uploads/r1K93Pwzkl.png "Adjacency Matriks")

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
![image](https://hackmd.io/_uploads/SJU9J_vM1l.png)
![image](https://hackmd.io/_uploads/Skn21OwGyl.png)

- Normalisasi  Degree Centrality: 
Untuk  node 1, degree centrality adalah 3;
Normalisasi degree centrality adalah  
3/(9-1)=3/8.

## Closeness Centrality
- **Closenes centrality** adalah nilai kedekatan antara satu node dengan node lain dalam jaringan dengan menghitung rata-rata dari jarak relasi node-node tersebut. Skor closeness centrality mewakili kecepatan dalam penyebaran informasi.

- Average Distance:
![image](https://hackmd.io/_uploads/HJOLe_wzye.png)

- Closeness Centrality:
![image](https://hackmd.io/_uploads/BkI_x_vM1e.png)

### Contoh Closeness Centrality
![image](https://hackmd.io/_uploads/B1HPMdvzJe.png)
![image](https://hackmd.io/_uploads/S1NigOPf1e.png)
**Node 4  lebih central  dari node 3**

## Betweenness Centrality
- _Skor betweeness Centrality_ mewakili seberapa besar informasi yang tersebar dari suatu aktor. Semakin besar skor, artinya aktor tersebut semakin berperan dalam penyebaran informasi 

- Semakin banyak lintasan yang harus melewati persimpangan itu (misal tidak ada jalan alternatif), maka semakin penting arti persimpangan tersebut. Hal ini menandakan seberapa besar suatu node diperlukan sebagai penghubung dalam penyebaran informasi di dalam jaringan
- Ukuran ini juga dapat digunakan untuk mengidentifikasi boundary spanners, yaitu orang atau node yang berperan sebagai penghubung (jembatan) antara dua komunitas
- Menghitung jumlah lintasan terpendek yang melewati suatu node
- Node dengan  betweenness  tinggi  adalah  penting dalam komunikasi dan penyebaran informasi
- Betweenness Centrality:
![image](https://hackmd.io/_uploads/rJgIZODzJe.png)
- Jumlah lintasan terpendek antara  s dan t
![image](https://hackmd.io/_uploads/B160WuDfke.png)
- Jumlah lintasan terpendek antara s dan t yang melewati vi
![image](https://hackmd.io/_uploads/H1AxfOvzJg.png)


![image](https://hackmd.io/_uploads/HJosGuPMke.png)
![image](https://hackmd.io/_uploads/rJgTz_wfkx.png)

- betweenness centrality  untuk node 5?

![image](https://hackmd.io/_uploads/HJqvmuPGkg.png)
![image](https://hackmd.io/_uploads/HJ2BXuDz1e.png)

![image](https://hackmd.io/_uploads/HkU4XOvfJl.png)

tes