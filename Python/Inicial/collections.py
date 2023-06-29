idade1 = 39
idade2 = 76
idade3 = 15
idade4 = 21

print(idade1)
print(idade2)
print(idade3)
print(idade4)

idades = [39, 76, 15, 21]
type(idades)

print(type(idades))
print(idades)
print(idades[3])

idades.append(87)

print(idades)

idades.remove(76)

print(idades)

idades.clear()

print(idades)

idades = [39, 76, 15, 21]

idades.insert(1, 87)

idades.extend([11, 25])

print(idades)

for idade in idades:
    print(idade + 1)

idades_prox_ano = []
for idade in idades:
    idades_prox_ano.append(idade + 1)

print(idades_prox_ano)

print([(idade + 1)for idade in idades])
