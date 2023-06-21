# 4-bit Multi-Adder

## Logic

<!-- 128 permutations of the inputs... Not something I fancy writing. Let's try
and write a script for this instead. -->

|Input A2|Input A1|Input A0|Input B2|Input B1|Input B0|Input C|Output C|Output S0|Output S1|Output S2|Decimal|
|:------:|:------:|:------:|:------:|:------:|:------:|:-----:|:------:|:-------:|:-------:|:-------:|:-----:|
|       0|       0|       0|       0|       0|       0|      0|       0|        0|        0|        0|      0|
|       0|       0|       0|       0|       0|       0|      1|       0|        0|        0|        1|      1|
|       0|       0|       0|       0|       0|       1|      0|       0|        0|        0|        1|      1|
|       0|       0|       0|       0|       0|       1|      1|       0|        0|        1|        0|      2|
|       0|       0|       0|       0|       1|       0|      0|       0|        0|        1|        0|      2|
|       0|       0|       0|       0|       1|       0|      1|       0|        0|        1|        1|      3|
|       0|       0|       0|       0|       1|       1|      0|       0|        0|        1|        1|      3|
|       0|       0|       0|       0|       1|       1|      1|       0|        1|        0|        0|      4|
|       0|       0|       0|       1|       0|       0|      0|       0|        1|        0|        0|      4|
|       0|       0|       0|       1|       0|       0|      1|       0|        1|        0|        1|      5|
|       0|       0|       0|       1|       0|       1|      0|       0|        1|        0|        1|      5|
|       0|       0|       0|       1|       0|       1|      1|       0|        1|        1|        0|      6|
|       0|       0|       0|       1|       1|       0|      0|       0|        1|        1|        0|      6|
|       0|       0|       0|       1|       1|       0|      1|       0|        1|        1|        1|      7|
|       0|       0|       0|       1|       1|       1|      0|       0|        1|        1|        1|      7|
|       0|       0|       0|       1|       1|       1|      1|       1|        0|        0|        0|      8|
|       0|       0|       1|       0|       0|       0|      0|       0|        0|        0|        1|      1|
|       0|       0|       1|       0|       0|       0|      1|       0|        0|        1|        0|      2|
|       0|       0|       1|       0|       0|       1|      0|       0|        0|        1|        0|      2|
|       0|       0|       1|       0|       0|       1|      1|       0|        0|        1|        1|      3|
|       0|       0|       1|       0|       1|       0|      0|       0|        0|        1|        1|      3|
|       0|       0|       1|       0|       1|       0|      1|       0|        1|        0|        0|      4|
|       0|       0|       1|       0|       1|       1|      0|       0|        1|        0|        0|      4|
|       0|       0|       1|       0|       1|       1|      1|       0|        1|        0|        1|      5|
|       0|       0|       1|       1|       0|       0|      0|       0|        1|        0|        1|      5|
|       0|       0|       1|       1|       0|       0|      1|       0|        1|        1|        0|      6|
|       0|       0|       1|       1|       0|       1|      0|       0|        1|        1|        0|      6|
|       0|       0|       1|       1|       0|       1|      1|       0|        1|        1|        1|      7|
|       0|       0|       1|       1|       1|       0|      0|       0|        1|        1|        1|      7|
|       0|       0|       1|       1|       1|       0|      1|       1|        0|        0|        0|      8|
|       0|       0|       1|       1|       1|       1|      0|       1|        0|        0|        0|      8|
|       0|       0|       1|       1|       1|       1|      1|       1|        0|        0|        1|      9|
|       0|       1|       0|       0|       0|       0|      0|       0|        0|        1|        0|      2|
|       0|       1|       0|       0|       0|       0|      1|       0|        0|        1|        1|      3|
|       0|       1|       0|       0|       0|       1|      0|       0|        0|        1|        1|      3|
|       0|       1|       0|       0|       0|       1|      1|       0|        1|        0|        0|      4|
|       0|       1|       0|       0|       1|       0|      0|       0|        1|        0|        0|      4|
|       0|       1|       0|       0|       1|       0|      1|       0|        1|        0|        1|      5|
|       0|       1|       0|       0|       1|       1|      0|       0|        1|        0|        1|      5|
|       0|       1|       0|       0|       1|       1|      1|       0|        1|        1|        0|      6|
|       0|       1|       0|       1|       0|       0|      0|       0|        1|        1|        0|      6|
|       0|       1|       0|       1|       0|       0|      1|       0|        1|        1|        1|      7|
|       0|       1|       0|       1|       0|       1|      0|       0|        1|        1|        1|      7|
|       0|       1|       0|       1|       0|       1|      1|       1|        0|        0|        0|      8|
|       0|       1|       0|       1|       1|       0|      0|       1|        0|        0|        0|      8|
|       0|       1|       0|       1|       1|       0|      1|       1|        0|        0|        1|      9|
|       0|       1|       0|       1|       1|       1|      0|       1|        0|        0|        1|      9|
|       0|       1|       0|       1|       1|       1|      1|       1|        0|        1|        0|     10|
|       0|       1|       1|       0|       0|       0|      0|       0|        0|        1|        1|      3|
|       0|       1|       1|       0|       0|       0|      1|       0|        1|        0|        0|      4|
|       0|       1|       1|       0|       0|       1|      0|       0|        1|        0|        0|      4|
|       0|       1|       1|       0|       0|       1|      1|       0|        1|        0|        1|      5|
|       0|       1|       1|       0|       1|       0|      0|       0|        1|        0|        1|      5|
|       0|       1|       1|       0|       1|       0|      1|       0|        1|        1|        0|      6|
|       0|       1|       1|       0|       1|       1|      0|       0|        1|        1|        0|      6|
|       0|       1|       1|       0|       1|       1|      1|       0|        1|        1|        1|      7|
|       0|       1|       1|       1|       0|       0|      0|       0|        1|        1|        1|      7|
|       0|       1|       1|       1|       0|       0|      1|       1|        0|        0|        0|      8|
|       0|       1|       1|       1|       0|       1|      0|       1|        0|        0|        0|      8|
|       0|       1|       1|       1|       0|       1|      1|       1|        0|        0|        1|      9|
|       0|       1|       1|       1|       1|       0|      0|       1|        0|        0|        1|      9|
|       0|       1|       1|       1|       1|       0|      1|       1|        0|        1|        0|     10|
|       0|       1|       1|       1|       1|       1|      0|       1|        0|        1|        0|     10|
|       0|       1|       1|       1|       1|       1|      1|       1|        0|        1|        1|     11|
|       1|       0|       0|       0|       0|       0|      0|       0|        1|        0|        0|      4|
|       1|       0|       0|       0|       0|       0|      1|       0|        1|        0|        1|      5|
|       1|       0|       0|       0|       0|       1|      0|       0|        1|        0|        1|      5|
|       1|       0|       0|       0|       0|       1|      1|       0|        1|        1|        0|      6|
|       1|       0|       0|       0|       1|       0|      0|       0|        1|        1|        0|      6|
|       1|       0|       0|       0|       1|       0|      1|       0|        1|        1|        1|      7|
|       1|       0|       0|       0|       1|       1|      0|       0|        1|        1|        1|      7|
|       1|       0|       0|       0|       1|       1|      1|       1|        0|        0|        0|      8|
|       1|       0|       0|       1|       0|       0|      0|       1|        0|        0|        0|      8|
|       1|       0|       0|       1|       0|       0|      1|       1|        0|        0|        1|      9|
|       1|       0|       0|       1|       0|       1|      0|       1|        0|        0|        1|      9|
|       1|       0|       0|       1|       0|       1|      1|       1|        0|        1|        0|     10|
|       1|       0|       0|       1|       1|       0|      0|       1|        0|        1|        0|     10|
|       1|       0|       0|       1|       1|       0|      1|       1|        0|        1|        1|     11|
|       1|       0|       0|       1|       1|       1|      0|       1|        0|        1|        1|     11|
|       1|       0|       0|       1|       1|       1|      1|       1|        1|        0|        0|     12|
|       1|       0|       1|       0|       0|       0|      0|       0|        1|        0|        1|      5|
|       1|       0|       1|       0|       0|       0|      1|       0|        1|        1|        0|      6|
|       1|       0|       1|       0|       0|       1|      0|       0|        1|        1|        0|      6|
|       1|       0|       1|       0|       0|       1|      1|       0|        1|        1|        1|      7|
|       1|       0|       1|       0|       1|       0|      0|       0|        1|        1|        1|      7|
|       1|       0|       1|       0|       1|       0|      1|       1|        0|        0|        0|      8|
|       1|       0|       1|       0|       1|       1|      0|       1|        0|        0|        0|      8|
|       1|       0|       1|       0|       1|       1|      1|       1|        0|        0|        1|      9|
|       1|       0|       1|       1|       0|       0|      0|       1|        0|        0|        1|      9|
|       1|       0|       1|       1|       0|       0|      1|       1|        0|        1|        0|     10|
|       1|       0|       1|       1|       0|       1|      0|       1|        0|        1|        0|     10|
|       1|       0|       1|       1|       0|       1|      1|       1|        0|        1|        1|     11|
|       1|       0|       1|       1|       1|       0|      0|       1|        0|        1|        1|     11|
|       1|       0|       1|       1|       1|       0|      1|       1|        1|        0|        0|     12|
|       1|       0|       1|       1|       1|       1|      0|       1|        1|        0|        0|     12|
|       1|       0|       1|       1|       1|       1|      1|       1|        1|        0|        1|     13|
|       1|       1|       0|       0|       0|       0|      0|       0|        1|        1|        0|      6|
|       1|       1|       0|       0|       0|       0|      1|       0|        1|        1|        1|      7|
|       1|       1|       0|       0|       0|       1|      0|       0|        1|        1|        1|      7|
|       1|       1|       0|       0|       0|       1|      1|       1|        0|        0|        0|      8|
|       1|       1|       0|       0|       1|       0|      0|       1|        0|        0|        0|      8|
|       1|       1|       0|       0|       1|       0|      1|       1|        0|        0|        1|      9|
|       1|       1|       0|       0|       1|       1|      0|       1|        0|        0|        1|      9|
|       1|       1|       0|       0|       1|       1|      1|       1|        0|        1|        0|     10|
|       1|       1|       0|       1|       0|       0|      0|       1|        0|        1|        0|     10|
|       1|       1|       0|       1|       0|       0|      1|       1|        0|        1|        1|     11|
|       1|       1|       0|       1|       0|       1|      0|       1|        0|        1|        1|     11|
|       1|       1|       0|       1|       0|       1|      1|       1|        1|        0|        0|     12|
|       1|       1|       0|       1|       1|       0|      0|       1|        1|        0|        0|     12|
|       1|       1|       0|       1|       1|       0|      1|       1|        1|        0|        1|     13|
|       1|       1|       0|       1|       1|       1|      0|       1|        1|        0|        1|     13|
|       1|       1|       0|       1|       1|       1|      1|       1|        1|        1|        0|     14|
|       1|       1|       1|       0|       0|       0|      0|       0|        1|        1|        1|      7|
|       1|       1|       1|       0|       0|       0|      1|       1|        0|        0|        0|      8|
|       1|       1|       1|       0|       0|       1|      0|       1|        0|        0|        0|      8|
|       1|       1|       1|       0|       0|       1|      1|       1|        0|        0|        1|      9|
|       1|       1|       1|       0|       1|       0|      0|       1|        0|        0|        1|      9|
|       1|       1|       1|       0|       1|       0|      1|       1|        0|        1|        0|     10|
|       1|       1|       1|       0|       1|       1|      0|       1|        0|        1|        0|     10|
|       1|       1|       1|       0|       1|       1|      1|       1|        0|        1|        1|     11|
|       1|       1|       1|       1|       0|       0|      0|       1|        0|        1|        1|     11|
|       1|       1|       1|       1|       0|       0|      1|       1|        1|        0|        0|     12|
|       1|       1|       1|       1|       0|       1|      0|       1|        1|        0|        0|     12|
|       1|       1|       1|       1|       0|       1|      1|       1|        1|        0|        1|     13|
|       1|       1|       1|       1|       1|       0|      0|       1|        1|        0|        1|     13|
|       1|       1|       1|       1|       1|       0|      1|       1|        1|        1|        0|     14|
|       1|       1|       1|       1|       1|       1|      0|       1|        1|        1|        0|     14|
|       1|       1|       1|       1|       1|       1|      1|       1|        1|        1|        1|     15|

```mermaid
---
title: Multi-bit Adder | 4-bit Output
---
flowchart LR;

subgraph fa1 [Full Adder];
  direction LR;
  fa1ina[a] & fa1inb[b] & fa1inc[c] ~~~ fa1oh[high] & fa1ol[low];
end;

subgraph fa2 [Full Adder];
  direction LR;
  fa2ina[a] & fa2inb[b] & fa2inc[c] ~~~ fa2oh[high] & fa2ol[low];
end;

subgraph fa3 [Full Adder];
  direction LR;
  fa3ina[a] & fa3inb[b] & fa3inc[c] ~~~ fa3oh[high] & fa3ol[low];
end;

subgraph inputs [Inputs];
  direction TB;
  subgraph a# [3-bit number];
    a0[a0];
    a1[a1];
    a2[a2];
  end
  subgraph b# [3-bit number];
    b0[b0];
    b1[b1];
    b2[b2];
  end
  subgraph c# [1-bit carry];
    c0[c0];
  end
end;

subgraph outputs [Outputs];
  direction TB;
  s0[s0];
  s1[s1];
  s2[s2];
  co[c];
end;

a0 --> fa1ina;
b0 --> fa1inb;
c0 --> fa1inc;
fa1ol --> s0;
a1 --> fa2ina;
b1 --> fa2inb;
fa1oh --> fa2inc;
fa2ol --> s1;
a2 --> fa3ina;
b2 --> fa3inb;
fa2oh --> fa3inc;
fa3ol --> s2;
fa3oh --> co;

linkStyle 18 stroke:#33f,stroke-width:3px;
linkStyle 19 stroke:#33f,stroke-width:3px;
linkStyle 20 stroke:#33f,stroke-width:3px;
linkStyle 21 stroke:#33f,stroke-width:3px;
linkStyle 22 stroke:#3f3,stroke-width:3px;
linkStyle 23 stroke:#3f3,stroke-width:3px;
linkStyle 24 stroke:#3f3,stroke-width:3px;
linkStyle 25 stroke:#3f3,stroke-width:3px;
linkStyle 26 stroke:#f33,stroke-width:3px;
linkStyle 27 stroke:#f33,stroke-width:3px;
linkStyle 28 stroke:#f33,stroke-width:3px;
linkStyle 29 stroke:#f33,stroke-width:3px;
linkStyle 30 stroke:#ff3,stroke-width:3px;
```

---

```mermaid
---
title: Multi-bit Adder | 5-bit Output
---
flowchart LR;

subgraph fa1 [Full Adder];
  direction LR;
  fa1ina[a] & fa1inb[b] & fa1inc[c] ~~~ fa1oh[high] & fa1ol[low];
end;

subgraph fa2 [Full Adder];
  direction LR;
  fa2ina[a] & fa2inb[b] & fa2inc[c] ~~~ fa2oh[high] & fa2ol[low];
end;

subgraph fa3 [Full Adder];
  direction LR;
  fa3ina[a] & fa3inb[b] & fa3inc[c] ~~~ fa3oh[high] & fa3ol[low];
end;

subgraph fa4 [Full Adder];
  direction LR;
  fa4ina[a] & fa4inb[b] & fa4inc[c] ~~~ fa4oh[high] & fa4ol[low];
end;

subgraph inputs [Inputs];
  direction TB;
  subgraph a# [4-bit number];
    a0[a0];
    a1[a1];
    a2[a2];
    a3[a3];
  end
  subgraph b# [4-bit number];
    b0[b0];
    b1[b1];
    b2[b2];
    b3[b3];
  end
  subgraph c# [1-bit carry];
    c0[c0];
  end
end;

subgraph outputs [Outputs];
  direction TB;
  s0[s0];
  s1[s1];
  s2[s2];
  s3[s3];
  co[c];
end;

a0 --> fa1ina;
b0 --> fa1inb;
c0 --> fa1inc;
fa1ol --> s0;
a1 --> fa2ina;
b1 --> fa2inb;
fa1oh --> fa2inc;
fa2ol --> s1;
a2 --> fa3ina;
b2 --> fa3inb;
fa2oh --> fa3inc;
fa3ol --> s2;
a3 --> fa4ina;
b3 --> fa4inb;
fa3oh --> fa4inc;
fa4ol --> s3;
fa4oh --> co;

linkStyle 24 stroke:#33f,stroke-width:3px;
linkStyle 25 stroke:#33f,stroke-width:3px;
linkStyle 26 stroke:#33f,stroke-width:3px;
linkStyle 27 stroke:#33f,stroke-width:3px;
linkStyle 28 stroke:#3f3,stroke-width:3px;
linkStyle 29 stroke:#3f3,stroke-width:3px;
linkStyle 30 stroke:#3f3,stroke-width:3px;
linkStyle 31 stroke:#3f3,stroke-width:3px;
linkStyle 32 stroke:#f33,stroke-width:3px;
linkStyle 33 stroke:#f33,stroke-width:3px;
linkStyle 34 stroke:#f33,stroke-width:3px;
linkStyle 35 stroke:#f33,stroke-width:3px;
linkStyle 36 stroke:#ff3,stroke-width:3px;
linkStyle 37 stroke:#ff3,stroke-width:3px;
linkStyle 38 stroke:#ff3,stroke-width:3px;
linkStyle 39 stroke:#ff3,stroke-width:3px;
linkStyle 40 stroke:#f3f,stroke-width:3px;
```
