"""
Testes simples para validar os algoritmos
Execução: python test_algorithms.py
"""

import sys
sys.path.insert(0, '/workspaces/Logica_pro')

from algorithms.macos_customizadas import calcular_macos_customizadas
from algorithms.idade import calcular_idade
from algorithms.jornada_trabalho import calcular_jornada_trabalho
from algorithms.comissao import calcular_comissao
from algorithms.conta_bancaria import calcular_conta_bancaria
from algorithms.peso_ideal import calcular_peso_ideal
from algorithms.desconto_produto import calcular_desconto_produto
from algorithms.desconto_combustivel import calcular_desconto_combustivel
from algorithms.venda_frutas import calcular_venda_frutas
from algorithms.codigo_usuario import validar_codigo_usuario

def test_all_algorithms():
    print("=" * 70)
    print("TESTANDO TODOS OS ALGORITMOS")
    print("=" * 70)
    
    # Teste 1: Maçãs Customizadas
    print("\n1. MAÇÃS CUSTOMIZADAS")
    print("-" * 70)
    resultado = calcular_macos_customizadas(15)
    print(f"Quantidade: {resultado['quantidade']}")
    print(f"Preço unitário: R${resultado['preco_unitario']}")
    print(f"Custo total: R${resultado['custo_total']}")
    
    # Teste 2: Idade
    print("\n2. CÁLCULO DE IDADE")
    print("-" * 70)
    resultado = calcular_idade(2026, 2005)
    print(f"Ano de nascimento: {resultado['ano_nascimento']}")
    print(f"Ano atual: {resultado['ano_atual']}")
    print(f"Idade: {resultado['idade']} anos")
    print(f"Pode votar: {resultado['pode_votar']} - {resultado['mensagem']}")
    
    # Teste 3: Jornada de Trabalho
    print("\n3. JORNADA DE TRABALHO")
    print("-" * 70)
    resultado = calcular_jornada_trabalho(180, 50.00)
    print(f"Horas trabalhadas: {resultado['horas_trabalhadas_mes']}h")
    print(f"Horas normais: {resultado['horas_normais_mes']}h")
    print(f"Horas extras: {resultado['horas_extras']}h")
    print(f"Valor hora: R${resultado['valor_hora_regular']}")
    print(f"Valor hora extra: R${resultado['valor_hora_extra']}")
    print(f"Salário total: R${resultado['salario_total']}")
    
    # Teste 4: Comissão
    print("\n4. COMISSÃO DE VENDAS")
    print("-" * 70)
    resultado = calcular_comissao(2000, 2000)
    print(f"Salário fixo: R${resultado['salario_fixo']}")
    print(f"Valor de vendas: R${resultado['valor_vendas']}")
    print(f"Comissão total: R${resultado['comissao_total']}")
    print(f"Salário total: R${resultado['salario_total']}")
    
    # Teste 5: Conta Bancária
    print("\n5. CONTA BANCÁRIA")
    print("-" * 70)
    resultado = calcular_conta_bancaria("12345", 1000, 200, 500)
    print(f"Número da conta: {resultado['numero_conta']}")
    print(f"Saldo inicial: R${resultado['saldo_inicial']}")
    print(f"Débito: R${resultado['debito']}")
    print(f"Crédito: R${resultado['credito']}")
    print(f"Saldo final: R${resultado['saldo_final']}")
    print(f"Status: {resultado['status']}")
    
    # Teste 6: Peso Ideal
    print("\n6. PESO IDEAL")
    print("-" * 70)
    resultado = calcular_peso_ideal(1.75, 'M')
    print(f"Altura: {resultado['altura']}m")
    print(f"Sexo: {resultado['sexo']}")
    print(f"Peso ideal: {resultado['peso_ideal']}kg")
    
    # Teste 7: Desconto em Produto
    print("\n7. DESCONTO EM PRODUTO")
    print("-" * 70)
    resultado = calcular_desconto_produto("Notebook", 15, 100)
    print(f"Produto: {resultado['nome_produto']}")
    print(f"Quantidade: {resultado['quantidade']}")
    print(f"Desconto: {resultado['percentual_desconto']}%")
    print(f"Total: R${resultado['total']}")
    print(f"Desconto (R$): R${resultado['desconto']}")
    print(f"Total a pagar: R${resultado['total_a_pagar']}")
    
    # Teste 8: Desconto em Combustível
    print("\n8. DESCONTO EM COMBUSTÍVEL")
    print("-" * 70)
    resultado = calcular_desconto_combustivel('A', 30)
    print(f"Combustível: {resultado['tipo_combustivel']}")
    print(f"Quantidade: {resultado['quantidade_litros']}L")
    print(f"Desconto: {resultado['percentual_desconto']}%")
    print(f"Valor a pagar: R${resultado['valor_a_pagar']}")
    
    # Teste 9: Venda de Frutas
    print("\n9. VENDA DE FRUTAS")
    print("-" * 70)
    resultado = calcular_venda_frutas(6, 4)
    print(f"Morango: {resultado['quantidade_morango_kg']}kg = R${resultado['valor_morango']}")
    print(f"Maçã: {resultado['quantidade_maca_kg']}kg = R${resultado['valor_maca']}")
    print(f"Total de compras: R${resultado['total_compras']}")
    print(f"Desconto (10%): R${resultado['desconto']}")
    print(f"Total final: R${resultado['total_final']}")
    
    # Teste 10: Código de Usuário
    print("\n10. CÓDIGO DE USUÁRIO")
    print("-" * 70)
    resultado = validar_codigo_usuario(1234, "9999")
    print(f"Válido: {resultado['valido']}")
    print(f"Mensagem: {resultado['mensagem']}")
    
    print("\n" + "=" * 70)
    print("TODOS OS TESTES COMPLETADOS COM SUCESSO!")
    print("=" * 70)

if __name__ == "__main__":
    test_all_algorithms()
