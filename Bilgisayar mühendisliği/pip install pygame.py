import sqlite3
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox, simpledialog
from datetime import datetime
import threading, time

DB = "todo.db"

# ------------------- VERİTABANI -------------------
def veritabani_olustur():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS gorevler (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 gorev TEXT,
                 kategori TEXT,
                 tarih TEXT,
                 tamamlandi INTEGER)''')
    conn.commit()
    conn.close()

def gorev_ekle(gorev, kategori, tarih):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT INTO gorevler (gorev, kategori, tarih, tamamlandi) VALUES (?, ?, ?, ?)",
              (gorev, kategori, tarih, 0))
    conn.commit()
    conn.close()

def gorevleri_getir(filtre=None):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    if filtre:
        c.execute("SELECT * FROM gorevler WHERE kategori=? ORDER BY tamamlandi, tarih", (filtre,))
    else:
        c.execute("SELECT * FROM gorevler ORDER BY tamamlandi, tarih")
    veriler = c.fetchall()
    conn.close()
    return veriler

def gorev_sil(gorev_id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("DELETE FROM gorevler WHERE id=?", (gorev_id,))
    conn.commit()
    conn.close()

def gorev_tamamla(gorev_id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("UPDATE gorevler SET tamamlandi=1 WHERE id=?", (gorev_id,))
    conn.commit()
    conn.close()

# ------------------- ALARM -------------------
def alarm_kontrol():
    while True:
        simdi = datetime.now().strftime("%Y-%m-%d %H:%M")
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("SELECT gorev, kategori FROM gorevler WHERE tarih=? AND tamamlandi=0", (simdi,))
        veriler = c.fetchall()
        conn.close()
        for v in veriler:
            messagebox.showwarning("🔔 Alarm", f"Görev zamanı geldi:\n{v[0]} ({v[1]})")
        time.sleep(30)

# ------------------- GUI FONKSİYONLARI -------------------
def listeyi_guncelle(filtre=None):
    for i in tree.get_children():
        tree.delete(i)
    gorevler = gorevleri_getir(filtre)
    for g in gorevler:
        durum = "✅" if g[4] else "❌"
        tarih = g[3] if g[3] else "-"
        tree.insert("", END, values=(g[0], g[1], g[2], tarih, durum))

def yeni_gorev():
    gorev = simpledialog.askstring("Görev", "Görev girin:")
    if not gorev:
        return
    kategori = simpledialog.askstring("Kategori", "Kategori (iş/okul/kişisel/genel):") or "genel"
    tarih = simpledialog.askstring("Tarih", "Tarih (YYYY-MM-DD HH:MM) veya boş bırakın:")
    gorev_ekle(gorev, kategori, tarih)
    listeyi_guncelle()

def secili_gorev_id():
    secim = tree.selection()
    if not secim:
        return None
    return tree.item(secim[0])["values"][0]

def gorev_sil_gui():
    gid = secili_gorev_id()
    if not gid:
        return
    gorev_sil(gid)
    listeyi_guncelle()

def gorev_tamamla_gui():
    gid = secili_gorev_id()
    if not gid:
        return
    gorev_tamamla(gid)
    listeyi_guncelle()

def filtrele(kategori):
    if kategori == "Hepsi":
        listeyi_guncelle()
    else:
        listeyi_guncelle(kategori.lower())

# ------------------- GUI -------------------
veritabani_olustur()

root = tb.Window(themename="superhero")
root.title("📝 Modern To-Do Uygulaması")
root.geometry("750x500")

# Stil ayarları (font ve tablo görünümü)
style = tb.Style()
style.configure("Treeview", font=("Segoe UI", 11), rowheight=28)
style.configure("Treeview.Heading", font=("Segoe UI", 12, "bold"))

# Başlık
baslik = tb.Label(root, text="📋 Görev Yöneticisi", 
                  font=("Segoe UI", 20, "bold"))
baslik.pack(pady=10)

# Tablo
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

# Butonlar
btn_frame = tb.Frame(root)
btn_frame.pack(pady=5)

tb.Button(btn_frame, text="➕ Görev Ekle", bootstyle="success-round", 
          command=yeni_gorev).grid(row=0, column=0, padx=5)

tb.Button(btn_frame, text="✅ Tamamla", bootstyle="info-round", 
          command=gorev_tamamla_gui).grid(row=0, column=1, padx=5)

tb.Button(btn_frame, text="🗑 Sil", bootstyle="danger-round", 
          command=gorev_sil_gui).grid(row=0, column=2, padx=5)

# Filtre butonları
filtre_frame = tb.Frame(root)
filtre_frame.pack(pady=5)

for kat in ["Hepsi", "iş", "okul", "kişisel", "genel"]:
    tb.Button(filtre_frame, text=kat.capitalize(), 
              bootstyle="secondary-round", 
              command=lambda k=kat: filtrele(k)).pack(side=LEFT, padx=3)

# Listeyi başlat
listeyi_guncelle()

# Alarm kontrolü ayrı thread’de
t = threading.Thread(target=alarm_kontrol, daemon=True)
t.start()

root.mainloop()
