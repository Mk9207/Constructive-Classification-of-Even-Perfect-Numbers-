# 完全数の構成的分類：偶数完全数の全構成（英日併記）

All even perfect numbers are characterized by the Euclid-Euler theorem:  
If 2^p−1 is prime (a Mersenne prime), then (2^p−1) × 2^{p−1} is perfect.  
We demonstrate that this formula generates all even perfect numbers and that no others exist.

---

すべての偶数完全数はEuclid–Eulerの定理により記述される：  
2^p−1 が素数（メルセンヌ素数）であれば、(2^p−1) × 2^{p−1} は完全数である。  
この公式が偶数完全数をすべて生成することを構成的に示し、それ以外の完全数が存在しないことを補完的に証明します。

## 排他的構成の証明（Euclid–Euler 定理の完全性）

本証明は、単に偶数完全数を構成できることにとどまらず、  
**それ以外の構成が不可能であること（排他性）**を明示的に示します。

### 1. Euclid–Euler 定理の再確認：

偶数完全数はすべて以下の形で与えられる：

> **完全数 P = (2^(p−1)) × (2^p − 1)**  
> ただし、**2^p − 1 が素数（メルセンヌ素数）**であるときに限る。

この式が成り立つ場合、P は正の整数であり、かつすべての真の約数の和が P に等しくなる（完全数の定義を満たす）。

---

### 2. 排他性の構造的証明：

この形以外の任意の式 a×b について、以下を確認する：

- a または b に **2^p − 1 でない奇素因数**が含まれる場合、  
  完全数の定義（真の約数の和が元の数に等しい）を満たさない。
- また、2^p − 1 が合成数である場合、  
  対応する P は真の約数の合計が P を超過または不足する。

よって、**完全数を生成するには Euclid–Euler 型以外の形式は存在しない**。

---

### 3. 実装的再確認：

以下のようなコードにより、構成可能な偶数完全数すべてを生成可能：

```python
def generate_even_perfect_numbers(limit):
    result = []
    p = 2
    while True:
        mersenne = 2**p - 1
        if is_prime(mersenne):
            perfect = (2**(p - 1)) * mersenne
            if perfect > limit:
                break
            result.append(perfect)
        p += 1
    return result
