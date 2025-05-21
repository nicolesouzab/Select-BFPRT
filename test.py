import random
import time
from bfprt import select_bfprt

def generate_random_vector(size):
    return [random.randint(1, 1000) for _ in range(size)]

def test_bfprt(num_triplas, r=5):
    total_time = 0.0
    y = 100000  #vetor fixo
    for i in range(num_triplas):
        x = generate_random_vector(y)
        z = random.randint(1, y)

        start_time = time.perf_counter()
        result = select_bfprt(x, y, z, r)
        elapsed = time.perf_counter() - start_time
        total_time += elapsed

    tempo_medio_ms = (total_time / num_triplas) * 1000

    print(f"\nPara r = {r}")
    print(f"  - Tamanho fixo dos vetores (y): {y}")
    print(f"  - Testes realizados: {num_triplas}")
    print(f"  - Tempo médio por tripla: {tempo_medio_ms:.4f} ms")

if __name__ == "__main__":
    num_triplas = 200000
    for r in [3, 5, 7, 9, 11]:
        test_bfprt(num_triplas, r)
