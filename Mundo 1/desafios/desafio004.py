Cores = {'White':' \033[0;30;47m',
'Invertido':' \033[7;30;47m',
'Bold':' \033[1;30;47m',
}


v = input("Digite algo: ")

print('O tipo primitivo desse número é', type(v))
print("É alfanumérico?", v.isalnum())
print("É alfabético?", v.isalpha())
print("É ASCII?", v.isascii())
print("É decimal?", v.isdecimal())
print("É dígito?", v.isdigit())
print("É numérico?", v.isnumeric())
