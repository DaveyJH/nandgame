# 16-bit Adder

## Logic

<!-- 8,589,934,592 permutations of the inputs...  NOPE! -->

Given the high number of permutations for this logic table (2³³), I have not
generated it. It follows the same logic as the 4 & 5-bit adders but with a _lot_
more digits!

I am not certain that this is the optimal solution for a 16-bit adder; it uses
140 NAND gates (9 per full-adder, 5 for the half-adder). It should be noted that
the nandgame website appears to use a full-adder, as opposed to a half-adder, in
their provided 16-bit adder which means an output is wasted. This configuration
would increase the NAND gates used to 144.

## Usage

Adds two 16-bit numbers and a 1-bit carry.

The output of this has a maximum decimal value of 131,071 (2³³ × 2 - 2 + 1).
The minus 2 accounts for numbers starting at 0.

16-bit numbers are often represented using hexadecimal nibbles. 65535 is
represented as `ffff` (Remember, we start at 0!). `ffff` plus `ffff` equals
`1fffe`. Add the carry bit to get a maximum hex value output of `1ffff`. Note
that the carry bit does, as always, just add 1 to the next position.

---

```mermaid
---
title: 16-bit Adder
---
flowchart LR;

subgraph ha [Half Adder];
  direction LR;
  haina[a] & hainb[b] ~~~ haoh[high] & haol[low];
end;

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

subgraph fa5 [Full Adder];
  direction LR;
  fa5ina[a] & fa5inb[b] & fa5inc[c] ~~~ fa5oh[high] & fa5ol[low];
end;

subgraph fa6 [Full Adder];
  direction LR;
  fa6ina[a] & fa6inb[b] & fa6inc[c] ~~~ fa6oh[high] & fa6ol[low];
end;

subgraph fa7 [Full Adder];
  direction LR;
  fa7ina[a] & fa7inb[b] & fa7inc[c] ~~~ fa7oh[high] & fa7ol[low];
end;

subgraph fa8 [Full Adder];
  direction LR;
  fa8ina[a] & fa8inb[b] & fa8inc[c] ~~~ fa8oh[high] & fa8ol[low];
end;

subgraph fa9 [Full Adder];
  direction LR;
  fa9ina[a] & fa9inb[b] & fa9inc[c] ~~~ fa9oh[high] & fa9ol[low];
end;

subgraph fa10 [Full Adder];
  direction LR;
  fa10ina[a] & fa10inb[b] & fa10inc[c] ~~~ fa10oh[high] & fa10ol[low];
end;

subgraph fa11 [Full Adder];
  direction LR;
  fa11ina[a] & fa11inb[b] & fa11inc[c] ~~~ fa11oh[high] & fa11ol[low];
end;

subgraph fa12 [Full Adder];
  direction LR;
  fa12ina[a] & fa12inb[b] & fa12inc[c] ~~~ fa12oh[high] & fa12ol[low];
end;

subgraph fa13 [Full Adder];
  direction LR;
  fa13ina[a] & fa13inb[b] & fa13inc[c] ~~~ fa13oh[high] & fa13ol[low];
end;

subgraph fa14 [Full Adder];
  direction LR;
  fa14ina[a] & fa14inb[b] & fa14inc[c] ~~~ fa14oh[high] & fa14ol[low];
end;

subgraph fa15 [Full Adder];
  direction LR;
  fa15ina[a] & fa15inb[b] & fa15inc[c] ~~~ fa15oh[high] & fa15ol[low];
end;

subgraph inputs [Inputs];
  direction TB;
  subgraph a# [16-but number];
    a0[a0];
    a1[a1];
    a2[a2];
    a3[a3];
    a4[a4];
    a5[a5];
    a6[a6];
    a7[a7];
    a8[a8];
    a9[a9];
    a10[a10];
    a11[a11];
    a12[a12];
    a13[a13];
    a14[a14];
    a15[a15];
  end
  subgraph b# [16-but number];
    b0[b0];
    b1[b1];
    b2[b2];
    b3[b3];
    b4[b4];
    b5[b5];
    b6[b6];
    b7[b7];
    b8[b8];
    b9[b9];
    b10[b10];
    b11[b11];
    b12[b12];
    b13[b13];
    b14[b14];
    b15[b15];
  end
end;

subgraph outputs [Outputs];
  direction TB;
  s0[s0];
  s1[s1];
  s2[s2];
  s3[s3];
  s4[s4];
  s5[s5];
  s6[s6];
  s7[s7];
  s8[s8];
  s9[s9];
  s10[s10];
  s11[s11];
  s12[s12];
  s13[s13];
  s14[s14];
  s15[s15];
  co[c];
end;


a0 --> haina;
b0 --> hainb;
haol --> s0;
a1 --> fa1ina;
b1 --> fa1inb;
haoh --> fa1inc;
fa1ol --> s1;
fa1oh --> fa2inc;
a2 --> fa2ina;
b2 --> fa2inb;
fa2ol --> s2;
fa2oh --> fa3inc;
a3 --> fa3ina;
b3 --> fa3inb;
fa3ol --> s3;
fa3oh --> fa4inc;
a4 --> fa4ina;
b4 --> fa4inb;
fa4ol --> s4;
fa4oh --> fa5inc;
a5 --> fa5ina;
b5 --> fa5inb;
fa5ol --> s5;
fa5oh --> fa6inc;
a6 --> fa6ina;
b6 --> fa6inb;
fa6ol --> s6;
fa6oh --> fa7inc;
a7 --> fa7ina;
b7 --> fa7inb;
fa7ol --> s7;
fa7oh --> fa8inc;
a8 --> fa8ina;
b8 --> fa8inb;
fa8ol --> s8;
fa8oh --> fa9inc;
a9 --> fa9ina;
b9 --> fa9inb;
fa9ol --> s9;
fa9oh --> fa10inc;
a10 --> fa10ina;
b10 --> fa10inb;
fa10ol --> s10;
fa10oh --> fa11inc;
a11 --> fa11ina;
b11 --> fa11inb;
fa11ol --> s11;
fa11oh --> fa12inc;
a12 --> fa12ina;
b12 --> fa12inb;
fa12ol --> s12;
fa12oh --> fa13inc;
a13 --> fa13ina;
b13 --> fa13inb;
fa13ol --> s13;
fa13oh --> fa14inc;
a14 --> fa14ina;
b14 --> fa14inb;
fa14ol --> s14;
fa14oh --> fa15inc;
a15 --> fa15ina;
b15 --> fa15inb;
fa15ol --> s15;
fa15oh --> co;

linkStyle 94 stroke:#33f,stroke-width:3px;
linkStyle 95 stroke:#33f,stroke-width:3px;
linkStyle 96 stroke:#33f,stroke-width:3px;
linkStyle 97 stroke:#3f3,stroke-width:3px;
linkStyle 98 stroke:#3f3,stroke-width:3px;
linkStyle 99 stroke:#3f3,stroke-width:3px;
linkStyle 100 stroke:#3f3,stroke-width:3px;
linkStyle 101 stroke:#f33,stroke-width:3px;
linkStyle 102 stroke:#f33,stroke-width:3px;
linkStyle 103 stroke:#f33,stroke-width:3px;
linkStyle 104 stroke:#f33,stroke-width:3px;
linkStyle 105 stroke:#ff3,stroke-width:3px;
linkStyle 106 stroke:#ff3,stroke-width:3px;
linkStyle 107 stroke:#ff3,stroke-width:3px;
linkStyle 108 stroke:#ff3,stroke-width:3px;
linkStyle 109 stroke:#f3f,stroke-width:3px;
linkStyle 110 stroke:#f3f,stroke-width:3px;
linkStyle 111 stroke:#f3f,stroke-width:3px;
linkStyle 112 stroke:#f3f,stroke-width:3px;
linkStyle 113 stroke:#3ff,stroke-width:3px;
linkStyle 114 stroke:#3ff,stroke-width:3px;
linkStyle 115 stroke:#3ff,stroke-width:3px;
linkStyle 116 stroke:#3ff,stroke-width:3px;
linkStyle 117 stroke:#33f,stroke-width:3px;
linkStyle 118 stroke:#33f,stroke-width:3px;
linkStyle 119 stroke:#33f,stroke-width:3px;
linkStyle 120 stroke:#33f,stroke-width:3px;
linkStyle 121 stroke:#3f3,stroke-width:3px;
linkStyle 122 stroke:#3f3,stroke-width:3px;
linkStyle 123 stroke:#3f3,stroke-width:3px;
linkStyle 124 stroke:#3f3,stroke-width:3px;
linkStyle 125 stroke:#f33,stroke-width:3px;
linkStyle 126 stroke:#f33,stroke-width:3px;
linkStyle 127 stroke:#f33,stroke-width:3px;
linkStyle 128 stroke:#f33,stroke-width:3px;
linkStyle 129 stroke:#ff3,stroke-width:3px;
linkStyle 130 stroke:#ff3,stroke-width:3px;
linkStyle 131 stroke:#ff3,stroke-width:3px;
linkStyle 132 stroke:#ff3,stroke-width:3px;
linkStyle 133 stroke:#f3f,stroke-width:3px;
linkStyle 134 stroke:#f3f,stroke-width:3px;
linkStyle 135 stroke:#f3f,stroke-width:3px;
linkStyle 136 stroke:#f3f,stroke-width:3px;
linkStyle 137 stroke:#3ff,stroke-width:3px;
linkStyle 138 stroke:#3ff,stroke-width:3px;
linkStyle 139 stroke:#3ff,stroke-width:3px;
linkStyle 140 stroke:#3ff,stroke-width:3px;
linkStyle 141 stroke:#33f,stroke-width:3px;
linkStyle 142 stroke:#33f,stroke-width:3px;
linkStyle 143 stroke:#33f,stroke-width:3px;
linkStyle 144 stroke:#33f,stroke-width:3px;
linkStyle 145 stroke:#3f3,stroke-width:3px;
linkStyle 146 stroke:#3f3,stroke-width:3px;
linkStyle 147 stroke:#3f3,stroke-width:3px;
linkStyle 148 stroke:#3f3,stroke-width:3px;
linkStyle 149 stroke:#f33,stroke-width:3px;
linkStyle 150 stroke:#f33,stroke-width:3px;
linkStyle 151 stroke:#f33,stroke-width:3px;
linkStyle 152 stroke:#f33,stroke-width:3px;
linkStyle 153 stroke:#ff3,stroke-width:3px;
linkStyle 154 stroke:#ff3,stroke-width:3px;
linkStyle 155 stroke:#ff3,stroke-width:3px;
linkStyle 156 stroke:#ff3,stroke-width:3px;
linkStyle 157 stroke:#f3f,stroke-width:3px;
```
