min = int(input("Введите количество минут: "))
sms = int(input("Введите количество смс: "))
minsum = 0
smssum = 0
tax = 4.4
nal = 1.05
d_min = 2.5
d_sms = 1.5
sum = 150
total = 0
if min > 50:
    minsum = (min - 50) * d_min
    print("Будет переплата за минуты в размере: ")
else: 
    print("Минуты в норме")
if sms > 50: 
    smssum = (sms - 50) * d_sms
    print("Будет переплата за смс в размере: ")
else: 
    print("Тариф в норме")
totalprice = (sum + minsum + smssum + tax)*nal 
print("Итого:", "%.2f" % totalprice)