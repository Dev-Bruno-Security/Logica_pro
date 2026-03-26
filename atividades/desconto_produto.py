"""
Algoritmo 7: Desconto em Produtos
Lê a descrição do produto (nome), a quantidade adquirida e o preço unitário.
Calcula e escreve o total (total = quantidade adquirida * preço unitário),
o desconto e o total a pagar (total a pagar = total - desconto), sabendo-se que:
- Se quantidade < 5 o desconto será de 2%
- Se quantidade >= 5 e quantidade < 10 o desconto será de 3%
- Se quantidade >= 10 o desconto será de 5%
"""

def calcular_desconto_produto(nome_produto: str, quantidade: int, preco_unitario: float) -> dict:
    """
    Calcula desconto em produto baseado na quantidade.
    
    Args:
        nome_produto: nome do produto
        quantidade: quantidade adquirida
        preco_unitario: preço por unidade
        
    Returns:
        dict com detalhes do cálculo de desconto
    """
    # Determinar percentual de desconto
    if quantidade < 5:
        percentual_desconto = 2
    elif 5 <= quantidade < 10:
        percentual_desconto = 3
    else:  # quantidade >= 10
        percentual_desconto = 5
    
    total = quantidade * preco_unitario
    desconto = total * (percentual_desconto / 100)
    total_a_pagar = total - desconto
    
    return {
        "nome_produto": nome_produto,
        "quantidade": quantidade,
        "preco_unitario": round(preco_unitario, 2),
        "percentual_desconto": percentual_desconto,
        "total": round(total, 2),
        "desconto": round(desconto, 2),
        "total_a_pagar": round(total_a_pagar, 2),
        "tipo": "desconto_produto"
    }
