"""
Questão 8
"""

def calcular_desconto_combustivel(tipo_combustivel: str, quantidade_litros: float) -> dict:
    """
    Calcula desconto e valor a pagar em combustível.
    
    Args:
        tipo_combustivel: 'A' para álcool ou 'G' para gasolina
        quantidade_litros: quantidade de litros vendidos
        
    Returns:
        dict com detalhes do cálculo de desconto e valor
    """
    tipo_combustivel = tipo_combustivel.upper()
    
    if tipo_combustivel == 'A':
        preco_por_litro = 2.90
        descricao = "Álcool"
        if quantidade_litros <= 20:
            percentual_desconto = 3
        else:
            percentual_desconto = 5
    elif tipo_combustivel == 'G':
        preco_por_litro = 3.30
        descricao = "Gasolina"
        if quantidade_litros <= 20:
            percentual_desconto = 4
        else:
            percentual_desconto = 6
    else:
        return {
            "erro": "Tipo de combustível inválido. Use 'A' para álcool ou 'G' para gasolina",
            "tipo": "desconto_combustivel"
        }
    
    valor_total = quantidade_litros * preco_por_litro
    desconto = valor_total * (percentual_desconto / 100)
    valor_a_pagar = valor_total - desconto
    
    return {
        "tipo_combustivel": descricao,
        "quantidade_litros": quantidade_litros,
        "preco_por_litro": preco_por_litro,
        "percentual_desconto": percentual_desconto,
        "valor_total": round(valor_total, 2),
        "desconto": round(desconto, 2),
        "valor_a_pagar": round(valor_a_pagar, 2),
        "tipo": "desconto_combustivel"
    }
