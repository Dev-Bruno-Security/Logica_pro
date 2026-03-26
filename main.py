"""
Backend com FastAPI - Lógica de Programação
Trabalho acadêmico - Matrícula: 01193399 - Bruno João da Silva
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Importar todos os algoritmos
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

# Criar aplicação FastAPI
app = FastAPI(
    title="API de Lógica de Programação",
    description="Backend com 10 algoritmos - Trabalho da Faculdade",
    version="1.0.0",
    contact={
        "name": "Bruno João da Silva",
        "email": "bruno@example.com"
    }
)

# ===================== MODELOS PYDANTIC =====================

class MacosCustomizadasRequest(BaseModel):
    quantidade: int

class IdadeRequest(BaseModel):
    ano_atual: int
    ano_nascimento: int

class JornadaTrabalhoRequest(BaseModel):
    horas_trabalhadas_mes: float
    valor_hora_regular: float

class ComissaoRequest(BaseModel):
    salario_fixo: float
    valor_vendas: float

class ContaBancariaRequest(BaseModel):
    numero_conta: str
    saldo: float
    debito: float
    credito: float

class PesoIdealRequest(BaseModel):
    altura: float
    sexo: str

class DescontoProductRequest(BaseModel):
    nome_produto: str
    quantidade: int
    preco_unitario: float

class DescontoCombustivelRequest(BaseModel):
    tipo_combustivel: str
    quantidade_litros: float

class VendaFrutasRequest(BaseModel):
    quantidade_morango_kg: float
    quantidade_maca_kg: float

class CodigoUsuarioRequest(BaseModel):
    codigo: int
    senha: Optional[str] = None

# ===================== ROTAS / ENDPOINTS =====================

@app.get("/", tags=["Info"])
async def root():
    """Informações sobre a API"""
    return {
        "titulo": "API de Lógica de Programação",
        "aluno": "Bruno João da Silva",
        "matricula": "01193399",
        "instituicao": "Trabalho da Faculdade",
        "endpoints": [
            "/docs - Documentação interativa (Swagger UI)",
            "/1/macos-customizadas",
            "/2/idade",
            "/3/jornada-trabalho",
            "/4/comissao",
            "/5/conta-bancaria",
            "/6/peso-ideal",
            "/7/desconto-produto",
            "/8/desconto-combustivel",
            "/9/venda-frutas",
            "/10/codigo-usuario"
        ]
    }

# Algoritmo 1: Maçãs Customizadas
@app.post("/1/macos-customizadas", tags=["Algoritmos"])
async def macos_customizadas(request: MacosCustomizadasRequest):
    """
    **Algoritmo 1: Maçãs Customizadas**
    
    Maçãs custom custam R$1,30 cada se compradas menos de uma dúzia.
    Se compradas pelo menos 12, custam R$1,00 cada.
    """
    return calcular_macos_customizadas(request.quantidade)

# Algoritmo 2: Idade
@app.post("/2/idade", tags=["Algoritmos"])
async def idade(request: IdadeRequest):
    """
    **Algoritmo 2: Cálculo de Idade**
    
    Lê o ano atual e o ano de nascimento. Determina se pode votar (18+).
    """
    return calcular_idade(request.ano_atual, request.ano_nascimento)

# Algoritmo 3: Jornada de Trabalho
@app.post("/3/jornada-trabalho", tags=["Algoritmos"])
async def jornada_trabalho(request: JornadaTrabalhoRequest):
    """
    **Algoritmo 3: Jornada de Trabalho**
    
    Calcula salário com horas extras (50% acréscimo após 40h/semana).
    Considera o mês com 4 semanas exatas (160 horas normais).
    """
    return calcular_jornada_trabalho(request.horas_trabalhadas_mes, request.valor_hora_regular)

# Algoritmo 4: Comissão de Vendas
@app.post("/4/comissao", tags=["Algoritmos"])
async def comissao(request: ComissaoRequest):
    """
    **Algoritmo 4: Comissão de Vendas**
    
    Calcula comissão: 3% até R$1.500 + 5% no que exceder.
    Retorna salário total (fixo + comissão).
    """
    return calcular_comissao(request.salario_fixo, request.valor_vendas)

# Algoritmo 5: Conta Bancária
@app.post("/5/conta-bancaria", tags=["Algoritmos"])
async def conta_bancaria(request: ContaBancariaRequest):
    """
    **Algoritmo 5: Conta Bancária**
    
    Calcula saldo final: saldo - débito + crédito.
    Identifica se é saldo positivo ou negativo.
    """
    return calcular_conta_bancaria(request.numero_conta, request.saldo, request.debito, request.credito)

# Algoritmo 6: Peso Ideal
@app.post("/6/peso-ideal", tags=["Algoritmos"])
async def peso_ideal(request: PesoIdealRequest):
    """
    **Algoritmo 6: Peso Ideal**
    
    Calcula peso ideal por sexo:
    - Masculino: (72.7 * altura) - 58
    - Feminino: (62.1 * altura) - 44.7
    """
    return calcular_peso_ideal(request.altura, request.sexo)

# Algoritmo 7: Desconto em Produto
@app.post("/7/desconto-produto", tags=["Algoritmos"])
async def desconto_produto(request: DescontoProductRequest):
    """
    **Algoritmo 7: Desconto em Produto**
    
    Aplicar desconto por quantidade:
    - < 5: 2%
    - 5-10: 3%
    - >= 10: 5%
    """
    return calcular_desconto_produto(request.nome_produto, request.quantidade, request.preco_unitario)

# Algoritmo 8: Desconto em Combustível
@app.post("/8/desconto-combustivel", tags=["Algoritmos"])
async def desconto_combustivel(request: DescontoCombustivelRequest):
    """
    **Algoritmo 8: Desconto em Combustível**
    
    Preços e descontos:
    - Álcool (R$2.90): até 20L=3%, acima=5%
    - Gasolina (R$3.30): até 20L=4%, acima=6%
    """
    return calcular_desconto_combustivel(request.tipo_combustivel, request.quantidade_litros)

# Algoritmo 9: Venda de Frutas
@app.post("/9/venda-frutas", tags=["Algoritmos"])
async def venda_frutas(request: VendaFrutasRequest):
    """
    **Algoritmo 9: Venda de Frutas**
    
    Preços:
    - Morango: até 5kg=R$2.50, acima=R$2.20
    - Maçã: até 5kg=R$1.80, acima=R$1.50
    - Desconto 10% se total > R$25
    """
    return calcular_venda_frutas(request.quantidade_morango_kg, request.quantidade_maca_kg)

# Algoritmo 10: Código de Usuário
@app.post("/10/codigo-usuario", tags=["Algoritmos"])
async def codigo_usuario(request: CodigoUsuarioRequest):
    """
    **Algoritmo 10: Validação de Código de Usuário**
    
    Código correto: 1234
    Senha correta: 9999
    Valida se código <= 9999 e verifica senha.
    """
    return validar_codigo_usuario(request.codigo, request.senha)

# ===================== TRATAMENTO DE ERROS =====================

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Tratador global de exceções"""
    return {
        "erro": "Erro no processamento",
        "detalhes": str(exc)
    }

# Pode ser executado com: uvicorn main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
