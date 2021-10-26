from tkinter import *
from controller import *

window=Tk()
def submit():
  obj=Controller()
  url=dirname.get()
  sql=v1.get()
  xss=v2.get()
  nmap=v3.get()
  dup=v4.get()
  obj.malicious(sql,xss,nmap,dup,url)


  
labelText=StringVar()
labelText.set("URL")
labelDir=Label(window, textvariable=labelText, height=1)
labelDir.pack()

dirname=Entry(window)
dirname.pack()
dirname.focus_set()
urlget=dirname.get()
  
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
C1 = Checkbutton(window, text = "SQL Injection", variable = v1)
C2 = Checkbutton(window, text = "XSS", variable = v2)
C3 = Checkbutton(window, text = "Nmap", variable = v3)
C4 = Checkbutton(window, text = "Default Username and Password", variable = v4)
C1.pack()
C2.pack()
C3.pack()
C4.pack()

btn=Button(window, text="Proceed", command=submit)
btn.pack()

window.title('Critical Analysis of Web Portals')
window.geometry("500x500")
window.mainloop()
