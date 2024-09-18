from datetime import datetime, timedelta
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
from consulta.consulta import Consulta
from paciente.servico_autenticacao_paciente import ServicoAutenticacaoPaciente
from psicologo.servico_autenticacao_psicologo import ServicoAutenticacaoPsicologo
from paciente.repositorio_paciente import RepositorioPaciente
from psicologo.repositorio_psicologo import RepositorioPsicologo
from paciente.paciente import Paciente
from psicologo.psicologo import Psicologo
from paciente.servico_paciente import ServicoPaciente
from psicologo.servico_psicologo import ServicoPsicologo
from consulta.repositorio_consulta import RepositorioConsulta
from consulta.servico_consulta import ServicoConsulta
from validate_docbr import CPF

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
        self.repositorio_consulta = RepositorioConsulta()
        self.servico_consulta = ServicoConsulta(self.repositorio_psicologo, self.repositorio_paciente, self.repositorio_consulta)
        self.paciente_autenticado = None
        self.psicologo_autenticado = None
        self.cpf_validator = CPF()
        self.tela_menu()
    
    # MENU PRINCIPAL
    def tela_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        titulo = tk.Label(self.root, text="Pysicologia", font=("Helvetica", 20))
        titulo.pack(pady=10)
        subtitle = tk.Label(self.root, text="Sistema de gestão de consultas", font=("Helvetica", 14))
        subtitle.pack(pady=20)

        self.entrar_btn = tk.Button(self.root, text="Fazer login", font=("Helvetica", 14), command=self.tela_login)
        self.entrar_btn.pack(pady=20)

        self.criar_conta_btn = tk.Button(self.root, text="Criar conta", font=("Helvetica", 14), command=self.tela_selecao_conta)
        self.criar_conta_btn.pack(pady=20)

        sair_button = tk.Button(self.root, text="Sair", font=("Helvetica", 14), command=self.root.quit)
        sair_button.pack(pady=20)

    # TELAS DE LOGIN
    def tela_login(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        title = tk.Label(self.root, text="Login", font=("Helvetica", 16))
        title.pack(pady=20)

        tk.Label(self.root, text="Email").pack(pady=2)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=10)

        tk.Label(self.root, text="Senha").pack(pady=2)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=10)

        # Botão de login
        login_button = tk.Button(self.root, text="Login", command=self.verificar_login)
        login_button.pack(pady=20)

        # Botão de voltar
        voltar_button = tk.Button(self.root, text="Voltar", command=self.tela_menu)
        voltar_button.pack(pady=10)

    def verificar_login(self):
        email = self.username_entry.get()
        senha = self.password_entry.get()

        paciente = self.servico_autenticacao_paciente.autenticar(email, senha)
        psicologo = self.servico_autenticacao_psicologo.autenticar(email, senha)

        if paciente:
            messagebox.showinfo("Login", "Login realizado com sucesso como Paciente!")
            self.paciente_autenticado = paciente
            self.tela_paciente()  # Vai para a tela do paciente após login bem-sucedido
        elif psicologo:
            messagebox.showinfo("Login", "Login realizado com sucesso como Psicólogo!")
            self.psicologo_autenticado = psicologo  # Adiciona o psicólogo autenticado
            self.tela_psicologo()  # Vai para a tela do psicólogo após login bem-sucedido
        else:
            messagebox.showerror("Login", "Email ou senha incorretos.")
    
    # TELAS DE CADASTRO
    def tela_selecao_conta(self):
        # Limpa a janela
        for widget in self.root.winfo_children():
            widget.destroy()
    
        # Cria o título
        title = tk.Label(self.root, text="Selecione o Tipo de Conta", font=("Helvetica", 16))
        title.pack(pady=20)
    
        # Botões para selecionar o tipo de conta
        paciente_button = tk.Button(self.root, text="Paciente", font=("Helvetica", 14), command=self.tela_cadastro_paciente)
        paciente_button.pack(pady=10)
    
        psicologo_button = tk.Button(self.root, text="Psicólogo", font=("Helvetica", 14), command=self.tela_cadastro_psicologo)
        psicologo_button.pack(pady=10)
    
        # Botão de voltar
        voltar_button = tk.Button(self.root, text="Voltar", font=("Helvetica", 14), command=self.tela_menu)
        voltar_button.pack(pady=10)
    
    def tela_cadastro_paciente(self):
        # Limpa a janela
        for widget in self.root.winfo_children():
            widget.destroy()
    
        # Cria o título
        title = tk.Label(self.root, text="Cadastro de Paciente", font=("Helvetica", 16))
        title.pack(pady=20)
    
        # Campos de entrada para os dados do paciente
        tk.Label(self.root, text="Nome").pack(pady=2)
        self.nome_entry = tk.Entry(self.root)
        self.nome_entry.pack(pady=5)
    
        tk.Label(self.root, text="Email").pack(pady=2)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack(pady=5)
    
        tk.Label(self.root, text="Senha").pack(pady=2)
        self.senha_entry = tk.Entry(self.root, show="*")
        self.senha_entry.pack(pady=5)
    
        tk.Label(self.root, text="Telefone").pack(pady=2)
        self.telefone_entry = tk.Entry(self.root)
        self.telefone_entry.pack(pady=5)
    
        tk.Label(self.root, text="CPF").pack(pady=2)
        self.cpf_entry = tk.Entry(self.root)
        self.cpf_entry.pack(pady=5)
    
        # Botão de cadastro
        cadastrar_button = tk.Button(self.root, text="Cadastrar", command=self.cadastrar_paciente)
        cadastrar_button.pack(pady=5)
    
        # Botão de voltar
        voltar_button = tk.Button(self.root, text="Voltar", command=self.tela_selecao_conta)
        voltar_button.pack(pady=5)
    
    def cadastrar_paciente(self):
        nome = self.nome_entry.get().strip()
        email = self.email_entry.get().strip()
        senha = self.senha_entry.get().strip()
        telefone = self.telefone_entry.get().strip()
        cpf = self.cpf_entry.get().strip()
    
        self.nome_entry.config(highlightbackground="gray", highlightcolor="gray", highlightthickness=0)
        self.email_entry.config(highlightbackground="gray", highlightcolor="gray", highlightthickness=0)
        self.senha_entry.config(highlightbackground="gray", highlightcolor="gray", highlightthickness=0)
        self.telefone_entry.config(highlightbackground="gray", highlightcolor="gray", highlightthickness=0)
        self.cpf_entry.config(highlightbackground="gray", highlightcolor="gray", highlightthickness=0)

        # Validação dos campos
        if not nome or len(nome) < 7:
            messagebox.showerror("Erro", "Nome inválido. O nome deve ter pelo menos 7 caracteres.")
            self.nome_entry.config(highlightbackground="red", highlightcolor="red", highlightthickness=2)
            return
        
        if not email or len(email) < 5 or "@" not in email:
            messagebox.showerror("Erro", "Email inválido.")
            self.email_entry.config(highlightbackground="red", highlightcolor="red", highlightthickness=2)
            return
        
        if not senha or len(senha) < 7:
            messagebox.showerror("Erro", "Senha inválida. A senha deve ter pelo menos 7 caracteres.")
            self.senha_entry.config(highlightbackground="red", highlightcolor="red", highlightthickness=2)
            return
        
        if not telefone or len(telefone) < 10 or not telefone.isdigit():
            messagebox.showerror("Erro", "Telefone inválido.")
            self.telefone_entry.config(highlightbackground="red", highlightcolor="red", highlightthickness=2)
            return
        
        if not self.cpf_validator.validate(cpf):
            messagebox.showerror("Erro", "CPF inválido.")
            self.cpf_entry.config(highlightbackground="red", highlightcolor="red", highlightthickness=2)
            return
        
        try:
            self.servico_paciente.salvar(Paciente(nome=nome, email=email, senha=senha, telefone=telefone, cpf=cpf))
            messagebox.showinfo("Sucesso", "Paciente cadastrado com sucesso!")
            self.tela_menu()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def tela_cadastro_psicologo(self):
        # Limpa a janela
        for widget in self.root.winfo_children():
            widget.destroy()

        # Cria o título
        title = tk.Label(self.root, text="Cadastro de Psicólogo", font=("Helvetica", 16))
        title.pack(pady=10)

        # Campos de entrada para os dados do psicólogo
        tk.Label(self.root, text="Nome").pack(pady=2)
        self.nome_entry = tk.Entry(self.root)
        self.nome_entry.pack(pady=5)

        tk.Label(self.root, text="Email").pack(pady=2)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack(pady=5)

        tk.Label(self.root, text="Senha").pack(pady=2)
        self.senha_entry = tk.Entry(self.root, show="*")
        self.senha_entry.pack(pady=5)

        tk.Label(self.root, text="Telefone").pack(pady=2)
        self.telefone_entry = tk.Entry(self.root)
        self.telefone_entry.pack(pady=5)

        tk.Label(self.root, text="CPF").pack(pady=2)
        self.cpf_entry = tk.Entry(self.root)
        self.cpf_entry.pack(pady=5)

        tk.Label(self.root, text="CRP").pack(pady=2)
        self.crp_entry = tk.Entry(self.root)
        self.crp_entry.pack(pady=5)

        tk.Label(self.root, text="Especialidade").pack(pady=2)
        self.especialidade_entry = tk.Entry(self.root)
        self.especialidade_entry.pack(pady=5)

        # Botão de cadastro
        cadastrar_button = tk.Button(self.root, text="Cadastrar", command=self.cadastrar_psicologo)
        cadastrar_button.pack(pady=5)

        # Botão de voltar
        voltar_button = tk.Button(self.root, text="Voltar", command=self.tela_menu)
        voltar_button.pack(pady=5)

    def cadastrar_psicologo(self):
        nome = self.nome_entry.get().strip()
        email = self.email_entry.get().strip()
        senha = self.senha_entry.get().strip()
        telefone = self.telefone_entry.get().strip()
        cpf = self.cpf_entry.get().strip()
        crp = self.crp_entry.get().strip()
        especialidade = self.especialidade_entry.get().strip()
    
        self.nome_entry.config(highlightbackground="gray", highlightcolor="gray", highlightthickness=0)
        self.email_entry.config(highlightbackground="gray", highlightcolor="gray", highlightthickness=0)
        self.senha_entry.config(highlightbackground="gray", highlightcolor="gray", highlightthickness=0)
        self.telefone_entry.config(highlightbackground="gray", highlightcolor="gray", highlightthickness=0)
        self.cpf_entry.config(highlightbackground="gray", highlightcolor="gray", highlightthickness=0)
        self.crp_entry.config(highlightbackground="gray", highlightcolor="gray", highlightthickness=0)
        self.especialidade_entry.config(highlightbackground="gray", highlightcolor="gray", highlightthickness=0)
    
        if not nome or len(nome) < 7:
            self.nome_entry.config(highlightbackground="red", highlightcolor="red", highlightthickness=1)
            messagebox.showerror("Erro", "Nome inválido. O nome deve ter pelo menos 7 caracteres.")
            return
    
        if not email or "@" not in email or len(email) < 5:
            self.email_entry.config(highlightbackground="red", highlightcolor="red", highlightthickness=1)
            messagebox.showerror("Erro", "Email inválido.")
            return
    
        if not senha or len(senha) < 7:
            self.senha_entry.config(highlightbackground="red", highlightcolor="red", highlightthickness=1)
            messagebox.showerror("Erro", "Senha inválida. A senha deve ter pelo menos 6 caracteres.")
            return
        
        if not telefone or not telefone.isdigit() or len(telefone) < 10:
            self.telefone_entry.config(highlightbackground="red", highlightcolor="red", highlightthickness=1)
            messagebox.showerror("Erro", "Telefone inválido.")
            return
    
        if not self.cpf_validator.validate(cpf):
            self.cpf_entry.config(highlightbackground="red", highlightcolor="red", highlightthickness=1)
            messagebox.showerror("Erro", "CPF inválido.")
            return
    
        if not crp or len(crp) < 7:
            self.crp_entry.config(highlightbackground="red", highlightcolor="red", highlightthickness=1)
            messagebox.showerror("Erro", "CRP inválido.")
            return
        
        if not especialidade:
            self.especialidade_entry.config(highlightbackground="red", highlightcolor="red", highlightthickness=1)
            messagebox.showerror("Erro", "Especialidade inválida.")
            return
    
        try:
            self.servico_psicologo.salvar(Psicologo(nome=nome, email=email, senha=senha, telefone=telefone, cpf=cpf, crp=crp, especialidade=especialidade))
            messagebox.showinfo("Sucesso", "Psicólogo cadastrado com sucesso!")
            self.tela_menu()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    # TELAS DE PERFIL PACIENTE
    def tela_paciente(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        title = tk.Label(self.root, text="Bem-vindo, Paciente", font=("Helvetica", 16))
        title.pack(pady=10)

        # Botão para acessar a tela de perfil
        perfil_button = tk.Button(self.root, text="Ver perfil", command=self.tela_perfil_paciente)
        perfil_button.pack(pady=5)

        # Botão para agendar consulta
        agendar_button = tk.Button(self.root, text="Agendar Consulta", command=self.tela_agendar_consulta)
        agendar_button.pack(pady=5)

        # Botão para detalhes das consultas
        detalhes_button = tk.Button(self.root, text="Detalhar Consultas", command=self.tela_detalhes_consultas_paciente)
        detalhes_button.pack(pady=5)

        # Exibe as próximas duas consultas
        proximas_consultas = self.servico_consulta.listar_proximas_consultas(self.paciente_autenticado.id)
        if proximas_consultas:
            consultas_frame = tk.Frame(self.root)
            consultas_frame.pack(pady=10)
            tk.Label(consultas_frame, text="Próximas Consultas:", font=("Helvetica", 14)).pack(pady=5)
            for consulta in proximas_consultas:
                nome_psicologo = self.repositorio_psicologo.buscar_por_id(consulta.id_psicologo).nome
                data_formatada = consulta.data.strftime("%d/%m/%Y")
                horario_formatado = (datetime.min + consulta.horario).time().strftime("%H:%M")

                consulta_text = f"Data: {data_formatada}, Hora: {horario_formatado}, Psicólogo: {nome_psicologo}"
                tk.Label(consultas_frame, text=consulta_text).pack(pady=2)
        else:
            tk.Label(self.root, text="Você não tem consultas agendadas.", font=("Helvetica", 12)).pack(pady=10)

        # Botão de logout
        logout_button = tk.Button(self.root, text="Logout", command=self.logout)
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

            # Botão de editar
            editar_button = tk.Button(self.root, text="Editar", command=self.tela_editar_paciente)
            editar_button.pack(pady=10)
        else:
            tk.Label(self.root, text="Nenhum paciente autenticado.").pack(pady=5)

        # Botão de voltar
        voltar_button = tk.Button(self.root, text="Voltar", command=self.tela_paciente)
        voltar_button.pack(pady=10)

    def tela_editar_paciente(self):
        # Limpa a janela
        for widget in self.root.winfo_children():
            widget.destroy()
    
        # Cria o título
        title = tk.Label(self.root, text="Editar Perfil do Paciente", font=("Helvetica", 16))
        title.pack(pady=10)
    
        # Campos de entrada para os dados do paciente
        tk.Label(self.root, text="Nome").pack(pady=5)
        self.nome_entry = tk.Entry(self.root)
        self.nome_entry.pack(pady=5)
        self.nome_entry.insert(0, self.paciente_autenticado.nome)
    
        tk.Label(self.root, text="Telefone").pack(pady=5)
        self.telefone_entry = tk.Entry(self.root)
        self.telefone_entry.pack(pady=5)
        self.telefone_entry.insert(0, self.paciente_autenticado.telefone)
    
        # Botão de salvar
        salvar_button = tk.Button(self.root, text="Salvar", command=self.salvar_edicao_paciente)
        salvar_button.pack(pady=5)
    
        # Botão de excluir
        excluir_button = tk.Button(self.root, text="Excluir", command=self.excluir_paciente)
        excluir_button.pack(pady=5)
    
        # Botão de voltar
        voltar_button = tk.Button(self.root, text="Voltar", command=self.tela_perfil_paciente)
        voltar_button.pack(pady=5)
    
    def salvar_edicao_paciente(self):
        nome = self.nome_entry.get().strip()
        telefone = self.telefone_entry.get().strip()
    
        # Validação dos campos
        if not nome or not telefone:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
            return
    
        # Atualiza os dados do paciente autenticado
        self.paciente_autenticado.nome = nome
        self.paciente_autenticado.telefone = telefone
    
        # Atualiza no repositório
        paciente_atualizado = self.repositorio_paciente.atualizar(self.paciente_autenticado, self.paciente_autenticado.id)
        if paciente_atualizado:
            messagebox.showinfo("Sucesso", "Dados atualizados com sucesso!")
            self.paciente_autenticado = paciente_atualizado
            self.tela_perfil_paciente()
        else:
            messagebox.showerror("Erro", "Erro ao atualizar os dados do paciente.")
    
    def excluir_paciente(self):
        resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir seu perfil?")
        if resposta:
            if self.repositorio_paciente.excluir(self.paciente_autenticado.id):
                messagebox.showinfo("Sucesso", "Conta encerrada")
                self.paciente_autenticado = None
                self.tela_menu()
            else:
                messagebox.showerror("Erro", "Erro ao excluir sua conta.")

    # TELAS DE PERFIL PSICÓLOGO
    def tela_psicologo(self):
        # Limpa a janela
        for widget in self.root.winfo_children():
            widget.destroy()
    
        # Cria o título
        title = tk.Label(self.root, text="Bem-vindo, Psicólogo", font=("Helvetica", 16))
        title.pack(pady=10)
    
        # Botão para ver perfil
        ver_perfil_button = tk.Button(self.root, text="Ver Perfil", command=self.tela_perfil_psicologo)
        ver_perfil_button.pack(pady=5)

        # Botão para detalhes das consultas
        detalhes_button = tk.Button(self.root, text="Detalhes Consultas", command=self.tela_detalhes_consultas_psicologo)
        detalhes_button.pack(pady=5)

        # Exibe as próximas duas consultas
        proximas_consultas = self.servico_consulta.listar_proximas_consultas_psicologo(self.psicologo_autenticado.id)
        if proximas_consultas:
            consultas_frame = tk.Frame(self.root)
            consultas_frame.pack(pady=10)
            tk.Label(consultas_frame, text="Próximas Consultas:", font=("Helvetica", 14)).pack(pady=5)
            for consulta in proximas_consultas:
                nome_paciente = self.repositorio_paciente.buscar_por_id(consulta.id_paciente).nome
                data_formatada = consulta.data.strftime("%d/%m/%Y")
                horario_formatado = (datetime.min + consulta.horario).time().strftime("%H:%M") if isinstance(consulta.horario, timedelta) else consulta.horario.strftime("%H:%M")
                consulta_text = f"Data: {data_formatada}, Hora: {horario_formatado}, Paciente: {nome_paciente}"
                tk.Label(consultas_frame, text=consulta_text).pack(pady=2)
        else:
            tk.Label(self.root, text="Você não tem consultas agendadas.", font=("Helvetica", 12)).pack(pady=10)

        # Botão de logout
        logout_button = tk.Button(self.root, text="Logout", command=self.logout)
        logout_button.pack(pady=5)

    def tela_perfil_psicologo(self):
        # Limpa a janela
        for widget in self.root.winfo_children():
            widget.destroy()

        # Cria o título
        title = tk.Label(self.root, text="Perfil do Psicólogo", font=("Helvetica", 16))
        title.pack(pady=10)

        psicologo = self.psicologo_autenticado
        if psicologo:
            tk.Label(self.root, text=f"Nome: {psicologo.nome}").pack(pady=5)
            tk.Label(self.root, text=f"Email: {psicologo.email}").pack(pady=5)
            tk.Label(self.root, text=f"Telefone: {psicologo.telefone}").pack(pady=5)
            tk.Label(self.root, text=f"CPF: {psicologo.cpf}").pack(pady=5)
            tk.Label(self.root, text=f"CRP: {psicologo.crp}").pack(pady=5)
            tk.Label(self.root, text=f"Especialidade: {psicologo.especialidade}").pack(pady=5)
                
            # Botão de editar
            editar_button = tk.Button(self.root, text="Editar", command=self.tela_editar_psicologo)
            editar_button.pack(pady=5)
        else:
            tk.Label(self.root, text="Nenhum psicólogo autenticado.").pack(pady=5)
        # Botão de voltar
        voltar_button = tk.Button(self.root, text="Voltar", command=self.tela_psicologo)
        voltar_button.pack(pady=5)

    def tela_editar_psicologo(self):
        # Limpa a janela
        for widget in self.root.winfo_children():
            widget.destroy()
    
        # Cria o título
        title = tk.Label(self.root, text="Editar Perfil do Psicólogo", font=("Helvetica", 16))
        title.pack(pady=10)
    
        # Campos de entrada para os dados do psicólogo
        tk.Label(self.root, text="Nome").pack(pady=5)
        self.nome_entry = tk.Entry(self.root)
        self.nome_entry.pack(pady=5)
        self.nome_entry.insert(0, self.psicologo_autenticado.nome)
    
        tk.Label(self.root, text="Telefone").pack(pady=5)
        self.telefone_entry = tk.Entry(self.root)
        self.telefone_entry.pack(pady=5)
        self.telefone_entry.insert(0, self.psicologo_autenticado.telefone)

        tk.Label(self.root, text="Especialidade").pack(pady=5)
        self.especialidade_entry = tk.Entry(self.root)
        self.especialidade_entry.pack(pady=5)
        self.especialidade_entry.insert(0, self.psicologo_autenticado.especialidade)
    
        # Botão de salvar
        salvar_button = tk.Button(self.root, text="Salvar", command=self.salvar_edicao_psicologo)
        salvar_button.pack(pady=10)
    
        # Botão de excluir
        excluir_button = tk.Button(self.root, text="Excluir", command=self.excluir_psicologo)
        excluir_button.pack(pady=10)
    
        # Botão de voltar
        voltar_button = tk.Button(self.root, text="Voltar", command=self.tela_perfil_psicologo)
        voltar_button.pack(pady=10)

    def salvar_edicao_psicologo(self):
        # Obtém os valores dos campos de entrada
        nome = self.nome_entry.get().strip()
        telefone = self.telefone_entry.get().strip()
        especialidade = self.especialidade_entry.get().strip()

        # Validação dos campos
        if not nome or not telefone or not especialidade:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
            return

        # Atualiza os dados do psicólogo autenticado
        self.psicologo_autenticado.nome = nome
        self.psicologo_autenticado.telefone = telefone
        self.psicologo_autenticado.especialidade = especialidade

        # Salva as alterações no repositório
        psicologo = self.repositorio_psicologo.atualizar(self.psicologo_autenticado, self.psicologo_autenticado.id)
        if psicologo:
            messagebox.showinfo("Sucesso", "Dados atualizados com sucesso!")
        else:
            messagebox.showerror("Erro", "Erro ao atualizar os dados.")

        # Volta para a tela de perfil do psicólogo
        self.tela_perfil_psicologo()

    def excluir_psicologo(self):
        resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir seu perfil?")
        if resposta:
            if self.repositorio_psicologo.excluir(self.psicologo_autenticado.id):
                messagebox.showinfo("Sucesso", "Conta Excluída!")
                self.logout()
            else:
                messagebox.showerror("Erro", "Erro ao encerrar conta.")
    
    # TELAS DE CONSULTA
    def tela_agendar_consulta(self):
        # Limpa a janela
        for widget in self.root.winfo_children():
            widget.destroy()

        # Cria o título
        title = tk.Label(self.root, text="Agendar Consulta", font=("Helvetica", 16))
        title.pack(pady=10)

        # Texto da pergunta
        tk.Label(self.root, text="Selecione sua principal necessidade").pack(pady=5)

        # Checkbox para as necessidades

        self.necessidades = {
            "Ansiedade": tk.BooleanVar(),
            "Depressão": tk.BooleanVar(),
            "Estresse": tk.BooleanVar(),
            "Relacionamento": tk.BooleanVar()
        }

        # Ao selecionar uma necessidade as outras são desmarcadas
        def marcar_necessidade(necessidade):
            for key in self.necessidades:
                if key != necessidade:
                    self.necessidades[key].set(False)
                    self.paciente_autenticado.necessidade = necessidade
        
        # Cria os checkboxes
        for key in self.necessidades:
            checkbox = tk.Checkbutton(self.root, text=key, variable=self.necessidades[key], command=lambda key=key: marcar_necessidade(key))
            checkbox.pack(pady=5)

        # Botão de continuar
        continuar_button = tk.Button(self.root, text="Continuar", command=self.tela_selecionar_psicologo)
        continuar_button.pack(pady=10)
        
        # Botão de voltar
        voltar_button = tk.Button(self.root, text="Voltar", command=self.tela_paciente)
        voltar_button.pack(pady=5)

    def tela_selecionar_psicologo(self):
        # Limpa a janela
        for widget in self.root.winfo_children():
            widget.destroy()

        # Cria o título
        title = tk.Label(self.root, text="Selecione um Psicólogo", font=("Helvetica", 16))
        title.pack(pady=10)

        # Lista de psicólogos
        psicologos = self.repositorio_psicologo.listar(especialidade=self.paciente_autenticado.necessidade)
        if not psicologos:
            tk.Label(self.root, text="Nenhum psicólogo encontrado.").pack(pady=5)

        # Cria um botão para cada psicólogo
        for psicologo in psicologos:
            button = tk.Button(self.root, text=psicologo.nome, command=lambda psicologo=psicologo: self.tela_confirmar_consulta(psicologo))
            button.pack(pady=5)

        # Botão de voltar
        voltar_button = tk.Button(self.root, text="Voltar", command=self.tela_agendar_consulta)
        voltar_button.pack(pady=5)

    def tela_confirmar_consulta(self, psicologo):
        for widget in self.root.winfo_children():
            widget.destroy()

        title = tk.Label(self.root, text="Confirmar Consulta", font=("Helvetica", 16))
        title.pack(pady=10)

        # Exibe os dados da consulta
        tk.Label(self.root, text=f"Psicólogo: {psicologo.nome}").pack(pady=5)
        tk.Label(self.root, text=f"Necessidade: {self.paciente_autenticado.necessidade}").pack(pady=5)

        # Entrada para a data da consulta
        tk.Label(self.root, text="Data da Consulta:").pack(pady=5)
        self.data_entry = DateEntry(self.root, date_pattern='yyyy-mm-dd')
        self.data_entry.pack(pady=5)

        # Entrada para a hora da consulta
        tk.Label(self.root, text="Hora da Consulta:").pack(pady=5)
        self.hora_entry = ttk.Combobox(self.root, values=[f"{h:02d}:00" for h in range(24)])
        self.hora_entry.pack(pady=5)

        # Botão de confirmar
        confirmar_button = tk.Button(self.root, text="Confirmar", command=lambda: self.salvar_consulta(psicologo))
        confirmar_button.pack(pady=10)

        # Botão de voltar
        voltar_button = tk.Button(self.root, text="Voltar", command=self.tela_selecionar_psicologo)
        voltar_button.pack(pady=5)

    def salvar_consulta(self, psicologo):
        # Obtém a data e a hora da consulta
        data_consulta = self.data_entry.get_date()
        hora_consulta = self.hora_entry.get()

        try:
            hora_consulta = datetime.strptime(hora_consulta, "%H:%M").time()
        except ValueError:
            messagebox.showerror("Erro", "Hora inválida.")

        # Cria a consulta
        consulta = Consulta(
            id_paciente=self.paciente_autenticado.id,
            id_psicologo=psicologo.id,
            data=data_consulta,
            horario=hora_consulta,
            especialidade= self.paciente_autenticado.necessidade
        )

        # Salva a consulta
        try:
            consulta_salva = self.servico_consulta.salvar(consulta)
            if consulta_salva:
                messagebox.showinfo("Sucesso", "Consulta agendada com sucesso!")
                self.tela_paciente()
            else:
                messagebox.showerror("Erro", "Erro ao agendar consulta")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def tela_detalhes_consultas_paciente(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        title = tk.Label(self.root, text="Detalhes das Consultas", font=("Helvetica", 16))
        title.pack(pady=10)

        # Exibe as próximas x consultas
        proximas_consultas = self.servico_consulta.listar_proximas_consultas(self.paciente_autenticado.id, quantidade=5)
        if proximas_consultas:
            consultas_frame = tk.Frame(self.root)
            consultas_frame.pack(pady=10)
            tk.Label(consultas_frame, text="Próximas Consultas:", font=("Helvetica", 14)).pack(pady=5)
            for consulta in proximas_consultas:
                psicologo = self.repositorio_psicologo.buscar_por_id(consulta.id_psicologo)
                data_formatada = consulta.data.strftime("%d/%m/%Y")
                horario_formatado = (datetime.min + consulta.horario).time().strftime("%H:%M")

                consulta_text = f"Data: {data_formatada}, Hora: {horario_formatado}, Psicólogo: {psicologo.nome}, Especialidade: {consulta.especialidade}"
                consulta_label = tk.Label(consultas_frame, text=consulta_text)
                consulta_label.pack(pady=2)
                cancelar_button = tk.Button(consultas_frame, text="Cancelar", command=lambda c=consulta: self.cancelar_consulta(c.id))
                cancelar_button.pack(pady=2)
        else:
            tk.Label(self.root, text="Você não tem consultas agendadas.", font=("Helvetica", 12)).pack(pady=10)

        # Botão para voltar à tela do paciente
        voltar_button = tk.Button(self.root, text="Voltar", command=self.tela_paciente)
        voltar_button.pack(pady=5)

    def tela_detalhes_consultas_psicologo(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        title = tk.Label(self.root, text="Detalhes das Consultas", font=("Helvetica", 16))
        title.pack(pady=10)

        # Exibe todas as consultas do psicólogo
        consultas = self.servico_consulta.listar_proximas_consultas_psicologo(self.psicologo_autenticado.id, quantidade=5)
        if consultas:
            consultas_frame = tk.Frame(self.root)
            consultas_frame.pack(pady=10)
            tk.Label(consultas_frame, text="Consultas Agendadas:", font=("Helvetica", 14)).pack(pady=5)
            for consulta in consultas:
                nome_paciente = self.repositorio_paciente.buscar_por_id(consulta.id_paciente).nome
                data_formatada = consulta.data.strftime("%d/%m/%Y")
                horario_formatado = (datetime.min + consulta.horario).time().strftime("%H:%M")
                consulta_text = f"Data: {data_formatada}, Hora: {horario_formatado}, Paciente: {nome_paciente}, Especialidade: {consulta.especialidade}"
                tk.Label(consultas_frame, text=consulta_text).pack(pady=2)
                cancelar_button = tk.Button(consultas_frame, text="Cancelar", command=lambda c=consulta: self.cancelar_consulta(c.id))
                cancelar_button.pack(pady=2)
        else:
            tk.Label(self.root, text="Você não tem consultas agendadas.", font=("Helvetica", 12)).pack(pady=10)

        # Botão para voltar à tela do psicólogo
        voltar_button = tk.Button(self.root, text="Voltar", command=self.tela_psicologo)
        voltar_button.pack(pady=5)
        
    def cancelar_consulta(self, id):
        confirma = messagebox.askyesno("Confirmação", "Tem certeza que deseja cancelar esta consulta?")
        if confirma:
            if self.repositorio_consulta.cancelar(id):
                messagebox.showinfo("Sucesso", "Consulta cancelada com sucesso!")
                self.tela_detalhes_consultas_paciente()
            else:
                messagebox.showerror("Erro", "Erro ao cancelar consulta.")

    def logout(self):
        self.paciente_autenticado = None
        self.psicologo_autenticado = None
        self.tela_menu()

                
if __name__ == "__main__":
    root = tk.Tk()
    app = UserInterface(root)
    root.mainloop()