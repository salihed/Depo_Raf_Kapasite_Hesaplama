import tkinter as tk
from tkinter import ttk

def hesapla():
    try:
        yillik_butce_tonaji = float(yillik_butce_tonaji_entry.get())
        palet_basina_agirlik = float(palet_basina_agirlik_entry.get())
        stok_gun_sayisi = float(stok_gun_sayisi_entry.get())
        donemsel_gun_sayisi = float(donemsel_gun_sayisi_entry.get())

        yillik_palet_sayisi = yillik_butce_tonaji / (palet_basina_agirlik/1000)
        gunluk_palet_sayisi = (yillik_palet_sayisi * stok_gun_sayisi) / donemsel_gun_sayisi

        # sonucu belirttiğiniz formatta formatlayın
        formatli_sonuc = "{:,.0f}".format(gunluk_palet_sayisi).replace(",", "X").replace(".", ",").replace("X", ".")

        sonuc_label.config(text=f"İhtiyaç (palet): {formatli_sonuc}")
    except ValueError:
        sonuc_label.config(text="Lütfen tüm değerleri doğru girdiğinizden emin olun.")

app = tk.Tk()
app.title("Depo Raf Hesaplama")

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Etiketler ve giriş kutucukları
ttk.Label(frame, text="Yıllık Bütçe (Ton):").grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
yillik_butce_tonaji_entry = ttk.Entry(frame)
yillik_butce_tonaji_entry.grid(column=1, row=0, padx=5, pady=5)

ttk.Label(frame, text="Palet Başına Ağırlık (KG):").grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
palet_basina_agirlik_entry = ttk.Entry(frame)
palet_basina_agirlik_entry.grid(column=1, row=1, padx=5, pady=5)

ttk.Label(frame, text="Stok Gün Sayısı:").grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
stok_gun_sayisi_entry = ttk.Entry(frame)
stok_gun_sayisi_entry.grid(column=1, row=2, padx=5, pady=5)

ttk.Label(frame, text="Dönemsel Gün Sayısı:").grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
donemsel_gun_sayisi_entry = ttk.Entry(frame)
donemsel_gun_sayisi_entry.grid(column=1, row=3, padx=5, pady=5)

# Hesapla butonu
hesapla_button = ttk.Button(frame, text="Hesapla", command=hesapla)
hesapla_button.grid(column=1, row=4, pady=20)

# Sonuç etiketi
sonuc_label = ttk.Label(frame, text="")
sonuc_label.grid(column=1, row=5, padx=5, pady=5)

app.mainloop()
