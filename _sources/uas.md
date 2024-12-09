# Ulangan Akhir Semester

## Logika matematika
Tabel:
| NO  | P  | Q  | R  | S
| --- | ---| ---| ---| ---|
| 1   | T  | F  | F  | T  |
| 2   | F  | T  | T  | F  |
| 3   | F  | T  | F  | F  |
| 4   | T  | T  | F  | F  |
| 5   | F  | F  | T  | T  |
| 6   | T  | F  | T  | F  |
| 7   | F  | F  | T  | T  |
| 8   | F  | T  | F  | F  |

Soal: (P -> Q) -> (R -> S)

Jawaban:
| NO  | P  | Q  | R  | S  | P -> Q | R -> S | (P -> Q) -> (R -> S) |
|---|---|---|---|---|---|---|---|
| 1   | T  | F  | F  | T  | F      | T      | T                   |
| 2   | F  | T  | T  | F  | T      | F      | F                   |
| 3   | F  | T  | F  | F  | T      | T      | T                   |
| 4   | T  | T  | F  | F  | T      | T      | T                   |
| 5   | F  | F  | T  | T  | T      | T      | T                   |
| 6   | T  | F  | T  | F  | F      | F      | T                   |
| 7   | F  | F  | T  | T  | T      | T      | T                   |
| 8   | F  | T  | F  | F  | T      | T      | T                   |

## Graph

| Node | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| A | 0 |1 |0 |1 |0 |0 |
| B | 1 |0 |1 |0 |1 |0 |
| C | 0 |1 |0 |1 |0 |1 |
| D | 1 |0 |1 |0 |1 |0 |
| E | 0 |1 |0 |1 |0 |1 |
| F | 0 |0 |1 |0 |1 |0 |

$$ Closeness Centrality (node i) = \frac{1}{\sum \frac{jarak(i,j)}{n-1}} $$

$$ Betweenness Centrality (node i) = \sum \frac{\sigma_{st}(i)}{\sigma_{st}} $$

### Hasilnya:
![image](img/uas.jpg)
