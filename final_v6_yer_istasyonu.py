# BISMILLAHIRRAHMANIRRAHIM
# VERSIYON6 ROKET TAKIMI TEKNOFEST 2024 YER ISTASYONU YAZILIMI


from customtkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from sys import platform

BG_COLOR = "#a54a49"
BG_COLOR_GREY = "#2e2e2e"


# Örnek Grafik Değerleri
aaaa = {
    0: 0,
    500: 850,
    800: 900,
    1500: 2000,
}

bbbb = {
    0: 0,
    400: 700,
    450: 800,
    1300: 1800,
}

cc = {
    0: 0,
    50: 70,
    100: 200,
    300: 350,
    400: 150,

}

dd = {
    0: 0,
    50: 70,
    80: 300,
    250: 350,
    400: 200,
}

fig1, ax1 = plt.subplots()
ax1.plot(list(aaaa.keys()), list(aaaa.values()))
ax1.set_title("Roket İrtifa")
ax1.set_ylabel("metre")
ax1.set_xlabel("Zaman / saniye")


fig2, ax2 = plt.subplots()
ax2.plot(list(bbbb.keys()), list(bbbb.values()))
ax2.set_title("İrtifa")
ax2.set_ylabel("metre")
ax2.set_xlabel("Zaman / saniye")
# plt.subplots_adjust(left=0.168, bottom=0.175, right=0.983, top=0.897)
# plt.show()


# -----GRAFİK OLUŞTURMA-----------------------------------------------------------
def create_figure(frame, data_x, data_y, title, xlabel, ylabel):
    fig = Figure(figsize=(3, 3), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(data_x, data_y, color=BG_COLOR)
    ax.set_title(title)
    ax.title.set_color("white")
    ax.set_xlabel(xlabel, color="white")
    ax.set_ylabel(ylabel, color="white")
    fig.patch.set_facecolor(BG_COLOR)
    ax.tick_params(colors="white")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines["bottom"].set_color(BG_COLOR_GREY)
    ax.spines["left"].set_color(BG_COLOR_GREY)
    fig.subplots_adjust(left=0.22, bottom=0.167, right=0.920, top=0.891)
    return fig, FigureCanvasTkAgg(fig, frame)


# -----PORT AÇMA-----------------------------------------------------------
def port_acma():
    messagebox.showerror(title="Port Ayarları / Versiyon6 Roket Takımı", message="Port açılamadı.\t\t\t",)


# -----SAYFA SİSTEMİ-----------------------------------------------------------
class Versiyon6YerIstasyonu(CTk):

    def __init__(self, *args, **kwargs):
        CTk.__init__(self, *args, **kwargs)
        container = CTkFrame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Anasayfa, YerIstasyonu):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Anasayfa)
        # print("w:", self.winfo_width(), "h:", self.winfo_height())

    # -----SAYFA GÖSTER-----------------------------------------------------------
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        self.iconbitmap("V6-logo.ico")
        self.title("Yer İstasyonu Yazılımı / Versiyon6 Roket Takımı")
        self.resizable(FALSE, FALSE)


# -----ANASAYFA-----------------------------------------------------------
class Anasayfa(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)
        self.configure(fg_color=BG_COLOR)
        versiyon_6 = CTkLabel(self, text="Versiyon6 Roket Takımı",
                              font=("Futura", 40, "bold"), bg_color=BG_COLOR).grid(row=0, column=0,
                                                                                   pady=(100, 0), padx=300)
        a = "bersiyon6 yer istasyonu"

        tabview = CTkTabview(self)
        tabview.grid(row=1, column=0, padx=300 ,pady=(70, 150), sticky="nsew")
        tabview.add("ZADA")
        port_ayarlari = CTkButton(tabview.tab("ZADA"), text="Port Ayarları", border_color=BG_COLOR,
                                  border_width=4, fg_color="transparent", corner_radius=32, command=self.port_ayarlama,
                                  width=200, height=50, hover_color=BG_COLOR).grid(row=0, column=0, padx=200, pady=50)
        port_ac = CTkButton(tabview.tab("ZADA"), text="Port Aç", border_color=BG_COLOR,
                            border_width=4, fg_color="transparent", corner_radius=32,
                            width=200, height=50, hover_color=BG_COLOR, command=port_acma).grid(row=1, column=0,
                                                                                                padx=200, pady=(0, 50))
        yer_istasyonu = CTkButton(tabview.tab("ZADA"), text="Yer İstasyonu", border_color=BG_COLOR,
                                  border_width=4, fg_color=BG_COLOR, corner_radius=32,
                                  command=lambda: controller.show_frame(YerIstasyonu),
                                  width=200, height=50, hover_color="#2e2e2e").grid(row=2, column=0, padx=200,
                                                                                    pady=(0, 50))

    # -----PORT AYARLAMA-----------------------------------------------------------
    def port_ayarlama(self):
        port_ayarla_window = CTkToplevel()
        port_ayarla_window.title("Port Ayarları / Versiyon6 Roket Takımı")
        port_ayarla_window.resizable(FALSE, FALSE)
        port_ayarla_window.iconbitmap(default="V6-logo.ico")
        port_ayarla_window.attributes("-topmost", True)
        if platform.startswith("win"):
            port_ayarla_window.after(200, lambda: port_ayarla_window.iconbitmap("V6-logo.ico"))
        port_ayarla_frame = CTkFrame(master=port_ayarla_window)
        port_ayarla_frame.grid(column=0, row=0, sticky="nsew", padx=20, pady=20)
        ayarla = CTkLabel(port_ayarla_frame, text="Ayarla", font=("Helvatica", 20, "bold"))
        ayarla.grid(column=0, row=0, columnspan=2, pady=(30, 20))
        port = CTkLabel(port_ayarla_frame, text="Port: ", font=("Helvatica", 15))
        port.grid(column=0, row=1, pady=(20, 10), padx=30)
        port_sec = CTkComboBox(port_ayarla_frame, fg_color=BG_COLOR, values=[" "],
                               border_color=BG_COLOR, dropdown_hover_color=BG_COLOR)
        port_sec.grid(row=1, column=1, padx=30)
        baud_rate = CTkLabel(port_ayarla_frame, text="Baud Rate: ", font=("Helvatica", 15))
        baud_rate.grid(row=2, column=0, pady=10, padx=30)
        baud_rate_sec = CTkComboBox(port_ayarla_frame, values=["14400", "19200", "38400", "56000",
                                                                "57600", "115200", "128000", "256000"],
                                    fg_color=BG_COLOR, border_color=BG_COLOR, dropdown_hover_color=BG_COLOR)
        baud_rate_sec.set("19200")
        baud_rate_sec.grid(row=2, column=1, padx=30)
        data_bits = CTkLabel(port_ayarla_frame, text="Data Bits: ", font=("Helvatica", 15))
        data_bits.grid(row=3, column=0, pady=10, padx=30)
        data_bits_sec = CTkComboBox(port_ayarla_frame, values=["5", "6", "7", "8"],
                                    fg_color=BG_COLOR, border_color=BG_COLOR, dropdown_hover_color=BG_COLOR)
        data_bits_sec.set("8")
        data_bits_sec.grid(row=3, column=1, padx=30)
        stop_bits = CTkLabel(port_ayarla_frame, text="Stop Bits: ", font=("Helvatica", 15))
        stop_bits.grid(row=4, column=0, pady=10, padx=30)
        stop_bits_sec = CTkComboBox(port_ayarla_frame, values=["1", "1.5", "2"],
                                    fg_color=BG_COLOR, border_color=BG_COLOR, dropdown_hover_color=BG_COLOR)
        stop_bits_sec.grid(row=4, column=1, padx=30)
        parity = CTkLabel(port_ayarla_frame, text="Parity: ", font=("Helvatica", 15))
        parity.grid(row=5, column=0, pady=10, padx=30)
        parity_sec = CTkComboBox(port_ayarla_frame, values=["None", "Odd", "Even", "Mark", "Space"],
                                 fg_color=BG_COLOR, border_color=BG_COLOR, dropdown_hover_color=BG_COLOR)
        parity_sec.grid(row=5, column=1, padx=30)
        flow_control = CTkLabel(port_ayarla_frame, text="Flow Control: ", font=("Helvatica", 15))
        flow_control.grid(row=6, column=0, pady=10, padx=30)
        flow_control_sec = CTkComboBox(port_ayarla_frame, values=["None", "Hardware", "Software", "Custom"],
                                       fg_color=BG_COLOR, border_color=BG_COLOR, dropdown_hover_color=BG_COLOR)
        flow_control_sec.grid(row=6, column=1, padx=30)

        ok_button = CTkButton(port_ayarla_frame, text="Tamam", command=port_ayarla_window.destroy, fg_color=BG_COLOR)
        ok_button.grid(row=7, column=0, padx=200, pady=(20, 30), columnspan=2)
        # self.update()
        # print(port_ayarla_window.winfo_width(), port_ayarla_window.winfo_height())


# -----YER İSTASYONU-----------------------------------------------------------
class YerIstasyonu(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)
        self.configure(fg_color=BG_COLOR)
        v6 = CTkLabel(master=self, text="Versiyon6 Yer İstasyonu", font=("Futura", 40, "bold"))
        v6.grid(column=0, row=0, columnspan=2, pady=(20, 10))
        left_frame = CTkFrame(master=self, width=490, height=470)
        left_frame.grid(column=0, row=1, sticky="nsew", padx=20)
        left_frame.grid_propagate(False)
        right_frame = CTkFrame(master=self, width=670, height=670)
        right_frame.grid(column=1, row=1, sticky="nsew", rowspan=3, padx=(0, 20), pady=(0, 20))
        right_frame.grid_propagate(False)
        bottom_frame = CTkFrame(master=self, height=120, width=500)
        bottom_frame.grid(column=0, row=2, sticky="nsew", padx=20, pady=(10, 0))
        bottom_frame.grid_propagate(False)
        button1 = CTkButton(self, text="Anasayfaya Dön", command=lambda:controller.show_frame(Anasayfa), height=40,
                            corner_radius=40)
        # , border_color=BG_COLOR_GREY, border_width=4, hover_color=BG_COLOR
        button1.grid(column=0, row=3, pady=(10, 20), sticky="nsew", padx=20)

        # -----DEĞERLER (left_frame)-----------------------------------------------------------
        degerler = CTkLabel(master=left_frame, text="Değerler", font=("Cambria", 30, "bold"), anchor="center").grid(column=0, row=0, pady=15, padx=185)
        alt_frame = CTkFrame(master=left_frame, border_color="white", border_width=2, width=450, height=395)
        alt_frame.grid(column=0, row=1)
        alt_frame.grid_propagate(False)
        takim_id = CTkLabel(master=alt_frame, text="Takım ID: V6 takım id'si", font=("Cambria", 14))
        takim_id.grid(row=0, column=0, padx=30, pady=(6, 0), columnspan=2)
        sayac = CTkLabel(master=alt_frame, text="Sayaç:\t\t\t\t\t173", font=("Cambria", 14)).grid(row=1, column=0, padx=50, pady=3)
        roket_irtifa = CTkLabel(master=alt_frame, text="Roket İrtifa:\t\t\t\t35m", font=("Cambria", 14))
        roket_irtifa.grid(row=2, column=0, padx=5, pady=3)
        roket_hiz = CTkLabel(master=alt_frame, text="Roket Hız:\t\t\t\t                35m/s", font=("Cambria", 14))
        roket_hiz.grid(row=3, column=0, padx=5, pady=3)
        gorev_yuku_irtifa = CTkLabel(master=alt_frame, text="Görev Yükü İrtifa:\t\t\t\t35m", font=("Cambria", 14))
        gorev_yuku_irtifa.grid(row=4, column=0, padx=5, pady=3)
        gorev_yuku_hiz = CTkLabel(master=alt_frame, text="Görev Yükü Hız:\t\t\t                35m/s", font=("Cambria", 14))
        gorev_yuku_hiz.grid(row=5, column=0, padx=5, pady=3)
        enlem = CTkLabel(master=alt_frame, text="Enlem:\t\t\t\t       39.910211", font=("Cambria", 14)).grid(row=6, column=0, pady=3)
        boylam = CTkLabel(master=alt_frame, text="Boylam:\t\t\t\t       32.852796", font=("Cambria", 14)).grid(row=7, column=0, pady=3)
        gorev_yuku_enlem = CTkLabel(master=alt_frame, text="Görev Yükü Enlem:\t\t\t       39.910211", font=("Cambria", 14)).grid(row=8, column=0,pady=3)
        gorev_yuku_boylam = CTkLabel(master=alt_frame, text="Görev Yükü Boylam:\t\t\t       32.852796", font=("Cambria", 14)).grid(row=9, column=0,pady=3)
        gyroscope_xyz = CTkLabel(master=alt_frame, text="Jiroskop X-Y-Z:\t\t\t         15-16-17", font=("Cambria", 14)).grid(row=10, column=0,pady=(3, 6))

        # -----AYRILMA DURUMU (bottom_frame)-----------------------------------------------------------
        progressbar_1 = CTkProgressBar(master=bottom_frame)
        progressbar_1.grid(row=1, column=0, pady=(30, 40), padx=150, columnspan=2)
        progressbar_1.configure(mode="indeterminnate")
        progressbar_1.start()
        ayrilma = CTkLabel(master=bottom_frame, text="Ayrılma Durumu:", font=("Helvatica", 15))
        ayrilma.grid(row=2, column=0)
        switch = CTkSwitch(master=bottom_frame, text="Gerçekleşmedi", onvalue="on", offvalue="off")
        switch.configure(state="disabled")
        switch.grid(row=2, column=1)

        # -----GRAFİKLER (right_frame)-----------------------------------------------------------

        charts_frame = CTkFrame(master=right_frame, width=837, height=837)
        charts_frame.grid(row=0, column=0, sticky="nsew")
        # self.update()
        # print(right_frame.winfo_width(), right_frame.winfo_height())
        upper_frame = CTkFrame(master=charts_frame)
        upper_frame.pack(fill="both", expand=True)
        lower_frame = CTkFrame(master=charts_frame)
        lower_frame.pack(fill="both", expand=True)

        fig1, canvas1 = create_figure(upper_frame, list(aaaa.keys()), list(aaaa.values()),
                                      "Roket İrtifa", "saniye", "metre")
        fig2, canvas2 = create_figure(upper_frame, list(bbbb.keys()), list(bbbb.values()),
                                      "Görev Yükü İrtifa", "saniye", "metre")
        fig3, canvas3 = create_figure(lower_frame, list(cc.keys()), list(cc.values()),
                                      "Roket Hız", "saniye", "metre")
        fig4, canvas4 = create_figure(lower_frame, list(dd.keys()), list(dd.values()),
                                      "Görev Yükü Hız", "saniye", "metre")

        canvas1.get_tk_widget().grid(row=0, column=0, padx=20, pady=20,)
        canvas2.get_tk_widget().grid(row=0, column=1, padx=(25, 0), pady=20,)
        canvas3.get_tk_widget().grid(row=0, column=0, padx=20, pady=20,)
        canvas4.get_tk_widget().grid(row=0, column=1, padx=(25, 0), pady=20,)


if __name__ == "__main__":
    app = Versiyon6YerIstasyonu()
    app.mainloop()
