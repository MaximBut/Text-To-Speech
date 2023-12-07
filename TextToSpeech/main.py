from gtts import gTTS
from tkinter import *
import os
import sys
from tkinter.filedialog import askopenfile, askdirectory, askopenfilename

root = Tk()
root.config(bg='#2f917f')
root.geometry('1000x700')
root.title('Текст в речь')
root.resizable(height=False, width=False)
lst = []
wordv = StringVar()
filev = StringVar()
outf = os.path.abspath('Output files')

lbll = Label(text='Настоятельно рекомендую прочитать инструкцию, нажав на "?"', font=('Arial', 10),
             bg='#2f917f', fg='white', wraplength=240)
lbll.place(x=20, y=15)

lbl = Label(root, text='Текст в речь', font=('Arial', 35), bg='#2f917f', fg='white')
lbl.pack()

lbl1 = Label(root, text='Ваш текст:', font=('Arial', 17), bg='#2f917f', fg='white')
lbl1.place(x=80, y=100)

word = Entry(root, textvariable=wordv, font=('Arial', 15), width=15, justify=CENTER, bg='#1f6155', fg='white')
word.place(x=55, y=140)

# ========================================== #

lbl2 = Label(root,
               text="Выберите язык:",
               font=("Arial", 18),
               bg='#2f917f',
               fg='white')
lbl2.place(x=400, y=100)

lang = IntVar()
eng = Radiobutton(root,
                   text="Английский",
                   font=("Arial", 16),
                   anchor='w',
                   value=1,
                   variable=lang,
                   indicator=0, border=4)
eng.place(x=380, y=140)

ru = Radiobutton(root,
                   text="Русский",
                   font=("Arial", 16),
                   anchor='w',
                   value=2,
                   variable=lang,
                   indicator=0, border=4)
ru.place(x=380, y=190)

ua = Radiobutton(root,
                   text="Украинский",
                   font=("Arial", 16),
                   anchor='w',
                   value=3,
                   variable=lang,
                   indicator=0, border=4
                   )
ua.place(x=380, y=240)

# ============================================== #

lbl1 = Label(root, text='Название файла:', font=('Arial', 17), bg='#2f917f', fg='white')
lbl1.place(x=750, y=100)

file = Entry(root, textvariable=filev, font=('Arial', 15), width=15, bg='#1f6155', fg='white', justify=CENTER)
file.place(x=762, y=140)

def sync():
    filev.set(wordv.get())

btnn = Button(root, text='Синхронизировать слово с названием файла', justify=CENTER, bg='#2f917f', fg='white',
              font=('Arial', 13), wraplength=150, command=sync, border=3)
btnn.place(x=85, y=190)
# ============================================= #

lbl4 = Label(root, text='', font=('Arial', 12), bg='#2f917f', fg='white')
lbl4.pack()

def voice():
    if lang.get() == 1:
        tts = gTTS(word.get(), lang='en')
        filename = os.path.join(os.path.abspath('Output files'), file.get() + ".mp3")
        tts.save(filename)
        lbl4.config(text=f'Файл {file.get()} сохранен в директорию {os.path.abspath("Output files")}')
        word.delete(0, END)
    
    if lang.get() == 2:
        tts = gTTS(word.get(), lang='ru')
        filename = os.path.join(os.path.abspath('Output files'), file.get() + ".mp3")
        tts.save(filename)
        lbl4.config(text=f'Файл {file.get()} сохранен в директорию {os.path.abspath("Output files")}')
        word.delete(0, END)
    
    if lang.get() == 3:
        tts = gTTS(word.get(), lang='uk')
        filename = os.path.join(os.path.abspath('Output files'), file.get() + ".mp3")
        tts.save(filename)
        lbl4.config(text=f'Файл {file.get()} сохранен в директорию {os.path.abspath("Output files")}')
        word.delete(0, END)


def openexp():
    os.startfile('Output files')
    
def helpp():
    os.startfile('Instructions.txt')
        
btn = Button(root, text='Озвучить и сохранить', command=voice, font=('Arial', 20), bg='#2f917f', fg='white', border=3)
btn.place(x=200, y=290)

btn1 = Button(root, text='Открыть проводник', command=openexp, font=('Arial', 20), bg='#2f917f', fg='white', border=3)
btn1.place(x=525, y=290)

btn2 = Button(root, text='?', command=helpp, font=('Arial', 30), bg='#2f917f', fg='white', border=3)
btn2.place(x=900, y=225)

# ============================================================================================================= #

lbl5 = Label(text='—'*45, bg='#2f917f', fg='white', font=('Arial', 16, 'bold'))
lbl5.place(x=30, y=350)

lbl6 = Label(root, text='Файл в речь', font=('Arial', 35), bg='#2f917f', fg='white')
lbl6.place(x=350, y=370)

txt = Text(wrap = "word", height=10, width=20, bg='#1f6155', fg='white', font=('Arial', 12))
txt.place(x=450, y=470)

def open_file():
    file_path = askopenfilename(filetypes=[('Text file', '*.txt')], initialdir=os.path.abspath('Spell_text_2.0'))
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.readlines()
            txt.delete("1.0", END)
            for line in content:
                line = line.rstrip()
                lst.append(line)
                txt.insert(END, line + '\n')
btn3 = Button(text='Открыть файл', bg='#2f917f', fg='white', border=3, command=open_file, font=('Arial', 17, 'bold'))
btn3.place(x=60, y=450)

lbl7 = Label(root, text='Выберите, куда сохранять папку с аудиофайлами,', font=('Arial', 11), bg='#2f917f', fg='white')
lbl7.place(x=60, y=507)

lbl8 = Label(root, text='язык выбираем сверху (стандартная директория -', font=('Arial', 11), bg='#2f917f', fg='white')
lbl8.place(x=60, y=527)

lblll = Label(root, text='- Output Files)', font=('Arial', 11), bg='#2f917f', fg='white')
lblll.place(x=60, y=547)

chs = IntVar()
th_d = Radiobutton(root,
                   text="Стандартная директория",
                   font=("Arial", 16),
                   anchor='w',
                   value=1,
                   variable=chs,
                   indicator=0, border=4)
th_d.place(x=85, y=580)

ot_d = Radiobutton(root,
                   text="Посторонняя директория",
                   font=("Arial", 16),
                   anchor='w',
                   value=2,
                   variable=chs,
                   indicator=0, border=4)
ot_d.place(x=85, y=630)

lbl9 = Label(root, text='Имя сохраняемой папки:', font=('Arial', 12), bg='#2f917f', fg='white')
lbl9.place(x=700, y=500)

dirr = Entry(root, font=('Arial', 15), width=15, justify=CENTER, bg='#1f6155', fg='white')
dirr.place(x=700, y=540)

# ================================================================================================================== #

def file_voice():
    if chs.get() == 1:
        os.chdir(os.path.abspath(outf))
        os.mkdir(dirr.get())
        for i in lst:
            if lang.get() == 1:
                tts = gTTS(str(i), lang='en')
                filename = os.path.join(os.path.abspath(dirr.get()), str(i) + ".mp3")
                tts.save(filename)
                txt.delete('1.0', END)
                os.chdir(os.path.abspath(outf))
            if lang.get() == 2:
                tts = gTTS(str(i), lang='ru')
                filename = os.path.join(os.path.abspath(dirr.get()), str(i) + ".mp3")
                tts.save(filename)
                txt.delete('1.0', END)
                os.chdir(os.path.abspath(outf))
            if lang.get() == 3:
                tts = gTTS(str(i), lang='uk')
                filename = os.path.join(os.path.abspath(dirr.get()), str(i) + ".mp3")
                tts.save(filename)
                txt.delete('1.0', END)
                os.chdir(os.path.abspath(outf))
        
        lst.clear()
                
                
    if chs.get() == 2:
        path = askdirectory(initialdir=f"{os.path.abspath('Spell_text_2.0')}", title="Выбрать каталог для сохранения")
        if path is not None:
            os.chdir(path)
            os.mkdir(dirr.get())
            for i in lst:
                if lang.get() == 1:
                    tts = gTTS(str(i), lang='en')
                    filename = os.path.join(os.path.abspath(dirr.get()), str(i) + ".mp3")
                    tts.save(filename)
                    txt.delete('1.0', END)
                    os.startfile(dirr.get())
                if lang.get() == 2:
                    tts = gTTS(str(i), lang='ru')
                    filename = os.path.join(os.path.abspath(dirr.get()), str(i) + ".mp3")
                    tts.save(filename)
                    txt.delete('1.0', END)
                    os.startfile(dirr.get())
                if lang.get() == 3:
                    tts = gTTS(str(i), lang='uk')
                    filename = os.path.join(os.path.abspath(dirr.get()), str(i) + ".mp3")
                    tts.save(filename)
                    txt.delete('1.0', END)
                    os.startfile(dirr.get())
                    
            lst.clear()

btn4 = Button(text="Озвучить", font=('Arial', 20), bg='#2f917f', fg='white', command=file_voice)
btn4.place(x=700, y=425)

# ================================================================================================== #

def exitt():
    sys.exit()

btn5 = Button(text='Выход', font=('Arial', 20), bg='#2f917f', fg='white', command=exitt)
btn5.place(x=830, y=600)

root.mainloop()