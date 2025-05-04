from tkinter import Label, Button, Entry
import tkinter as tk
from validacao import validar_documento

from enviar_contrato import (
    EnviarContrato,
    dict_vendedores,
    nome_cliente,
    cpf_cliente,
    email_cliente,
    cod_cliente,
    cod_vendedor,
    cod_equipamento
)


if validar_documento(cpf_cliente):
    cor_da_letra_cpf = "black"
else:
    cor_da_letra_cpf = "red"

# INSTANCIA DA JANELA
app = tk.Tk()
app.geometry("430x430")
app.title("Enviar Contratos ClickSign")


# INFORMAÕES DO RESPONSAVEL
valor_nome_cliente  = tk.StringVar(value=nome_cliente)
valor_email_cliente = tk.StringVar(value=email_cliente)
valor_cpf_cliente   = tk.StringVar(value=cpf_cliente)
valor_cod_cliente   = tk.StringVar(value=cod_cliente)
valor_cod_vendedor  = tk.StringVar(value=cod_vendedor)
valor_cod_equipamento = tk.StringVar(value=cod_equipamento)



# region LABELS
informacoes_do_responsavel = Label(
    app, text="Informações do Reponsável", font=("Arial", 22, "bold")
)
informacoes_do_responsavel.place(x=15, y=8)

nome_do_responsavel = Label(app, text="Nome:", font=("Arial", 15, "bold"))
nome_do_responsavel.place(x=10, y=70)

email_do_responsavel = Label(app, text="E-mail:", font=("Arial", 15, "bold"))
email_do_responsavel.place(x=10, y=120)

cpf_do_responsavel = Label(app, text="CPF:", font=("Arial", 15, "bold"))
cpf_do_responsavel.place(x=10, y=170)

codigo_do_equipamento = Label(app, text="Código Equipamento:", font=("Arial", 15, "bold"))
codigo_do_equipamento.place(x=10, y=220)

codigo_do_cliente_responsavel = Label(
    app, text="Código Cliente:", font=("Arial", 15, "bold")
)
codigo_do_cliente_responsavel.place(x=10, y=270)

codigo_do_vendedor = Label(app, text="Código Vendedor:", font=("Arial", 15, "bold"))
codigo_do_vendedor.place(x=10, y=320)
# endregion


# region ENTRY'S
entry_nome = Entry(app, width=29, textvariable=valor_nome_cliente, font=("Arial", 15))
entry_nome.place(x=85, y=72)

entry_email = Entry(app, width=29, textvariable=valor_email_cliente, font=("Arial", 15))
entry_email.place(x=85, y=122)

entry_cpf = Entry(app, width=29, textvariable=valor_cpf_cliente, font=("Arial", 15), foreground=cor_da_letra_cpf)
entry_cpf.place(x=85, y=172)

entry_codigo_equipamento = Entry(app, width=11, textvariable=valor_cod_equipamento, font=("Arial", 15), justify="center")
entry_codigo_equipamento.place(x=222, y=220)

entry_codigo_cliente = Entry(app, width=8, textvariable=valor_cod_cliente, font=("Arial", 15))
entry_codigo_cliente.place(x=165, y=270)

entry_codigo_vendedor = Entry(app, width=6, textvariable=valor_cod_vendedor, font=("Arial", 15))
entry_codigo_vendedor.place(x=190, y=320)
# endregion

cliente1 = EnviarContrato(
    nome_cliente, cpf_cliente, email_cliente, cod_cliente, cod_vendedor
)

def enviar_contrato():

    cliente1.abrir_clicksign()
    cliente1.abrir_explorador_arquivos()
    cliente1.selecionar_contrato()
    cliente1.adicionar_signatario_existente(nome_signatario="Distribuidora", tipo_assinatura="Comodante")
    cliente1.adicionar_signatario_existente(
        nome_signatario=dict_vendedores[cod_vendedor],
        tipo_assinatura="Testemunha"
    )
    cliente1.adicionar_signatario_novo(tipo_assinatura="Comodat")


# region BOTÕES
botao_enviar = Button(
    app,
    text="Enviar",
    font=("Arial", 15, "bold"), 
    width=15, 
    command=enviar_contrato
    )
botao_enviar.place(x=10, y=385)


botao_cancelar = Button(
    app,
    text="Cancelar",
    font=("Arial", 15, "bold"),
    width=15, 
    command=app.destroy
    )
botao_cancelar.place(x=230, y=385)
# endregion

app.mainloop()
