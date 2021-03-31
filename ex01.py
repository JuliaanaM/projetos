termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

decimo = termo + (10 - 1) * razao
print('......PROGRESSÃO ARITMÉTICA......')
for c in range(termo, decimo + razao, razao):
    print('{}'.format(c), end='-> ')
print('FIM')
