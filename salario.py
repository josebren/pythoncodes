print('#######################################')
sal = float(input('qual o seu salario: '))
print('#######################################')

#calcula o salario final
if (sal <= 1.250):
    fsal = (sal * 1.15)
else:
    fsal = (sal * 1.10)
#print o salario final
print('--------------------------------------')
print('o seu salario final irá ser de: {} R$'.format(fsal))
print('--------------------------------------')
