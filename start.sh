#!/bin/bash
# Script para iniciar a API

echo "=========================================="
echo "Backend de Lógica de Programação"
echo "Aluno: Bruno João da Silva"
echo "Matrícula: 01193399"
echo "=========================================="
echo ""

# Verificar se Python está instalado
if ! command -v python &> /dev/null; then
    echo "❌ Python não encontrado. Por favor, instale Python 3.8+"
    exit 1
fi

echo "✓ Python encontrado: $(python --version)"

# Verificar se requirements estão instalados
echo ""
echo "Verificando dependências..."
pip list | grep -q fastapi

if [ $? -ne 0 ]; then
    echo "Instalando dependências..."
    pip install -r requirements.txt
else
    echo "✓ Dependências já instaladas"
fi

echo ""
echo "=========================================="
echo "Iniciando servidor FastAPI..."
echo "=========================================="
echo ""
echo "Aguarde... o servidor está iniciando"
echo ""
echo "✓ Quando ver 'Uvicorn running' abaixo, a API está pronta!"
echo ""
echo "Acesse em seu navegador:"
echo "  - Documentação: http://localhost:8000/docs"
echo "  - ReDoc: http://localhost:8000/redoc"
echo "  - API: http://localhost:8000"
echo ""
echo "Pressione CTRL+C para parar o servidor"
echo "=========================================="
echo ""

python main.py
