s = input("Введите пин код:")
if s.isnumeric() and len(s) in (4, 6):
    print("Пин-код верный")
else:
    print("Ошибка, попробуйте снова")
