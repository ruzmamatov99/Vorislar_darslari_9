#1. k va n butun sonlari berilgan (n > 0). k sonini n marta chiqaruvchi dastur tuzilsin.
# k = int(input("k = "))
# n = int(input("n = "))
# for i in range(n):
#     print(k)

    #2. a va b butun sonlari berilgan (a < b). a dan b gacha bo'lgan barcha butun sonlarni chiqaruvchi dastur.
# a = int(input("a = "))
# b = int(input("b = "))
# for i in range(a, b + 1):
#     print(i)

#3. a va b butun sonlari berilgan (a < b). a dan b gacha bo'lgan sonlarni kamayish tartibida chiqarish.
# a = int(input("a = "))
# b = int(input("b = "))
# for i in range(b, a - 1, -1):
#     print(i)

#4. 1 kg konfet narxi berilgan (haqiqiy son). 1 dan 10 kg gacha narxini chiqarish.
# price = float(input("1 kg konfet narxi = "))
# for i in range(1, 11):
#     print(f"{i} kg = {price * i}")

#5. 1 kg konfet narxi berilgan. 0.1, 0.2, ..., 0.9, 1 kg uchun narxlarni chiqarish.
# price = float(input("1 kg konfet narxi = "))
# for i in range(1, 11):
#     print(f"{i / 10} kg = {price * i / 10}")

#6. 1 kg konfet narxi berilgan. 1.2, 1.4, ..., 2 kg uchun narxni chiqarish.
# price = float(input("1 kg konfet narxi = "))
# x = 1.2
# while x <= 2.01:
#     print(f"{x:.1f} kg = {price * x:.2f}")
#     x += 0.2

#7. a va b butun sonlari berilgan (a < b). a dan b gacha bo‘lgan sonlar yig‘indisini topish.
# a = int(input("a = "))
# b = int(input("b = "))
# summa = 0
# for i in range(a, b + 1):
#     summa += i
# print("Yig‘indi:", summa)

#8. a va b butun sonlari berilgan (a < b). a dan b gacha bo‘lgan sonlar ko‘paytmasini topish.
# a = int(input("a = "))
# b = int(input("b = "))
# p = 1
# for i in range(a, b + 1):
#     p *= i
# print("Ko‘paytma:", p)

#9. a va b butun sonlari berilgan (a < b). a dan b gacha bo‘lgan sonlar kvadratlari yig‘indisini topish.
# a = int(input("a = "))
# b = int(input("b = "))
# s = 0
# for i in range(a, b + 1):
#     s += i ** 2
# print("Kvadratlar yig‘indisi:", s)

#10. n butun soni berilgan (n > 0). 1 + 1/2 + 1/3 + ... + 1/n ni hisoblash.
# n = int(input("n = "))
# s = 0
# for i in range(1, n + 1):
#     s += 1 / i
# print("Yig‘indi:", s)

#11. n butun soni berilgan. n^2 + (n+1)^2 + ... + (2n)^2 ni hisoblash.
# n = int(input("n = "))
# s = 0
# for i in range(n, 2 * n + 1):
#     s += i ** 2
# print("Natija:", s)

#12. n butun soni berilgan (n > 0). 1 * 2 * ... * n ni hisoblash.
# n = int(input("n = "))
# p = 1
# for i in range(1, n + 1):
#     p *= i
# print("Ko‘paytma (faktorial):", p)