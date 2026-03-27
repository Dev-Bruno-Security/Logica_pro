"""
Questão 1
"""

def calcular_macos_customizadas(quantidade: int) -> dict:
    """
    Calcula o custo total de maçãs customizadas com desconto por quantidade.
    
    Args:
        quantidade: número de maçãs a comprar
        
    Returns:
        dict com preço unitário, quantidade e custo total
    """
    if quantidade < 12:
        preco_unitario = 1.30
    else:
        preco_unitario = 1.00
    
    custo_total = quantidade * preco_unitario
    
    return {
        "quantidade": quantidade,
        "preco_unitario": preco_unitario,
        "custo_total": round(custo_total, 2),
        "tipo": "macos_customizadas"
    }
