import random as rd
import tkinter as tk
from tkinter import font as tkfont
from tkinter.colorchooser import askcolor
from PIL import Image, ImageTk

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry('200x250')
        self.resizable(0,0)
        self.title_font = tkfont.Font(family='Helvetica', size=25, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Create, Folders, Settings):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        
    def traduce(self, text):
        return text
        
        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="POST IT!", bg = 'black',fg ='white',font=controller.title_font)
        label.grid(column=0, row=0, columnspan=2, sticky=tk.EW, ipady=15)
        
        images_folder ='D:\Documentos\PYTHON\proyectos\PostIt'       
        
        img_newPI_folder = Image.open(fr'{images_folder}\button_newPI.png')
        img_newPI_resize= img_newPI_folder.resize((80,80), Image.ANTIALIAS)
        img_newPI= ImageTk.PhotoImage(img_newPI_resize)
        
        img_folders_folder = Image.open(fr'{images_folder}\img_folders.png')
        img_folders_resize= img_folders_folder.resize((60,60), Image.ANTIALIAS)
        img_folders= ImageTk.PhotoImage(img_folders_resize)
        
        img_settings_folder = Image.open(fr'{images_folder}\img_settings.jpg')
        img_settings_resize= img_settings_folder.resize((80,80), Image.ANTIALIAS)
        img_settings= ImageTk.PhotoImage(img_settings_resize)
        
        
        button_newPI = tk.Button(self,image= img_newPI,
                            command=lambda: controller.show_frame("Create"))
        button_newPI.grid(column=0, row=1, columnspan=2, sticky=tk.EW)
        
        button_newPI.image = img_newPI
        
        button_folders = tk.Button(self, image = img_folders,
                            command=lambda: controller.show_frame("Folders"))
        button_folders.grid(column=0, row=2, ipady=30, ipadx=20)
        
        button_folders.image = img_folders
        
        button_settings = tk.Button(self,image = img_settings,
                            command=lambda: controller.show_frame("Settings"))
        button_settings.grid(column=1, row=2, ipady=30, ipadx=20)
        
        button_settings.image = img_settings
        
        widgets = [button_newPI,button_folders,button_settings]
        
        for widget in widgets:
            widget.configure(bg='black',borderwidth=0,activebackground='black')
        
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=2)
        self.rowconfigure(2,weight=2)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)


class Create(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        def change_color():
            global color
            colors = askcolor(title="Post It Color Chooser")
            create.configure(bg=colors[1])
            color=colors[1]    
    
        def random_color():
            global color
            r_color = ["#"+''.join([rd.choice('0123456789ABCDEF') for i in range(6)])]
            color = r_color   
            for widget in widgets: widget.configure(fg = color)
            
        def NewPI():
            global color
            PostIt(color, [txt_txt.get("1.0", "end-1c"), Font.get(), size.get()],width.get(), height.get())
            
        
        
        
        menuFont = tkfont.Font(family="Poplar Std", size = 10)        
        
        button = tk.Button(self, text="←",font=('arial',10),borderwidth=0,
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=0,sticky='w')
        
        color_lbl = tk.Label(self,text = 'Color:', font=menuFont)
        color_lbl.grid(row=1,sticky='w')    
            
        color_btn=tk.Button(self,text='Choose one',font = "Arial 12",borderwidth=0,command=change_color)
        color_btn.grid(row=2,sticky='we')
        
        rd_color=tk.Button(self,text='Random',font = "Arial 12", fg = 'black',borderwidth=0,command=random_color)
        rd_color.grid(row=3,sticky='we')
        
        txt_lbl = tk.Label(self,text = 'Text:',font=menuFont)
        txt_lbl.grid(row=4,sticky='w')   
        
        #txt = tk.StringVar()
        #txt_ent = tk.Entry(self,font=("Arial", 14),textvariable=txt)
        #txt_ent.grid(row=5,column=0,ipady=30,columnspan=2,sticky='we')     
        
        txt_txt = tk.Text(self,font="Arial 14 bold",width=1,height=1)
        txt_txt.grid(row=5,ipady=15,sticky='we')
        
        create = tk.Button(self, text = "Create",font=("Arial", 14),borderwidth=0,command=NewPI)     
        create.grid(row=6,sticky='we')   
        
        widgets = [button, color_lbl,color_btn,rd_color,txt_lbl,txt_txt,create]
        random_color()     
        
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        for i in range(2,7): self.rowconfigure(i,weight=2)
        

class PostIt():
    
    def __init__(self, color,txt_style,width = 250, height = 250, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        width = int(width)
        height = int(height)
        
        def round_rectangle( x2, y2, Xcolor = color, radius=40, x1=0, y1=0, **kwargs): # Creating a rounded rectangle
        
            points = [x1+radius, y1, x1+radius, y1, x2-radius, y1, x2-radius, y1, x2, y1,
                    x2, y1+radius, x2, y1+radius, x2, y2-radius, x2, y2-radius, x2, y2,
                    x2-radius, y2, x2-radius, y2, x1+radius, y2, x1+radius, y2, x1, y2,
                    x1, y2-radius, x1, y2-radius, x1, y1+radius, x1, y1+radius, x1, y1]

            return PostIt.create_polygon(points, **kwargs, smooth=True, fill=Xcolor)
        
        def create_circle(x, y, r,Xcolor = color, **kwargs):
            return PostIt.create_oval(x-r, y-r, x+r, y+r, **kwargs, fill=Xcolor)
        
        # Setting window
        PostItRoot = tk.Tk()
        PostItRoot.resizable(1,1)
        PostItRoot.overrideredirect(1)
        PostItRoot.geometry(f"{width}x{height}")
        PostItRoot.attributes('-topmost',True)  
        PostItRoot.eval('tk::PlaceWindow . center')
        PostItRoot.attributes("-transparentcolor", "grey")
        
        PostIt = tk.Canvas(PostItRoot, bg="grey", highlightthickness=0)
        PostIt.pack(fill= "both", expand=1)
        rectangle = round_rectangle( width, height) 
        
        txt = tk.Label(PostIt, 
            text = txt_style[0],
            font=(txt_style[1], txt_style[2]), 
            bg = color, fg = "black",
            wraplengt=width-10)
        txt.pack(side="left" , expand=1, pady=10)
        
        # DRAG WINDOW 
        
        def first_click(event):
            global first_click_x, first_click_y
            first_click_x = event.x
            first_click_y = event.y

        def do_move(event):
            x = event.x - first_click_x + PostItRoot.winfo_x()
            y = event.y - first_click_y + PostItRoot.winfo_y()
            PostItRoot.geometry(f"+{x}+{y}")
        
        PostItRoot.bind("<ButtonPress-1>", first_click)
        PostItRoot.bind("<B1-Motion>", do_move)
        
        # CLOSE BUTTON
        close = tk.Button(PostIt, 
                text = 'x', 
                font = "Helvetica 10", 
                borderwidth=0, 
                bg=color, 
                command=PostItRoot.destroy)
        close.place(x= width - 30,y=10)
        
        # MINIIZE BUTTON
        
      
        self.is_open = True
        def toggle(event):
            
            x_pos_close = PostIt.winfo_pointerx()-10
            y_pos_close = PostIt.winfo_pointery()-10
            x_pos_open = PostIt.winfo_pointerx() - width//2
            y_pos_open = PostIt.winfo_pointery() - height//2
                        
            if(self.is_open): 
            
                #PostIt.pack_forget()
                #circle.pack(fill= "both", expand=1)
                PostIt.delete(rectangle)
                txt.configure(bg = 'grey', fg='grey')
                circle = create_circle(width//2, height//2, 10,'black')
                
                self.is_open = False              
            else: 
                PostIt.delete(circle)
                round_rectangle( width, height) 
                self.is_open = True
        
        txt.bind("<ButtonPress-3>", toggle)   
        PostIt.bind("<ButtonPress-3>", toggle) 
        # mainloop
        PostItRoot.mainloop  
        
class Folders(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        button = tk.Button(self, text="←",font=('arial',10),borderwidth=0,
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=0,column=0,sticky='w')
        
        label = tk.Label(self, text="In progress", font=controller.title_font)
        label.grid(row=1,column=0,sticky='ew')

class Settings(tk.Frame):
    

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        global height
        height = tk.IntVar()
        height.set("250")
        global width 
        width = tk.IntVar()
        width.set("250")
        global Font
        Font = tk.StringVar()
        Font.set("Arial")
        global size
        size = tk.IntVar()
        size.set("25")
                
        SettingsFont = tkfont.Font(family="Poplar Std", size = 10)  
        
        button = tk.Button(self, text="←",font=('arial',10),borderwidth=0,
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=0,column=0,sticky='w')
        
        SizeLabel = tk.Label(self,text = controller.traduce('PostIt Size:'),font=SettingsFont)
        SizeLabel.grid(row=1,column=0, columnspan = 3,sticky='w') 
        
        heightLabel = tk.Label(self,text = controller.traduce('Altura:'),font=SettingsFont)
        heightLabel.grid(row=2,column=0,sticky='w') 
        
        heightEntry = tk.Entry(self, textvariable=height, justify='left',
                font=SettingsFont, bg = 'white', fg = "black", borderwidth=0)
        heightEntry.grid(row=2,column=1,sticky='w') 
        
        widthLabel = tk.Label(self,text = controller.traduce('Ancho:'),font=SettingsFont)
        widthLabel.grid(row=2,column=2,sticky='w') 
    
        widthEntry = tk.Entry(self, textvariable=width, justify='left',
                font=SettingsFont, bg = 'white', fg = "black", borderwidth=0)
        widthEntry.grid(row=2,column=3,sticky='w') 
        
        # SETTING FONT MENU
        
        FontLabel = tk.Label(self,text = controller.traduce('PostIt Font:'),font=SettingsFont)
        FontLabel.grid(row=3,column=0, columnspan = 3,sticky='w') 
        
        FontLabel = tk.Label(self,text = controller.traduce('Fuente:'),font=SettingsFont)
        FontLabel.grid(row=4,column=0,sticky='w') 
        
        FontEntry = tk.OptionMenu(self, Font,*list(tkfont.families()))
        FontEntry.grid(row=4,column=1,sticky='w') 
        
        FontLabel = tk.Label(self,text = controller.traduce('Tamaño:'),font=SettingsFont)
        FontLabel.grid(row=4,column=2,sticky='w') 
    
        FontEntry = tk.Entry(self, textvariable=size, justify='left',
                font=SettingsFont, bg = 'white', fg = "black", borderwidth=0)
        FontEntry.grid(row=4,column=3,sticky='w') 
        
    
        


if __name__ == "__main__":
   
    app = SampleApp()
    app.mainloop()
