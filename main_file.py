from PIL import Image
from pytesseract import image_to_string
from googletrans import Translator
from tkinter import messagebox
from tkinter import Button
from tkinter import Tk
from tkinter.filedialog import askopenfilename

filename = askopenfilename(initialdir='C:\\',title = "Select file")

image = image_to_string(Image.open(filename), lang='hin+eng+guj')
str2 = " "
result2=image.split()
b=str2.join(result2)
print(b)

top= Tk()
top.geometry("250x50")
result=[]
str1 = " "
def translation(): 
    for word in result2:
        translator = Translator()
        demo = translator.translate(word)
        m=demo.text
        result.append(m)
    a=str1.join(result)
    messagebox.showinfo("result",a)
    
b=Button(top,text="Click for Output", command=translation)
b.pack()
top.mainloop()



