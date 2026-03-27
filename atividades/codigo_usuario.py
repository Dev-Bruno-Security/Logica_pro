"""
Questão 10
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
