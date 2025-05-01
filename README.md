# 📊 Dashboard de Dados Financeiros com Backend em Python

Este repositório apresenta o desenvolvimento de um sistema web completo para visualização e análise de dados financeiros de instituições financeiras. A aplicação foi elaborada utilizando Python, Streamlit e Dash, com backend estruturado, banco de dados e ingestão automatizada de dados via APIs.

---

## ✅ Escopo da Solução

A aplicação desenvolvida é um **MVP de dashboard interativo**, com backend e frontend, ingestão de dados financeiros, autenticação de usuários, banco de dados relacional e visualização de KPIs.

- Permite a tomada de decisões com base em dados reais do mercado.
- Atende ao objetivo 8 dos Objetivos de Desenvolvimento Sustentável (ODS).
- Foi construída inteiramente em Python, tecnologia amplamente utilizada em análise de dados.
- Está pronta para futura integração com outras soluções, como chatbots e sistemas mobile.

---

## 🧰 Tecnologias Utilizadas

| Camada                 | Ferramentas / Bibliotecas                                      |
|------------------------|---------------------------------------------------------------|
| **Frontend Web**       | Streamlit, Dash                                               |
| **Backend**            | Python (pandas, requests, SQLAlchemy, authlib)                |
| **Banco de Dados**     | SQLite (local) ou PostgreSQL (produção)                       |
| **APIs Externas**      | Banco Central, B3, Tesouro Direto (via REST)                  |
| **Testes**             | pytest, requests-mock                                         |
| **Deploy / CI-CD**     | Docker, GitHub Actions                                        |

---

## 🏗️ Arquitetura do Sistema (Modelo C4)

### 🔹 Nível 1 – Diagrama de Contexto

**Usuários** acessam o **Dashboard Web** para visualizar informações financeiras obtidas de **APIs externas**, processadas pelo **backend Python**, e armazenadas em um **banco de dados relacional**.

### 🔹 Nível 2 – Diagrama de Containers

```
[Usuário] → [Frontend: Streamlit/Dash]
                   ↓            ↑
             [Backend: ETL, Analytics, Auth]
                   ↓            ↑
         [Banco de Dados Relacional] ← [APIs Externas]
```

### 🔹 Nível 3 – Componentes

- **database.py**: conexão e definição de schema com SQLAlchemy
- **etl.py**: coleta, transformação e carga de dados (ETL)
- **analytics.py**: funções de cálculo de indicadores (média móvel, variação percentuais)
- **auth.py**: autenticação de usuários (JWT/OAuth2)
- **app.py / frontend.py**: aplicação web com Streamlit ou Dash
- **tests/**: casos de teste para ETL e analytics

---

## 📋 Requisitos Funcionais

- [x] Visualizar indicadores financeiros atualizados
- [x] Ingestão automática de dados via API
- [x] Autenticação de usuários
- [x] Banco de dados persistente
- [x] Filtros interativos (data, símbolo, intervalo)

---

## 🧾 Histórias de Usuário

| ID    | História                                                                 |
|-------|--------------------------------------------------------------------------|
| HU01  | Como analista, desejo acessar gráficos de mercado para tomar decisões    |
| HU02  | Como gestor, desejo exportar relatórios em PDF para reuniões             |
| HU03  | Como usuário, desejo filtrar dados por período, símbolo e intervalo      |
| HU04  | Como usuário autenticado, desejo ver dados privados de minha instituição |

---

## 🔄 Processo de Desenvolvimento Ágil

Metodologia **SCRUM**, com sprints quinzenais:

- **Sprint 1**: Elicitação de requisitos e modelagem inicial
- **Sprint 2**: Desenvolvimento do backend e ingestão de dados (ETL)
- **Sprint 3**: Criação do frontend e visualizações (TP3)
- **Sprint 4**: Testes, autenticação, deploy e documentação

---

## 🧪 Testes

- **pytest** e **requests-mock** para validar o fluxo ETL e cálculos de indicadores
- Cobertura mínima de 70% nas camadas ETL e analytics

---

## 🐳 Gerência de Configuração

- Versionamento via **Git + GitHub**
- Branches: `main`, `dev`, `feature/*`, `hotfix/*`
- CI pelo GitHub Actions (`.github/workflows/ci.yml`): instalação de dependências, execução de testes e lint
- Deploy via Docker em ambientes como Render ou AWS

---

## ⚙️ Instalação e Inicialização

```bash
# 1) Clone o repositório
git clone https://github.com/mtuliodev/Dash-ENGSOFTWARE.git
autcd Dash-ENGSOFTWARE

# 2) Crie o ambiente virtual
python -m venv venv
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\\Scripts\\activate

# 3) Instale as dependências
pip install -r requirements.txt
```

### Variáveis de ambiente (opcional)
- `DATABASE_URL` (ex.: `sqlite:///data.db`)
- `API_URL` (ex.: `https://api.exemplo.com/market`)

---

## 📂 Estrutura de Código 

- `database.py`: conexão e schema via SQLAlchemy
- `etl.py`: fetch, transform e load de dados na tabela `market_data`
- `analytics.py`: cálculo de KPIs (média móvel, pct change)
- `app.py / frontend.py`: dashboard web em Streamlit ou Dash
- `tests/`
  - `test_etl.py`: testes de ETL com mocks
  - `test_analytics.py`: testes de funções analytics

---

## 🚀 Comandos Principais

```bash
# Inicializar o banco de dados
python database.py

# Executar pipeline ETL (ex.: ticker ABC)
python etl.py ABC

# Rodar testes unitários
pytest --disable-warnings -q

# Iniciar dashboard
streamlit run app.py
# ou para frontend.py (Streamlit)
streamlit run frontend.py
```

---

## 🔧 Integração Contínua

O arquivo `.github/workflows/ci.yml` executa:
1. Configuração do ambiente Python
2. Instalação de dependências (`requirements.txt`)
3. Execução de `pytest` e lint (`flake8`)

Adicione o badge de status do workflow no topo do README:

```md
![CI](https://github.com/mtuliodev/Dash-ENGSOFTWARE/actions/workflows/ci.yml/badge.svg)
```

