a = input('введите название товара:')
push = input('введите массу товара:')
push = push.replace('ml', '')
x = a[0:3]
x = x.upper()
alpha = x + push
print(alpha)
