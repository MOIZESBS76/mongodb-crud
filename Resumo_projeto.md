'''# Projeto: Operaçõeses CRUD com MongoDB em Python

Este repositório contem um exemplo de script Python (`mongodb_crud.py`) que demonstra as operaçõeses básicas conforme solicitado:
Criar um código python que simule as operações de CRUD(CREATE, READ, UPDATE, DELETE) no mongodb, local, docker ou nuvem.

---

O que foi feito neste projeto?

Este projeto foi configurado do zero para garantir um historico Git limpo e organizado no GitHub. O processo envolveu os seguintes passos principais:

1.  Limpeza do Repositório Local:
    A pasta oculta `.git` (que continha o histórico Git anterior e problemático) foi excluída do diretório local do projeto. Isso efetivamente "desvinculou" o projeto local de qualquer repositório Git existente, permitindo um novo começo. (isso foi difícil)

2.  Inicializaçãoo de um Novo Repositório Git Local:
    Um novo repositório Git foi inicializado na pasta do projeto local (`Atividade_P1`). Isso criou um novo controle de versão para o projeto a partir daquele ponto.

3.  Criação e Vinculação ao Repositório no GitHub:**
    *   Um novo repositório vazio foi criado no GitHub.
    *   O repositório Git local recém-criado foi vinculado a este novo repositório remoto no GitHub.

4.  Configuração de `.gitignore`:
    Devido aparecer arquivos indesejados, um arquivo ".gitignore" foi criado e configurado. Este arquivo é crucial para excluir do controle de versão arquivos e pastas que não devem ser enviados para o GitHub, como:
        A pasta do ambiente virtual (`venv/`).
        Arquivos de cache do Python (`__pycache__`, `*.pyc`).
        Arquivos temporários ou de documentos (`*.docx`, `*.pdf`, etc.).
        Isso mantém o repositório limpo, focando apenas no código-fonte essencial.

5.  Primeiro Commit e Envio para o GitHub:
    Os arquivos do projeto (`mongodb_crud.py`, `README.md`, e o próprio `.gitignore`) foram adicionados ao controle de versão e um commit inicial foi realizado.
    Finalmente, todas as mudanças locais foram enviadas (push) para o repositório no GitHub, tornando o projeto visível e versionado corretamente.

---

## Como rodar o código `mongodb_crud.py`

Para executar o script e ver as operações CRUD em ação, siga estes passos:

1.  Certifique-se de que o MongoDB Server está rodando
    O script Python se conecta a uma instância do MongoDB. Inicie seu servidor MongoDB (ex: usando `mongod` em um terminal separado, ou garantindo que o serviço MongoDB esteja ativo).

2.  Navegue até o diretório do projeto:
    ```bash
    cd C:\Moizes\Faculdade\Vassouras\5º PERIODO\Banco de Dados Não Relacionais\Atividade_P1
    ```

3.  Ative o ambiente virtual:
    ```bash
    .\venv\Scripts\activate
    ```
    (Você verá `(venv)` no início da sua linha de comando).

4.  Instale as dependências:
    O script usa `pymongo` para interagir com o MongoDB.
    ```bash
    pip install pymongo
    ```

5.  Execute o script Python:
    ```bash
    python mongodb_crud.py
    ```

Ao executar, o script se conectará ao seu MongoDB local (padronizado para `mongodb://localhost:27017/`), realizará uma série de operações de criação, leitura, atualização e exclusão em uma coleção (`mycollection`) dentro de um banco de dados (`mydatabase`), e exibirá os resultados no terminal.

---

Tecnologias Utilizadas

*   **Python:** Linguagem de programação principal.
*   **MongoDB:** Banco de dados NoSQL para armazenamento dos dados.
*   **PyMongo:** Driver oficial do Python para interagir com o MongoDB.
*   **Git & GitHub:** Sistema de controle de versão e plataforma para hospedagem do código.
'''