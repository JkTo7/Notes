from Tkinter import *
from tkColorChooser import askcolor                  

def callback():       #Starling color, Window's title
    result = askcolor(color="", title = "Select A Color") 
    print result
    
root = Tk()

#     (Window, Button's label,    forground color, Buttun's Action).(Formats button)
Button(root, text='Choose Color', bg="darkgreen", command=callback).pack(side=LEFT, padx=10)


#     (Button's label, WINDOW's action, forground color).(Formats button)
Button(text='Quit', command=root.quit,bg="red").pack(side=LEFT, padx=10)
mainloop()
