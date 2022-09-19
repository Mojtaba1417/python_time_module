from Time import Time
import datetime as dt
import tkinter as tk
from tkinter import messagebox
now=dt.datetime.now()
t=Time(now.hour,now.minute,now.second)
def start():
    
    next(t)
    lbHour.config(
        text=f"{t.hour:02d}"
        )
    lbMinute.config(
        text=f"{t.minute:02d}"
        )
    lbSecond.config(
        text=f"{t.second:02d}"
        )
    btStart.after(1000,start)
    
    lbHour.config(
        text=f"{t.hour:02d}"
        )
    lbMinute.config(
        text=f"{t.minute:02d}"
        )
    lbSecond.config(
        text=f"{t.second:02d}"
            )

if __name__=="__main__":
    
    top=tk.Tk()
    top.geometry("-%d+%d" % (0, 30))
    top.title('ساعت')
    top.resizable(False,False)
    frTop=tk.Frame(master=top)
    frTop.grid(row=0,column=0)
    
    lbHour=tk.Label(master=frTop,
                text='HH',
                width=4,
                pady=10,
                bg='#0000BB',
                fg='yellow',
                font='size=30',
                )
    lbHour.grid(row=0,column=0)
    tk.Label(master=frTop,
                text=':',
                width=2,
                pady=10,
                bg='#0000BB',
                fg='yellow',
                font='size=30',
                ).grid(row=0,column=1)

    lbMinute=tk.Label(master=frTop,
                text='MM',

                width=4,
                pady=10,
                bg='#0000BB',
                fg='yellow',
                font='size=30',
                )
    lbMinute.grid(row=0,column=2)
    tk.Label(master=frTop,
                text=':',

                width=2,
                pady=10,
                bg='#0000BB',
                fg='yellow',
                font='size=30',
                ).grid(row=0,column=3)

    lbSecond=tk.Label(master=frTop,
                text='SS',

                width=4,
                pady=10,
                bg='#0000BB',
                fg='yellow',
                font='size=30',
                )
    lbSecond.grid(row=0,column=4)
    frButton=tk.Frame(master=top)
    frButton.grid(row=1,column=0)

    btExit=tk.Button(master=frButton,

            pady=3,
            padx=4,
            width=8,
            bg='red',
            fg='#22FFFF',
            font='size=30',
            text='خروج',
            command=top.destroy,  
              )
    btExit.grid(row=0,column=1)
    btStart=tk.Button(master=frButton,

                pady=3,
                width=8,
                padx=3,
                bg='#22FFFF',
                fg='red',
                font='size=30',
                text='شروع',
                command=start,  
                  )
    btStart.grid(row=0,column=0)
    top.overrideredirect(True)
    top.mainloop()



