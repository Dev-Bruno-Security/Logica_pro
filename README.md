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
  Backend de Lógica de Programação
  Informações do Aluno
  Nome: Bruno João da Silva
  Matrícula: 01193399
  Atividade: Comando condicionais.
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