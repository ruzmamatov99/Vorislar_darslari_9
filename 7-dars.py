import tkinter as tk
from tkinter import font

def ekranga_kiritish(qiymat):
    """Tugmalar bosilganda qiymatni ekran (kiritish maydoni)ga qo'shadi."""
    hozirgi = kiritish_maydoni.get()
    kiritish_maydoni.delete(0, tk.END)
    kiritish_maydoni.insert(0, hozirgi + str(qiymat))

def tozalash():
    """Ekran (kiritish maydoni)ni tozalaydi."""
    kiritish_maydoni.delete(0, tk.END)

def hisoblash():
    """Kiritish maydonidagi ifodani hisoblaydi va natijani ko'rsatadi."""
    try:
        ifoda = kiritish_maydoni.get()
        # 'eval' xavfli bo'lishi mumkin, lekin oddiy kalkulyator uchun qulay
        natija = str(eval(ifoda))
        tozalash()
        kiritish_maydoni.insert(0, natija)
    except ZeroDivisionError:
        tozalash()
        kiritish_maydoni.insert(0, "Nolga bo'lish xatosi")
    except Exception:
        tozalash()
        kiritish_maydoni.insert(0, "Xatolik")

# 1. Asosiy oyna (window) yaratish
oyna = tk.Tk()
oyna.title("Kalkulyator")
oyna.geometry("300x450")
oyna.resizable(0, 0) # O'lchamini o'zgartirishni o'chirish

# Ranglar sozlamasi
rang_fon = "#2E2E2E"       # To'q kulrang
rang_son = "#FFFFFF"       # Oq (sonlar rangi)
rang_amal = "#FFA500"      # To'q sariq (amal tugmalari)
rang_tozalash = "#8B0000"  # To'q qizil (Tozalash/C)
rang_hisoblash = "#008000" # Yashil (=)

# Oyna fonini sozlash
oyna.configure(bg=rang_fon)

# Fontni sozlash
katta_font = font.Font(family='Arial', size=20)
tugma_font = font.Font(family='Arial', size=14, weight='bold')

# 2. Natija/Kiritish maydoni (Entry Widget)
kiritish_maydoni = tk.Entry(oyna, 
                            width=15, 
                            font=katta_font, 
                            bd=10, 
                            relief=tk.SUNKEN, # Kiritish maydonining shakli
                            justify='right', # Matnni o'ng tomonga hizalash
                            bg="#F0F0F0", # Yengil kulrang fon
                            fg="#000000") # Qora matn
kiritish_maydoni.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# 3. Tugmalar Layoutini yaratish
tugma_matnlari = [
    ('C', 1, 0, rang_tozalash), ('/', 1, 3, rang_amal),
    ('7', 2, 0, rang_son), ('8', 2, 1, rang_son), ('9', 2, 2, rang_son), ('*', 2, 3, rang_amal),
    ('4', 3, 0, rang_son), ('5', 3, 1, rang_son), ('6', 3, 2, rang_son), ('-', 3, 3, rang_amal),
    ('1', 4, 0, rang_son), ('2', 4, 1, rang_son), ('3', 4, 2, rang_son), ('+', 4, 3, rang_amal),
    ('0', 5, 0, rang_son), ('.', 5, 1, rang_son), ('=', 5, 2, rang_hisoblash), # '=' tugmasi keyinroq qo'shiladi
]

# 4. Tugmalarni yaratish va joylashtirish
r = 1 # Qator (row) 0 band
for (matn, row, col, rang) in tugma_matnlari:
    # '=' tugmasi butun qatorni egallashi uchun alohida sozlanadi
    if matn == '=':
        tugma = tk.Button(oyna, 
                          text=matn, 
                          font=tugma_font, 
                          fg=rang_fon, # Matn rangi qora
                          bg=rang, 
                          padx=20, 
                          pady=20,
                          relief=tk.RAISED, # Tugmaning shakli/ko'rinishi
                          command=hisoblash)
        # "=" tugmasi 5-qatorning 2-va 3-ustunlarini egallaydi
        tugma.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=5, pady=5)
    
    # Qolgan tugmalar
    else:
        tugma = tk.Button(oyna, 
                          text=matn, 
                          font=tugma_font, 
                          fg=rang_fon if rang == rang_tozalash else "#000000", # C tugmasini qora fon ustida oq rang qilish
                          bg=rang, 
                          padx=20, 
                          pady=20,
                          relief=tk.RAISED,
                          command=lambda m=matn: tozalash() if m == 'C' else ekranga_kiritish(m))
        
        tugma.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# 5. Tugmalarni oynaga moslash (kengaytirish)
for i in range(1, 6):
    oyna.grid_rowconfigure(i, weight=1)
for i in range(4):
    oyna.grid_columnconfigure(i, weight=1)

# Asosiy tsiklni ishga tushirish (oynani doimo ochiq ushlab turish)
oyna.mainloop()