# 📊 Dashboard de Dados Financeiros com Backend em Python

Este repositório apresenta o desenvolvimento de um sistema web completo para visualização e análise de dados financeiros de instituições financeiras. A aplicação foi elaborada utilizando Python, Streamlit e Dash, com backend estruturado, banco de dados e ingestão automatizada de dados via APIs.

---

## ✅ Escopo da Solução

A aplicação desenvolvida é um **dashboard de dados interativo**, com backend e frontend, ingestão de dados financeiros, autenticação de usuários, banco de dados relacional e visualização de KPIs.

A solução foi escolhida por:

- Possibilitar a tomada de decisões com base em dados reais do mercado;
- Atende ao objetivo 8 dos Objetivos de Desenvolvimento Sustentável (ODS).
- Ser totalmente construída em Python, tecnologia amplamente utilizada em análise de dados;
- Permitir integração com outras soluções, como chatbots e sistemas mobile futuramente.

---

## 🧰 Tecnologias Utilizadas

| Camada                 | Ferramentas / Bibliotecas                                      |
|------------------------|---------------------------------------------------------------|
| **Frontend Web**       | [Streamlit](https://streamlit.io), [Dash](https://dash.plotly.com) |
| **Backend**            | Python (pandas, plotly, requests, authlib)                    |
| **Banco de Dados**     | SQLite (local) ou PostgreSQL (produção)                       |
| **APIs Externas**      | Banco Central, B3, Tesouro Direto                             |
| **Testes**             | `pytest`, `unittest`                                          |
| **Deploy / CI-CD**     | Docker, GitHub Actions, Render                                |

---

## 🏗️ Arquitetura do Sistema (Modelo C4)

### 🔹 Nível 1 – Diagrama de Contexto

**Usuários** acessam o **Dashboard Web** para visualizar informações financeiras obtidas de **APIs externas**, processadas por um **backend em Python**, e armazenadas em um **banco de dados relacional**.

[Usuário] | v [Dashboard Web] | v [Backend Python] ---> [APIs Públicas] | v [Banco de Dados Relacional]


---

### 🔹 Nível 2 – Diagrama de Containers

[Usuário] | v [Frontend: Streamlit/Dash] ------------------------+ | | v v [Backend Python: lógica de negócio, ETL, auth] --> [APIs externas] | v [Database: SQLite/PostgreSQL]


**Descrição dos containers:**

- **Frontend (Streamlit ou Dash)**: Interface gráfica interativa para o usuário final.
- **Backend**: Scripts de ingestão de dados, autenticação de usuários, lógica de análise.
- **APIs**: Fornecem dados brutos financeiros (BACEN, B3, etc).
- **Banco de Dados**: Armazena dados históricos para acesso rápido e análises.

---

### 🔹 Nível 3 – Componentes

**Componentes principais:**

- `frontend.py`: Interface de usuário (UI/UX)
- `auth.py`: Autenticação e controle de acesso
- `etl.py`: Coleta e transformação de dados
- `analytics.py`: Indicadores e gráficos
- `database.py`: Conexão com o banco de dados
- `tests/`: Testes unitários para os componentes principais

---

## 📋 Requisitos Funcionais

- [x] Visualizar indicadores financeiros atualizados
- [x] Ingestão automática de dados via API
- [x] Autenticação de usuários
- [x] Banco de dados persistente
- [x] Filtros interativos (data, setor, tipo de ativo)

---

## 🧾 Histórias de Usuário

| ID    | História                                                                 |
|-------|--------------------------------------------------------------------------|
| HU01  | Como analista, desejo acessar gráficos de mercado para tomar decisões    |
| HU02  | Como gestor, desejo exportar relatórios em PDF para reuniões             |
| HU03  | Como usuário, desejo filtrar dados por período, tipo de ativo e setor    |
| HU04  | Como usuário autenticado, desejo ver dados privados de minha instituição |

---

## 🔄 Processo de Desenvolvimento Ágil

Utilizou-se metodologia **SCRUM**, com sprints quinzenais:

- **Sprint 1**: Elicitação de requisitos e modelagem inicial
- **Sprint 2**: Desenvolvimento do backend e ingestão de dados
- **Sprint 3**: Criação do frontend e visualizações
- **Sprint 4**: Testes, autenticação, deploy e documentação

---

## 🧪 Testes

- `pytest` e `unittest` para módulos ETL, autenticação e análise
- Testes manuais de interface com diferentes navegadores e inputs
- Verificação de performance e consistência de dados

---

## 🐳 Gerência de Configuração

- Versionamento via `Git + GitHub`
- Deploy contínuo com `Docker` e `GitHub Actions`
- Ambientes virtuais com `venv`
- Organização por branches: `main`, `dev`, `feature/*`, `hotfix/*`

---

## ⚙️ Como Executar Localmente

# Clone o repositório
git clone https://github.com/seu-usuario/dashboard-financeiro.git
cd dashboard-financeiro

# Crie o ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
streamlit run frontend.py
# ou, para Dash:
python app.py

## Estrutura

📦 dashboard-financeiro/
├── app.py / frontend.py
├── etl.py
├── auth.py
├── analytics.py
├── database.py
├── tests/
├── requirements.txt
├── README.md
└── .github/
    └── workflows/
