# 🚀 Quick Start - API de Lógica de Programação

## Aluno: Bruno João da Silva | Matrícula: 01193399

---

## ⚡ Iniciar em 2 Minutos

### Opção 1: Script Automático (Linux/Mac)
```bash
./start.sh
```

### Opção 2: Comando Manual
```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Iniciar servidor
python main.py
```

### Opção 3: Com Uvicorn
```bash
uvicorn main:app --reload
```

---

## 📖 Acessar a Documentação

Quando o servidor estiver rodando:

- **Swagger UI (Interativo):** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc
- **Raiz da API:** http://localhost:8000

---

## ✅ Testar os Algoritmos

### Executar Testes Locais (sem servidor)
```bash
python test_algorithms.py
```

### Testar via HTTP (com servidor rodando)
```bash
# Você pode usar curl, Postman ou Python
python test_api.py
```

---

## 🎯 Exemplos Rápidos com cURL

Certifique-se que o servidor está rodando em http://localhost:8000

### 1️⃣ Maçãs Customizadas
```bash
curl -X POST "http://localhost:8000/1/macos-customizadas" \
  -H "Content-Type: application/json" \
  -d '{"quantidade": 15}'
```
**Resposta esperada:** R$15.00 (15 × R$1.00)

### 2️⃣ Calcular Idade
```bash
curl -X POST "http://localhost:8000/2/idade" \
  -H "Content-Type: application/json" \
  -d '{"ano_atual": 2026, "ano_nascimento": 2005}'
```
**Resposta esperada:** 21 anos, pode votar

### 3️⃣ Jornada de Trabalho
```bash
curl -X POST "http://localhost:8000/3/jornada-trabalho" \
  -H "Content-Type: application/json" \
  -d '{"horas_trabalhadas_mes": 180, "valor_hora_regular": 50}'
```
**Resposta esperada:** Salário total considerando 20 horas extras

### 4️⃣ Comissão
```bash
curl -X POST "http://localhost:8000/4/comissao" \
  -H "Content-Type: application/json" \
  -d '{"salario_fixo": 2000, "valor_vendas": 2000}'
```
**Resposta esperada:** Salário total com comissão

### 5️⃣ Conta Bancária
```bash
curl -X POST "http://localhost:8000/5/conta-bancaria" \
  -H "Content-Type: application/json" \
  -d '{"numero_conta": "12345", "saldo": 1000, "debito": 200, "credito": 500}'
```
**Resposta esperada:** Saldo final R$1300 (Positivo)

### 6️⃣ Peso Ideal
```bash
curl -X POST "http://localhost:8000/6/peso-ideal" \
  -H "Content-Type: application/json" \
  -d '{"altura": 1.75, "sexo": "M"}'
```
**Resposta esperada:** Peso ideal ≈ 69.23kg

### 7️⃣ Desconto em Produto
```bash
curl -X POST "http://localhost:8000/7/desconto-produto" \
  -H "Content-Type: application/json" \
  -d '{"nome_produto": "Notebook", "quantidade": 15, "preco_unitario": 100}'
```
**Resposta esperada:** 5% desconto, total R$1425.00

### 8️⃣ Desconto em Combustível
```bash
curl -X POST "http://localhost:8000/8/desconto-combustivel" \
  -H "Content-Type: application/json" \
  -d '{"tipo_combustivel": "A", "quantidade_litros": 30}'
```
**Resposta esperada:** 5% desconto (>20L), total R$82.65

### 9️⃣ Venda de Frutas
```bash
curl -X POST "http://localhost:8000/9/venda-frutas" \
  -H "Content-Type: application/json" \
  -d '{"quantidade_morango_kg": 6, "quantidade_maca_kg": 4}'
```
**Resposta esperada:** Total R$20.40

### 🔟 Código de Usuário (Sucesso)
```bash
curl -X POST "http://localhost:8000/10/codigo-usuario" \
  -H "Content-Type: application/json" \
  -d '{"codigo": 1234, "senha": "9999"}'
```
**Resposta esperada:** "Acesso permitido"

### 🔟 Código de Usuário (Erro)
```bash
curl -X POST "http://localhost:8000/10/codigo-usuario" \
  -H "Content-Type: application/json" \
  -d '{"codigo": 5678, "senha": "9999"}'
```
**Resposta esperada:** "Usuário inválido!!"

---

## 📁 Estrutura do Projeto

```
Logica_pro/
├── main.py                    ← Aplicação FastAPI
├── config.py                  ← Configurações constantes
├── requirements.txt           ← Dependências
├── start.sh                   ← Script para iniciar
├── README.md                  ← Documentação completa
├── QUICKSTART.md              ← Este arquivo
├── test_algorithms.py         ← Testes dos algoritmos
├── test_api.py                ← Testes HTTP
│
├── algorithms/                ← Módulos dos algoritmos
│   ├── macos_customizadas.py
│   ├── idade.py
│   ├── jornada_trabalho.py
│   ├── comissao.py
│   ├── conta_bancaria.py
│   ├── peso_ideal.py
│   ├── desconto_produto.py
│   ├── desconto_combustivel.py
│   ├── venda_frutas.py
│   └── codigo_usuario.py
│
└── utils/
    └── __init__.py
```

---

## 🔧 Solucionar Problemas

### Porta 8000 já está em uso?
```bash
# Linux/Mac: Encontrar processo
lsof -i :8000

# Pode usar outra porta
uvicorn main:app --reload --port 8001
```

### ModuleNotFoundError?
```bash
# Certifique-se que está na pasta correta
cd /workspaces/Logica_pro

# E que as dependências estão instaladas
pip install -r requirements.txt
```

### Python não encontrado?
```bash
# Use python3 em vez de python
python3 main.py
```

---

## 📚 Saiba Mais

- [FastAPI Documentação](https://fastapi.tiangolo.com/)
- [Pydantic Docs](https://docs.pydantic.dev/)
- [HTTP Status Codes](https://httpwg.org/specs/rfc9110.html#status.codes)

---

## 👤 Informações do Aluno

- **Nome:** Bruno João da Silva
- **Matrícula:** 01193399
- **Trabalho:** Desenvolvimento de Backend Acadêmico
- **Data:** Março 2026

---

**Última atualização:** Março 2026
