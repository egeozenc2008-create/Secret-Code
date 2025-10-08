import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Pillow kütüphanesi

class HesapMakinesi(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("🌟 Süslü Hesap Makinesi 🌟")
        self.configure(bg="#1E1E1E")
        self.minsize(360, 520)

        # Hoşgeldiniz ekranı için çerçeve
        self.greet_frame = tk.Frame(self, bg="#1E1E1E")
        self.greet_frame.pack(expand=True, fill="both")

        # Yasuo resmi yükle ve boyutlandır
        try:
            self.yasuo_img = Image.open("yasuo.png")
            self.yasuo_img = self.yasuo_img.resize((200, 200), Image.ANTIALIAS)
            self.yasuo_photo = ImageTk.PhotoImage(self.yasuo_img)
            self.img_label = tk.Label(self.greet_frame, image=self.yasuo_photo, bg="#1E1E1E")
            self.img_label.pack(pady=10)
        except Exception as e:
            print("Resim yüklenemedi:", e)

        # Hoşgeldiniz yazısı
        self.greet_label = tk.Label(self.greet_frame, text="Egenin Projesine Hoşgeldiniz!\nİyi işlemler 😊",
                                    font=("Segoe UI", 20, "bold"),
                                    fg="#FFA500", bg="#1E1E1E", justify="center")
        self.greet_label.pack(pady=10)

        # 2 saniye sonra hesap makinesi arayüzü gösterilecek
        self.after(2000, self.greet_sonlandir)

        self.ekran_var = tk.StringVar(value="0")

        # Hesap makinesi arayüzü burada oluşturulacak ama gizlenecek başlangıçta
        self.calc_frame = tk.Frame(self, bg="#1E1E1E")

        self.ekran = tk.Entry(self.calc_frame, textvariable=self.ekran_var,
                              font=("Segoe UI", 32, "bold"), bg="#2A2A2A", fg="white",
                              bd=0, relief="flat", justify="right", insertbackground="white")
        self.ekran.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=12, pady=(15, 10), ipady=20)

        self.btns = [
            ["C", "⌫", "±", "%"],
            ["7", "8", "9", "÷"],
            ["4", "5", "6", "×"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"]
        ]

        self.renkler = {
            "islem": "#FF9500",
            "sayi": "#3B3B3B",
            "func": "#4A4A4A",
            "yazi": "white",
            "hover_sayi": "#555555",
            "hover_islem": "#E38F01",
            "hover_func": "#606060",
        }

        for i in range(6):
            self.calc_frame.rowconfigure(i, weight=1)
        for j in range(4):
            self.calc_frame.columnconfigure(j, weight=1)

        for i, row in enumerate(self.btns, start=1):
            col = 0
            for text in row:
                genişlik = 1
                if text == "0":
                    genişlik = 2

                renk = self._get_color(text)

                btn = tk.Button(self.calc_frame, text=text, font=("Segoe UI", 24, "bold"),
                                bg=renk, fg=self.renkler["yazi"],
                                bd=0, relief="flat", cursor="hand2",
                                activebackground=self._darken_color(renk, 0.85),
                                command=lambda t=text: self.buton_tiklama(t))

                btn.grid(row=i, column=col, columnspan=genişlik, sticky="nsew", padx=8, pady=8)

                btn.bind("<Enter>", lambda e, b=btn, r=renk, t=text: self.hover_in(b, r, t))
                btn.bind("<Leave>", lambda e, b=btn, r=renk: self.hover_out(b, r))

                col += genişlik

        self.calc_frame.pack_forget()
        self.bind("<Return>", lambda e: self.buton_tiklama("="))
        self.bind("<BackSpace>", lambda e: self.buton_tiklama("⌫"))
        self.bind("<Escape>", lambda e: self.buton_tiklama("C"))
        self.bind("<Key>", self.klavye_girdisi)

        self.bind("<Configure>", self.resize_fonts)

    def greet_sonlandir(self):
        self.greet_frame.pack_forget()
        self.calc_frame.pack(fill="both", expand=True, padx=12, pady=12)

    def hover_in(self, btn, renk, text):
        if text in ["÷", "×", "-", "+", "="]:
            btn.config(bg=self.renkler["hover_islem"])
        elif text in ["C", "⌫", "±", "%"]:
            btn.config(bg=self.renkler["hover_func"])
        else:
            btn.config(bg=self.renkler["hover_sayi"])

    def hover_out(self, btn, renk):
        btn.config(bg=renk)

    def _darken_color(self, hex_color, factor=0.7):
        hex_color = hex_color.lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2 ,4))
        rgb_dark = tuple(max(0, int(c*factor)) for c in rgb)
        return '#%02x%02x%02x' % rgb_dark

    def _get_color(self, text):
        if text in ["÷", "×", "-", "+", "="]:
            return self.renkler["islem"]
        elif text in ["C", "⌫", "±", "%"]:
            return self.renkler["func"]
        else:
            return self.renkler["sayi"]

    def klavye_girdisi(self, event):
        allowed = "0123456789.+-*/%"
        if event.char in allowed:
            self.buton_tiklama(event.char)
        elif event.keysym == "Return":
            self.buton_tiklama("=")
        elif event.keysym == "BackSpace":
            self.buton_tiklama("⌫")
        elif event.keysym == "Escape":
            self.buton_tiklama("C")

    def buton_tiklama(self, deger):
        ekran_icerik = self.ekran_var.get()

        if deger == "C":
            self.ekran_var.set("0")
        elif deger == "⌫":
            if len(ekran_icerik) > 1:
                self.ekran_var.set(ekran_icerik[:-1])
            else:
                self.ekran_var.set("0")
        elif deger == "=":
            self.hesapla()
        elif deger == "±":
            self.pozitif_negatif()
        elif deger == "%":
            self.yuzde()
        else:
            if ekran_icerik == "0" and deger not in [".", "+", "-", "*", "/", "%"]:
                self.ekran_var.set(deger)
            else:
                if deger == "÷":
                    deger = "/"
                elif deger == "×":
                    deger = "*"

                self.ekran_var.set(ekran_icerik + deger)

    def hesapla(self):
        try:
            ifade = self.ekran_var.get()
            ifade = ifade.replace("÷", "/").replace("×", "*")
            sonuc = eval(ifade)
            self.ekran_var.set(str(sonuc))
        except ZeroDivisionError:
            messagebox.showerror("Hata", "Sıfıra bölünemez!")
            self.ekran_var.set("0")
        except Exception:
            messagebox.showerror("Hata", "Geçersiz ifade!")
            self.ekran_var.set("0")

    def pozitif_negatif(self):
        try:
            ifade = self.ekran_var.get()
            if ifade.startswith("-"):
                self.ekran_var.set(ifade[1:])
            else:
                self.ekran_var.set("-" + ifade)
        except:
            pass

    def yuzde(self):
        try:
            ifade = self.ekran_var.get()
            sonuc = eval(ifade) / 100
            self.ekran_var.set(str(sonuc))
        except:
            self.ekran_var.set("0")

    def resize_fonts(self, event):
        genislik = event.width
        yukseklik = event.height

        ekran_font_size = max(16, min(48, yukseklik // 15))
        btn_font_size = max(14, min(30, yukseklik // 25))
        greet_font_size = max(14, min(36, yukseklik // 20))

        self.ekran.config(font=("Segoe UI", ekran_font_size, "bold"))
        self.greet_label.config(font=("Segoe UI", greet_font_size, "bold"))

        for child in self.calc_frame.winfo_children():
            if isinstance(child, tk.Button):
                child.config(font=("Segoe UI", btn_font_size, "bold"))

if __name__ == "__main__":
    app = HesapMakinesi()
    app.mainloop()





