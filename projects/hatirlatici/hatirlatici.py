from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox

master = Tk()
master.title("Hatirlatici")

canvas = Canvas(master, height=400, width=750)
canvas.pack()  #pack, place, grid nesneyi inkişaf ettirmek için

frame_ust = Frame(master,background="#add8e6")  # çerçeve oluşturma renklendirme
frame_ust.place(relx=0,rely=0,relwidth=1,relheight=0.2) # relative x,y gibi 

frame_sol = Frame(master,background="#add8e6")  
frame_sol.place(relx=0,rely=0.21,relwidth=0.24,relheight=0.79)

frame_sag = Frame(master,background="#add8e6")  
frame_sag.place(relx=0.245,rely=0.21,relwidth=0.755,relheight=0.79)

hatirlat_tipi = Label(master=frame_ust, bg="#add8e6", text="Hatirlatma Tipi:", font= "Verdana 12 bold")
hatirlat_tipi.pack(padx=10, pady=10, side =LEFT)

hatirlatma_tipi_opsiyon = StringVar(frame_ust)
hatirlatma_tipi_opsiyon.set("\t")

hatirlatma_tipi_acilir_menu = OptionMenu(
    frame_ust,
    hatirlatma_tipi_opsiyon,
    "Dogum gunu", "Alisveris", "Odeme",)
hatirlatma_tipi_acilir_menu.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tarih_secici = DateEntry(frame_ust, width=15, background="orange", foreground="black", borderwidth=1, locale="tr_TR",)
hatirlatma_tarih_secici._top_cal.overrideredirect(True)
hatirlatma_tarih_secici.pack(padx=10, pady=10, side=RIGHT)

hatirlat_tarihi = Label(master=frame_ust, bg="#add8e6", text="Hatirlatma Tarihi:", font= "Verdana 12 bold")
hatirlat_tarihi.pack(padx=10, pady=10, side =RIGHT)

Label(master=frame_sol, bg="#add8e6", text="Hatirlatma Yöntemi:", font= "Verdana 10 bold").pack(padx=10, pady=20, anchor="nw")

var = IntVar()

R1 = Radiobutton(frame_sol, text="Sisteme Kaydet", variable=var, value=1, bg="#add8e6", font="Verdana 10")
R1.pack(anchor="nw",pady=5,padx=15)

R2 = Radiobutton(frame_sol, text="E-posta Gonder", variable=var, value=2, bg="#add8e6", font="Verdana 10")
R2.pack(anchor="nw",pady=5,padx=15)

var1 = IntVar()
C1= Checkbutton(frame_sol, text="Ayni gun", variable=var1, onvalue=1, offvalue=0, bg="#add8e6", font="Verdana 10")
C1.pack(anchor="nw",pady=5,padx=25)

var2 = IntVar()
C2= Checkbutton(frame_sol, text="Bir gun önce", variable=var2, onvalue=1, offvalue=0, bg="#add8e6", font="Verdana 10")
C2.pack(anchor="nw",pady=5,padx=25)

var3 = IntVar()
C3= Checkbutton(frame_sol, text="Bir hafta once", variable=var3, onvalue=1, offvalue=0, bg="#add8e6", font="Verdana 10")
C3.pack(anchor="nw",pady=5,padx=25)

Label(master=frame_sag, bg="#add8e6", text="Hatirlatma Mesaji:", font= "Verdana 10 bold").pack(padx=10, pady=20, anchor="nw")

metin_alani = Text(frame_sag, height=14, width=65)
# metin_alani.tag_configure(tagName="",foreground="#bfbfbf", font=("Verdana", 7, "bold"))
# metin_alani.insert(END,"")
metin_alani.pack()

def gonder():
    son_mesaj = ""

    if var.get() == 1:
        son_mesaj += "Veriniz başariyla sisteme kaydedilmiştir."

        tip = hatirlatma_tipi_opsiyon.get() 
        if hatirlatma_tipi_opsiyon.get() == "":
            tip = "Genel"
        tarih = hatirlatma_tarih_secici.get()
        mesaj = metin_alani.get("1.0", "end")

        with open("./projects/hatirlatici/hatirlatmalar.txt","w") as dosya:
            dosya.write(
                "{} kategorisinde, {} tarihinde, {} icerikli hatirlatma olusturuldu.".format(tip,tarih,mesaj)
            )
            dosya.close()

    elif var.get() ==2:
        son_mesaj += "E-posta yoluyla hatirlatma size ulasacaktir."
    messagebox.showinfo("İslem basarili", son_mesaj)


gonder_butonu = Button(frame_sag, text="Gönder", command=gonder)
gonder_butonu.pack(anchor="s",pady=5)

master.mainloop()