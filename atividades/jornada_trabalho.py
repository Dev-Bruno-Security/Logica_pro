"""
Questão 3
"""

def calcular_jornada_trabalho(horas_trabalhadas_mes: float, valor_hora_regular: float) -> dict:
    """
    Calcula salário total com horas extras.
    
    Args:
        horas_trabalhadas_mes: total de horas trabalhadas no mês (4 semanas)
        valor_hora_regular: valor da hora regular
        
    Returns:
        dict com detalhes do cálculo de salário e horas extras
    """
    # 4 semanas * 40 horas/semana = 160 horas normais
    horas_normais_mes = 160
    
    if horas_trabalhadas_mes <= horas_normais_mes:
        horas_extras = 0
        valor_hora_extra = 0
        salario_horas_normais = horas_trabalhadas_mes * valor_hora_regular
    else:
        horas_extras = horas_trabalhadas_mes - horas_normais_mes
        valor_hora_extra = valor_hora_regular * 1.5  # 50% acréscimo
        salario_horas_normais = horas_normais_mes * valor_hora_regular
    
    salario_horas_extras = horas_extras * valor_hora_extra
    salario_total = salario_horas_normais + salario_horas_extras
    
    return {
        "horas_trabalhadas_mes": horas_trabalhadas_mes,
        "horas_normais_mes": horas_normais_mes,
        "horas_extras": horas_extras,
        "valor_hora_regular": round(valor_hora_regular, 2),
        "valor_hora_extra": round(valor_hora_extra, 2),
        "salario_horas_normais": round(salario_horas_normais, 2),
        "salario_horas_extras": round(salario_horas_extras, 2),
        "salario_total": round(salario_total, 2),
        "tipo": "jornada_trabalho"
    }
