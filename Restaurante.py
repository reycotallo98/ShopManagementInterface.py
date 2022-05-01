import tkinter
from tkinter import *
from tkinter import filedialog, messagebox
import random
import datetime

operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def click_button(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    visor_calculadora.delete(0, END)
    global operador
    operador = ''


def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    borrar()
    visor_calculadora.insert(0, resultado)


def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()  # con esto hacemos que el cursor s eprepare para escribir ahí automaticamente
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set(0)

        x += 1
    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set(0)
        x += 1
    x = 0
    for c in cuadros_postres:
        if variablespdotres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0, END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set(0)
        x += 1


def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1
    p = 0
    sub_total_bebida = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1
    p = 0
    sub_total_postres = 0
    for cantidad in texto_postres:
        sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postres[p])
        p += 1
    sub_total = sub_total_comida + sub_total_postres + sub_total_bebida
    impuestos = sub_total * 0.7
    var_costo_comida.set(f'$ {round(sub_total_comida, 2)}')
    var_costo_bebida.set(f'$ {round(sub_total_bebida, 2)}')
    var_costo_postres.set(f'$ {round(sub_total_postres, 2)}')
    var_costo_subtotal.set(f'${round(sub_total, 2)}')
    var_costo_impuestos.set(f'$ {round(impuestos, 2)}')
    var_costo_total.set(f'$ {round(sub_total - impuestos, 2)}')


def generar_recibo():
    texto_de_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}:{fecha.second}'
    texto_de_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_de_recibo.insert(END, f'*' * 61 + '\n')
    texto_de_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_de_recibo.insert(END, f'-' * 73 + '\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_de_recibo.insert(END,
                                   f'{lista_comidas[x]}\t\t{comida.get()}\t$ {round(int(comida.get()) * precios_comida[x], 2)}\n')
        x += 1
    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_de_recibo.insert(END,
                                   f'{lista_bebidas[x]}\t\t{bebida.get()}\t$ {round(int(bebida.get()) * precios_bebida[x], 2)}\n')
        x += 1
    x = 0
    for postres in texto_postres:
        if postres.get() != '0':
            texto_de_recibo.insert(END,
                                   f'{lista_postres[x]}\t\t{postres.get()}\t$ {round(int(postres.get()) * precios_postres[x], 2)}\n')
        x += 1
    texto_de_recibo.insert(END, f'-' * 73 + '\n')
    texto_de_recibo.insert(END, f'Costo de la comida: \t\t\t{var_costo_comida.get()}\n')
    texto_de_recibo.insert(END, f'Costo de la bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_de_recibo.insert(END, f'Costo de los postres: \t\t\t{var_costo_postres.get()}\n')
    texto_de_recibo.insert(END, f'Costo de subtotal: \t\t\t{var_costo_subtotal.get()}\n')
    texto_de_recibo.insert(END, f'Costo de impuestos: \t\t\t{var_costo_impuestos.get()}\n')
    texto_de_recibo.insert(END, f'Costo total: \t\t\t\t{var_costo_total.get()}\n')
    texto_de_recibo.insert(END, f'*' * 61 + '\n')
    texto_de_recibo.insert(END, f'Lo esperamos pronto\n')


def guardar_recibo():
    info_recibo = texto_de_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Su recibo ha sido guardado')
    reset()


def reset():
    texto_de_recibo.delete(0.1, END)
    #reseteamos los cuadros de texto
    for text in texto_comida:
        text.set('0')
    for text in texto_bebida:
        text.set('0')
    for text in texto_postres:
        text.set('0')
    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)
    #descativamos los cuadros de texto
    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variablespdotres:
        v.set(0)
    #reseteamos las variables
    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postres.set('')
    var_costo_impuestos.set('')
    var_costo_subtotal.set('')
    var_costo_total.set('')


# iniciar tkinter
aplicacion = Tk()

# Tamaño de la ventana- tamaño yxj-posicion x -posicion y
aplicacion.geometry('1120x630+0+0')

# evitar maximizar
aplicacion.resizable(0, 0)

# titulo de la ventana
aplicacion.title("Mi Restaurante - Sistema de facturacion")

# Color de fondo
aplicacion.config(bg='burlywood')

# panel superior|| donde se aloja,tamaño del borde,efecto de fondo
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)

panel_superior.pack(side=TOP)

# etiqueta titulo|donde va, texto que queremos que lleve,color de la fuente,fuente, color de fondo
etiqueta_titulo = Label(panel_superior, text='Sistema de facturacion', fg='black',
                        font=('Dosis', 58), bg='burlywood', width=20, anchor=tkinter.CENTER)

etiqueta_titulo.grid(row=0, column=0)

# Panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)

# Panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4',
                           bg='burlywood2')
panel_comidas.pack(side=LEFT)

# Panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4',
                           bg='burlywood2')
panel_bebidas.pack(side=LEFT)

# Panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4',
                           bg='burlywood2')
panel_postres.pack(side=LEFT)

panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)
# Panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()  # Si no pones nada se va para arriba por defecto

# Panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()  # Si no pones nada se va para arriba por defecto

# Panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='azure4')
panel_botones.pack()  # Si no pones nada se va para arriba por defecto

# lista de productos
lista_comidas = ['pollo', 'cordero', 'salmon', 'merluza', 'kebab', 'pizza1', 'pizza2', 'pizza3']
lista_bebidas = ['agua', 'soda', 'jugo', 'cola', 'vino1', 'vino2', 'cerveza1', 'cerveza2']
lista_postres = ['galleta', 'helado', 'fruta', 'flan', 'mousse', 'pastel1', 'pastel2', 'pastel3']

# cargar dentro de paneles y generar items comida
contador = 0
variables_comida = []
cuadros_comida = []
texto_comida = []
for comida in lista_comidas:
    # crear checkbutton

    variables_comida.append('')
    variables_comida[contador] = IntVar()  # Clase de TKinder que almacena el 0 o el 1
    comida = Checkbutton(panel_comidas,
                         text=comida,
                         font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0,
                         bg='burlywood2',
                         variable=variables_comida[contador],
                         command=revisar_check)
    comida.grid(row=contador,
                column=0,
                sticky=W)

    # crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()  # variable por defecto de TKinder
    texto_comida[contador].set('0')  # Le asignamos el valor por defecto 0
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador]
                                     )
    cuadros_comida[contador].grid(row=contador, column=1)
    contador += 1

contador = 0
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()  # Clase de TKinder que almacena el 0 o el 1
    bebida = Checkbutton(panel_comidas, text=bebida,
                         font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0, bg='burlywood2',
                         variable=variables_bebida[contador],
                         command=revisar_check)
    bebida.grid(row=contador, column=2, sticky=W)
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()  # variable por defecto de TKinder
    texto_bebida[contador].set('0')  # Le asignamos el valor por defecto 0
    cuadros_bebida[contador] = Entry(panel_comidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador]
                                     )
    cuadros_bebida[contador].grid(row=contador, column=3)
    contador += 1

contador = 0
variablespdotres = []
cuadros_postres = []
texto_postres = []
for postre in lista_postres:
    variablespdotres.append('')
    variablespdotres[contador] = IntVar()  # Clase de TKinder que almacena el 0 o el 1
    postre = Checkbutton(panel_comidas,
                         text=postre,
                         font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0,
                         bg='burlywood2',
                         variable=variablespdotres[contador],
                         command=revisar_check)
    postre.grid(row=contador, column=4, sticky=W)
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()  # variable por defecto de TKinder
    texto_postres[contador].set('0')  # Le asignamos el valor por defecto 0
    cuadros_postres[contador] = Entry(panel_comidas,
                                      font=('Dosis', 18, 'bold'),
                                      bd=1,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=texto_postres[contador]
                                      )
    cuadros_postres[contador].grid(row=contador, column=5)
    contador += 1

# variables
var_costo_comida = StringVar()

# etiquetas de costo y campos de entrada

etiqueta_costocomida = Label(panel_costos,
                             text='Costo comida',
                             font=('Dosis', 12, 'bold'),
                             bg='azure4',
                             fg='white')
etiqueta_costocomida.grid(row=0, column=0, pady=2)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, pady=2)

# variables
var_costo_bebida = StringVar()

# etiquetas de costo y campos de entrada

etiqueta_costobebida = Label(panel_costos,
                             text='Costo bebidas',
                             font=('Dosis', 12, 'bold'),
                             bg='azure4',
                             fg='white')
etiqueta_costobebida.grid(row=0, column=2, pady=2)

texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=0, column=3, pady=2)

# variables
var_costo_postres = StringVar()

# etiquetas de costo y campos de entrada

etiqueta_costopostres = Label(panel_costos,
                              text='Costo postres',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costopostres.grid(row=0, column=4, pady=2)

texto_costo_postres = Entry(panel_costos,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costo_postres)
texto_costo_postres.grid(row=0, column=5, pady=2)

# variables
var_costo_subtotal = StringVar()

# etiquetas de costo y campos de entrada

etiqueta_costosubtotal = Label(panel_costos,
                               text='subtotal',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_costosubtotal.grid(row=1, column=0, pady=2)

texto_costo_subtotal = Entry(panel_costos,
                             font=('Dosis', 12, 'bold'),
                             bd=1,
                             width=10,
                             state='readonly',
                             textvariable=var_costo_subtotal)
texto_costo_subtotal.grid(row=1, column=1, pady=2)

# variables
var_costo_total = StringVar()

# etiquetas de costo y campos de entrada

etiqueta_costototal = Label(panel_costos,
                            text='Costo total',
                            font=('Dosis', 12, 'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_costototal.grid(row=1, column=2, pady=2)

texto_costo_total = Entry(panel_costos,
                          font=('Dosis', 12, 'bold'),
                          bd=1,
                          width=10,
                          state='readonly',
                          textvariable=var_costo_total)
texto_costo_total.grid(row=1, column=3, pady=2)

# variables
var_costo_impuestos = StringVar()

# etiquetas de costo y campos de entrada

etiqueta_costoimpuestos = Label(panel_costos,
                                text='Costo impuestos',
                                font=('Dosis', 12, 'bold'),
                                bg='azure4',
                                fg='white')
etiqueta_costoimpuestos.grid(row=1, column=4)

texto_costo_impuestos = Entry(panel_costos,
                              font=('Dosis', 12, 'bold'),
                              bd=1,
                              width=10,
                              state='readonly',
                              textvariable=var_costo_impuestos)
texto_costo_impuestos.grid(row=1, column=5)
# area de recibo

texto_de_recibo = Text(panel_recibo,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=41,
                       height=10)
texto_de_recibo.grid(row=0, column=0)

# botones
botones = ['total', 'recibo', 'guardar', 'resetear']
botones_creados = []
columnas = 0
for a in botones:
    boton = Button(panel_botones,
                   text=a,
                   font=('Dosis', 14, 'bold'),
                   fg='white',
                   bg='azure4',
                   width=9)
    boton.grid(row=0, column=columnas)
    columnas += 1
    botones_creados.append(boton)
botones_creados[0].config(command=total)
botones_creados[1].config(command=generar_recibo)
botones_creados[2].config(command=guardar_recibo)
botones_creados[3].config(command=reset)

# calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold',),
                          width=38,
                          bd=1)
visor_calculadora.grid(row=0, column=0, columnspan=4)
botones_calc = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', 'x', 'CE', 'Enter', '0', '/']
botones_guardados = []
fila = 1
columna = 0
for b in botones_calc:
    b = Button(panel_calculadora,
               text=b.title(),
               font=('Dosis', 16, 'bold'),
               fg='white',
               bg='azure4',
               bd=1,
               width=8)
    botones_guardados.append(b)
    b.grid(row=fila, column=columna)
    if columna == 3:
        fila += 1
    columna += 1
    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda: click_button('7'))
botones_guardados[1].config(command=lambda: click_button('8'))
botones_guardados[2].config(command=lambda: click_button('9'))
botones_guardados[3].config(command=lambda: click_button('+'))
botones_guardados[4].config(command=lambda: click_button('4'))
botones_guardados[5].config(command=lambda: click_button('5'))
botones_guardados[6].config(command=lambda: click_button('6'))
botones_guardados[7].config(command=lambda: click_button('-'))
botones_guardados[8].config(command=lambda: click_button('1'))
botones_guardados[9].config(command=lambda: click_button('2'))
botones_guardados[10].config(command=lambda: click_button('3'))
botones_guardados[11].config(command=lambda: click_button('*'))
botones_guardados[12].config(command=lambda: borrar())
botones_guardados[13].config(command=lambda: obtener_resultado())
botones_guardados[14].config(command=lambda: click_button('0'))
botones_guardados[15].config(command=lambda: click_button('/'))

# mequieromorir.py

#
# Hacer que la pantalla no se cierre(Esto siempre al final)
aplicacion.mainloop()
