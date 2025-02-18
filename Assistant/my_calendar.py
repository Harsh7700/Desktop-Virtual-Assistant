from tkinter import*
import calendar


def show():
    root = Tk()
    root.config(background='grey')
    root.title('Calendar')
    root.geometry('500x660')
    year = int (year_field.get())
    context = calendar.calendar(year)
    cal_year = Label(root, text=context, font="times 10 bold")
    cal_year.grid(row=5, column=1, padx=10)
    root.mainloop



if __name__=="__main__":
    new = Tk()
    new.config(background='grey')
    new.title('calendar')
    new.geometry('150x150')

    cal = Label(new, text="Calendar", bg='grey', font=("times",25,"bold"))
    cal.grid(row=1,column=1)
    year = Label(new, text="Enter Year: ", bg= 'dark grey')
    year.grid(row=2, column=1)
    year_field = Entry(new)
    year_field.grid(row=3, column=1)
    button = Button(new, text='show Calendar', fg='black',bg='grey',command=show)
    button.grid(row=4, columns=2)
    new.mainloop()
