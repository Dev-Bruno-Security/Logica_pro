"""
Questão 6
"""

def calcular_peso_ideal(altura: float, sexo: str) -> dict:
    """
    Calcula o peso ideal baseado em altura e sexo.
    
    Args:
        altura: altura em metros
        sexo: 'M' para masculino ou 'F' para feminino
        
    Returns:
        dict com altura, sexo e peso ideal
    """
    sexo = sexo.upper()
    
    if sexo == 'M':
        peso_ideal = (72.7 * altura) - 58
    elif sexo == 'F':
        peso_ideal = (62.1 * altura) - 44.7
    else:
        return {
            "erro": "Sexo inválido. Use 'M' para masculino ou 'F' para feminino",
            "tipo": "peso_ideal"
        }
    
    return {
        "altura": altura,
        "sexo": sexo,
        "peso_ideal": round(peso_ideal, 2),
        "tipo": "peso_ideal"
    }
