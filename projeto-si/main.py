import tkinter as tk
from view.user_interface import UserInterface

def main():
    # Inicializa a interface gráfica
    root = tk.Tk()
    ui = UserInterface(root)

    # Adiciona os botões ao menu principal
    ui.tela_menu()

    # Inicia o loop principal do Tkinter
    root.mainloop()

if __name__ == "__main__":
    main()