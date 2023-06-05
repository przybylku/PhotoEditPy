import datetime
import glob
import os.path
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

class PhotoUI(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)
        for index in [0,1,2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)
        self.option_menu_list = ["", "OptionMenu", "Option 1", "Option 2"]

        self.setup_widgets()
        self.img = ''
        self.photoName = ''
        self.imphoto = None



    def setup_widgets(self):
        self.check_frame = ttk.LabelFrame(self, text="Checkbuttons", padding=(20,10))
        self.check_frame.grid(row=0, column=0,padx=(20, 10), pady=(20, 10), sticky="nsew")
        self.check_1 = ttk.Checkbutton(
            self.check_frame, text="checked", variable=tk.BooleanVar(value=True)
        )
        self.check_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

        self.imgFrame = ttk.Frame(padding=(20, 20))
        self.imgFrame.grid(row=1, column=0, sticky="nsew")
        self.upload_btn = ttk.Button(self.imgFrame, text="Upload File", width=20, command=lambda: self.upload_file())
        self.upload_btn.grid(row=1, column=1)
        self.resize_frame = ttk.LabelFrame(text="resize photo", padding=(10,10))
        self.resize_frame.grid(row=0, column=1)
        self.resize_input_1 = ttk.Entry(self.resize_frame)
        self.resize_input_2 = ttk.Entry(self.resize_frame)
        self.resize_input_1.grid(row=0, column=0)
        self.resize_input_2.grid(row=0, column=1)
        self.resize_btn = ttk.Button(self.resize_frame, text="Resize!", command=lambda: self.resize_img((int(self.resize_input_1.get()), int(self.resize_input_2.get()))))
        self.resize_btn.grid(row=1, column=0)
    def upload_file(self):
        global img, imphoto, photoName
        self.f_types = [("png files", "*.png"), ("jpg files", "*.jpg")]
        filename = filedialog.askopenfilename(filetypes=self.f_types)
        print(filename)
        self.imphoto = Image.open(filename).resize((100, 200))
        self.photoName, ext = os.path.splitext(filename)
        img = ImageTk.PhotoImage(self.imphoto)
        b2 = ttk.Button(self, image=img)
        b2.grid(row=2, column=0)
    def resize_img(self, size):
        if self.imphoto is not None:
            self.imphoto.resize(size)
            file = filedialog.asksaveasfilename(filetypes=self.f_types, defaultextension=self.f_types)
            print(file)
            self.imphoto.save(f"{file}", "PNG")
            self.resize_btn.config(text="Resized!")
class PhotoPy():
    def opening(self, src, fo="png"):
        for ifile in glob.glob(f"{src}"):
            file, ext = os.path.splitext(ifile)
            im = Image.open(ifile)
            return im

    def thumbnail(self, src, sizing):
        im = self.opening(src, 'png')
        im.thumbnail(sizing)
        date = datetime.datetime.now()
        im.save(f"{date.strftime('%M%S %a %b %Y')} miniaturka.png", "PNG")

if __name__ ==  "__main__":
    root = tk.Tk()
    root.title("Edit your photo!")
    p = PhotoPy()
    # root.tk.call("source", )
    app = PhotoUI(root)
    app.grid(row=0, column=0)
    style = ttk.Style(root)
    root.tk.call("source", "forest-dark.tcl")
    style.theme_use("forest-dark")
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cord = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cord = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cord, y_cord))


    # sizing = 64, 64
    # p.thumbnail("uncle", sizing)
    root.mainloop()