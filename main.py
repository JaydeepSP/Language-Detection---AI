from tkinter import * 
from tkinter import ttk, filedialog 
import googletrans 
from googletrans import Translator 
from PIL import Image 
from langdetect import detect 
import pytesseract 
pytesseract.pytesseract.tesseract_cmd = r’F:\sem 7\tesseract.exe’ 
root = Tk() 
root.title(“Translator”) 
root.geometry(“1080x400”) 
root.resizable(False, False) 
root.configure(background=”white”) 
image_icon=PhotoImage(file=’KS.png’) 
root.iconphoto(False,image_icon) 
def label_change(): 
 if “Image” in combo1.get(): 
 return 
 c = combo1.get() 
 c1 = combo2.get() 
 label1.configure(text=c)
  label2.configure(text=c1) 
 root.after(1000, label_change) 
def detect_language(text): 
 try: 
 language = detect(text) 
 return language 
 except: 
 return None 
def choose_file(): 
 file_path = filedialog.askopenfilename(filetypes=[(“Image files”, “.png;*.jpg;*.jpeg”)]) 
 if file_path: 
 print(file_path) 
 fetched_text = process_image(file_path) 
 text1.delete(1.0, END) 
 text1.insert(END, fetched_text) 
 detected_language = detect_language(fetched_text) 
 if detected_language: 
 language_name = language.get(detected_language) 
 combo1.set(language_name) 
 label1.configure(text=language_name) 
 else: 
 combo1.set(“SELECT LANGUAGE”) 
def translate_now(): 
 text_ = text1.get(1.0, END)
 t1 = Translator() 
 trans_text = t1.translate(text_, src=combo1.get(), dest=combo2.get()) 
 trans_text = trans_text.text 
 text2.delete(1.0, END) 
 text2.insert(END, trans_text) 
def process_image(file_path): 
 image = Image.open(file_path) 
 text = pytesseract.image_to_string(image) 
 return text 
language = googletrans.LANGUAGES 
 anguage = list(language.values()) 
combo1 = ttk.Combobox(root, values= anguage, font=”Roboto 14”, state=”r”) 
combo1.place(x=110, y=20) 
combo1.set(“ENGLISH”) 
label1 = Label(root, text=”ENGLISH”, font=”segoe 30 bold”, bg=”white”, width=18, bd=5, relief=GROOVE) 
label1.place(x=10, y=50) 
combo2 = ttk.Combobox(root, values= anguage, font=”Roboto 14”, state=”r”) 
combo2.place(x=730, y=20) 
combo2.set(“SELECT LANGUAGE”) 
label2 = Label(root, text=”ENGLISH”, font=”segoe 30 bold”, bg=”white”, width=18, bd=5, relief=GROOVE) 
label2.place(x=620, y=50)
f = Frame(root, bg=”Black”, bd=5) 
f.place(x=10, y=118, width=440, height=210) 
text1 = Text(f, font=”Robote 20”, bg=”white”, relief=GROOVE, wrap=WORD) 
text1.place(x=0, y=0, width=430, height=200) 
Scrollbar1 = Scrollbar(f) 
Scrollbar1.pack(side=”right”, fill=’y’) 
Scrollbar1.configure(command=text1.yview) 
text1.configure(yscrollcommand=Scrollbar1.set) 
choos_file=Button(root,text=”Image”,font=(“Roboto”,15),activebackground=”white”,cursor=”hand2”, bd=1,width=10,height=1,bg=”blue”,fg=”white”,command=choose_file) 
choos_file.place(x=355,y=11) 
f1=Frame(root,bg=”Black”,bd=5) 
f1.place(x=620,y=118,width=440,height=210) 
text2=Text(f1,font=”Robote 20”,bg=”white”,relief=GROOVE,wrap=WORD) 
text2.place(x=0,y=0,width=430,height=200) 
Scrollbar2=Scrollbar(f1) 
Scrollbar2.pack(side=”right”,fill=’y’) 
Scrollbar2.configure(command=text2.yview) 
text2.configure(yscrollcommand=Scrollbar2.set) 
translate=Button(root,text=”Translate”,font=(“Roboto”,15),activebackground=”white”,cursor=”hand2”,bd=1,width=10,height=2,bg=”blue”,fg=”white”,command=translate_now) 
translate.place(x=476,y=250) 
label_change() 
root.mainloop()