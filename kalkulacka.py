import tkinter
canvas=tkinter.Canvas(height=200,width=700)
canvas.pack()



for i in range (10):
    canvas.create_rectangle(i*30,40,(i+1)*30,70)
    canvas.create_text(i*30+15,55,text=i)
for i in range (4):
    canvas.create_rectangle(i*30,70,(i+1)*30,100)

canvas.create_text(15,85,text='C')
canvas.create_text(45,85,text='+')
canvas.create_text(75,85,text='-')
canvas.create_text(105,85,text='=')
operacia=0
vysledok=0
ukazka=canvas.create_text(3,3,anchor ='nw',font='Arial 30',text=0)
canvas.bind('<Button>',klik)
