"""
 for loop sikl yaratishda ishlatiladi
"""

# oquvchilar = ["kamolbek", "boburbek", "atxambek", "lazizbek", "mirkomil", "sayfulloh"]
# print(f"Assalomu alaykum hurmatli {oquvchilar[0].title()}, ishlar qanday")
# print(f"Assalomu alaykum hurmatli {oquvchilar[1].title()}, ishlar qanday")
# print(f"Assalomu alaykum hurmatli {oquvchilar[2].title()}, ishlar qanday")
# print(f"Assalomu alaykum hurmatli {oquvchilar[3].title()}, ishlar qanday")
# print(f"Assalomu alaykum hurmatli {oquvchilar[4].title()}, ishlar qanday")
# print(f"Assalomu alaykum hurmatli {oquvchilar[5].title()}, ishlar qanday")

# for ism in oquvchilar:
#     print(f"Assalomu alaykum {ism.title()}")
#     print(f"Xayr hurmatli {ism.upper()}")


# raqamlar = list((1,5,9,-8,63))
# for k in raqamlar:
#     print(k**2)

# raqamlar = list(range(30,91))
# for raqam in raqamlar:
#     print(f"{raqam} sonni to'qqizga bo'lganda{raqam/9} ga teng")


sonlar2 = []
sonlar = list(range(27,54,7))

print(f"Asl royhat : {sonlar}")
for son in sonlar:
    sonlar2.append(son**4)
print(f"4-darajaga oshgan royhat {sonlar2}")