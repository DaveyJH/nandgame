# XOR Gate

## Logic

|Input A|Input B|Output|
|:-----:|:-----:|:----:|
|      0|      0|     0|
|      1|      0|     1|
|      0|      1|     1|
|      1|      1|     0|

## Usage

High output if only one input is high.

---

```mermaid
---
title: XOR -- 0 | 0
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

a[a] --> n1ina & n2ina;
b[b] --> n1inb & n3inb;
n1o --> n2inb & n3ina;
n2o --> n4ina;
n3o --> n4inb;
n4o --> res[result];
linkStyle 3 stroke:#33f,stroke-width:3px;
linkStyle 4 stroke:#33f,stroke-width:3px;
linkStyle 6 stroke:#33f,stroke-width:3px;
linkStyle 7 stroke:#33f,stroke-width:3px;
linkStyle 12 stroke:#33f,stroke-width:3px;
linkStyle 13 stroke:#33f,stroke-width:3px;
linkStyle 14 stroke:#33f,stroke-width:3px;
linkStyle 15 stroke:#33f,stroke-width:3px;
```

```mermaid
---
title: XOR -- 1 | 0
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

a[a]:::ON --> n1ina & n2ina;
b[b] --> n1inb & n3inb;
n1o --> n2inb & n3ina;
n2o --> n4ina;
n3o --> n4inb;
n4o --> res[result]:::ON;
classDef ON stroke:#33f,stroke-width:3px;
linkStyle 0 stroke:#33f,stroke-width:3px;
linkStyle 2 stroke:#33f,stroke-width:3px;
linkStyle 3 stroke:#33f,stroke-width:3px;
linkStyle 4 stroke:#33f,stroke-width:3px;
linkStyle 7 stroke:#33f,stroke-width:3px;
linkStyle 8 stroke:#33f,stroke-width:3px;
linkStyle 9 stroke:#33f,stroke-width:3px;
linkStyle 12 stroke:#33f,stroke-width:3px;
linkStyle 13 stroke:#33f,stroke-width:3px;
linkStyle 15 stroke:#33f,stroke-width:3px;
linkStyle 16 stroke:#33f,stroke-width:3px;
```

```mermaid
---
title: XOR -- 0 | 1
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

a[a] --> n1ina & n2ina;
b[b]:::ON --> n1inb & n3inb;
n1o --> n2inb & n3ina;
n2o --> n4ina;
n3o --> n4inb;
n4o --> res[result]:::ON;
classDef ON stroke:#33f,stroke-width:3px;
linkStyle 1 stroke:#33f,stroke-width:3px;
linkStyle 3 stroke:#33f,stroke-width:3px;
linkStyle 4 stroke:#33f,stroke-width:3px;
linkStyle 5 stroke:#33f,stroke-width:3px;
linkStyle 6 stroke:#33f,stroke-width:3px;
linkStyle 10 stroke:#33f,stroke-width:3px;
linkStyle 11 stroke:#33f,stroke-width:3px;
linkStyle 12 stroke:#33f,stroke-width:3px;
linkStyle 13 stroke:#33f,stroke-width:3px;
linkStyle 14 stroke:#33f,stroke-width:3px;
linkStyle 16 stroke:#33f,stroke-width:3px;
```

```mermaid
---
title: XOR -- 1 | 1
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

a[a]:::ON --> n1ina & n2ina;
b[b]:::ON --> n1inb & n3inb;
n1o --> n2inb & n3ina;
n2o --> n4ina;
n3o --> n4inb;
n4o --> res[result];
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
linkStyle 14 stroke:#33f,stroke-width:3px;
linkStyle 15 stroke:#33f,stroke-width:3px;
```

---

```mermaid
---
title: Simplified XOR (no I/O shown)
---
flowchart LR;

subgraph XOR;
  direction LR;
  o1i[input a] & o2i[input b] --> a1o[output];
end;
```
