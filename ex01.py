termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

'''valor = termo
for c in range(termo, 11):
    if valor == termo:
        print(valor)
        valor = valor + razao
    else:
        print(valor)
        valor = valor + razao'''
decimo = termo + (10 - 1) * razao

for c in range(termo, decimo + razao, razao):
    print('{}'.format(c), end='-> ')
print('FIM')
