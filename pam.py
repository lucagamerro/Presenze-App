from tkinter import *
import datetime
from time import sleep

i = datetime.datetime.now()
uscd = "Uscita di %s" %i.month
if uscd == "Uscita di 1":
    usc = "Uscita di Gennaio"
if uscd == "Uscita di 2":
    usc = "Uscita di Febbraio"
if uscd == "Uscita di 3":
    usc = "Uscita di Marzo"
if uscd == "Uscita di 4":
    usc = "Uscita di Aprile"
if uscd == "Uscita di 5":
    usc = "Uscita di Maggio"
if uscd == "Uscita di 6":
    usc = "Uscita di Giugno"
if uscd == "Uscita di 7":
    usc = "Uscita di Luglio"
if uscd == "Uscita di 8":
    usc = "Uscita di Agosto"
if uscd == "Uscita di 9":
    usc = "Uscita di Settembre"
if uscd == "Uscita di 10":
    usc = "Uscita di Ottobre"
if uscd == "Uscita di 11":
    usc = "Uscita di Novembre"
if uscd == "Uscita di 12":
    usc = "Uscita di Dicembre"



def si():
    global nomep, sqp
    nomep = nome.get()
    sqp = sq.get()
    tt = Label(ro, text="Salvataggio in corso...")
    sleep(1)
    out_file = open("presenze.csv", "a")
    out_file.write(nomep)
    out_file.write(" ;")
    out_file.write(sqp)
    out_file.write(" ;")
    out_file.write("Presente a tutta l'uscita")
    out_file.write("\n"*2)
    out_file.close()
    exit()

def no():
    global nomep, sqp
    nomep = nome.get()
    sqp = sq.get()
    tt = Label(ro, text="Salvataggio in corso...")
    sleep(1)
    out_file = open("presenze.csv", "a")
    out_file.write(nomep)
    out_file.write(" ;")
    out_file.write(sqp)
    out_file.write(" ;")
    out_file.write("Non verra' all'uscita")
    out_file.write("\n"*2)
    out_file.close()
    exit()

def sr():
    global nomep, sqp
    nomep = nome.get()
    sqp = sq.get()
    tt = Label(ro, text="Salvataggio in corso...")
    sleep(1)
    out_file = open("presenze.csv", "a")
    out_file.write(nomep)
    out_file.write(" ;")
    out_file.write(sqp)
    out_file.write(" ;")
    out_file.write("Arrivera' alla sera dell'uscita")
    out_file.write("\n"*2)
    out_file.close()
    exit()

def rs():
    global nomep, sqp
    nomep = nome.get()
    sqp = sq.get()
    tt = Label(ro, text="Salvataggio in corso...")
    sleep(1)
    out_file = open("presenze.csv", "a")
    out_file.write(nomep)
    out_file.write(" ;")
    out_file.write(sqp)
    out_file.write(" ;")
    out_file.write("Andra' via alla sera della uscita")
    out_file.write("\n")
    out_file.close()
    exit()

def mt():
    global nomep, sqp
    nomep = nome.get()
    sqp = sq.get()
    tt = Label(ro, text="Salvataggio in corso...")
    sleep(1)
    out_file = open("presenze.csv", "a")
    out_file.write(nomep)
    out_file.write(" ;")
    out_file.write(sqp)
    out_file.write(" ;")
    out_file.write("Arrivara' al mattino dell'uscita")
    out_file.write("\n"*2)
    out_file.close()
    exit()

def tm():
    global nomep, sqp
    nomep = nome.get()
    sqp = sq.get()
    tt = Label(ro, text="Salvataggio in corso...")
    sleep(1)
    out_file = open("presenze.csv", "a")
    out_file.write(nomep)
    out_file.write(" ;")
    out_file.write(sqp)
    out_file.write(" ;")
    out_file.write("Andra via al mattino dell'uscita")
    out_file.write("\n"*2)
    out_file.close()
    exit()

def la():
    global nomep, sqp, alp
    nomep = nome.get()
    sqp = sq.get()
    alp = al.get()
    tt = Label(ro, text="Salvataggio in corso...")
    sleep(1)
    out_file = open("presenze.csv", "a")
    out_file.write(nomep)
    out_file.write(" ;")
    out_file.write(sqp)
    out_file.write(" ;")
    out_file.write(al)
    out_file.write("\n"*2)
    out_file.close()
    exit()

ro = Tk()
ro.geometry("400x900")
ro.title("Presenze")
t = Label(ro, text=usc).pack()
q = Label(ro, text="Nome:").pack()
nome = Entry(ro)
nome.pack()
salt = Label(ro, text=" ").pack()
w = Label(ro, text="Squadriglia:").pack()
sq = Entry(ro)
sq.pack()
salt = Label(ro, text=" ").pack()
e = Checkbutton(ro, text="Io verro' all'uscita", command=si).pack()
r = Checkbutton(ro, text="Io non verro' all'uscita", command=no).pack()
t = Checkbutton(ro, text="Io arrivero' alla sera dell'uscita", command=sr).pack()
y = Checkbutton(ro, text="Io arrivero' alla mattina dell'uscita", command=mt).pack()
u = Checkbutton(ro, text="Io andro' via alla sera dell'uscita", command=rs).pack()
i = Checkbutton(ro, text="Io andro' via al matino dell'uscita", command=tm).pack()
salt = Label(ro, text=" ").pack()
but = Button(ro, text="Esci", command=exit).pack()
ro.mainloop()
