# Full Adder

## Logic

|Input A|Input B|Input C|Output H|Output L|
|:-----:|:-----:|:-----:|:------:|:------:|
|      0|      0|      0|       0|       0|
|      1|      0|      0|       0|       1|
|      0|      1|      0|       0|       1|
|      0|      0|      1|       0|       1|
|      1|      1|      0|       1|       0|
|      1|      0|      1|       1|       0|
|      0|      1|      1|       1|       0|
|      1|      1|      1|       1|       1|

## Usage

Adds two bits.

- Output H is high if at least two inputs are high.
- Output L is high if one or all inputs are high.

---

```mermaid
---
title: Full Adder -- 0 | 0 | 0
---
flowchart LR;

subgraph n1 [NAND];
  direction LR;
  n1ina[a] & n1inb[b] --> n1o[output];
end;

subgraph n2 [NAND];
  direction LR;
  n2ina[a] & n2inb[b] --> n2o[output];
end;

subgraph n3 [NAND];
  direction LR;
  n3ina[a] & n3inb[b] --> n3o[output];
end;

subgraph n4 [NAND];
  direction LR;
  n4ina[a] & n4inb[b] --> n4o[output];
end;

subgraph n5 [NAND];
  direction LR;
  n5ina[a] & n5inb[b] --> n5o[output];
end;

subgraph n6 [NAND];
  direction LR;
  n6ina[a] & n6inb[b] --> n6o[output];
end;

subgraph n7 [NAND];
  direction LR;
  n7ina[a] & n7inb[b] --> n7o[output];
end;

subgraph n8 [NAND];
  direction LR;
  n8ina[a] & n8inb[b] --> n8o[output];
end;

subgraph n9 [NAND];
  direction LR;
  n9ina[a] & n9inb[b] --> n9o[output];
end;

subgraph inputs [Inputs];
  direction TB;
  a[a];
  b[b];
  c[c];
end;

a[a] ---------> n1inb & n2ina;
b[b] --> n3ina & n4ina;
c[c] --> n4inb & n5inb;
n1o ---> n2inb & n6ina & n9ina;
n2o --> n7ina;
n3o --> n8ina;
n4o --> n3inb & n5ina & n6inb;
n5o --> n8inb;
n6o ----> h[h];
n7o --> l[l];
n8o --> n1ina & n9inb;
n9o --> n7inb;
linkStyle 3 stroke:#33f,stroke-width:3px;
linkStyle 5 stroke:#33f,stroke-width:3px;
linkStyle 8 stroke:#33f,stroke-width:3px;
linkStyle 10 stroke:#33f,stroke-width:3px;
linkStyle 11 stroke:#33f,stroke-width:3px;
linkStyle 12 stroke:#33f,stroke-width:3px;
linkStyle 13 stroke:#33f,stroke-width:3px;
linkStyle 14 stroke:#33f,stroke-width:3px;
linkStyle 15 stroke:#33f,stroke-width:3px;
linkStyle 16 stroke:#33f,stroke-width:3px;
linkStyle 24 stroke:#33f,stroke-width:3px;
linkStyle 25 stroke:#33f,stroke-width:3px;
linkStyle 26 stroke:#36f,stroke-width:3px;
linkStyle 27 stroke:#33f,stroke-width:3px;
linkStyle 28 stroke:#33f,stroke-width:3px;
linkStyle 29 stroke:#33f,stroke-width:3px;
linkStyle 30 stroke:#33f,stroke-width:3px;
linkStyle 31 stroke:#33f,stroke-width:3px;
linkStyle 32 stroke:#33f,stroke-width:3px;
linkStyle 37 stroke:#33f,stroke-width:3px;
```

```mermaid
---
title: Full Adder -- 1 | 0 | 0
---
flowchart LR;

subgraph n1 [NAND];
  direction LR;
  n1ina[a] & n1inb[b] --> n1o[output];
end;

subgraph n2 [NAND];
  direction LR;
  n2ina[a] & n2inb[b] --> n2o[output];
end;

subgraph n3 [NAND];
  direction LR;
  n3ina[a] & n3inb[b] --> n3o[output];
end;

subgraph n4 [NAND];
  direction LR;
  n4ina[a] & n4inb[b] --> n4o[output];
end;

subgraph n5 [NAND];
  direction LR;
  n5ina[a] & n5inb[b] --> n5o[output];
end;

subgraph n6 [NAND];
  direction LR;
  n6ina[a] & n6inb[b] --> n6o[output];
end;

subgraph n7 [NAND];
  direction LR;
  n7ina[a] & n7inb[b] --> n7o[output];
end;

subgraph n8 [NAND];
  direction LR;
  n8ina[a] & n8inb[b] --> n8o[output];
end;

subgraph n9 [NAND];
  direction LR;
  n9ina[a] & n9inb[b] --> n9o[output];
end;

subgraph inputs [Inputs];
  direction TB;
  a[a];
  b[b];
  c[c];
end;

a[a]:::ON ---------> n1inb & n2ina;
b[b] --> n3ina & n4ina;
c[c] --> n4inb & n5inb;
n1o ---> n2inb & n6ina & n9ina;
n2o --> n7ina;
n3o --> n8ina;
n4o --> n3inb & n5ina & n6inb;
n5o --> n8inb;
n6o ----> h[h];
n7o --> l[l]:::ON;
n8o --> n1ina & n9inb;
n9o --> n7inb;
classDef ON stroke:#33f,stroke-width:3px;
linkStyle 1 stroke:#33f,stroke-width:3px;
linkStyle 2 stroke:#33f,stroke-width:3px;
linkStyle 3 stroke:#33f,stroke-width:3px;
linkStyle 5 stroke:#33f,stroke-width:3px;
linkStyle 8 stroke:#33f,stroke-width:3px;
linkStyle 10 stroke:#33f,stroke-width:3px;
linkStyle 11 stroke:#33f,stroke-width:3px;
linkStyle 13 stroke:#33f,stroke-width:3px;
linkStyle 14 stroke:#33f,stroke-width:3px;
linkStyle 15 stroke:#33f,stroke-width:3px;
linkStyle 16 stroke:#33f,stroke-width:3px;
linkStyle 18 stroke:#33f,stroke-width:3px;
linkStyle 19 stroke:#33f,stroke-width:3px;
linkStyle 24 stroke:#33f,stroke-width:3px;
linkStyle 25 stroke:#33f,stroke-width:3px;
linkStyle 26 stroke:#36f,stroke-width:3px;
linkStyle 28 stroke:#33f,stroke-width:3px;
linkStyle 29 stroke:#33f,stroke-width:3px;
linkStyle 30 stroke:#33f,stroke-width:3px;
linkStyle 31 stroke:#33f,stroke-width:3px;
linkStyle 32 stroke:#33f,stroke-width:3px;
linkStyle 34 stroke:#33f,stroke-width:3px;
linkStyle 37 stroke:#33f,stroke-width:3px;
```

```mermaid
---
title: Full Adder -- 0 | 1 | 0
---
flowchart LR;

subgraph n1 [NAND];
  direction LR;
  n1ina[a] & n1inb[b] --> n1o[output];
end;

subgraph n2 [NAND];
  direction LR;
  n2ina[a] & n2inb[b] --> n2o[output];
end;

subgraph n3 [NAND];
  direction LR;
  n3ina[a] & n3inb[b] --> n3o[output];
end;

subgraph n4 [NAND];
  direction LR;
  n4ina[a] & n4inb[b] --> n4o[output];
end;

subgraph n5 [NAND];
  direction LR;
  n5ina[a] & n5inb[b] --> n5o[output];
end;

subgraph n6 [NAND];
  direction LR;
  n6ina[a] & n6inb[b] --> n6o[output];
end;

subgraph n7 [NAND];
  direction LR;
  n7ina[a] & n7inb[b] --> n7o[output];
end;

subgraph n8 [NAND];
  direction LR;
  n8ina[a] & n8inb[b] --> n8o[output];
end;

subgraph n9 [NAND];
  direction LR;
  n9ina[a] & n9inb[b] --> n9o[output];
end;

subgraph inputs [Inputs];
  direction TB;
  a[a];
  b[b];
  c[c];
end;

a[a] ---------> n1inb & n2ina;
b[b]:::ON --> n3ina & n4ina;
c[c] --> n4inb & n5inb;
n1o ---> n2inb & n6ina & n9ina;
n2o --> n7ina;
n3o --> n8ina;
n4o --> n3inb & n5ina & n6inb;
n5o --> n8inb;
n6o ----> h[h];
n7o --> l[l]:::ON;
n8o --> n1ina & n9inb;
n9o --> n7inb;
classDef ON stroke:#33f,stroke-width:3px;
linkStyle 0 stroke:#33f,stroke-width:3px;
linkStyle 3 stroke:#33f,stroke-width:3px;
linkStyle 4 stroke:#33f,stroke-width:3px;
linkStyle 5 stroke:#33f,stroke-width:3px;
linkStyle 6 stroke:#33f,stroke-width:3px;
linkStyle 8 stroke:#33f,stroke-width:3px;
linkStyle 10 stroke:#33f,stroke-width:3px;
linkStyle 11 stroke:#33f,stroke-width:3px;
linkStyle 12 stroke:#33f,stroke-width:3px;
linkStyle 15 stroke:#33f,stroke-width:3px;
linkStyle 16 stroke:#33f,stroke-width:3px;
linkStyle 17 stroke:#33f,stroke-width:3px;
linkStyle 20 stroke:#33f,stroke-width:3px;
linkStyle 21 stroke:#33f,stroke-width:3px;
linkStyle 24 stroke:#33f,stroke-width:3px;
linkStyle 25 stroke:#33f,stroke-width:3px;
linkStyle 26 stroke:#36f,stroke-width:3px;
linkStyle 27 stroke:#33f,stroke-width:3px;
linkStyle 29 stroke:#33f,stroke-width:3px;
linkStyle 30 stroke:#33f,stroke-width:3px;
linkStyle 31 stroke:#33f,stroke-width:3px;
linkStyle 32 stroke:#33f,stroke-width:3px;
linkStyle 34 stroke:#33f,stroke-width:3px;
linkStyle 35 stroke:#33f,stroke-width:3px;
linkStyle 36 stroke:#33f,stroke-width:3px;
```

```mermaid
---
title: Full Adder -- 0 | 0 | 1
---
flowchart LR;

subgraph n1 [NAND];
  direction LR;
  n1ina[a] & n1inb[b] --> n1o[output];
end;

subgraph n2 [NAND];
  direction LR;
  n2ina[a] & n2inb[b] --> n2o[output];
end;

subgraph n3 [NAND];
  direction LR;
  n3ina[a] & n3inb[b] --> n3o[output];
end;

subgraph n4 [NAND];
  direction LR;
  n4ina[a] & n4inb[b] --> n4o[output];
end;

subgraph n5 [NAND];
  direction LR;
  n5ina[a] & n5inb[b] --> n5o[output];
end;

subgraph n6 [NAND];
  direction LR;
  n6ina[a] & n6inb[b] --> n6o[output];
end;

subgraph n7 [NAND];
  direction LR;
  n7ina[a] & n7inb[b] --> n7o[output];
end;

subgraph n8 [NAND];
  direction LR;
  n8ina[a] & n8inb[b] --> n8o[output];
end;

subgraph n9 [NAND];
  direction LR;
  n9ina[a] & n9inb[b] --> n9o[output];
end;

subgraph inputs [Inputs];
  direction TB;
  a[a];
  b[b];
  c[c];
end;

a[a] ---------> n1inb & n2ina;
b[b] --> n3ina & n4ina;
c[c]:::ON --> n4inb & n5inb;
n1o ---> n2inb & n6ina & n9ina;
n2o --> n7ina;
n3o --> n8ina;
n4o --> n3inb & n5ina & n6inb;
n5o --> n8inb;
n6o ----> h[h];
n7o --> l[l]:::ON;
n8o --> n1ina & n9inb;
n9o --> n7inb;
classDef ON stroke:#33f,stroke-width:3px;
linkStyle 0 stroke:#33f,stroke-width:3px;
linkStyle 3 stroke:#33f,stroke-width:3px;
linkStyle 5 stroke:#33f,stroke-width:3px;
linkStyle 7 stroke:#33f,stroke-width:3px;
linkStyle 8 stroke:#33f,stroke-width:3px;
linkStyle 9 stroke:#33f,stroke-width:3px;
linkStyle 10 stroke:#33f,stroke-width:3px;
linkStyle 11 stroke:#33f,stroke-width:3px;
linkStyle 12 stroke:#33f,stroke-width:3px;
linkStyle 14 stroke:#33f,stroke-width:3px;
linkStyle 16 stroke:#33f,stroke-width:3px;
linkStyle 17 stroke:#33f,stroke-width:3px;
linkStyle 22 stroke:#33f,stroke-width:3px;
linkStyle 23 stroke:#33f,stroke-width:3px;
linkStyle 24 stroke:#33f,stroke-width:3px;
linkStyle 25 stroke:#33f,stroke-width:3px;
linkStyle 26 stroke:#36f,stroke-width:3px;
linkStyle 27 stroke:#33f,stroke-width:3px;
linkStyle 28 stroke:#33f,stroke-width:3px;
linkStyle 29 stroke:#33f,stroke-width:3px;
linkStyle 30 stroke:#33f,stroke-width:3px;
linkStyle 31 stroke:#33f,stroke-width:3px;
linkStyle 34 stroke:#33f,stroke-width:3px;
linkStyle 35 stroke:#33f,stroke-width:3px;
linkStyle 36 stroke:#33f,stroke-width:3px;
```

```mermaid
---
title: Full Adder -- 1 | 1 | 0
---
flowchart LR;

subgraph n1 [NAND];
  direction LR;
  n1ina[a] & n1inb[b] --> n1o[output];
end;

subgraph n2 [NAND];
  direction LR;
  n2ina[a] & n2inb[b] --> n2o[output];
end;

subgraph n3 [NAND];
  direction LR;
  n3ina[a] & n3inb[b] --> n3o[output];
end;

subgraph n4 [NAND];
  direction LR;
  n4ina[a] & n4inb[b] --> n4o[output];
end;

subgraph n5 [NAND];
  direction LR;
  n5ina[a] & n5inb[b] --> n5o[output];
end;

subgraph n6 [NAND];
  direction LR;
  n6ina[a] & n6inb[b] --> n6o[output];
end;

subgraph n7 [NAND];
  direction LR;
  n7ina[a] & n7inb[b] --> n7o[output];
end;

subgraph n8 [NAND];
  direction LR;
  n8ina[a] & n8inb[b] --> n8o[output];
end;

subgraph n9 [NAND];
  direction LR;
  n9ina[a] & n9inb[b] --> n9o[output];
end;

subgraph inputs [Inputs];
  direction TB;
  a[a];
  b[b];
  c[c];
end;

a[a]:::ON ---------> n1inb & n2ina;
b[b]:::ON --> n3ina & n4ina;
c[c] --> n4inb & n5inb;
n1o ---> n2inb & n6ina & n9ina;
n2o --> n7ina;
n3o --> n8ina;
n4o --> n3inb & n5ina & n6inb;
n5o --> n8inb;
n6o ----> h[h]:::ON;
n7o --> l[l];
n8o --> n1ina & n9inb;
n9o --> n7inb;
classDef ON stroke:#33f,stroke-width:3px;
linkStyle 0 stroke:#33f,stroke-width:3px;
linkStyle 1 stroke:#33f,stroke-width:3px;
linkStyle 2 stroke:#33f,stroke-width:3px;
linkStyle 4 stroke:#33f,stroke-width:3px;
linkStyle 5 stroke:#33f,stroke-width:3px;
linkStyle 6 stroke:#33f,stroke-width:3px;
linkStyle 8 stroke:#33f,stroke-width:3px;
linkStyle 11 stroke:#33f,stroke-width:3px;
linkStyle 12 stroke:#33f,stroke-width:3px;
linkStyle 13 stroke:#33f,stroke-width:3px;
linkStyle 15 stroke:#33f,stroke-width:3px;
linkStyle 17 stroke:#33f,stroke-width:3px;
linkStyle 18 stroke:#33f,stroke-width:3px;
linkStyle 19 stroke:#33f,stroke-width:3px;
linkStyle 20 stroke:#33f,stroke-width:3px;
linkStyle 21 stroke:#33f,stroke-width:3px;
linkStyle 27 stroke:#33f,stroke-width:3px;
linkStyle 29 stroke:#33f,stroke-width:3px;
linkStyle 30 stroke:#33f,stroke-width:3px;
linkStyle 31 stroke:#33f,stroke-width:3px;
linkStyle 32 stroke:#33f,stroke-width:3px;
linkStyle 33 stroke:#33f,stroke-width:3px;
linkStyle 35 stroke:#33f,stroke-width:3px;
linkStyle 36 stroke:#33f,stroke-width:3px;
linkStyle 37 stroke:#33f,stroke-width:3px;
```

```mermaid
---
title: Full Adder -- 1 | 0 | 1
---
flowchart LR;

subgraph n1 [NAND];
  direction LR;
  n1ina[a] & n1inb[b] --> n1o[output];
end;

subgraph n2 [NAND];
  direction LR;
  n2ina[a] & n2inb[b] --> n2o[output];
end;

subgraph n3 [NAND];
  direction LR;
  n3ina[a] & n3inb[b] --> n3o[output];
end;

subgraph n4 [NAND];
  direction LR;
  n4ina[a] & n4inb[b] --> n4o[output];
end;

subgraph n5 [NAND];
  direction LR;
  n5ina[a] & n5inb[b] --> n5o[output];
end;

subgraph n6 [NAND];
  direction LR;
  n6ina[a] & n6inb[b] --> n6o[output];
end;

subgraph n7 [NAND];
  direction LR;
  n7ina[a] & n7inb[b] --> n7o[output];
end;

subgraph n8 [NAND];
  direction LR;
  n8ina[a] & n8inb[b] --> n8o[output];
end;

subgraph n9 [NAND];
  direction LR;
  n9ina[a] & n9inb[b] --> n9o[output];
end;

subgraph inputs [Inputs];
  direction TB;
  a[a];
  b[b];
  c[c];
end;

a[a]:::ON ---------> n1inb & n2ina;
b[b] --> n3ina & n4ina;
c[c]:::ON --> n4inb & n5inb;
n1o ---> n2inb & n6ina & n9ina;
n2o --> n7ina;
n3o --> n8ina;
n4o --> n3inb & n5ina & n6inb;
n5o --> n8inb;
n6o ----> h[h]:::ON;
n7o --> l[l];
n8o --> n1ina & n9inb;
n9o --> n7inb;
classDef ON stroke:#33f,stroke-width:3px;
linkStyle 0 stroke:#33f,stroke-width:3px;
linkStyle 1 stroke:#33f,stroke-width:3px;
linkStyle 2 stroke:#33f,stroke-width:3px;
linkStyle 5 stroke:#33f,stroke-width:3px;
linkStyle 7 stroke:#33f,stroke-width:3px;
linkStyle 8 stroke:#33f,stroke-width:3px;
linkStyle 9 stroke:#33f,stroke-width:3px;
linkStyle 11 stroke:#33f,stroke-width:3px;
linkStyle 12 stroke:#33f,stroke-width:3px;
linkStyle 13 stroke:#33f,stroke-width:3px;
linkStyle 14 stroke:#33f,stroke-width:3px;
linkStyle 17 stroke:#33f,stroke-width:3px;
linkStyle 18 stroke:#33f,stroke-width:3px;
linkStyle 19 stroke:#33f,stroke-width:3px;
linkStyle 22 stroke:#33f,stroke-width:3px;
linkStyle 23 stroke:#33f,stroke-width:3px;
linkStyle 27 stroke:#33f,stroke-width:3px;
linkStyle 28 stroke:#33f,stroke-width:3px;
linkStyle 29 stroke:#33f,stroke-width:3px;
linkStyle 30 stroke:#33f,stroke-width:3px;
linkStyle 31 stroke:#33f,stroke-width:3px;
linkStyle 33 stroke:#33f,stroke-width:3px;
linkStyle 35 stroke:#33f,stroke-width:3px;
linkStyle 36 stroke:#33f,stroke-width:3px;
linkStyle 37 stroke:#33f,stroke-width:3px;
```

```mermaid
---
title: Full Adder -- 0 | 1 | 1
---
flowchart LR;

subgraph n1 [NAND];
  direction LR;
  n1ina[a] & n1inb[b] --> n1o[output];
end;

subgraph n2 [NAND];
  direction LR;
  n2ina[a] & n2inb[b] --> n2o[output];
end;

subgraph n3 [NAND];
  direction LR;
  n3ina[a] & n3inb[b] --> n3o[output];
end;

subgraph n4 [NAND];
  direction LR;
  n4ina[a] & n4inb[b] --> n4o[output];
end;

subgraph n5 [NAND];
  direction LR;
  n5ina[a] & n5inb[b] --> n5o[output];
end;

subgraph n6 [NAND];
  direction LR;
  n6ina[a] & n6inb[b] --> n6o[output];
end;

subgraph n7 [NAND];
  direction LR;
  n7ina[a] & n7inb[b] --> n7o[output];
end;

subgraph n8 [NAND];
  direction LR;
  n8ina[a] & n8inb[b] --> n8o[output];
end;

subgraph n9 [NAND];
  direction LR;
  n9ina[a] & n9inb[b] --> n9o[output];
end;

subgraph inputs [Inputs];
  direction TB;
  a[a];
  b[b];
  c[c];
end;

a[a] ---------> n1inb & n2ina;
b[b]:::ON --> n3ina & n4ina;
c[c]:::ON --> n4inb & n5inb;
n1o ---> n2inb & n6ina & n9ina;
n2o --> n7ina;
n3o --> n8ina;
n4o --> n3inb & n5ina & n6inb;
n5o --> n8inb;
n6o ----> h[h]:::ON;
n7o --> l[l];
n8o --> n1ina & n9inb;
n9o --> n7inb;
classDef ON stroke:#33f,stroke-width:3px;
linkStyle 2 stroke:#33f,stroke-width:3px;
linkStyle 4 stroke:#33f,stroke-width:3px;
linkStyle 6 stroke:#33f,stroke-width:3px;
linkStyle 7 stroke:#33f,stroke-width:3px;
linkStyle 9 stroke:#33f,stroke-width:3px;
linkStyle 10 stroke:#33f,stroke-width:3px;
linkStyle 12 stroke:#33f,stroke-width:3px;
linkStyle 13 stroke:#33f,stroke-width:3px;
linkStyle 14 stroke:#33f,stroke-width:3px;
linkStyle 15 stroke:#33f,stroke-width:3px;
linkStyle 16 stroke:#33f,stroke-width:3px;
linkStyle 20 stroke:#33f,stroke-width:3px;
linkStyle 21 stroke:#33f,stroke-width:3px;
linkStyle 22 stroke:#33f,stroke-width:3px;
linkStyle 23 stroke:#33f,stroke-width:3px;
linkStyle 24 stroke:#33f,stroke-width:3px;
linkStyle 25 stroke:#33f,stroke-width:3px;
linkStyle 26 stroke:#36f,stroke-width:3px;
linkStyle 27 stroke:#33f,stroke-width:3px;
linkStyle 28 stroke:#33f,stroke-width:3px;
linkStyle 32 stroke:#33f,stroke-width:3px;
linkStyle 33 stroke:#33f,stroke-width:3px;
linkStyle 37 stroke:#33f,stroke-width:3px;
```

```mermaid
---
title: Full Adder -- 0 | 1 | 1
---
flowchart LR;

subgraph n1 [NAND];
  direction LR;
  n1ina[a] & n1inb[b] --> n1o[output];
end;

subgraph n2 [NAND];
  direction LR;
  n2ina[a] & n2inb[b] --> n2o[output];
end;

subgraph n3 [NAND];
  direction LR;
  n3ina[a] & n3inb[b] --> n3o[output];
end;

subgraph n4 [NAND];
  direction LR;
  n4ina[a] & n4inb[b] --> n4o[output];
end;

subgraph n5 [NAND];
  direction LR;
  n5ina[a] & n5inb[b] --> n5o[output];
end;

subgraph n6 [NAND];
  direction LR;
  n6ina[a] & n6inb[b] --> n6o[output];
end;

subgraph n7 [NAND];
  direction LR;
  n7ina[a] & n7inb[b] --> n7o[output];
end;

subgraph n8 [NAND];
  direction LR;
  n8ina[a] & n8inb[b] --> n8o[output];
end;

subgraph n9 [NAND];
  direction LR;
  n9ina[a] & n9inb[b] --> n9o[output];
end;

subgraph inputs [Inputs];
  direction TB;
  a[a];
  b[b];
  c[c];
end;

a[a]:::ON ---------> n1inb & n2ina;
b[b]:::ON --> n3ina & n4ina;
c[c]:::ON --> n4inb & n5inb;
n1o ---> n2inb & n6ina & n9ina;
n2o --> n7ina;
n3o --> n8ina;
n4o --> n3inb & n5ina & n6inb;
n5o --> n8inb;
n6o ----> h[h]:::ON;
n7o --> l[l]:::ON;
n8o --> n1ina & n9inb;
n9o --> n7inb;
classDef ON stroke:#33f,stroke-width:3px;
linkStyle 1 stroke:#33f,stroke-width:3px;
linkStyle 2 stroke:#33f,stroke-width:3px;
linkStyle 3 stroke:#33f,stroke-width:3px;
linkStyle 4 stroke:#33f,stroke-width:3px;
linkStyle 6 stroke:#33f,stroke-width:3px;
linkStyle 7 stroke:#33f,stroke-width:3px;
linkStyle 9 stroke:#33f,stroke-width:3px;
linkStyle 10 stroke:#33f,stroke-width:3px;
linkStyle 13 stroke:#33f,stroke-width:3px;
linkStyle 14 stroke:#33f,stroke-width:3px;
linkStyle 15 stroke:#33f,stroke-width:3px;
linkStyle 16 stroke:#33f,stroke-width:3px;
linkStyle 18 stroke:#33f,stroke-width:3px;
linkStyle 19 stroke:#33f,stroke-width:3px;
linkStyle 20 stroke:#33f,stroke-width:3px;
linkStyle 21 stroke:#33f,stroke-width:3px;
linkStyle 22 stroke:#33f,stroke-width:3px;
linkStyle 23 stroke:#33f,stroke-width:3px;
linkStyle 24 stroke:#33f,stroke-width:3px;
linkStyle 25 stroke:#33f,stroke-width:3px;
linkStyle 26 stroke:#36f,stroke-width:3px;
linkStyle 28 stroke:#33f,stroke-width:3px;
linkStyle 32 stroke:#33f,stroke-width:3px;
linkStyle 33 stroke:#33f,stroke-width:3px;
linkStyle 34 stroke:#33f,stroke-width:3px;
linkStyle 37 stroke:#33f,stroke-width:3px;
```

---

```mermaid
---
title: Simplified Full Adder (no I/O shown)
---
flowchart LR;

subgraph Full Adder;
  direction LR;
  fa1ina[input a] & fa1inb[input b] & fa1inc[input c] ~~~ fa1oh[output high] & fa1ol[output low];
end;
```
