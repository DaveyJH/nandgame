# Half Adder

## Logic

|Input A|Input B|Output H|Output L|
|:-----:|:-----:|:------:|:------:|
|      0|      0|       0|       0|
|      1|      0|       0|       1|
|      0|      1|       0|       1|
|      1|      1|       1|       0|

## Usage

Adds two bits.

- Output H is high if both inputs are high.
- Output L is high if only one input is high.

---

```mermaid
---
title: Half Adder -- 0 | 0
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

subgraph i1 [Invert];
  direction LR;
  i1i[input] --> i1o[output];
end;

a[a] --> n1ina & n2ina;
b[b] --> n1inb & n3inb;
n1o --> i1i & n2inb & n3ina;
i1o ----> oh[high];
n2o --> n4ina;
n3o --> n4inb;
n4o --> ol[low];
linkStyle 3 stroke:#33f,stroke-width:3px;
linkStyle 4 stroke:#33f,stroke-width:3px;
linkStyle 6 stroke:#33f,stroke-width:3px;
linkStyle 7 stroke:#33f,stroke-width:3px;
linkStyle 13 stroke:#33f,stroke-width:3px;
linkStyle 14 stroke:#33f,stroke-width:3px;
linkStyle 15 stroke:#33f,stroke-width:3px;
linkStyle 17 stroke:#33f,stroke-width:3px;
linkStyle 18 stroke:#33f,stroke-width:3px;
```

```mermaid
---
title: Half Adder -- 1 | 0
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

subgraph i1 [Invert];
  direction LR;
  i1i[input] --> i1o[output];
end;

a[a]:::ON --> n1ina & n2ina;
b[b] --> n1inb & n3inb;
n1o --> i1i & n2inb & n3ina;
i1o ----> oh[high];
n2o --> n4ina;
n3o --> n4inb;
n4o --> ol[low]:::ON;
classDef ON stroke:#33f,stroke-width:3px;
linkStyle 0 stroke:#33f,stroke-width:3px;
linkStyle 2 stroke:#33f,stroke-width:3px;
linkStyle 3 stroke:#33f,stroke-width:3px;
linkStyle 4 stroke:#33f,stroke-width:3px;
linkStyle 7 stroke:#33f,stroke-width:3px;
linkStyle 9 stroke:#33f,stroke-width:3px;
linkStyle 10 stroke:#33f,stroke-width:3px;
linkStyle 13 stroke:#33f,stroke-width:3px;
linkStyle 14 stroke:#33f,stroke-width:3px;
linkStyle 15 stroke:#33f,stroke-width:3px;
linkStyle 18 stroke:#33f,stroke-width:3px;
linkStyle 19 stroke:#33f,stroke-width:3px;
```

```mermaid
---
title: Half Adder -- 0 | 1
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

subgraph i1 [Invert];
  direction LR;
  i1i[input] --> i1o[output];
end;

a[a] --> n1ina & n2ina;
b[b]:::ON --> n1inb & n3inb;
n1o --> i1i & n2inb & n3ina;
i1o ----> oh[high];
n2o --> n4ina;
n3o --> n4inb;
n4o --> ol[low]:::ON;
classDef ON stroke:#33f,stroke-width:3px;
linkStyle 1 stroke:#33f,stroke-width:3px;
linkStyle 3 stroke:#33f,stroke-width:3px;
linkStyle 4 stroke:#33f,stroke-width:3px;
linkStyle 5 stroke:#33f,stroke-width:3px;
linkStyle 6 stroke:#33f,stroke-width:3px;
linkStyle 7 stroke:#33f,stroke-width:3px;
linkStyle 11 stroke:#33f,stroke-width:3px;
linkStyle 12 stroke:#33f,stroke-width:3px;
linkStyle 13 stroke:#33f,stroke-width:3px;
linkStyle 14 stroke:#33f,stroke-width:3px;
linkStyle 15 stroke:#33f,stroke-width:3px;
linkStyle 17 stroke:#33f,stroke-width:3px;
linkStyle 19 stroke:#33f,stroke-width:3px;
```

```mermaid
---
title: Half Adder -- 1 | 1
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

subgraph i1 [Invert];
  direction LR;
  i1i[input] --> i1o[output];
end;

a[a]:::ON --> n1ina & n2ina;
b[b]:::ON --> n1inb & n3inb;
n1o --> i1i & n2inb & n3ina;
i1o ----> oh[high]:::ON;
n2o --> n4ina;
n3o --> n4inb;
n4o --> ol[low];
classDef ON stroke:#33f,stroke-width:3px;
linkStyle 0 stroke:#33f,stroke-width:3px;
linkStyle 1 stroke:#33f,stroke-width:3px;
linkStyle 2 stroke:#33f,stroke-width:3px;
linkStyle 5 stroke:#33f,stroke-width:3px;
linkStyle 6 stroke:#33f,stroke-width:3px;
linkStyle 7 stroke:#33f,stroke-width:3px;
linkStyle 8 stroke:#33f,stroke-width:3px;
linkStyle 9 stroke:#33f,stroke-width:3px;
linkStyle 10 stroke:#33f,stroke-width:3px;
linkStyle 11 stroke:#33f,stroke-width:3px;
linkStyle 12 stroke:#33f,stroke-width:3px;
linkStyle 16 stroke:#33f,stroke-width:3px;
linkStyle 17 stroke:#33f,stroke-width:3px;
linkStyle 18 stroke:#33f,stroke-width:3px;
```

---

```mermaid
---
title: Simplified Half Adder (no I/O shown)
---
flowchart LR;

subgraph Half Adder;
  direction LR;
  ha1ina[input a] & ha1inb[input b] ~~~ ha1oh[output high] & ha1ol[output low];
end;
```
