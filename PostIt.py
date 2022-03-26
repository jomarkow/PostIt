import random as rd
import tkinter as tk
from tkinter.colorchooser import askcolor

def New_PostIt(color: str, txt_style: list):
    
    # Setting window
    PostIt = tk.Tk()
    PostIt.resizable(1,1)
    PostIt.geometry("300x300")
    PostIt.configure(bg=color)
    PostIt.overrideredirect(1)
    
    # TEXTO DEL POS IT
    
    txt = tk.Label(PostIt, 
            text = txt_style[0],
            font=(txt_style[1], txt_style[2]), 
            anchor='c',
            bg = color, fg = "black",
            wraplengt=290)
    
    #txt.place(x=0,y=20,width=300, height= 280)
    txt.pack(side="left", fill="both", expand=True)
    
    # DRAG WINDOW 
    
    def first_click(event):
        global first_click_x, first_click_y
        first_click_x = event.x
        first_click_y = event.y

    def do_move(event):
        x = event.x - first_click_x + PostIt.winfo_x()
        y = event.y - first_click_y + PostIt.winfo_y()
        PostIt.geometry(f"+{x}+{y}")
    
    PostIt.bind("<ButtonPress-1>", first_click)
    PostIt.bind("<B1-Motion>", do_move)
    
    # CLOSE BUTTON
    close = tk.Button(PostIt, 
            text = 'x', 
            font = "Helvetica 10", 
            borderwidth=0, 
            bg=color, 
            command=PostIt.destroy)
    
    close.place(x=280,y=0)
    
    # BLOCK BUTTON
    def toggle():

        if block.config('relief')[-1] == 'sunken':
            block.config(relief="raised", text= 'Blocked')
            PostIt.attributes('-topmost',True)
        else:
            block.config(relief="sunken", text= 'Unblocked')
            PostIt.attributes('-topmost',False)   
            
    PostIt.attributes('-topmost',True)
    
    block = tk.Button(PostIt,
            text="Blocked", 
            font = "Helvetica 10", 
            borderwidth=0, 
            bg=color, 
            command=toggle)
    
    block.place(x=0,y=0)
    
    # mainloop
    PostIt.mainloop()
    
    
def run():  
    
    wd = tk.Tk()
    wd.resizable(0,0)
    wd.geometry("200x180")
    wd.attributes('-topmost',True)

    #FRAME PARA CREACION DE NUEVO POST IT
    create_frame = tk.Frame()
    create_frame.config(width=400, height=400, bg="cyan")
    create_frame.pack()
        
        
    logo = tk.Label(create_frame,
            text = 'POST IT!',
            font=('arial',15),
            bg="white")
    logo.grid(row=0,column=0,columnspan=2, sticky='ew')
    
    
    color_lbl = tk.Label(create_frame,
            text = 'Color:',
            font=('arial',10),
            bg="white")
    color_lbl.grid(row=1,column=0,sticky='we')    
  
  
    def change_color():
        global color
        colors = askcolor(title="Post It Color Chooser")
        color_btn.configure(bg=colors[1],text='')
        color=colors[1]
        
    color_btn=tk.Button(create_frame,
            text='Select',
            borderwidth=0,
            command=change_color)
    color_btn.grid(row=2, column=0,sticky='we')
    
    
    def random_color():
        global color
        r_color = ["#"+''.join([rd.choice('0123456789ABCDEF') for i in range(6)])]
        color_btn.configure(bg=r_color,text='')
        color = r_color        
    
    rd_color=tk.Button(create_frame,
            text='Random',
            borderwidth=0,
            command=random_color)
    rd_color.grid(row=2, column=1,sticky='we')
    
    
    
    txt = tk.StringVar()

    txt_lbl = tk.Label(create_frame,
            text = 'Texto:',
            font=('arial',10),
            bg="white",
            )
    txt_lbl.grid(row=3,column=0,sticky='we')   
    
    
    txt_ent = tk.Entry(create_frame,
            textvariable=txt)
    txt_ent.grid(row=4,column=0,columnspan=2)     
    
    def NewPI():
        global color
        New_PostIt(color,[txt.get(), "cmmi10", 30])

    create = tk.Button(create_frame, 
            text = "Crear", 
            font=("Arial", 14), 
            bg="white",
            command=NewPI)     
    create.grid(row=5,column=0,columnspan=2,sticky='we')
        
    wd.mainloop()
    
    
run()   
    
  
#New_PostIt("red",["nuevo post it", "arial", 12])
