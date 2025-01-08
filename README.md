# Projeto Django CRUD de Pessoas com Autenticação de Usuário

Este projeto Django demonstra um CRUD (Create, Read, Update, Delete) completo para gerenciamento de pessoas, com um sistema de autenticação de usuário integrado.
## Funcionalidades

*   **CRUD de Pessoas:** Permite criar, visualizar, editar e excluir registros de pessoas.
*   **Autenticação de Usuário:** Implementa um sistema de login e registro de usuários, protegendo o acesso às funcionalidades administrativas.


## Pré-requisitos

*   Python instalado (versão 3.7 ou superior recomendada)
*   Pip instalado (gerenciador de pacotes do Python)
*   Ambiente virtual Python (recomendado)

## Instalação

1.  **Clone o repositório:**

    ```bash
    git clone [URL inválido removido]
    cd seu_repositorio
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**

    ```bash
    python -m venv venv  # Cria o ambiente virtual
    venv\Scripts\activate  # Ativa no Windows
    source venv/bin/activate  # Ativa no Linux/macOS
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure o banco de dados:**

    Edite o arquivo `settings.py` do seu projeto Django para configurar as informações de conexão com o banco de dados.

5.  **Crie as migrações:**

    ```bash
    python manage.py makemigrations
    ```

6.  **Aplique as migrações:**

    ```bash
    python manage.py migrate
    ```

7.  **Crie um superusuário (para acessar o painel administrativo):**

    ```bash
    python manage.py createsuperuser
    ```

8.  **Inicie o servidor de desenvolvimento:**

    ```bash
    python manage.py runserver
    ```

9.  **Acesse a aplicação no seu navegador:**

    ```
    http://127.0.0.1:8000/
    ```