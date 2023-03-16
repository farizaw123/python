from tkinter import *

# Fungsi untuk menambahkan angka pada layar kalkulator
def click(angka):
    global operator
    operator += str(angka)
    var.set(operator)

# Fungsi untuk menghapus layar kalkulator
def clear():
    global operator
    operator = ""
    var.set(operator)

# Fungsi untuk menghitung hasil kalkulasi
def equal():
    try:
        global operator
        hasil = str(eval(operator))
        var.set(hasil)
        operator = ""
    except:
        var.set("Error")
        operator = ""

# Membuat tampilan UI
root = Tk()
root.title("Kalkulator Sederhana")

operator = ""
var = StringVar()

# Menambahkan label untuk menampilkan layar kalkulator
layar = Entry(root, textvariable=var, font=("Arial", 20, "bold"), bd=5, insertwidth=4, bg="powder blue", justify="right")
layar.grid(columnspan=4)

# Menambahkan tombol angka pada kalkulator
tombol_1 = Button(root, text="1", padx=16, pady=16, font=("Arial", 12, "bold"), command=lambda: click(1))
tombol_1.grid(row=1, column=0)

tombol_2 = Button(root, text="2", padx=16, pady=16, font=("Arial", 12, "bold"), command=lambda: click(2))
tombol_2.grid(row=1, column=1)

tombol_3 = Button(root, text="3", padx=16, pady=16, font=("Arial", 12, "bold"), command=lambda: click(3))
tombol_3.grid(row=1, column=2)

tombol_4 = Button(root, text="4", padx=16, pady=16, font=("Arial", 12, "bold"), command=lambda: click(4))
tombol_4.grid(row=2, column=0)

tombol_5 = Button(root, text="5", padx=16, pady=16, font=("Arial", 12, "bold"), command=lambda: click(5))
tombol_5.grid(row=2, column=1)

tombol_6 = Button(root, text="6", padx=16, pady=16, font=("Arial", 12, "bold"), command=lambda: click(6))
tombol_6.grid(row=2, column=2)

tombol_7 = Button(root, text="7", padx=16, pady=16, font=("Arial", 12, "bold"), command=lambda: click(7))
tombol_7.grid(row=3, column=0)

tombol_8 = Button(root, text="8", padx=16, pady=16, font=("Arial", 12, "bold"), command=lambda: click(8))
tombol_8.grid(row=3, column=1)

tombol_9 = Button(root, text="9", padx=16, pady=16, font=("Arial", 12, "bold"), command=lambda: click(9))
tombol_9.grid(row=3, column=2)

tombol_0 = Button(root, text="0", padx=16, pady=16, font=("Arial", 12, "bold"), command=lambda: click(0))
tombol_0.grid(row=4, column=0)

#Menambahkan tombol operasi pada kalkulator
tombol_tambah = Button(root, text="+", padx=16, pady=16, font=("Arial", 12, "bold"), command=lambda: click("+"))
tombol_tambah.grid(row=1, column=3)

tombol_kurang = Button(root, text="-", padx=16, pady=16, font=("Arial", 12, "bold"), command=lambda: click("-"))
tombol_kurang.grid(row=2, column=3)

tombol_kali = Button(root, text="", padx=16, pady=16, font=("Arial", 12, "bold"), command=lambda: click(""))
tombol_kali.grid(row=3, column=3)

tombol_bagi = Button(root, text="/", padx=16, pady=16, font=("Arial", 12, "bold"), command=lambda: click("/"))
tombol_bagi.grid(row=4, column=3)

#Menambahkan tombol lainnya pada kalkulator
tombol_clear = Button(root, text="Clear", padx=16, pady=16, font=("Arial", 12, "bold"), command=clear)
tombol_clear.grid(row=4, column=1)

tombol_sama_dengan = Button(root, text="=", padx=16, pady=16, font=("Arial", 12, "bold"), command=equal)
tombol_sama_dengan.grid(row=4, column=2)

#Menjalankan tampilan UI kalkulator
root.mainloop()