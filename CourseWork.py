def out(event):
    mainWindow.destroy()

from tkinter import *

def distance(a, b):

    n, m = len(a), len(b)
    t = b
    if n > m:

        a, b = b, a
        n, m = m, n
        t = a

    current_row = range(n+1)
    for i in range(1, m+1):
        previous_row, current_row = current_row, [i]+[0]*n
        for j in range(1,n+1):
                add, delete, change = previous_row[j]+1, current_row[j-1]+1, previous_row[j-1]
                if a[j-1] != b[i-1]:
                    change += 1
               # if  min(add, delete, change) < 4 and min(add, delete, change) > 0  :
                current_row[j] = min(add, delete, change)

    return [current_row[n], t]

#ФУНКЦИЯ, КОТОРУЮ ВЫЗЫВАЕТ КНОПКА
def work(event):
    s1 = Input1.get()
    variants = [[3, '455']]
    for s2 in dic:
        d = distance(s1, s2)
        if d[0] <= int(variants[len(variants) - 1][0]):
            #  variants.clear()
            variants.append(d)
    if len(variants) < 2:
        Label2["text"] = 'Нет Результата'
        Label2["fg"] = 'red'
    else:
        Label2["text"] = 'Результат: ' + variants[len(variants) - 1][1]
        Label2["fg"] = 'black'


# ПОДКЛЮЧЕНИЕ СЛОВАРЯ
dict_file = "dictrus.txt"
dic = []
with open(dict_file, 'r') as read_file:
    for line in read_file:
        dic.append(line.strip('\n'))

#РАЗЛИЧНЫЕ НАСТРОЙКИ ОКНА
mainWindow = Tk()
mainWindow.title('Орфоредактор')
mainWindow.geometry('300x150')
Input1 = Entry(mainWindow,width=20)
ButtonCheck = Button(mainWindow,text='Проверить',bg='black',width=18)
Label1=Label(mainWindow,text='Введите слово:',height=1,fg='black',font='arial 14')
Label2=Label(mainWindow,text='Результат',height=2,fg='gray',font='arial 14')
ButtonExit = Button(mainWindow,text='Выход',bg='black')


Label1.pack(side='top')
Input1.pack()
ButtonCheck.pack()
Label2.pack()
ButtonExit.pack(side='right')

ButtonCheck.bind("<Button-1>", work)
ButtonExit.bind("<Button-1>", out)

mainWindow.mainloop()