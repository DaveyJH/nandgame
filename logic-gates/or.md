# OR Gate

## Logic

|Input A|Input B|Output|
|:-----:|:-----:|:----:|
|      0|      0|     0|
|      1|      0|     1|
|      0|      1|     1|
|      1|      1|     1|

## Usage

High output if at least one input is high.

---

```mermaid
---
title: OR -- 0 | 0
---
flowchart LR;

subgraph i1 [Invert];
  direction LR;
  i1i[input] --> i1o[output];
end;

subgraph i2 [Invert];
  direction LR;
  i2i[input] --> i2o[output];
end;

subgraph n1 [NAND];
  direction LR;
  n1ina[a] & n1inb[b] --> n1o[output];
end;

a[a] --> i1i;
b[b] --> i2i;
i1o --> n1ina;
i2o --> n1inb;
n1o --> res[result];
linkStyle 0 stroke:#33f,stroke-width:3px;
linkStyle 1 stroke:#33f,stroke-width:3px;
linkStyle 2 stroke:#33f,stroke-width:3px;
linkStyle 3 stroke:#33f,stroke-width:3px;
linkStyle 6 stroke:#33f,stroke-width:3px;
linkStyle 7 stroke:#33f,stroke-width:3px;
```

```mermaid
---
title: OR -- 1 | 0
---
flowchart LR;

subgraph i1 [Invert];
  direction LR;
  i1i[input] --> i1o[output];
end;

subgraph i2 [Invert];
  direction LR;
  i2i[input] --> i2o[output];
end;

subgraph n1 [NAND];
  direction LR;
  n1ina[a] & n1inb[b] --> n1o[output];
end;

a[a]:::ON --> i1i;
b[b] --> i2i;
i1o --> n1ina;
i2o --> n1inb;
n1o --> res[result]:::ON;
classDef ON stroke:#33f,stroke-width:3px;
linkStyle 1 stroke:#33f,stroke-width:3px;
linkStyle 3 stroke:#33f,stroke-width:3px;
linkStyle 4 stroke:#33f,stroke-width:3px;
linkStyle 7 stroke:#33f,stroke-width:3px;
linkStyle 8 stroke:#33f,stroke-width:3px;
```

```mermaid
---
title: OR -- 0 | 1
---
flowchart LR;

subgraph i1 [Invert];
  direction LR;
  i1i[input] --> i1o[output];
end;

subgraph i2 [Invert];
  direction LR;
  i2i[input] --> i2o[output];
end;

subgraph n1 [NAND];
  direction LR;
  n1ina[a] & n1inb[b] --> n1o[output];
end;

a[a] --> i1i;
b[b]:::ON --> i2i;
i1o --> n1ina;
i2o --> n1inb;
n1o --> res[result]:::ON;
classDef ON stroke:#33f,stroke-width:3px;
linkStyle 0 stroke:#33f,stroke-width:3px;
linkStyle 2 stroke:#33f,stroke-width:3px;
linkStyle 5 stroke:#33f,stroke-width:3px;
linkStyle 6 stroke:#33f,stroke-width:3px;
linkStyle 8 stroke:#33f,stroke-width:3px;
```

```mermaid
---
title: OR -- 1 | 1
---
flowchart LR;

subgraph i1 [Invert];
  direction LR;
  i1i[input] --> i1o[output];
end;

subgraph i2 [Invert];
  direction LR;
  i2i[input] --> i2o[output];
end;

subgraph n1 [NAND];
  direction LR;
  n1ina[a] & n1inb[b] --> n1o[output];
end;

a[a]:::ON --> i1i;
b[b]:::ON --> i2i;
i1o --> n1ina;
i2o --> n1inb;
n1o --> res[result]:::ON;
classDef ON stroke:#33f,stroke-width:3px;
linkStyle 4 stroke:#33f,stroke-width:3px;
linkStyle 5 stroke:#33f,stroke-width:3px;
linkStyle 8 stroke:#33f,stroke-width:3px;
```

---

```mermaid
---
title: Simplified OR (no I/O shown)
---
flowchart LR;

subgraph OR;
  direction LR;
  o1i[input a] & o2i[input b] --> a1o[output];
end;
```
