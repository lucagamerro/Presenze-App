import tkinter as tk
import datetime

i = datetime.datetime.now()
usc = "Uscita di %s" %i.month

def gettone():
    def si():
    global nomep, sqp
    nomep = nome.get()
    sqp = sq.get()
    out_file = open("presenze.csv", "a")
    out_file.write(nomep)
    out_file.write(" ;")
    out_file.write(sqp)
    out_file.write(" ;")
    out_file.write("Presente a tutta l'uscita")
    out_file.write("\n")

    def no():
    global nomep, sqp
    nomep = nome.get()
    sqp = sq.get()
    out_file = open("presenze.csv", "a")
    out_file.write(nomep)
    out_file.write(" ;")
    out_file.write(sqp)
    out_file.write(" ;")
    out_file.write("Non verra' all'uscita")
    out_file.write("\n")

    def sr():
    global nomep, sqp
    nomep = nome.get()
    sqp = sq.get()
    out_file = open("presenze.csv", "a")
    out_file.write(nomep)
    out_file.write(" ;")
    out_file.write(sqp)
    out_file.write(" ;")
    out_file.write("Arrivera' alla sera dell'uscita")
    out_file.write("\n")

    def rs():
    global nomep, sqp
    nomep = nome.get()
    sqp = sq.get()
    out_file = open("presenze.csv", "a")
    out_file.write(nomep)
    out_file.write(" ;")
    out_file.write(sqp)
    out_file.write(" ;")
    out_file.write("Andra' via alla sera della uscita")
    out_file.write("\n")

    def mt():
    global nomep, sqp
    nomep = nome.get()
    sqp = sq.get()
    out_file = open("presenze.csv", "a")
    out_file.write(nomep)
    out_file.write(" ;")
    out_file.write(sqp)
    out_file.write(" ;")
    out_file.write("Arrivara' al mattino dell'uscita")
    out_file.write("\n")

    def tm():
    global nomep, sqp
    nomep = nome.get()
    sqp = sq.get()
    out_file = open("presenze.csv", "a")
    out_file.write(nomep)
    out_file.write(" ;")
    out_file.write(sqp)
    out_file.write(" ;")
    out_file.write("Andra via al mattino dell'uscita")
    out_file.write("\n")

    def la():
    global nomep, sqp, alp
    nomep = nome.get()
    sqp = sq.get()
    alp = al.get()
    out_file = open("presenze.csv", "a")
    out_file.write(nomep)
    out_file.write(" ;")
    out_file.write(sqp)
    out_file.write(" ;")
    out_file.write(al)
    out_file.write("\n")

ro = Tk.tk()
ro.geometry("400x900")
ro.title("Presenze")
ro.Label(text=usc)
ro.Label(text="Nome:").pack()
nome = ro.Entry(ro)
nome.pack()
ro.Label(text="Squadriglia:").pack()
sq = ro.Entry(ro)
sq.pack()
ro.Checkbutton(ro, text="Io verro' all'uscita", command=si).pack()
ro.Checkbutton(ro, text="Io non verro' all'uscita", command=no).pack()
ro.Checkbutton(ro, text="Io arrivero' alla sera dell'uscita", command=sr).pack()
ro.Checkbutton(ro, text="Io arrivero' alla mattina dell'uscita", command=mt).pack()
ro.Checkbutton(ro, text="Io andro' via alla sera dell'uscita", command=rs).pack()
ro.Checkbutton(ro, text="Io andro' via al matino dell'uscita", command=tm).pack()
al = ro.Entry(ro, text="Altro:", command=la)
al.pack()
but = ro.Button(ro, text="Salva ed esci", command=gettone)
ro.mainloop()

