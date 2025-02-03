def verificar_data(data):
    try:
        dia, mes, ano = map(int, data.split('/'))
        if 1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= ano <= 2100:
            return True
        else:
            return "Data inválida"
    except ValueError:
        return "Data inválida"

# Exemplos de uso
print(verificar_data("15/08/2021"))  # True
print(verificar_data("31/02/2020"))  # Data inválida
print(verificar_data("01/13/2020"))  # Data inválida
print(verificar_data("32/12/2020"))  # Data inválida
print(verificar_data("15/08/1899"))  # Data inválida