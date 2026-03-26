# 📋 Sumário de Arquivos do Projeto

## Aluno: Bruno João da Silva | Matrícula: 01193399

---

## 📁 Estrutura de Pastas

```
Logica_pro/
├── algorithms/          # Módulo principal com todos os algoritmos
├── utils/               # Utilitários (expansível para futuro)
└── [arquivos raiz]      # Configuração e aplicação principal
```

---

## 📄 Descrição de Cada Arquivo

### 🔧 **Configuração e Execução**

| Arquivo | Tipo | Descrição |
|---------|------|-----------|
| `main.py` | Python | 🔴 **PRINCIPAL** - Aplicação FastAPI com todos os 10 endpoints REST |
| `config.py` | Python | Arquivo com constantes e configurações (preços, porcentagens, limites) |
| `requirements.txt` | TXT | Dependências do projeto (FastAPI, Pydantic, Uvicorn) |
| `start.sh` | Shell | Script executável para iniciar o servidor rapidamente |

### 📚 **Documentação**

| Arquivo | Descrição |
|---------|-----------|
| `README.md` | Documentação completa e detalhada do projeto |
| `QUICKSTART.md` | Guia rápido para começar em 2 minutos |
| `FILES.md` | Este arquivo - descrição de todos os arquivos |

### 🧮 **Módulos de Algoritmos** (`algorithms/`)

| Arquivo | Algoritmo | Descrição |
|---------|-----------|-----------|
| `macos_customizadas.py` | #1 | Cálculo de preço com desconto por quantidade |
| `idade.py` | #2 | Cálculo de idade e validação para voto |
| `jornada_trabalho.py` | #3 | Cálculo de salário com horas extras |
| `comissao.py` | #4 | Cálculo de comissão sobre vendas |
| `conta_bancaria.py` | #5 | Cálculo de saldo e status da conta |
| `peso_ideal.py` | #6 | Cálculo de peso ideal por sexo e altura |
| `desconto_produto.py` | #7 | Cálculo de desconto progressivo em produto |
| `desconto_combustivel.py` | #8 | Cálculo de desconto em combustível |
| `venda_frutas.py` | #9 | Cálculo de preço de frutas com desconto |
| `codigo_usuario.py` | #10 | Validação de código e senha de usuário |

### ✅ **Testes**

| Arquivo | Descrição |
|---------|-----------|
| `test_algorithms.py` | Testes unitários de todos os 10 algoritmos (sem servidor) |
| `test_api.py` | Testes HTTP dos endpoints da API (requer servidor rodando) |

### 📦 **Utilitários** (`utils/`)

| Arquivo | Descrição |
|---------|-----------|
| `__init__.py` | Inicializador do pacote utils |

### 🚫 **Ignorar**

| Arquivo | Descrição |
|---------|-----------|
| `.gitignore` | Arquivo para git ignorar pastas/arquivos de desenvolvimento |

---

## 🎯 Fluxo de Uso Recomendado

### 1️⃣ **Primeiro Acesso**
- Leia o `README.md` para entender o projeto
- Verifique o `QUICKSTART.md` para instruções rápidas

### 2️⃣ **Validar Localmente** (sem servidor)
```bash
python test_algorithms.py
```
Isso testa todos os 10 algoritmos diretamente em Python.

### 3️⃣ **Iniciar o Servidor**
```bash
python main.py
# ou
./start.sh
```

### 4️⃣ **Testar via API**
- Acesse http://localhost:8000/docs (Swagger UI)
- Ou execute `python test_api.py`

---

## 📊 Quantidade de Linhas de Código

| Arquivo | Linhas | Tipo |
|---------|--------|------|
| `main.py` | ~250 | Aplicação |
| `test_algorithms.py` | ~120 | Testes |
| Algoritmos (10 arquivos) | ~700 | Lógica |
| `config.py` | ~60 | Configuração |
| Documentação (3 arquivos) | ~500+ | Markdown |
| **TOTAL** | **~1.630** | **Linhas** |

---

## 🔄 Modificar ou Estender

O projeto está estruturado para facilitar:

- **Adicionar novo algoritmo:** Criar novo arquivo em `algorithms/`, implementar função, adicionar endpoint em `main.py`
- **Mudar preços/fatores:** Editar `config.py`
- **Adicionar testes:** Expandir `test_algorithms.py` ou `test_api.py`

---

## 🌐 Endpoints Disponíveis

Quando o servidor estiver rodando, todos esses pertencem ao `main.py`:

| # | Endpoint | Método |
|---|----------|--------|
| - | `/` | GET |
| 1 | `/1/macos-customizadas` | POST |
| 2 | `/2/idade` | POST |
| 3 | `/3/jornada-trabalho` | POST |
| 4 | `/4/comissao` | POST |
| 5 | `/5/conta-bancaria` | POST |
| 6 | `/6/peso-ideal` | POST |
| 7 | `/7/desconto-produto` | POST |
| 8 | `/8/desconto-combustivel` | POST |
| 9 | `/9/venda-frutas` | POST |
| 10 | `/10/codigo-usuario` | POST |

---

## 👤 Metadados do Projeto

```
Nome:           Backend de Lógica de Programação
Aluno:          Bruno João da Silva
Matrícula:      01193399
Tipo:           Trabalho Acadêmico
Instituição:    Faculdade
Data:           Março 2026
Linguagem:      Python 3.8+
Framework:      FastAPI
BD:             N/A (Estado em memória)
Deploy:         Requer Python + pip
```

---

## ✨ Características Principais

✅ **10 Algoritmos Implementados** conforme especificação
✅ **API REST** com FastAPI (framework moderno e rápido)
✅ **Documentação Automática** via Swagger UI
✅ **Validação de Dados** com Pydantic
✅ **Testes Inclusos** (unitários e HTTP)
✅ **Código Bem Estruturado** e documentado
✅ **Fácil de Estender** e modificar
✅ **Informações do Aluno** incluídas em todo projeto

---

**Última atualização:** Março 2026
