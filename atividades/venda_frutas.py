"""
Questão 9
"""

def calcular_venda_frutas(quantidade_morango_kg: float, quantidade_maca_kg: float) -> dict:
    """
    Calcula o preço de venda de frutas com desconto.
    
    Args:
        quantidade_morango_kg: quantidade de morango em Kg
        quantidade_maca_kg: quantidade de maçã em Kg
        
    Returns:
        dict com detalhes do cálculo de venda
    """
    # Calcular preço do morango
    if quantidade_morango_kg <= 5:
        preco_morango_kg = 2.50
    else:
        preco_morango_kg = 2.20
    
    valor_morango = quantidade_morango_kg * preco_morango_kg
    
    # Calcular preço da maçã
    if quantidade_maca_kg <= 5:
        preco_maca_kg = 1.80
    else:
        preco_maca_kg = 1.50
    
    valor_maca = quantidade_maca_kg * preco_maca_kg
    
    # Total antes de desconto
    total_compras = valor_morango + valor_maca
    
    # Aplicar desconto se ultrapassar R$ 25,00
    if total_compras > 25.00:
        desconto = total_compras * 0.10
        total_final = total_compras - desconto
    else:
        desconto = 0
        total_final = total_compras
    
    return {
        "quantidade_morango_kg": quantidade_morango_kg,
        "preco_morango_kg": preco_morango_kg,
        "valor_morango": round(valor_morango, 2),
        "quantidade_maca_kg": quantidade_maca_kg,
        "preco_maca_kg": preco_maca_kg,
        "valor_maca": round(valor_maca, 2),
        "total_compras": round(total_compras, 2),
        "desconto": round(desconto, 2),
        "total_final": round(total_final, 2),
        "tipo": "venda_frutas"
    }
