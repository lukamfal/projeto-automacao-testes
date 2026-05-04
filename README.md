# Projeto de Automação de Testes

Projeto de automação de testes desenvolvido como avaliação técnica, cobrindo testes de API REST e testes Web E2E (end-to-end).

---

## Tecnologias utilizadas

| Camada | Tecnologia |
|--------|-----------|
| Linguagem | Python 3.11 |
| Testes de API | `pytest` + `requests` |
| Testes Web | `selenium` + `webdriver-manager` |
| Design Pattern | Page Object Model (POM) |
| CI/CD | GitHub Actions |

---

## Estrutura do projeto

```
projeto_testes/
├── .github/
│   └── workflows/
│       └── ci.yml               # Pipeline de CI/CD
├── core/
│   └── api_client.py            # Cliente HTTP reutilizável
├── tests/
│   ├── conftest.py              # Fixtures compartilhadas
│   ├── api/
│   │   ├── test_pet/
│   │   │   └── test_pet_endpoints.py
│   │   ├── test_store/
│   │   │   └── test_store_endpoints.py
│   │   └── test_user/
│   │       └── test_user_endpoints.py
│   └── web/
│       ├── pages/
│       │   ├── login_page.py
│       │   ├── inventory_page.py
│       │   └── checkout_page.py
│       └── test_e2e_compra.py
├── requirements.txt
└── pytest.ini
```

---

## Como instalar e executar

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/projeto-automacao-testes.git
cd projeto-automacao-testes
```

### 2. Criar e ativar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar os testes

```bash
# Todos os testes
python -m pytest

# Somente testes de API
python -m pytest tests/api/ -v

# Somente testes Web
python -m pytest tests/web/ -v

# Gerar relatório HTML
python -m pytest --html=relatorio.html --self-contained-html
```

---

## Cenários de teste

### API — Petstore (`https://petstore.swagger.io/v2`)

**Pet:**
- Criar pet
- Buscar pet por ID
- Atualizar pet
- Buscar pets por status (available, pending, sold)
- Buscar pet inexistente (404)
- Deletar pet

**Store:**
- Consultar inventário
- Criar pedido
- Buscar pedido por ID
- Buscar pedido inexistente (404)
- Deletar pedido

**User:**
- Criar usuário
- Buscar usuário por username
- Atualizar usuário
- Login e logout
- Buscar usuário inexistente (404)
- Criar lista de usuários
- Deletar usuário

### Web E2E — SauceDemo (`https://www.saucedemo.com`)

- Fluxo completo: Login → Adicionar produtos ao carrinho → Finalizar compra

---

## CI/CD — GitHub Actions

O pipeline é executado automaticamente em todo `push` ou `pull request` para a branch `main`.

**Jobs:**
- `testes-api` — roda os testes de API no Ubuntu
- `testes-web` — roda os testes Web com Chrome headless

---

## Padrões utilizados

- **Page Object Model (POM):** cada página da aplicação web tem sua própria classe, separando a lógica de UI dos testes.
- **Fixtures do pytest:** dados e objetos compartilhados entre testes são centralizados no `conftest.py`.
- **Cliente HTTP reutilizável:** a classe `ApiClient` centraliza todas as chamadas HTTP, evitando duplicação de código.
