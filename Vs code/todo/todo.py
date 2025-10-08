import sqlite3
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox, simpledialog
from datetime import datetime
import threading, time

# ------------------- VERİTABANI -------------------
def veritabani_olustur():
    conn = sqlite3.connect("gorevler.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS gorevler (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ad TEXT,
                    kategori TEXT,
                    tarih TEXT,
                    durum TEXT
                )""")
    conn.commit()
    conn.close()

def gorev_ekle(ad, kategori, tarih):
    conn = sqlite3.connect("gorevler.db")
    c = conn.cursor()
    c.execute("INSERT INTO gorevler (ad, kategori, tarih, durum) VALUES (?, ?, ?, ?)",
              (ad, kategori, tarih, "⏳ Beklemede"))
    conn.commit()
    conn.close()

def gorevleri_getir():
    conn = sqlite3.connect("gorevler.db")
    c = conn.cursor()
    c.execute("SELECT * FROM gorevler")
    veriler = c.fetchall()
    conn.close()
    return veriler

def gorev_tamamla(id):
    conn = sqlite3.connect("gorevler.db")
    c = conn.cursor()
    c.execute("UPDATE gorevler SET durum=? WHERE id=?", ("✅ Tamamlandı", id))
    conn.commit()
    conn.close()

def gorev_sil(id):
    conn = sqlite3.connect("gorevler.db")
    c = conn.cursor()
    c.execute("DELETE FROM gorevler WHERE id=?", (id,))
    conn.commit()
    conn.close()

# ------------------- GUI -------------------
def listeyi_guncelle():
    for row in tree.get_children():
        tree.delete(row)
    for gorev in gorevleri_getir():
        tree.insert("", END, values=gorev)

def yeni_gorev():
    ad = simpledialog.askstring("Yeni Görev", "Görev adını giriniz:")
    if not ad:
        return
    kategori = simpledialog.askstring("Kategori", "Kategori giriniz (iş, okul, kişisel, genel):")
    if not kategori:
        kategori = "genel"
    tarih = simpledialog.askstring("Tarih", "Tarih/Saat giriniz (örn: 2025-09-23 18:30):")
    if not tarih:
        tarih = datetime.now().strftime("%Y-%m-%d %H:%M")
    gorev_ekle(ad, kategori, tarih)
    listeyi_guncelle()

def gorev_tamamla_gui():
    secilen = tree.selection()
    if not secilen:
        return
    id = tree.item(secilen)["values"][0]
    gorev_tamamla(id)
    listeyi_guncelle()

def gorev_sil_gui():
    secilen = tree.selection()
    if not secilen:
        return
    id = tree.item(secilen)["values"][0]
    gorev_sil(id)
    listeyi_guncelle()

def filtrele(kategori):
    for row in tree.get_children():
        tree.delete(row)
    for gorev in gorevleri_getir():
        if kategori == "Hepsi" or gorev[2] == kategori:
            tree.insert("", END, values=gorev)

def alarm_kontrol():
    while True:
        simdi = datetime.now().strftime("%Y-%m-%d %H:%M")
        for gorev in gorevleri_getir():
            if gorev[3] == simdi and gorev[4] != "✅ Tamamlandı":
                messagebox.showinfo("⏰ Alarm", f"{gorev[1]} görevini yapma zamanı!")
        time.sleep(30)

# ------------------- ARAYÜZ -------------------
veritabani_olustur()

root = tb.Window(themename="superhero")
root.title("📝 Modern To-Do Uygulaması")
root.geometry("750x500")

# STİL
style = tb.Style()
style.configure("Treeview", font=("Segoe UI", 11), rowheight=28)
style.configure("Treeview.Heading", font=("Segoe UI", 12, "bold"))

# BAŞLIK
baslik = tb.Label(root, text="📋 Görev Yöneticisi", 
                  font=("Segoe UI", 20, "bold"))
baslik.pack(pady=10)

# TABLO
tree = tb.Treeview(root, 
                   columns=("ID", "Görev", "Kategori", "Tarih", "Durum"), 
                   show="headings", height=15, bootstyle=INFO)
tree.heading("ID", text="ID")
tree.heading("Görev", text="Görev")
tree.heading("Kategori", text="Kategori")
tree.heading("Tarih", text="Tarih/Saat")
tree.heading("Durum", text="Durum")
tree.column("ID", width=40)
tree.pack(pady=10, fill=BOTH, expand=True)

# BUTONLAR
btn_frame = tb.Frame(root)
btn_frame.pack(pady=5)

tb.Button(btn_frame, text="➕ Görev Ekle", bootstyle="success",
          command=yeni_gorev).grid(row=0, column=0, padx=5)

tb.Button(btn_frame, text="✅ Tamamla", bootstyle="info",
          command=gorev_tamamla_gui).grid(row=0, column=1, padx=5)

tb.Button(btn_frame, text="🗑 Sil", bootstyle="danger",
          command=gorev_sil_gui).grid(row=0, column=2, padx=5)

# FİLTRE
filtre_frame = tb.Frame(root)
filtre_frame.pack(pady=5)

for kat in ["Hepsi", "iş", "okul", "kişisel", "genel"]:
    tb.Button(filtre_frame, text=kat.capitalize(),
              bootstyle="secondary",
              command=lambda k=kat: filtrele(k)).pack(side=LEFT, padx=3)

# PROGRAM BAŞLAT
listeyi_guncelle()
t = threading.Thread(target=alarm_kontrol, daemon=True)
t.start()
root.mainloop()
