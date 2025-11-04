"""· O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
· Ro'yxatning uzunligini konsolga chiqaring
· sorted () funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
· sorted () yordamida ro'yxatni teskari tartibda konsolga chiqaring
· Asl ro'yxatni qaytadan konsolga chiqaring
· reverse () metodi yordamida ro'yxatni ortidan boshlab chiqaring
· sort () metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
· 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
· Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
· Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
· Ro'yxatdagi elementlar sonini hisoblang
· Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
· taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting"""

# 1. O'zingizga ma'lum davlatlarning ro'yxatini tuzish
davlatlar = ["O'zbekiston", "AQSH", "Kanada", "Germaniya", "Yaponiya", "Braziliya", "Misr"]

# 2. Ro'yxatni konsolga chiqarish
print("1. Asl davlatlar ro'yxati:", davlatlar)

# 3. Ro'yxatning uzunligini konsolga chiqarish
print("2. Ro'yxatning uzunligi:", len(davlatlar))

# 4. sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqarish
print("3. sorted() bilan tartiblangan ro'yxat (asl ro'yxat o'zgarmaydi):", sorted(davlatlar))

# 5. sorted() yordamida ro'yxatni teskari tartibda konsolga chiqarish
print("4. sorted() bilan teskari tartiblangan ro'yxat (asl ro'yxat o'zgarmaydi):", sorted(davlatlar, reverse=True))

# 6. Asl ro'yxatni qaytadan konsolga chiqarish
print("5. Asl ro'yxat (o'zgarmaganligini ko'rish uchun):", davlatlar)

# 7. reverse() metodi yordamida ro'yxatni ortidan boshlab chiqarish (asl ro'yxatni o'zgartiradi)
davlatlar.reverse()
print("6. reverse() metodi bilan teskarisiga aylantirilgan asl ro'yxat:", davlatlar)

# Asl tartibga qaytarish (keyingi amallar uchun)
davlatlar.reverse()

# 8. sort() metodi yordamida ro'yxatni avval alifbo bo'yicha tartiblash (asl ro'yxatni o'zgartiradi)
davlatlar.sort()
print("7. sort() metodi bilan alifbo tartibida tartiblangan asl ro'yxat:", davlatlar)

# 9. sort() metodi yordamida ro'yxatni alifboga teskari tartibda tartiblash (asl ro'yxatni o'zgartiradi)
davlatlar.sort(reverse=True)
print("8. sort() metodi bilan alifboga teskari tartibda tartiblangan asl ro'yxat:", davlatlar)

# 10. 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzish (range() dan foydalanamiz)
juft_sonlar = list(range(120, 1201, 2))
# Ro'yxatning bir qismini ko'rsatish
print("\n9. Juft sonlar ro'yxatining boshlanishi:", juft_sonlar[:5])
print("   Juft sonlar ro'yxatining oxiri:", juft_sonlar[-5:])

# 11. Ro'yxatdagi sonlar yig'indisini hisoblash
yigindi = sum(juft_sonlar)
print("10. Ro'yxatdagi barcha sonlar yig'indisi:", yigindi)

# 12. Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblash
ayirma = max(juft_sonlar) - min(juft_sonlar)
print("11. Eng katta va eng kichik son o'rtasidagi ayirma:", ayirma)
print(f"    (Eng katta: {max(juft_sonlar)}, Eng kichik: {min(juft_sonlar)})")

# 13. Ro'yxatdagi elementlar sonini hisoblash
elementlar_soni = len(juft_sonlar)
print("12. Ro'yxatdagi elementlar soni:", elementlar_soni)

# 14. Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqarish

# Boshidan 20 ta
boshidan_20 = juft_sonlar[:20]
print("13. Ro'yxat boshidan 20 ta qiymat:", boshidan_20)

# O'rtasidan 20 ta (O'rta indeksni topish)
orta_indeks = len(juft_sonlar) // 2
orta_boshi = orta_indeks - 10
orta_oxiri = orta_indeks + 10
o_rtadan_20 = juft_sonlar[orta_boshi:orta_oxiri]
print("14. Ro'yxat o'rtasidan 20 ta qiymat:", o_rtadan_20)

# Oxiridan 20 ta
oxiridan_20 = juft_sonlar[-20:]
print("15. Ro'yxat oxiridan 20 ta qiymat:", oxiridan_20)

# 15. taomlar degan ro'yxat yaratish va ichiga istalgan 5ta taomni kiritish
taomlar = ["Palov", "Manti", "Somsa", "Lag'mon", "Shashlik"]
print("\n16. Taomlar ro'yxati:", taomlar)