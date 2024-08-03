from tkinter import Frame, Label, Button

import tk
root = tk
root.geomerty("500*500")
root.tittle("Tic TAc Toe")

frame1 = Frame(root)
frame1.pack()
titlelelbel = Label(frame1, text = "Tic Tac Toe")
titlelelbel.pack()

frame2 = Frame(root, bg="yellow")
frame2.pack()


#first row

button1 = Button(frame2 , text= " " ,width=16 , height=8)
button1.grib(row = 0, column=0)

button1 = Button(frame2 , text= " " ,width=16 , height=8)
button1.grib(row = 0, column=1)

button1 = Button(frame2 , text= " " ,width=16 , height=8  )
button1.grib(row = 0, column=2)

#second row

button1 = Button(frame2 , text= " " ,width=16 , height=8)
button1.grib(row = 1, column=0)

button1 = Button(frame2 , text= " " ,width=16 , height=8)
button1.grib(row = 1, column=1)

button1 = Button(frame2 , text= " " ,width=16 , height=8  )
button1.grib(row = 1, column=2)

#thurd row

button1 = Button(frame2 , text= " " ,width=16 , height=8)
button1.grib(row = 2, column=0)

button1 = Button(frame2 , text= " " ,width=16 , height=8)
button1.grib(row = 2, column=1)

button1 = Button(frame2 , text= " " ,width=16 , height=8  )
button1.grib(row = 2, column=2)





root.mainloop()