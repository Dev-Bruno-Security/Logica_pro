"""
Questão 2
"""

def calcular_idade(ano_atual: int, ano_nascimento: int) -> dict:
    """
    Calcula a idade e verifica se pode votar.
    
    Args:
        ano_atual: ano atual
        ano_nascimento: ano em que a pessoa nasceu
        
    Returns:
        dict com idade, ano de nascimento e permissão de voto
    """
    idade = ano_atual - ano_nascimento
    pode_votar = idade >= 18
    
    mensagem = f"{'Pode' if pode_votar else 'Não pode'} votar"
    
    return {
        "ano_nascimento": ano_nascimento,
        "ano_atual": ano_atual,
        "idade": idade,
        "pode_votar": pode_votar,
        "mensagem": mensagem,
        "tipo": "idade"
    }
