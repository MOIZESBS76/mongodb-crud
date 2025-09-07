# Projeto de Simulação CRUD MongoDB com Python e PyMongo

Este projeto demonstra operações básicas de CRUD (Create, Read, Update, Delete) em um banco de dados MongoDB utilizando a biblioteca `pymongo` em Python. É ideal para entender como interagir com o MongoDB de forma programática.

## Funcionalidades

- **C**reate (Criação): Inserir um ou múltiplos documentos em uma coleção.
- **R**ead (Leitura): Buscar documentos com base em critérios de consulta, com opção de projeção de campos.
- **U**pdate (Atualização): Modificar documentos existentes, individualmente ou em massa.
- **D**elete (Exclusão): Remover documentos da coleção, individualmente ou em massa.
- Tratamento básico de erros de conexão e operação.

## Tecnologias Utilizadas

- **Python 3.x**
- **PyMongo**: Driver oficial do MongoDB para Python.
- **MongoDB**: Banco de dados NoSQL. Pode ser executado localmente, via Docker, ou em serviços de nuvem como MongoDB Atlas.

## Pré-requisitos

Antes de executar este projeto, certifique-se de ter os seguintes softwares instalados:

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/) (gerenciador de pacotes do Python, geralmente vem com o Python)
- **MongoDB**:
    - [Instalação Local](https://docs.mongodb.com/manual/installation/) ou
    - [Docker Desktop](https://www.docker.com/products/docker-desktop/) (para rodar via Docker) ou
    - Uma conta no [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)

## Instalação

1.  **Clone o repositório** (ou crie os arquivos manualmente):
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```
    *(Ajuste `seu-usuario/seu-repositorio` para o seu próprio)*

2.  **Instale as dependências do Python**:
    ```bash
    pip install pymongo
    ```

## Como Executar

1.  **Inicie seu servidor MongoDB**:
    -   **Docker (recomendado para desenvolvimento):**
        ```bash
        docker run -d -p 27017:27017 --name my-mongo mongo
        ```
    -   **Localmente:** Inicie o serviço MongoDB em sua máquina.
    -   **MongoDB Atlas:** Certifique-se de que sua instância na nuvem está rodando e anote sua string de conexão.

2.  **Abra o arquivo `mongodb_crud.py`**:
    -   Se você estiver usando uma string de conexão diferente (por exemplo, do MongoDB Atlas), atualize a linha no bloco `if __name__ == "__main__":`:
        ```python
        # Altere esta linha para sua URI se não for local
        manager = MongoDBManager(uri="mongodb+srv://<user>:<password>@<cluster-url>/", db_name="mydatabase", collection_name="mycollection")
        ```
        Certifique-se de substituir `<user>`, `<password>` e `<cluster-url>` pelos seus dados reais.

3.  **Execute o script Python**:
    ```bash
    python mongodb_crud.py
    ```

Você verá a saída das operações CRUD no console, demonstrando a interação com o banco de dados.

## Estrutura do Código

O código está organizado na classe `MongoDBManager` para facilitar a reutilização e modularidade.

-   **`MongoDBManager.__init__(uri, db_name, collection_name)`**: Conecta ao MongoDB.
-   **`create_document(document)`**: Insere um documento.
-   **`create_many_documents(documents)`**: Insere uma lista de documentos.
-   **`read_documents(query=None, projection=None)`**: Busca documentos.
-   **`update_document(query, new_values, multi=False)`**: Atualiza documentos.
-   **`delete_document(query, multi=False)`**: Deleta documentos.
-   **`close_connection()`**: Fecha a conexão.

O bloco `if __name__ == "__main__":` contém um exemplo completo de uso de cada uma dessas operações.

## Contribuição

Sinta-se à vontade para fazer um fork deste repositório, propor melhorias ou adicionar novas funcionalidades.

## Licença

Este projeto está sob a licença MIT. 