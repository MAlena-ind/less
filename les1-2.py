# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. 
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. 
# Объяснить полученный результат.

a = 5
b = 6

# И: При логическом побитовом И двоичный разряд результата равен 1, 
# когда оба соответствующих бита первого и второго операнда = 1. 
# 101 & 110 = 100 (4 двоичная)
n = bin(a&b)
print(n, int(n, 2))

# ИЛИ: Двоичный разряд результата равен 0 только тогда, 
# когда оба соответствующих бита в равны 0. 
# 101 | 110 = 111 (7 двоичная)
n = bin(a|b)
print(n, int(n, 2))

# Побитовый сдвиг вправо.
# 101 >> 2 = 1
n = bin(a>>2)
print(n, int(n, 2))

# Побитовый сдвиг влево.
# 101 << 2 = 101000
n = bin(a<<2)
print(n, int(n, 2))

# Побитовое число 5 равно 101. 
# При побитовом сдвиге вправо биты сдвигаются вправо на указанное кол-во единиц. Остается только первая 1.
# При побитовом сдвиге влево биты сдвигаются влево на указанное кол-во единиц. На пустые 
# места встают нули, если число положительное, 10100.