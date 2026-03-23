
vector = []
vector_reverce = []

for i in range(1, 6):
    vector.append(int(input(f'Num1 [{ i }]: ')))

for i in range(4, -1, -1):
    vector_reverce.append(vector[i])

print(vector)
print(vector_reverce)