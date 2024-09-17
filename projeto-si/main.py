import tkinter as tk
from view.user_interface import UserInterface

# Constantes
AGENDAR_NOVA_CONSULTA = "1"
LISTAR_CONSULTAS_AGENDADAS = "2"
MOSTRAR_PERFIL = "2"
VOLTAR = "V"
CONTINUAR = "1"
ENTRAR = "Entrar"
CADASTRAR = "Cadastrar"

def main():
    # Inicializa a interface gráfica
    root = tk.Tk()
    ui = UserInterface(root)

    # Adiciona os botões ao menu principal
    ui.menu()

    # Inicia o loop principal do Tkinter
    root.mainloop()

if __name__ == "__main__":
    main()