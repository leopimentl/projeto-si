from consulta.repositorio_consulta import RepositorioConsulta
from paciente.repositorio_paciente import RepositorioPaciente
from paciente.servico_autenticacao_paciente import ServicoAutenticacaoPaciente
from paciente.servico_paciente import ServicoPaciente
from consulta.consulta import Consulta
from consulta.servico_consulta import ServicoConsulta 
from psicologo.repositorio_psicologo import RepositorioPsicologo
from psicologo.servico_autenticacao_psicologo import ServicoAutenticacaoPsicologo
from psicologo.servico_psicologo import ServicoPsicologo
from view.user_interface import UserInterface

# Repositórios
repositorio_paciente = RepositorioPaciente()
repositorio_psicologo = RepositorioPsicologo()
repositorio_consultas = RepositorioConsulta("consultas.txt")

# Serviços
servico_autenticacao_paciente = ServicoAutenticacaoPaciente(repositorio_paciente)
servico_autenticacao_psicologo = ServicoAutenticacaoPsicologo(repositorio_psicologo)

servico_paciente = ServicoPaciente(repositorio_paciente, repositorio_consultas)
servico_psicologo = ServicoPsicologo(repositorio_psicologo, repositorio_consultas)
servico_consultas = ServicoConsulta(repositorio_psicologo, repositorio_paciente, repositorio_consultas)

# Interface
UI = UserInterface()

# Constantes
ENTRAR = "1"
CADASTRAR = "2"
SAIR = "S"

TIPO_PACIENTE = "1"
TIPO_PSICOLOGO = "2"

MENU_DE_CONSULTAS = "1"

AGENDAR_NOVA_CONSULTA = "1"
LISTAR_CONSULTAS_AGENDADAS = "2"

MOSTRAR_PERFIL = "2"

VOLTAR = "V"

CONTINUAR = "1"

while True:
    escolha = UI.menu()
    if (escolha == ENTRAR): # LOGIN
        while True:
            dados_paciente = UI.login()
            if (dados_paciente["tipo"] == TIPO_PACIENTE):
                paciente_autenticado = servico_autenticacao_paciente.autenticar(dados_paciente)
                if paciente_autenticado is None:
                    UI.erro_login()
                    break

                UI.login_success()
                while True:
                    escolha = UI.menu_paciente()
                    if (escolha.upper() == SAIR):
                        break

                    if (escolha == MENU_DE_CONSULTAS):
                        while True:
                            escolha_menu_consultas = UI.menu_paciente_consultas()
                            if escolha_menu_consultas.upper() == VOLTAR:
                                break

                            if escolha_menu_consultas == AGENDAR_NOVA_CONSULTA: # AGENDAR NOVA CONSULTA
                                psicologos = servico_psicologo.encontrar_todos()
                                id_fornecido = UI.escolha_de_psicologo(psicologos)
                                if servico_psicologo.existe_pelo_id(id_fornecido):
                                    dados_consulta = {
                                        "patient_id": paciente_autenticado.id,
                                        "psychologist_id": id_fornecido
                                        }
                                    consulta_agendada = servico_consultas.agendar_consulta(dados_consulta)
                                    if consulta_agendada is None:
                                        UI.erro_consulta()
                                    else:
                                        UI.consulta_criada()

                                elif id_fornecido.upper() == VOLTAR:
                                    break 
                                else:
                                    UI.printa_opcao_invalida()

                            elif escolha_menu_consultas == LISTAR_CONSULTAS_AGENDADAS: # LISTAR CONSULTAS AGENDADAS
                                    consultas = servico_paciente.encontrar_consultas_pelo_id(paciente_autenticado.id)
                                    while True:
                                        escolha = UI.consultas_do_paciente(consultas)
                                        if escolha.upper() == VOLTAR:
                                            break      

                    elif (escolha == MOSTRAR_PERFIL): # MOSTRAR PERFIL
                            while True:
                                escolha = UI.perfil_paciente(servico_paciente.paciente_to_dict(paciente_autenticado))
                                if escolha.upper() == VOLTAR:
                                    break
                    
            elif dados_paciente["tipo"] == TIPO_PSICOLOGO: # TIPO PSICOLOGO
                psicologo_autenticado = servico_autenticacao_psicologo.autenticar(dados_paciente)
                if psicologo_autenticado is None:
                    UI.erro_login()
                    break

                UI.login_success()
                while True:
                    escolha = UI.menu_psicologo()
                    if (escolha.upper() == SAIR):
                        break

                    if (escolha == MENU_DE_CONSULTAS): # MENU DE CONSULTAS
                        while True:
                            escolha_menu_consultas = UI.menu_psicologo_consultas()
                            if (escolha_menu_consultas.upper() == VOLTAR):
                                break

                            if (escolha_menu_consultas == LISTAR_CONSULTAS_AGENDADAS): # LISTAR_CONSULTA_AGENDADAS
                                consultas = servico_psicologo.encontrar_consultas_pelo_id(psicologo_autenticado.id)
                                while True:
                                    escolha = UI.consultas_do_psicologo(consultas)
                                    if escolha.upper() == VOLTAR:
                                        break

                    elif (escolha == MOSTRAR_PERFIL):
                        while True:
                            escolha_perfil = UI.perfil_psicologo(servico_psicologo.psicologo_to_dict(psicologo_autenticado))
                            if escolha_perfil.upper() == VOLTAR:
                                break

            else:
                UI.erro_login()
                break
        
    elif escolha == CADASTRAR: # CADASTRAR
        while True:
            tipo_conta = UI.tela_criacao_conta()   
            if (tipo_conta.upper() == VOLTAR): # VOLTA PARA MENU PRINCIPAL
                break
            elif (tipo_conta == TIPO_PACIENTE): # CADASTRAR PACIENTE
                confirmacao = UI.input_confirmacao()
                if confirmacao.upper() == VOLTAR:
                    break
                if confirmacao == CONTINUAR: # CONTINUA PARA INSERIR DADOS
                    while True:
                        dados_paciente = UI.tela_dados_paciente()
                        if (dados_paciente is None):
                            continue
                        paciente = servico_paciente.salvar(dados_paciente)
                        if (paciente is None):
                            UI.tela_erro_criacao_conta()
                            continue
                        UI.tela_conta_criada()
                        break
                else:
                    UI.printa_opcao_invalida()
            elif (tipo_conta == TIPO_PSICOLOGO): # CADASTRAR PSICOLOGO
                confirmacao = UI.input_confirmacao()
                if confirmacao.upper() == VOLTAR:
                    break
                
                if (confirmacao == CONTINUAR):
                    dados_psicologo = UI.input_detalhes_psicologo()
                    psicologo = servico_psicologo.salvar(dados_psicologo)
                    if (psicologo is None):
                        UI.tela_erro_criacao_conta()
                    else:
                        UI.tela_conta_criada()

                else:
                    UI.printa_opcao_invalida()
            else:
                UI.printa_opcao_invalida()
        
    elif (escolha.upper() == SAIR): # ENCERRA SISTEMA
        UI.saida()
        break

     