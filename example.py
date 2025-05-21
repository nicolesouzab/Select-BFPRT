from bfprt import select_bfprt

x = [9, 6, 3, 21, 13]
y = 5
z = 3

print(f"Vetor: {x}")
print(f"Tamanho: {y}")

result = select_bfprt(x, y, z)
print(f"Resultado da busca: {result}")