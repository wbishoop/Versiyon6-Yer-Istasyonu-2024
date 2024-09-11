from customtkinter import *
from pages import Anasayfa, YerIstasyonu, VeriCek


# -----Genel Yapı ve Sayfa Sistemi-----------------------------------------------------------
class Versiyon6YerIstasyonu(CTk):
    def __init__(self, *args, **kwargs):
        CTk.__init__(self, *args, **kwargs)
        container = CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Anasayfa, YerIstasyonu, VeriCek):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Anasayfa)
        # print("w:", self.winfo_width(), "h:", self.winfo_height())
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    # -----------Yeni Sayfaya Geçiş -----------------------------------------------------
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        self.iconbitmap("V6-logo.ico")
        self.title("Yer İstasyonu Yazılımı / Versiyon6 Roket Takımı")
        self.resizable(FALSE, FALSE)

    def on_closing(self):
        self.destroy()  # Pencereyi kapatır
        sys.exit()  # Programı sonlandırır


if __name__ == "__main__":
    app = Versiyon6YerIstasyonu()
    app.mainloop()
