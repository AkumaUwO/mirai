from tkinter import *
from PIL import ImageTk, Image
import chatbot
import funcionesExtras


root = Tk()
miraiImage = Image.open('mirai.jpg')
miraiImage = miraiImage.resize((177, 384))
miraiImage = ImageTk.PhotoImage(miraiImage)
root.title("Mirai pre-a1.0")
root.resizable(0,0)

MFrame = Frame(root, width="600", height="500")
MFrame.pack(fill="both", expand = "True")
MFrame.config(bg="gray")

entrada = StringVar()
respuesta = ""

text1=Text(MFrame)
text1.grid(row=1, column=1, padx="10", pady="10")
text1.insert(0.0, "Escribe tu pregunta y pulsa el boton enviar, Para recibir una respuesta.")
text1.config(state='disabled')
scroll= Scrollbar(MFrame, command=text1.yview)
scroll.grid(row=1, column=2, sticky="nsew")
text1.config(yscrollcommand=scroll.set)

label1= Label(MFrame, text="Mirai v-alpha1.0", fg="green", font=("Arial",14))
label1.grid(row=0, column=1, padx="10", pady="10")

labelImage= Label(MFrame, image=miraiImage, fg="green", font=("Times new Roman",12))
labelImage.grid(row=1, column=0, padx="10", pady="10")

label2= Label(MFrame, text="Introduce un Mensaje:", fg="green", font=("Times new Roman",12))
label2.grid(row=2, column=0, padx="10", pady="10")

entry1= Entry(MFrame,width="107", textvariable=entrada)
entry1.grid(row=2, column=1, padx="10", pady="10")


def onEnter(event):
	ejecutar()


def ejecutar():
	text1.config(state='normal')
	entradaUsuario = funcionesExtras.normalize(entrada.get())
	entradaNormal = entradaUsuario.lower()
	respuestaU = "Usuario: " + entrada.get()
	respuestaIA = "Mirai: " + chatbot.iniciar(entradaUsuario.lower())
	print(entradaUsuario.lower())
	entrada.set("")
	info = funcionesExtras.funcionPrincipal(respuestaIA, entradaNormal)
	respuestaD = text1.get(0.0, END) + "\n" + respuestaU+ "\n" + "\n" + info
	text1.delete(0.0, END)
	text1.insert(0.0, respuestaD)
	text1.config(state='disabled')

entry1.bind("<Return>", onEnter)

button1= Button(root, text="Enviar Mensaje", command=ejecutar)
button1.pack()

root.mainloop()
