from validate_docbr import CPF, CNPJ
# pip install validate-docbr


def validar_documento(documento):
    documento_com_mascara = documento.replace(".","").replace("-","").replace("/","")

    if len(documento_com_mascara) == 11:
        return validar_cpf(documento)

    elif len(documento_com_mascara) == 14:
        return validar_cnpj(documento)

    else:
        raise ValueError ("Documento Inválido")


def validar_cpf(documento_cpf):

    cpf = CPF()

    cpf_validado = cpf.validate(documento_cpf)

    return cpf_validado 


def validar_cnpj(documento_cnpj):

    cnpj = CNPJ()

    cnpj_validado = cnpj.validate(documento_cnpj)

    return cnpj_validado 

