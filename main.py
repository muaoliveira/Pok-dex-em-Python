from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk

### CORES ###
cor0 = '#444466'
cor1 = '#feffff'
cor2 = '#6f9fbd'
cor3 = '#38576b'
cor4 = '#403d3d'
cor5 = '#ef5350'

### Window

janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=cor1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

#framePokemon

framePokemon = Frame(janela, width=550, height=290, relief='flat')
framePokemon.grid(row=1, column=0)

#Nome Pokémon

nomePokemon = Label(framePokemon, text='Pikachu', relief='flat', anchor='center', font=('Fixedsys 20'),
                    bg=cor1, fg=cor0)
nomePokemon.place(x=12,y=15)

#Elemento Pokémon
elementoPokemon = Label(framePokemon, text='Elétrico', relief='flat', anchor='center', font=('Ivy 10 bold'),
                        bg=cor1, fg=cor0)
elementoPokemon.place(x=20, y=60)

#PokeId
pokeId = Label(framePokemon, text='#025', anchor='center', relief='flat', font=("Ivy 10 bold"), bg=cor1, fg=cor0)
pokeId.place(x=20, y=90)

#PokeImage
pokeImage = Image.open('images/pikachu.png')
pokeImage = pokeImage.resize((238, 238))
pokeImage = ImageTk.PhotoImage(pokeImage)

exibeImagem = Label(framePokemon, image=pokeImage, relief='flat', bg=cor1, fg=cor0)
exibeImagem.place(x=60, y=50)

elementoPokemon.lift()

#status
pokeStatus = Label(janela, text='Status', relief='flat', anchor='center', font=('Verdana 20 bold'),
                   bg=cor1, fg=cor0)
pokeStatus.place(x=15, y=310)

#PokeHp
pokeHp = Label(janela, text='HP: 100', relief='flat', anchor='center', font=('Verdana 10'), bg=cor1, fg=cor0)
pokeHp.place(x=20, y=350)

#PokeAtaque
pokeAtk = Label(janela, text='Ataque: 600', relief='flat', anchor='center', font=('Verdana 10'),
                bg=cor1, fg=cor0)
pokeAtk.place(x=20, y=375)

#PokeDefesa
pokeDef = Label(janela, text='Defesa: 500', relief='flat', anchor='center', font=('Verdana 10'),
                bg=cor1, fg=cor0)
pokeDef.place(x=20, y=400)

#PokeVelocidade
pokeVelocidade = Label(janela, text='Velocidade: 300', relief='flat', anchor='center', font=('Verdana 10'),
                       bg=cor1, fg=cor0)
pokeVelocidade.place(x=20, y=425)

#TotalAtributos
totalAttr = Label(janela, text='Total: 1700', relief='flat', anchor='center', font=('Verdana 10'),
                  bg=cor1, fg=cor0)
totalAttr.place(x=20, y=450)

#PokeSkills
pokeSkills = Label(janela, text='Skills', relief='flat', anchor='center', font=('Verdana 20 bold'),
                   bg=cor1, fg=cor0)
pokeSkills.place(x=200, y=310)

#PokeSkill1
pokeSkill1 = Label(janela, text='Choque do Trovão', relief='flat', anchor='center', font=('Verdana 10'),
                   bg=cor1, fg=cor0)
pokeSkill1.place(x=200, y=350)

#PokeSkill2
pokeSkill2 = Label(janela, text='Cabeçada', relief='flat', anchor='center', font=('Verdana 10'),
                   bg=cor1, fg=cor0)
pokeSkill2.place(x=200, y=375)



janela.mainloop()
