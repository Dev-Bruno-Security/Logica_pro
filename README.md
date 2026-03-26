# Backend de Lógica de Programação

## Informações do Aluno

- **Nome:** Bruno João da Silva
- **Matrícula:** 01193399
- **Tipo:** Trabalho Acadêmico - Faculdade

---

## 📋 Descrição do Projeto

Este é um backend em Python implementando 10 algoritmos de lógica de programação conforme especificação do trabalho acadêmico. Utiliza **FastAPI** para criar uma API RESTful com documentação automática.

## 🎯 Algoritmos Implementados

### 1. Maçãs Customizadas
- **Descrição:** Calcula o custo total de maçãs com desconto por quantidade
- **Regra:** R$1,30 cada (< 12 unidades) ou R$1,00 cada (≥ 12 unidades)
- **Endpoint:** `POST /1/macos-customizadas`
- **Parâmetros:**
  - `quantidade`: número de maçãs (int)

### 2. Cálculo de Idade
- **Descrição:** Determina a idade e se a pessoa pode votar
- **Regra:** Pode votar se tiver 18 anos ou mais
- **Endpoint:** `POST /2/idade`
- **Parâmetros:**
  - `ano_atual`: ano atual (int)
  - `ano_nascimento`: ano de nascimento (int)

### 3. Jornada de Trabalho
- **Descrição:** Calcula salário com horas extras
- **Regra:** 40 horas/semana normal, 50% acréscimo em horas extras (4 semanas/mês = 160h)
- **Endpoint:** `POST /3/jornada-trabalho`
- **Parâmetros:**
  - `horas_trabalhadas_mes`: total de horas no mês (float)
  - `valor_hora_regular`: valor da hora normal (float)

### 4. Comissão de Vendas
- **Descrição:** Calcula comissão sobre vendas
- **Regra:** 3% até R$1.500 + 5% acima desse valor
- **Endpoint:** `POST /4/comissao`
- **Parâmetros:**
  - `salario_fixo`: salário base (float)
  - `valor_vendas`: total de vendas (float)

### 5. Conta Bancária
- **Descrição:** Calcula saldo final da conta e status
- **Fórmula:** saldo_final = saldo - débito + crédito
- **Endpoint:** `POST /5/conta-bancaria`
- **Parâmetros:**
  - `numero_conta`: número da conta (string)
  - `saldo`: saldo inicial (float)
  - `debito`: valor debitado (float)
  - `credito`: valor creditado (float)

### 6. Peso Ideal
- **Descrição:** Calcula peso ideal por altura e sexo
- **Fórmulas:**
  - Masculino: peso_ideal = (72.7 × altura) - 58
  - Feminino: peso_ideal = (62.1 × altura) - 44.7
- **Endpoint:** `POST /6/peso-ideal`
- **Parâmetros:**
  - `altura`: altura em metros (float)
  - `sexo`: 'M' ou 'F' (string)

### 7. Desconto em Produto
- **Descrição:** Aplica desconto por quantidade
- **Regras:**
  - < 5 unidades: 2%
  - 5-10 unidades: 3%
  - ≥ 10 unidades: 5%
- **Endpoint:** `POST /7/desconto-produto`
- **Parâmetros:**
  - `nome_produto`: nome do produto (string)
  - `quantidade`: quantidade (int)
  - `preco_unitario`: preço por unidade (float)

### 8. Desconto em Combustível
- **Descrição:** Calcula desconto para combustível
- **Preços:**
  - Álcool: R$2,90 por litro
  - Gasolina: R$3,30 por litro
- **Descontos:**
  - Álcool: 3% (≤20L) ou 5% (>20L)
  - Gasolina: 4% (≤20L) ou 6% (>20L)
- **Endpoint:** `POST /8/desconto-combustivel`
- **Parâmetros:**
  - `tipo_combustivel`: 'A' (álcool) ou 'G' (gasolina)
  - `quantidade_litros`: quantidade em litros (float)

### 9. Venda de Frutas
- **Descrição:** Calcula preço de morangos e maçãs com desconto progressivo
- **Preços:**
  - Morango: R$2,50/Kg (≤5Kg) ou R$2,20/Kg (>5Kg)
  - Maçã: R$1,80/Kg (≤5Kg) ou R$1,50/Kg (>5Kg)
- **Desconto Extra:** 10% se total > R$25
- **Endpoint:** `POST /9/venda-frutas`
- **Parâmetros:**
  - `quantidade_morango_kg`: quantidade em Kg (float)
  - `quantidade_maca_kg`: quantidade em Kg (float)

### 10. Validação de Código de Usuário
- **Descrição:** Valida código e senha de usuário
- **Valores:** Código correto = 1234, Senha correta = 9999
- **Validação:** Código deve ser ≤ 9999
- **Endpoint:** `POST /10/codigo-usuario`
- **Parâmetros:**
  - `codigo`: código do usuário (int)
  - `senha`: senha (string, opcional)

---

## 🚀 Instalação e Execução

### Pré-requisitos
- Python 3.8+
- pip ou conda

### Passos

1. **Clonar/Acessar o repositório**
```bash
cd /workspaces/Logica_pro
```

2. **Criar ambiente virtual (recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. **Instalar dependências**
```bash
pip install -r requirements.txt
```

4. **Executar o servidor**
```bash
python main.py
```

Ou com uvicorn diretamente:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Saída esperada
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete
```

---

## 📚 Usando a API

### Documentação Interativa
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

### Exemplos de Requisições

#### 1. Maçãs Customizadas
```bash
curl -X POST "http://localhost:8000/1/macos-customizadas" \
  -H "Content-Type: application/json" \
  -d '{"quantidade": 15}'
```

#### 2. Calcular Idade
```bash
curl -X POST "http://localhost:8000/2/idade" \
  -H "Content-Type: application/json" \
  -d '{"ano_atual": 2026, "ano_nascimento": 2005}'
```

#### 3. Jornada de Trabalho
```bash
curl -X POST "http://localhost:8000/3/jornada-trabalho" \
  -H "Content-Type: application/json" \
  -d '{"horas_trabalhadas_mes": 180, "valor_hora_regular": 50.00}'
```

#### 4. Comissão
```bash
curl -X POST "http://localhost:8000/4/comissao" \
  -H "Content-Type: application/json" \
  -d '{"salario_fixo": 2000, "valor_vendas": 2000}'
```

#### 5. Conta Bancária
```bash
curl -X POST "http://localhost:8000/5/conta-bancaria" \
  -H "Content-Type: application/json" \
  -d '{"numero_conta": "12345", "saldo": 1000, "debito": 200, "credito": 500}'
```

#### 6. Peso Ideal
```bash
curl -X POST "http://localhost:8000/6/peso-ideal" \
  -H "Content-Type: application/json" \
  -d '{"altura": 1.75, "sexo": "M"}'
```

#### 7. Desconto em Produto
```bash
curl -X POST "http://localhost:8000/7/desconto-produto" \
  -H "Content-Type: application/json" \
  -d '{"nome_produto": "Notebook", "quantidade": 15, "preco_unitario": 100}'
```

#### 8. Desconto em Combustível
```bash
curl -X POST "http://localhost:8000/8/desconto-combustivel" \
  -H "Content-Type: application/json" \
  -d '{"tipo_combustivel": "A", "quantidade_litros": 30}'
```

#### 9. Venda de Frutas
```bash
curl -X POST "http://localhost:8000/9/venda-frutas" \
  -H "Content-Type: application/json" \
  -d '{"quantidade_morango_kg": 6, "quantidade_maca_kg": 4}'
```

#### 10. Código de Usuário
```bash
curl -X POST "http://localhost:8000/10/codigo-usuario" \
  -H "Content-Type: application/json" \
  -d '{"codigo": 1234, "senha": "9999"}'
```

---

## 📁 Estrutura do Projeto

```
Logica_pro/
├── main.py                          # Aplicação FastAPI principal
├── requirements.txt                 # Dependências Python
├── README.md                        # Este arquivo
├── algorithms/                      # Módulo de algoritmos
│   ├── __init__.py
│   ├── macos_customizadas.py       # Algoritmo 1
│   ├── idade.py                    # Algoritmo 2
│   ├── jornada_trabalho.py         # Algoritmo 3
│   ├── comissao.py                 # Algoritmo 4
│   ├── conta_bancaria.py           # Algoritmo 5
│   ├── peso_ideal.py               # Algoritmo 6
│   ├── desconto_produto.py         # Algoritmo 7
│   ├── desconto_combustivel.py     # Algoritmo 8
│   ├── venda_frutas.py             # Algoritmo 9
│   └── codigo_usuario.py           # Algoritmo 10
└── utils/                           # Utilitários
    └── __init__.py
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+** - Linguagem de programação
- **FastAPI** - Framework web moderno
- **Pydantic** - Validação de dados
- **Uvicorn** - Servidor ASGI

---

## ✅ Validações Implementadas

Cada algoritmo implementa validações apropriadas:
- Conversão automática de tipos
- Verificação de valores válidos
- Tratamento de casos especiais
- Arredondamento de valores monetários para 2 casas decimais

---

## 📝 Notas Importantes

1. Os valores monetários são retornados com até 2 casas decimais
2. A API valida automaticamente os tipos de dados nos modelos Pydantic
3. Documentação completa disponível em `/docs` quando o servidor está rodando
4. Todos os endpoints são POST para facilitar o envio de múltiplos parâmetros

---

## 📞 Contato

**Aluno:** Bruno João da Silva  
**Matrícula:** 01193399  
**Trabalho:** Lógica de Programação - Faculdade

---

## 📄 Licença

Este trabalho é fornecido como material acadêmico para a faculdade.

---

**Última atualização:** Março 2026