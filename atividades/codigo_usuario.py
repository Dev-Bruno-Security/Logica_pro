"""
Algoritmo 10: Validação de Código de Usuário
Faça um algoritmo para ler um número que é um código de usuário.
Caso este código seja diferente de um código armazenado (igual a 1234)
deve ser apresentada uma mensagem de usuário inválido!!.
Caso a senha esteja incorreta, deve ser lido outro valor que é a senha.
Se esta estiver correta, deve ser mostrada uma mensagem 'Acesso permitido'.
Caso contrário, deve ser mostrada uma mensagem 'Senha Incorreta'.
Caso a senha esteja correta, a dever ser mostrada uma mensagem 'Acesso permitido'.
Caso o número digitado seja maior que 9999, deve ser mostrada uma mensagem 'Número incorreto'.
"""

def validar_codigo_usuario(codigo: int, senha: str = None) -> dict:
    """
    Valida o código de usuário e a senha.
    
    Args:
        codigo: código do usuário
        senha: senha do usuário (opcional, required se código é válido)
        
    Returns:
        dict com resultado da validação
    """
    CODIGO_CORRETO = 1234
    SENHA_CORRETA = "9999"
    
    # Verificar se o código é um número válido
    if codigo > 9999:
        return {
            "valido": False,
            "mensagem": "Número incorreto",
            "tipo": "codigo_usuario"
        }
    
    # Verificar se o código está correto
    if codigo != CODIGO_CORRETO:
        return {
            "valido": False,
            "mensagem": "Usuário inválido!!",
            "tipo": "codigo_usuario"
        }
    
    # Código correto, agora verificar a senha
    if senha is None:
        return {
            "valido": False,
            "mensagem": "Senha necessária",
            "tipo": "codigo_usuario"
        }
    
    if senha == SENHA_CORRETA:
        return {
            "valido": True,
            "mensagem": "Acesso permitido",
            "tipo": "codigo_usuario"
        }
    else:
        return {
            "valido": False,
            "mensagem": "Senha incorreta",
            "tipo": "codigo_usuario"
        }
