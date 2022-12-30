from Scrapper_mind import Scrapper
import tkinter
import customtkinter
import threading


customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x380")
app.title("Fórum scraper")


def button_callback():
    scrapper = Scrapper(link.get())

    try:

        if 'prohardver' in link.get():
            scrapper.get_prohardver_data(filename.get())
            tkinter.messagebox.showinfo(title='Üzenet', message='Sikeres letöltés!')

        elif 'mobilarena' in link.get():
            scrapper.get_prohardver_data(filename.get())
            tkinter.messagebox.showinfo(title='Üzenet', message='Sikeres letöltés!')

        elif 'itcafe' in link.get():
            scrapper.get_prohardver_data(filename.get())
            tkinter.messagebox.showinfo(title='Üzenet', message='Sikeres letöltés!')

        elif 'gamepod' in link.get():
            scrapper.get_prohardver_data(filename.get())
            tkinter.messagebox.showinfo(title='Üzenet', message='Sikeres letöltés!')

        elif 'portfolio' in link.get():
            scrapper.get_portfolio_data(filename.get())
            tkinter.messagebox.showinfo(title='Üzenet', message='Sikeres letöltés!')

        elif 'forum.index' in link.get():
            scrapper.get_index_data(filename.get())
            tkinter.messagebox.showinfo(title='Üzenet', message='Sikeres letöltés!')

        else:
            tkinter.messagebox.showinfo(title='Üzenet', message='Ismeretlen fórum')

    except Exception as e:

        tkinter.messagebox.showinfo(title='Üzenet', message=e)


def mid():
    th = threading.Thread(target=button_callback)
    th.start()


link = customtkinter.StringVar(app)
filename = customtkinter.StringVar(app)




frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)


label_1 = customtkinter.CTkLabel(master=frame_1, text='Magyar fórum web scraping program', justify=tkinter.LEFT)
label_1.pack(pady=10, padx=10)

entry_1 = customtkinter.CTkEntry(master=frame_1, textvariable = link)
entry_1.pack(pady=10, padx=10)
entry_1.insert(0, "link")


entry_2 = customtkinter.CTkEntry(master=frame_1, textvariable = filename)
entry_2.pack(pady=10, padx=10)
entry_2.insert(0, "filename")

button_1 = customtkinter.CTkButton(master=frame_1, text='Indítás', command=mid)
button_1.pack(pady=10, padx=10)



radiobutton_var = tkinter.IntVar(value=1)



app.mainloop()