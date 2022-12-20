from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk

# CORES
cor0 = '#444466'
cor1 = '#feffff'
cor2 = '#6f9fbd'
cor3 = '#38576b'
cor4 = '#403d3d'
cor5 = '#ef5350'

# Window

janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=cor1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

# framePokemon

framePokemon = Frame(janela, width=550, height=290, relief='flat')
framePokemon.grid(row=1, column=0)

# Nome Pokémon

nomePokemon = Label(framePokemon, text='Pikachu', relief='flat', anchor='center', font='Fixedsys 20',
                    bg=cor1, fg=cor0)
nomePokemon.place(x=12, y=15)

# Elemento Pokémon
elementoPokemon = Label(framePokemon, text='Elétrico', relief='flat', anchor='center', font='Ivy 10 bold',
                        bg=cor1, fg=cor0)
elementoPokemon.place(x=20, y=60)

# PokeId
pokeId = Label(framePokemon, text='#025', anchor='center', relief='flat', font='Ivy 10 bold', bg=cor1, fg=cor0)
pokeId.place(x=20, y=90)

# PokeImage
pokeImage = Image.open('images/pikachu.png')
pokeImage = pokeImage.resize((238, 238))
pokeImage = ImageTk.PhotoImage(pokeImage)

exibeImagem = Label(framePokemon, image=pokeImage, relief='flat', bg=cor1, fg=cor0)
exibeImagem.place(x=60, y=50)

elementoPokemon.lift()

# status
pokeStatus = Label(janela, text='Status', relief='flat', anchor='center', font='Verdana 20 bold',
                   bg=cor1, fg=cor0)
pokeStatus.place(x=15, y=310)

# PokeHp
pokeHp = Label(janela, text='HP: 100', relief='flat', anchor='center', font='Verdana 10', bg=cor1, fg=cor0)
pokeHp.place(x=20, y=350)

# PokeAtaque
pokeAtk = Label(janela, text='Ataque: 600', relief='flat', anchor='center', font='Verdana 10',
                bg=cor1, fg=cor0)
pokeAtk.place(x=20, y=375)

# PokeDefesa
pokeDef = Label(janela, text='Defesa: 500', relief='flat', anchor='center', font='Verdana 10',
                bg=cor1, fg=cor0)
pokeDef.place(x=20, y=400)

# PokeVelocidade
pokeVelocidade = Label(janela, text='Velocidade: 300', relief='flat', anchor='center', font='Verdana 10',
                       bg=cor1, fg=cor0)
pokeVelocidade.place(x=20, y=425)

# TotalAtributos
totalAttr = Label(janela, text='Total: 1700', relief='flat', anchor='center', font='Verdana 10',
                  bg=cor1, fg=cor0)
totalAttr.place(x=20, y=450)

# PokeSkills
pokeSkills = Label(janela, text='Skills', relief='flat', anchor='center', font='Verdana 20 bold',
                   bg=cor1, fg=cor0)
pokeSkills.place(x=200, y=310)

# PokeSkill1
pokeSkill1 = Label(janela, text='Choque do Trovão', relief='flat', anchor='center', font='Verdana 10',
                   bg=cor1, fg=cor0)
pokeSkill1.place(x=200, y=350)

# PokeSkill2
pokeSkill2 = Label(janela, text='Cabeçada', relief='flat', anchor='center', font='Verdana 10',
                   bg=cor1, fg=cor0)
pokeSkill2.place(x=200, y=375)

# Imagem-Button1
pokeImageButton1 = Image.open('images/cabeca-pikachu.png')
pokeImageButton1 = pokeImageButton1.resize((40, 40))
pokeImageButton1 = ImageTk.PhotoImage(pokeImageButton1)

# Imagem-Button2
pokeImageButton2 = Image.open('images/cabeca-bulbasaur.png')
pokeImageButton2 = pokeImageButton2.resize((40, 40))
pokeImageButton2 = ImageTk.PhotoImage(pokeImageButton2)

# Imagem-Button3
pokeImageButton3 = Image.open('images/cabeca-charmander.png')
pokeImageButton3 = pokeImageButton3.resize((40, 40))
pokeImageButton3 = ImageTk.PhotoImage(pokeImageButton3)

# Imagem-Button4
pokeImageButton4 = Image.open('images/cabeca-dragonite.png')
pokeImageButton4 = pokeImageButton4.resize((40, 40))
pokeImageButton4 = ImageTk.PhotoImage(pokeImageButton4)

# Imagem-Button5
pokeImageButton5 = Image.open('images/cabeca-gyarados.png')
pokeImageButton5 = pokeImageButton5.resize((40, 40))
pokeImageButton5 = ImageTk.PhotoImage(pokeImageButton5)

# Imagem-Button6
pokeImageButton6 = Image.open('images/cabeca-gengar.png')
pokeImageButton6 = pokeImageButton6.resize((40, 40))
pokeImageButton6 = ImageTk.PhotoImage(pokeImageButton6)

# Button1
pokeButton1 = Button(janela, image=pokeImageButton1, text='Pikachu', width=150, relief='raised',
                     compound=LEFT, padx=5, anchor=NW, overrelief=RIDGE, font='Verdana 12', bg=cor1, fg=cor0)
pokeButton1.place(x=375, y=50)

# Button2
pokeButton2 = Button(janela, image=pokeImageButton2, text='Charmander', width='150', padx=5, font='Verdana 12',
                     relief='raised', compound=LEFT, anchor=NW, overrelief=RIDGE, bg=cor1, fg=cor0)
pokeButton2.place(x=375, y=105)

# Button3
pokeButton3 = Button(janela, image=pokeImageButton3, text='Charmander', width=150, compound=LEFT, anchor=NW, padx=5,
                     font='Verdana 12', relief='raised', overrelief=RIDGE, bg=cor1, fg=cor0)
pokeButton3.place(x=375, y=160)

# Button4
pokeButton4 = Button(janela, image=pokeImageButton4, width='150', padx=5, text='Dragonite', anchor=NW, relief='raised',
                     overrelief=RIDGE, compound=LEFT, font='Verdana 12', bg=cor1, fg=cor0)
pokeButton4.place(x=375, y=215)

# Button5
pokeButton5 = Button(janela, image=pokeImageButton5, text='Gyarados', width='150', padx=5, font='Verdana 12',
                     relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, bg=cor1, fg=cor0)
pokeButton5.place(x=375, y=270)

# Button6
pokeButton6 = Button(janela, image=pokeImageButton6, text='Gengar', width='150', padx=5, font='Verdana 12',
                     relief='raised', overrelief=RIDGE, anchor=NW, compound=LEFT, bg=cor1, fg=cor0)
pokeButton6.place(x=375, y=325)

janela.mainloop()
