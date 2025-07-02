# Generate all even perfect numbers from Mersenne primes
# メルセンヌ素数から偶数完全数を生成

def is_prime(n):
    # Check if n is prime / 素数判定
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def mersenne_primes(limit):
    # Find Mersenne primes up to limit / limit以下のメルセンヌ素数を探す
    result = []
    for p in range(2, limit):
        m = 2**p - 1
        if is_prime(m):
            result.append(p)
    return result

def even_perfect_numbers(limit):
    # Generate even perfect numbers from Mersenne primes / 偶数完全数を生成
    result = []
    for p in mersenne_primes(limit):
        m = 2**p - 1
        perfect = m * 2**(p-1)
        result.append(perfect)
    return result

# Test / テスト実行
if __name__ == "__main__":
    for n in even_perfect_numbers(32):
        print(n)