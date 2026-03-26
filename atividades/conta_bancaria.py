"""
Algoritmo 5: Conta Bancária
Lê o número da conta do cliente, saldo, débito e crédito.
Após, calcula e escreve o saldo atual (saldo atual = saldo - débito + crédito).
Também testa se saldo atual for maior que ou igual a zero escrever uma mensagem
'Saldo Positivo', senão escrever uma mensagem 'Saldo Negativo'.
"""

def calcular_conta_bancaria(numero_conta: str, saldo: float, debito: float, credito: float) -> dict:
    """
    Calcula o saldo final de uma conta bancária.
    
    Args:
        numero_conta: número da conta
        saldo: saldo inicial
        debito: valor debitado
        credito: valor creditado
        
    Returns:
        dict com detalhes da conta e saldo final
    """
    saldo_final = saldo - debito + credito
    status = "Saldo Positivo" if saldo_final >= 0 else "Saldo Negativo"
    
    return {
        "numero_conta": numero_conta,
        "saldo_inicial": round(saldo, 2),
        "debito": round(debito, 2),
        "credito": round(credito, 2),
        "saldo_final": round(saldo_final, 2),
        "status": status,
        "tipo": "conta_bancaria"
    }
