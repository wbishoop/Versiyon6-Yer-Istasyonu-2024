from customtkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from sys import platform
from PIL import Image
import random

# --------- Kullanılan Renkler -------------------------------------------------------
BG_COLOR = "#a54a49"
DARKER_BG_COLOR = "#953A39"
BG_COLOR_GREY = "#2e2e2e"

# --------- Örnek Grafik Değerleri ----------------------------------------------------
aaaa = {
    1: 130,
    2:133,
    3:132,
    4:134
}

bbbb = {
    1: 132,
    2:131,
    3:133,
    4:130
}

cc = {
    1: 0,
    2:0,
    3:0,
    4:0
}

dd = {
    1: 0,
    2:0,
    3:0,
    4:0
}
paket = 0

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


# ----------Grafik Oluşturma ve Yapısı------------------------------------------------------
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


# ----------Grafik Yerleşimi------------------------------------------------------
def place_graph(frame):
    charts_frame = CTkFrame(master=frame, width=837, height=837)
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

    canvas1.get_tk_widget().grid(row=0, column=0, padx=20, pady=20, )
    canvas2.get_tk_widget().grid(row=0, column=1, padx=(25, 0), pady=20, )
    canvas3.get_tk_widget().grid(row=0, column=0, padx=20, pady=20, )
    canvas4.get_tk_widget().grid(row=0, column=1, padx=(25, 0), pady=20, )


# ------- Anasayfa ---------------------------------------------------------
class Anasayfa(CTkFrame):
    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)
        self.configure(fg_color=BG_COLOR)
        versiyon_6 = CTkLabel(self, text="Versiyon6 Roket Takımı",
                              font=("Futura", 45, "bold"), bg_color=BG_COLOR).grid(row=0, column=0,
                                                                                   pady=(100, 0), padx=300)
        tabview = CTkTabview(self, segmented_button_selected_color=BG_COLOR,
                             segmented_button_selected_hover_color=DARKER_BG_COLOR)
        tabview.grid(row=1, column=0, padx=300 ,pady=(100, 150), sticky="nsew", )
        tabview.add("ZADA")
        port_ayarlari = CTkButton(tabview.tab("ZADA"), text="Port Ayarları", border_color=BG_COLOR,
                                  border_width=4, fg_color="transparent", corner_radius=32, command=self.port_ayarlama,
                                  width=200, height=50, hover_color=BG_COLOR)
        port_ayarlari.grid(row=0, column=0, padx=(80, 20), pady=50)
        port_ac = CTkButton(tabview.tab("ZADA"), text="Port Aç", border_color=BG_COLOR,
                            border_width=4, fg_color="transparent", corner_radius=32,
                            width=200, height=50, hover_color=BG_COLOR, command=self.port_acma).grid(row=0, column=1,
                                                                                                padx=(20, 80), pady=50)
        yer_istasyonu = CTkButton(tabview.tab("ZADA"), text="Yer İstasyonu", border_color=BG_COLOR,
                                  border_width=4, fg_color=BG_COLOR, corner_radius=32,
                                  command=lambda: controller.show_frame(YerIstasyonu),
                                  width=200, height=50, hover_color="#2e2e2e").grid(row=1, column=0,
                                                                                    pady=(0, 50), padx=(80, 20))
        veri_cek = CTkButton(tabview.tab("ZADA"), text="Veri Çek", border_color=BG_COLOR,
                                  border_width=4, fg_color=BG_COLOR, corner_radius=32,
                                  command=lambda: controller.show_frame(VeriCek),
                                  width=200, height=50, hover_color="#2e2e2e").grid(row=1, column=1,
                                                                                    pady=(0, 50), padx=(20, 80))
        sene = CTkLabel(tabview.tab("ZADA"), text="2024", bg_color=BG_COLOR, corner_radius=200, width=20)
        sene.grid(row=2, column=0, columnspan=2, padx=80, pady=(0, 20))

    # -----Port Açma-----------------------------------------------------------
    def port_acma(self):
        messagebox.showerror(title="Port Ayarları / Versiyon6 Roket Takımı", message="Port açılamadı.\t\t\t", )

    # -----Port Ayarlama-----------------------------------------------------------
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
        hyi_port = CTkLabel(port_ayarla_frame, text="HYİ Port: ", font=("Helvatica", 15))
        hyi_port.grid(column=0, row=2, pady=10, padx=30)
        hyi_port_sec = CTkComboBox(port_ayarla_frame, fg_color=BG_COLOR, values=[" "],
                               border_color=BG_COLOR, dropdown_hover_color=BG_COLOR)
        hyi_port_sec.grid(row=2, column=1, padx=30)
        baud_rate = CTkLabel(port_ayarla_frame, text="Baud Rate: ", font=("Helvatica", 15))
        baud_rate.grid(row=3, column=0, pady=10, padx=30)
        baud_rate_sec = CTkComboBox(port_ayarla_frame, values=["14400", "19200", "38400", "56000",
                                                                "57600", "115200", "128000", "256000"],
                                    fg_color=BG_COLOR, border_color=BG_COLOR, dropdown_hover_color=BG_COLOR)
        baud_rate_sec.set("19200")
        baud_rate_sec.grid(row=3, column=1, padx=30)
        data_bits = CTkLabel(port_ayarla_frame, text="Data Bits: ", font=("Helvatica", 15))
        data_bits.grid(row=4, column=0, pady=10, padx=30)
        data_bits_sec = CTkComboBox(port_ayarla_frame, values=["5", "6", "7", "8"],
                                    fg_color=BG_COLOR, border_color=BG_COLOR, dropdown_hover_color=BG_COLOR)
        data_bits_sec.set("8")
        data_bits_sec.grid(row=4, column=1, padx=30)
        stop_bits = CTkLabel(port_ayarla_frame, text="Stop Bits: ", font=("Helvatica", 15))
        stop_bits.grid(row=5, column=0, pady=10, padx=30)
        stop_bits_sec = CTkComboBox(port_ayarla_frame, values=["1", "1.5", "2"],
                                    fg_color=BG_COLOR, border_color=BG_COLOR, dropdown_hover_color=BG_COLOR)
        stop_bits_sec.grid(row=5, column=1, padx=30)
        parity = CTkLabel(port_ayarla_frame, text="Parity: ", font=("Helvatica", 15))
        parity.grid(row=6, column=0, pady=10, padx=30)
        parity_sec = CTkComboBox(port_ayarla_frame, values=["None", "Odd", "Even", "Mark", "Space"],
                                 fg_color=BG_COLOR, border_color=BG_COLOR, dropdown_hover_color=BG_COLOR)
        parity_sec.grid(row=6, column=1, padx=30)
        flow_control = CTkLabel(port_ayarla_frame, text="Flow Control: ", font=("Helvatica", 15))
        flow_control.grid(row=7, column=0, pady=10, padx=30)
        flow_control_sec = CTkComboBox(port_ayarla_frame, values=["None", "Hardware", "Software", "Custom"],
                                       fg_color=BG_COLOR, border_color=BG_COLOR, dropdown_hover_color=BG_COLOR)
        flow_control_sec.grid(row=7, column=1, padx=30)

        ok_button = CTkButton(port_ayarla_frame, text="Tamam",
                              command=port_ayarla_window.destroy, fg_color=BG_COLOR, hover_color=DARKER_BG_COLOR)
        ok_button.grid(row=8, column=0, padx=(150, 20), pady=(20, 30))

        refresh_button = CTkButton(port_ayarla_frame, text="Yenile",
                              command=port_ayarla_window.destroy, fg_color=BG_COLOR, hover_color=DARKER_BG_COLOR)
        refresh_button.grid(row=8, column=1, padx=(20,150), pady=(20, 30))
        # self.update()z
        # print(port_ayarla_window.winfo_width(), port_ayarla_window.winfo_height())


# ------------- Yer İstasyonu ---------------------------------------------------
class YerIstasyonu(CTkFrame):
    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)
        self.configure(fg_color=BG_COLOR)
        v6 = CTkLabel(master=self, text="Versiyon6 - Yer İstasyonu", font=("Futura", 40, "bold"))
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
                            corner_radius=40, border_color=BG_COLOR_GREY, border_width=6,
                            fg_color=BG_COLOR_GREY, hover_color=BG_COLOR)
        # , border_color=BG_COLOR_GREY, border_width=4, hover_color=BG_COLOR
        button1.grid(column=0, row=3, pady=(10, 20), sticky="nsew", padx=20)

        # ----- Değerler (left_frame)-----------------------------------------------------------
        degerler = CTkLabel(master=left_frame, text="Değerler", font=("Cambria", 30, "bold"), anchor="center")
        degerler.grid(column=0, row=0, pady=15, padx=185)
        alt_frame = CTkFrame(master=left_frame, border_color="white", border_width=2, width=450, height=395)
        alt_frame.grid(column=0, row=1)
        alt_frame.grid_propagate(False)
        self.takim_id = CTkLabel(master=alt_frame, text="Takım ID: 0", font=("Cambria", 14))
        self.takim_id.grid(row=0, column=0, padx=30, pady=(6, 0), columnspan=2)
        self.sayac = CTkLabel(master=alt_frame, text="Sayaç:\t\t\t\t\t173", font=("Cambria", 14))
        self.sayac.grid(row=1, column=0, padx=50, pady=3)
        self.roket_irtifa = CTkLabel(master=alt_frame, text="Roket İrtifa:\t\t\t\t61m", font=("Cambria", 14))
        self.roket_irtifa.grid(row=2, column=0, padx=5, pady=3)
        self.roket_hiz = CTkLabel(master=alt_frame,
                                  text="Roket Hız:\t\t\t\t                35m/s", font=("Cambria", 14))
        self.roket_hiz.grid(row=3, column=0, padx=5, pady=3)
        self.gorev_yuku_irtifa = CTkLabel(master=alt_frame, text="Görev Yükü İrtifa:\t\t\t\t61m", font=("Cambria", 14))
        self.gorev_yuku_irtifa.grid(row=4, column=0, padx=5, pady=3)
        self.gorev_yuku_hiz = CTkLabel(master=alt_frame,
                                       text="Görev Yükü Hız:\t\t\t                35m/s", font=("Cambria", 14))
        self.gorev_yuku_hiz.grid(row=5, column=0, padx=5, pady=3)
        self.enlem = CTkLabel(master=alt_frame, text="Enlem:\t\t\t\t       41.1374978", font=("Cambria", 14))
        self.enlem.grid(row=6, column=0, pady=3)
        self.boylam = CTkLabel(master=alt_frame, text="Boylam:\t\t\t\t       29.1134879", font=("Cambria", 14))
        self.boylam.grid(row=7, column=0, pady=3)
        self.gorev_yuku_enlem = CTkLabel(master=alt_frame,
                                         text="Görev Yükü Enlem:\t\t\t       41.1374978", font=("Cambria", 14))
        self.gorev_yuku_enlem.grid(row=8, column=0,pady=3)
        self.gorev_yuku_boylam = CTkLabel(master=alt_frame,
                                          text="Görev Yükü Boylam:\t\t\t       29.1134879", font=("Cambria", 14))
        self.gorev_yuku_boylam.grid(row=9, column=0,pady=3)
        self.gyroscope_xyz = CTkLabel(master=alt_frame,
                                      text="Jiroskop X-Y-Z:\t\t\t         -0.01-0.05-0.03", font=("Cambria", 14))
        self.gyroscope_xyz.grid(row=10, column=0,pady=(3, 6))
        self.update_values()

        # ----- Ayrılma Durumu (bottom_frame)-----------------------------------------------------------
        progressbar_1 = CTkProgressBar(master=bottom_frame, progress_color=BG_COLOR)
        progressbar_1.grid(row=1, column=0, pady=(30, 40), padx=150, columnspan=2)
        progressbar_1.configure(mode="indeterminnate")
        progressbar_1.start()
        ayrilma = CTkLabel(master=bottom_frame, text="Ayrılma Durumu:", font=("Helvatica", 15))
        ayrilma.grid(row=2, column=0)
        switch = CTkSwitch(master=bottom_frame, text="Gerçekleşmedi", onvalue="on", offvalue="off")
        switch.configure(state="disabled")
        switch.grid(row=2, column=1)

        # -----Grafik Yapısı (right_frame)-----------------------------------------------------------
        place_graph(right_frame)
        # self.update_graphs()

    # -----Değer Değişikliği-----------------------------------------------------------
    def update_values(self):
        global paket
        paket += 1
        a = random.randint(60, 62)
        b = random.randint(60, 62)
        self.sayac.configure(text=f"Sayaç:\t\t\t\t\t       {paket}")
        self.roket_irtifa.configure(text="Roket İrtifa:\t\t\t\t{}m".format(a))
        self.roket_hiz.configure(text="Roket Hız:\t\t\t\t                      {}m/s".format(random.randint(0, 0)))
        self.gorev_yuku_irtifa.configure(text="Görev Yükü İrtifa:\t\t\t\t{}m".format(b))
        self.gorev_yuku_hiz.configure(text="Görev Yükü Hız:\t\t\t                      {}m/s".format(0))
        self.gyroscope_xyz.configure(
            text="Jiroskop X-Y-Z:\t\t\t " + str(round(random.uniform(0, 0.1), 2) * -1) + " " +
                 str(round(random.uniform(0, 0.1), 2)) + " " + str(round(random.uniform(0, 0.1), 2)))
        self.after(1000, self.update_values)  # 1000 milisaniye = 1 saniye


# -------------Veri Çekim---------------------------------------------------
class VeriCek(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)
        self.configure(fg_color=BG_COLOR)
        v6 = CTkLabel(master=self, text="Versiyon6 - Veri Çek", font=("Futura", 40, "bold"))
        v6.grid(column=0, row=0, columnspan=2, pady=(20, 10))

        veritabview = CTkTabview(self, width=490, height=600, segmented_button_selected_color=BG_COLOR,
                                 segmented_button_selected_hover_color=DARKER_BG_COLOR)
        veritabview.grid(row=1, column=0, padx=20, sticky="nsew")
        veritabview.add("Değerler")
        veritabview.grid_propagate(False)

        right_frame = CTkFrame(master=self, width=670, height=670)
        right_frame.grid(column=1, row=1, sticky="nsew", rowspan=3, padx=(0, 20), pady=(0, 20))
        right_frame.grid_propagate(False)

        button1 = CTkButton(self, text="Anasayfaya Dön", command=lambda: controller.show_frame(Anasayfa), height=40,
                            corner_radius=40, border_color=BG_COLOR_GREY,
                            border_width=6, fg_color=BG_COLOR_GREY, hover_color=BG_COLOR)
        button1.grid(column=0, row=3, pady=(10, 20), sticky="nsew", padx=20)

        # --------- Değerler -------------------------------------------------------
        degerler = CTkLabel(veritabview.tab("Değerler"), text="Değerler",
                            font=("Cambria", 30, "bold"), anchor="center")
        degerler.grid(column=0, row=0, pady=(0, 15), padx=185, columnspan=2)
        alt_frame = CTkFrame(veritabview.tab("Değerler"), border_color="white", border_width=2, width=450, height=395)
        alt_frame.grid(column=0, row=1, padx=(0, 15), columnspan=2)
        alt_frame.grid_propagate(False)
        self.takim_id = CTkLabel(master=alt_frame, text="Takım ID: 0", font=("Cambria", 14))
        self.takim_id.grid(row=0, column=0, padx=30, pady=(6, 0), columnspan=2)
        self.sayac = CTkLabel(master=alt_frame, text="Sayaç:\t\t\t\t\t173", font=("Cambria", 14))
        self.sayac.grid(row=1, column=0, padx=50, pady=3)
        self.roket_irtifa = CTkLabel(master=alt_frame, text="Roket İrtifa:\t\t\t\t61m", font=("Cambria", 14))
        self.roket_irtifa.grid(row=2, column=0, padx=5, pady=3)
        self.roket_hiz = CTkLabel(master=alt_frame, text="Roket Hız:\t\t\t\t                35m/s",
                                  font=("Cambria", 14))
        self.roket_hiz.grid(row=3, column=0, padx=5, pady=3)
        self.gorev_yuku_irtifa = CTkLabel(master=alt_frame, text="Görev Yükü İrtifa:\t\t\t\t61m", font=("Cambria", 14))
        self.gorev_yuku_irtifa.grid(row=4, column=0, padx=5, pady=3)
        self.gorev_yuku_hiz = CTkLabel(master=alt_frame, text="Görev Yükü Hız:\t\t\t                35m/s",
                                       font=("Cambria", 14))
        self.gorev_yuku_hiz.grid(row=5, column=0, padx=5, pady=3)
        self.enlem = CTkLabel(master=alt_frame, text="Enlem:\t\t\t\t       41.1374978", font=("Cambria", 14)).grid(
            row=6, column=0, pady=3)
        self.boylam = CTkLabel(master=alt_frame, text="Boylam:\t\t\t\t       29.1134879", font=("Cambria", 14)).grid(
            row=7, column=0, pady=3)
        self.gorev_yuku_enlem = CTkLabel(master=alt_frame, text="Görev Yükü Enlem:\t\t\t       41.1374978",
                                         font=("Cambria", 14)).grid(row=8, column=0, pady=3)
        self.gorev_yuku_boylam = CTkLabel(master=alt_frame, text="Görev Yükü Boylam:\t\t\t       29.1134879",
                                          font=("Cambria", 14)).grid(row=9, column=0, pady=3)
        self.gyroscope_xyz = CTkLabel(master=alt_frame, text="Jiroskop X-Y-Z:\t\t\t-0.01-0.05-0.03",
                                      font=("Cambria", 14))
        self.gyroscope_xyz.grid(row=10, column=0, pady=(3, 6))
        self.zaman = 0
        self.progressbar_2 = CTkProgressBar(veritabview.tab("Değerler"), orientation="horizontal",
                                            width=420, progress_color=BG_COLOR)
        self.progressbar_2.grid(row=2, column=0, columnspan=2, padx=(0, 20), pady=(10, 10), sticky="ns")
        self.slider = CTkSlider(veritabview.tab("Değerler"), orientation="horizontal",
                                width=420, button_color=BG_COLOR, button_hover_color=DARKER_BG_COLOR)
        self.slider.grid(row=3, column=0, columnspan=2, padx=(0, 20), pady=(0, 10), sticky="ns")
        self.slider.configure(command=self.slider_deger_degisti)
        self.son = CTkLabel(veritabview.tab("Değerler"),
                            text="Saniye: {}".format(self.zaman), font=("Cambria", 20, "normal"))
        self.son.grid(row=4, column=0, padx=70)
        secme_ekrani = CTkButton(veritabview.tab("Değerler"), text="Değer Girerek Seç",
                                 command=self.deger_gir, fg_color=BG_COLOR, hover_color="#953A39")
        secme_ekrani.grid(row=4, column=1, padx=(0, 50))


        # -------- Grafikler --------------------------------------------------------
        place_graph(right_frame)
        # self.update_graphs()

    # -------Değer Girişi ---------------------------------------------------------
    def deger_gir(self):
        dialog = CTkInputDialog(text="Değer Girin:", title="Versiyon6 - Değer Girişi",
                                font=("Futura",  15, "normal"), entry_border_color=BG_COLOR,
                                button_fg_color=BG_COLOR, button_hover_color="#953A39")
        dialog.iconbitmap(default="V6-logo.ico")
        dialog.attributes("-topmost", True)
        if platform.startswith("win"):
            dialog.after(200, lambda: dialog.iconbitmap("V6-logo.ico"))
        dialog.wait_visibility()  # Dialog kutusu görünür hale gelene kadar bekle


        self.cekilen_veri = float(dialog.get_input())
        self.slider.set(self.cekilen_veri)
        self.progressbar_2.set(self.cekilen_veri)
        self.son.configure(text="Saniye: " + str(self.cekilen_veri))

    # --------------Slider Değer Değişimi --------------------------------------------------
    def slider_deger_degisti(self, yeni_deger):
        self.progressbar_2.set(yeni_deger)
        self.son.configure(text=f"Saniye: {yeni_deger:.2f}")


