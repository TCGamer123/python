n = input('Digite algo: ')
print('{} é númerico ?'.format(n), n.isnumeric())
print('{} é alphabetico ?'.format(n), n.isalpha())
print('{} é alphanumerico ?'.format(n), n.isalnum())
print('{} so contém letras maiusculas ?'.format(n), n.isupper())
print('{} so contém letras minusculas ?'.format(n), n.islower())
