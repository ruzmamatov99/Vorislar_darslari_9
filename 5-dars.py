# string, methods, f"" string

# ism = 'bobur'
# familiya = 'murodov'
# otchestva = 'anvarovich'
# FIO =f"Assalomu alaykum {familiya} {ism} {otchestva}!"
# print(FIO.title())
# print(f"Assalomu alaykum {familiya} {ism} {otchestva}!")


# meva = 'anor, olma, shaftoli, anjir'
# txt = f"bobur hello {meva} yisanmi"
# x = txt.capitalize()
# print(x)


# lower(), casefold() matndagi barcha katta harflarni kichik harfga o'zgartiradi
# ism = 'Ibodulla Ahmedov'
# txt = "Hello, And Welcome To My World!"
# x = txt.casefold()
# print(x)
# print(ism.lower())


# centr() string malumotning o'rtasiga bo'sh joy joylashtiradi
# txt = "banana"
# x = txt.center(150)
# print(x)


#count() string malumotda nechta ma'lum bir so'z yoki harf borligini hisoblaydi
# txt = "I love apples, apple are my favourite fruit"
# x = txt.count("a")
# print(x)


# endswith() string ma'lumot ma'lum bir so'z yoki harf bilan tugashini tekshiradi
# txt ="Hello, welcome to my world."
# x = txt.endswith(".")
# print(x)


# expantabs() string malumotdagi tab belgilarini bosh joy bilan almashtiradi
# txt = "K\tamol\tbek"
# x = txt.expandtabs(3)
# print(x)


# find() string malumotda ma'lum bir so'z yoki harfning indeksini qaytaradi
# txt = "Hello, welcome to my world."
# x = txt.find(".")
# print(x)


# ism = input("Ismingizni kiriting: ")
# yosh = int(input("Yoshingizni kiriting: "))
# manzil = input("Manzilingizni kiriting: ")
# maktab = input("Maktabingizni kiriting: ")
# qiziqish = input("Qiziqishlaringizni kiriting: ")
# jura = input("Yaqin insonlaringizni kiriting: ")

# print(f"Hurmatli {ism.title()} ning yoshi {yosh} da, \n Manzili {manzil.title()} da joylashgan \n {maktab} maktabda o'qiydi. \n Uning qiziqishlari {qiziqish.title()} va Eng yaqin insonlari {jura.title()} dan iborat.")