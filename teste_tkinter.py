import tkinter as tk

janela = tk.Tk()
janela.title("Teste Tkinter")
janela.geometry("300x200")

label = tk.Label(janela, text="Janela funcionando!", font=("Arial", 14))
label.pack(pady=50)

janela.mainloop()