import tkinter as tk
from tkinter import messagebox
from paciente.servico_autenticacao_paciente import ServicoAutenticacaoPaciente
from psicologo.servico_autenticacao_psicologo import ServicoAutenticacaoPsicologo
from paciente.repositorio_paciente import RepositorioPaciente
from psicologo.repositorio_psicologo import RepositorioPsicologo
from paciente.paciente import Paciente
from psicologo.psicologo import Psicologo
from paciente.servico_paciente import ServicoPaciente
from psicologo.servico_psicologo import ServicoPsicologo

class UserInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Pysicologia - Sistema de gestão de consultas")
        self.root.geometry("500x500")
        self.repositorio_paciente = RepositorioPaciente()
        self.repositorio_psicologo = RepositorioPsicologo()
        self.servico_autenticacao_paciente = ServicoAutenticacaoPaciente(self.repositorio_paciente)
        self.servico_autenticacao_psicologo = ServicoAutenticacaoPsicologo(self.repositorio_psicologo)
        self.servico_paciente = ServicoPaciente(self.repositorio_paciente)
        self.servico_psicologo = ServicoPsicologo(self.repositorio_psicologo)
        self.paciente_autenticado = None
        self.padding = 10
        self.menu()
    
    def menu(self):
        # Limpa a janela
        for widget in self.root.winfo_children():
            widget.destroy()

        # Cria o título
        title = tk.Label(self.root, text="Pysicologia", font=("Helvetica", 20))
        title.pack(pady=self.padding*2)

        subtitle = tk.Label(self.root, text="Sistema de gestão de consultas", font=("Helvetica", 14))
        subtitle.pack(pady=self.padding)

        # Cria os botões do menu
        self.entrar_btn = tk.Button(self.root, text="Fazer login", font=("Helvetica", 14), command=self.tela_login)
        self.entrar_btn.pack(pady=self.padding)

        self.criar_conta_btn = tk.Button(self.root, text="Criar conta", font=("Helvetica", 14), command=self.tela_selecao_conta)
        self.criar_conta_btn.pack(pady=self.padding)

        sair_button = tk.Button(self.root, text="Sair", font=("Helvetica", 14), command=self.root.quit)
        sair_button.pack(pady=self.padding)

    def tela_login(self):
        # Limpa a janela
        for widget in self.root.winfo_children():
            widget.destroy()

        # Cria o título
        title = tk.Label(self.root, text="Login", font=("Helvetica", 16))
        title.pack(pady=self.padding * 2)

        # Campos de entrada para nome de usuário e senha
        tk.Label(self.root, text="Email").pack(pady=self.padding)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=self.padding)

        tk.Label(self.root, text="Senha").pack(pady=self.padding)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=self.padding)

        # Botão de login
        login_button = tk.Button(self.root, text="Login", command=self.verificar_login)
        login_button.pack(pady=self.padding * 2)

        # Botão de voltar
        voltar_button = tk.Button(self.root, text="Voltar", command=self.menu)
        voltar_button.pack(pady=self.padding)

    def verificar_login(self):
        email = self.username_entry.get()
        senha = self.password_entry.get()
    
        # Verifica as credenciais usando o ServicoAutenticacaoPaciente e ServicoAutenticacaoPsicologo
        paciente = self.servico_autenticacao_paciente.autenticar(email, senha)
        psicologo = self.servico_autenticacao_psicologo.autenticar(email, senha)
        
        if paciente:
            messagebox.showinfo("Login", "Login realizado com sucesso como Paciente!")
            self.paciente_autenticado = paciente
            self.tela_paciente()  # Vai para a tela do paciente após login bem-sucedido
        elif psicologo:
            messagebox.showinfo("Login", "Login realizado com sucesso como Psicólogo!")
            self.tela_psicologo()  # Vai para a tela do psicólogo após login bem-sucedido
        else:
            messagebox.showerror("Login", "Email ou senha incorretos.")
    
    def tela_selecao_conta(self):
        # Limpa a janela
        for widget in self.root.winfo_children():
            widget.destroy()
    
        # Cria o título
        title = tk.Label(self.root, text="Selecione o Tipo de Conta", font=("Helvetica", 16))
        title.pack(pady=self.padding * 2)
    
        # Botões para selecionar o tipo de conta
        paciente_button = tk.Button(self.root, text="Paciente", font=("Helvetica", 14), command=self.tela_cadastro_paciente)
        paciente_button.pack(pady=self.padding)
    
        psicologo_button = tk.Button(self.root, text="Psicólogo", font=("Helvetica", 14), command=self.tela_cadastro_psicologo)
        psicologo_button.pack(pady=self.padding)
    
        # Botão de voltar
        voltar_button = tk.Button(self.root, text="Voltar", font=("Helvetica", 14), command=self.menu)
        voltar_button.pack(pady=self.padding)
    
    def tela_cadastro_paciente(self):
        # Limpa a janela
        for widget in self.root.winfo_children():
            widget.destroy()
    
        # Cria o título
        title = tk.Label(self.root, text="Cadastro de Paciente", font=("Helvetica", 16))
        title.pack(pady=self.padding * 2)
    
        # Campos de entrada para os dados do paciente
        tk.Label(self.root, text="Nome").pack(pady=self.padding/5)
        self.nome_entry = tk.Entry(self.root)
        self.nome_entry.pack(pady=self.padding)
    
        tk.Label(self.root, text="Email").pack(pady=self.padding/5)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack(pady=self.padding)
    
        tk.Label(self.root, text="Senha").pack(pady=self.padding/5)
        self.senha_entry = tk.Entry(self.root, show="*")
        self.senha_entry.pack(pady=self.padding)
    
        tk.Label(self.root, text="Telefone").pack(pady=self.padding/5)
        self.telefone_entry = tk.Entry(self.root)
        self.telefone_entry.pack(pady=self.padding)
    
        tk.Label(self.root, text="CPF").pack(pady=self.padding/5)
        self.cpf_entry = tk.Entry(self.root)
        self.cpf_entry.pack(pady=self.padding)
    
        # Botão de cadastro
        cadastrar_button = tk.Button(self.root, text="Cadastrar", command=self.cadastrar_paciente)
        cadastrar_button.pack(pady=self.padding)
    
        # Botão de voltar
        voltar_button = tk.Button(self.root, text="Voltar", command=self.tela_selecao_conta)
        voltar_button.pack(pady=self.padding)
    
    def cadastrar_paciente(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        telefone = self.telefone_entry.get()
        cpf = self.cpf_entry.get()
    
            # Validação dos campos
        if not nome or not email or not senha or not telefone or not cpf:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
            return
        
        # Código para cadastrar o paciente
        try:
            self.servico_paciente.salvar(Paciente(nome, email, senha, telefone, cpf))
            messagebox.showinfo("Sucesso", "Paciente cadastrado com sucesso!")
            self.menu()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def tela_cadastro_psicologo(self):
        # Limpa a janela
        for widget in self.root.winfo_children():
            widget.destroy()

        # Cria o título
        title = tk.Label(self.root, text="Cadastro de Psicólogo", font=("Helvetica", 16))
        title.pack(pady=self.padding)

        # Campos de entrada para os dados do psicólogo
        tk.Label(self.root, text="Nome").pack(pady=self.padding/5)
        self.nome_entry = tk.Entry(self.root)
        self.nome_entry.pack(pady=self.padding/2)

        tk.Label(self.root, text="Email").pack(pady=self.padding/5)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack(pady=self.padding/2)

        tk.Label(self.root, text="Senha").pack(pady=self.padding/5)
        self.senha_entry = tk.Entry(self.root, show="*")
        self.senha_entry.pack(pady=self.padding/2)

        tk.Label(self.root, text="Telefone").pack(pady=self.padding/5)
        self.telefone_entry = tk.Entry(self.root)
        self.telefone_entry.pack(pady=self.padding/2)

        tk.Label(self.root, text="CPF").pack(pady=self.padding/5)
        self.cpf_entry = tk.Entry(self.root)
        self.cpf_entry.pack(pady=self.padding/2)

        tk.Label(self.root, text="CRP").pack(pady=self.padding/5)
        self.crp_entry = tk.Entry(self.root)
        self.crp_entry.pack(pady=self.padding/2)

        # Botão de cadastro
        cadastrar_button = tk.Button(self.root, text="Cadastrar", command=self.cadastrar_psicologo)
        cadastrar_button.pack(pady=self.padding/2)

        # Botão de voltar
        voltar_button = tk.Button(self.root, text="Voltar", command=self.menu)
        voltar_button.pack(pady=self.padding)

    def cadastrar_psicologo(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        telefone = self.telefone_entry.get()
        cpf = self.cpf_entry.get()
        crp = self.crp_entry.get()

        # Validação dos campos
        if not nome or not email or not senha or not telefone or not cpf or not crp:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
            return

        # Salvando o psicólogo no banco de dados
        if self.servico_psicologo.salvar(Psicologo(nome=nome, email=email, senha=senha, telefone=telefone, cpf=cpf, crp=crp)):
            messagebox.showinfo("Sucesso", "Psicólogo cadastrado com sucesso!")
            self.menu()
        else:
            messagebox.showerror("Erro", "Erro ao salvar psicólogo.")

    def tela_paciente(self):
    # Limpa a janela
        for widget in self.root.winfo_children():
            widget.destroy()

        # Cria o título
        title = tk.Label(self.root, text="Bem-vindo, Paciente", font=("Helvetica", 16))
        title.pack(pady=10)

        # Botão para acessar a tela de perfil
        perfil_button = tk.Button(self.root, text="Tela de Perfil", command=self.tela_perfil_paciente)
        perfil_button.pack(pady=5)

        # Botão para agendar consulta
        agendar_button = tk.Button(self.root, text="Agendar Consulta", command=self.agendar_consulta)
        agendar_button.pack(pady=5)

        # Botão de logout
        logout_button = tk.Button(self.root, text="Logout", command=self.menu)
        logout_button.pack(pady=5)

    def tela_perfil_paciente(self):
        # Limpa a janela
        for widget in self.root.winfo_children():
            widget.destroy()

        # Cria o título
        title = tk.Label(self.root, text="Perfil do Paciente", font=("Helvetica", 16))
        title.pack(pady=10)

        # Exibe os dados do paciente
        paciente = self.paciente_autenticado
        if paciente:
            tk.Label(self.root, text=f"Nome: {paciente.nome}").pack(pady=5)
            tk.Label(self.root, text=f"Email: {paciente.email}").pack(pady=5)
            tk.Label(self.root, text=f"Telefone: {paciente.telefone}").pack(pady=5)
            tk.Label(self.root, text=f"CPF: {paciente.cpf}").pack(pady=5)
        else:
            tk.Label(self.root, text="Nenhum paciente autenticado.").pack(pady=5)

        # Botão de voltar
        voltar_button = tk.Button(self.root, text="Voltar", command=self.tela_paciente)
        voltar_button.pack(pady=10)

    def tela_psicologo(self):
        # Limpa a janela
        for widget in self.root.winfo_children():
            widget.destroy()

        # Cria o título
        title = tk.Label(self.root, text="Bem-vindo, Psicólogo", font=("Helvetica", 16))
        title.pack(pady=10)

        # Adicione mais widgets específicos para psicólogos aqui
        # Exemplo: botão para ver consultas agendadas
        ver_consultas_button = tk.Button(self.root, text="Ver Consultas Agendadas", command=self.ver_consultas)
        ver_consultas_button.pack(pady=5)

        # Botão de logout
        logout_button = tk.Button(self.root, text="Logout", command=self.menu)
        logout_button.pack(pady=5)

    def agendar_consulta(self):
        messagebox.showinfo("Agendar Consulta", "Função de agendamento ainda não implementada.")

    def ver_consultas(self):
        messagebox.showinfo("Ver Consultas", "Função de visualização de consultas ainda não implementada.")

if __name__ == "__main__":
    root = tk.Tk()
    app = UserInterface(root)
    root.mainloop()