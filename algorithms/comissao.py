"""
Algoritmo 4: Comissão de Vendas
Lê o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa.
Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00
mais 5% sobre o que ultrapassar este valor, calcula e escreve o seu salário total.
"""

def calcular_comissao(salario_fixo: float, valor_vendas: float) -> dict:
    """
    Calcula o salário total com comissão sobre vendas.
    
    Args:
        salario_fixo: salário fixo do vendedor
        valor_vendas: valor total das vendas efetuadas
        
    Returns:
        dict com detalhes do cálculo de comissão
    """
    # Primeira faixa: 3% até R$ 1.500,00
    if valor_vendas <= 1500:
        comissao_primeira_faixa = valor_vendas * 0.03
        comissao_segunda_faixa = 0
    else:
        comissao_primeira_faixa = 1500 * 0.03
        valor_excedente = valor_vendas - 1500
        comissao_segunda_faixa = valor_excedente * 0.05
    
    comissao_total = comissao_primeira_faixa + comissao_segunda_faixa
    salario_total = salario_fixo + comissao_total
    
    return {
        "salario_fixo": round(salario_fixo, 2),
        "valor_vendas": round(valor_vendas, 2),
        "comissao_primeira_faixa": round(comissao_primeira_faixa, 2),
        "comissao_segunda_faixa": round(comissao_segunda_faixa, 2),
        "comissao_total": round(comissao_total, 2),
        "salario_total": round(salario_total, 2),
        "tipo": "comissao_vendas"
    }
