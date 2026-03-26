"""
GUIA DE TESTES DA API
Este arquivo contém exemplos de como testar os endpoints da API
"""

# Você pode salvar este arquivo e carregá-lo no Postman ou executar com Python:
# python -m requests (após instalar requests: pip install requests)

import requests
import json

BASE_URL = "http://localhost:8000"

def test_endpoint(name, method, endpoint, data):
    """Testa um endpoint da API"""
    url = f"{BASE_URL}{endpoint}"
    print(f"\n{'='*70}")
    print(f"TESTANDO: {name}")
    print(f"{'='*70}")
    print(f"URL: {method} {url}")
    print(f"Dados: {json.dumps(data, indent=2)}")
    
    try:
        if method == "POST":
            response = requests.post(url, json=data)
        elif method == "GET":
            response = requests.get(url)
        
        print(f"Status: {response.status_code}")
        print(f"Resposta:")
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"ERRO: {str(e)}")

# ===================== TESTES =====================

def main():
    print("\nAVISO: Certifique-se que o servidor está rodando:")
    print("python main.py")
    print("ou")
    print("uvicorn main:app --reload")
    
    # Teste 1
    test_endpoint(
        "Maçãs Customizadas",
        "POST",
        "/1/macos-customizadas",
        {"quantidade": 15}
    )
    
    # Teste 2
    test_endpoint(
        "Calcular Idade",
        "POST",
        "/2/idade",
        {"ano_atual": 2026, "ano_nascimento": 2005}
    )
    
    # Teste 3
    test_endpoint(
        "Jornada de Trabalho",
        "POST",
        "/3/jornada-trabalho",
        {"horas_trabalhadas_mes": 180, "valor_hora_regular": 50.00}
    )
    
    # Teste 4
    test_endpoint(
        "Comissão de Vendas",
        "POST",
        "/4/comissao",
        {"salario_fixo": 2000, "valor_vendas": 2000}
    )
    
    # Teste 5
    test_endpoint(
        "Conta Bancária",
        "POST",
        "/5/conta-bancaria",
        {
            "numero_conta": "12345",
            "saldo": 1000,
            "debito": 200,
            "credito": 500
        }
    )
    
    # Teste 6
    test_endpoint(
        "Peso Ideal",
        "POST",
        "/6/peso-ideal",
        {"altura": 1.75, "sexo": "M"}
    )
    
    # Teste 7
    test_endpoint(
        "Desconto em Produto",
        "POST",
        "/7/desconto-produto",
        {"nome_produto": "Notebook", "quantidade": 15, "preco_unitario": 100}
    )
    
    # Teste 8
    test_endpoint(
        "Desconto em Combustível",
        "POST",
        "/8/desconto-combustivel",
        {"tipo_combustivel": "A", "quantidade_litros": 30}
    )
    
    # Teste 9
    test_endpoint(
        "Venda de Frutas",
        "POST",
        "/9/venda-frutas",
        {"quantidade_morango_kg": 6, "quantidade_maca_kg": 4}
    )
    
    # Teste 10
    test_endpoint(
        "Código de Usuário (Sucesso)",
        "POST",
        "/10/codigo-usuario",
        {"codigo": 1234, "senha": "9999"}
    )
    
    # Teste 10 (Falha)
    test_endpoint(
        "Código de Usuário (Falha)",
        "POST",
        "/10/codigo-usuario",
        {"codigo": 5678, "senha": "1234"}
    )

if __name__ == "__main__":
    main()
