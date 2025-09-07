import pymongo
from pymongo.errors import ConnectionFailure, OperationFailure

class MongoDBManager:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="mydatabase", collection_name="mycollection"):
        """
        Inicializa o gerenciador MongoDB.
        :param uri: String de conexão URI para o MongoDB.
        :param db_name: Nome do banco de dados a ser usado.
        :param collection_name: Nome da coleção a ser usada.
        """
        self.uri = uri
        self.db_name = db_name
        self.collection_name = collection_name
        self.client = None
        self.db = None
        self.collection = None
        self._connect()

    def _connect(self):
        """Tenta conectar ao MongoDB."""
        try:
            self.client = pymongo.MongoClient(self.uri)
            self.client.admin.command('ping') # Verifica a conexão
            self.db = self.client[self.db_name]
            self.collection = self.db[self.collection_name]
            print(f"Conectado ao MongoDB: {self.uri}, Database: {self.db_name}, Coleção: {self.collection_name}")
        except ConnectionFailure as e:
            print(f"Erro de conexão com o MongoDB: {e}")
            self.client = None
            self.db = None
            self.collection = None
        except Exception as e:
            print(f"Um erro inesperado ocorreu durante a conexão: {e}")
            self.client = None
            self.db = None
            self.collection = None

    def close_connection(self):
        """Fecha a conexão com o MongoDB."""
        if self.client:
            self.client.close()
            print("Conexão com o MongoDB fechada.")

    def create_document(self, document):
        """
        Insere um único documento na coleção.
        :param document: O documento a ser inserido (dicionário Python).
        :return: O ID do documento inserido, ou None em caso de falha.
        """
        if self.collection is None:
            print("Não foi possível realizar a operação: conexão com o MongoDB não estabelecida.")
            return None
        try:
            result = self.collection.insert_one(document)
            print(f"Documento inserido com ID: {result.inserted_id}")
            return result.inserted_id
        except OperationFailure as e:
            print(f"Erro ao inserir documento: {e}")
            return None
        except Exception as e:
            print(f"Erro inesperado ao inserir documento: {e}")
            return None

    def create_many_documents(self, documents):
        """
        Insere múltiplos documentos na coleção.
        :param documents: Uma lista de documentos a serem inseridos.
        :return: Uma lista de IDs dos documentos inseridos, ou uma lista vazia em caso de falha.
        """
        if self.collection is None:
            print("Não foi possível realizar a operação: conexão com o MongoDB não estabelecida.")
            return []
        try:
            result = self.collection.insert_many(documents)
            print(f"Múltiplos documentos inseridos com IDs: {result.inserted_ids}")
            return result.inserted_ids
        except OperationFailure as e:
            print(f"Erro ao inserir múltiplos documentos: {e}")
            return []
        except Exception as e:
            print(f"Erro inesperado ao inserir múltiplos documentos: {e}")
            return []

    def read_documents(self, query=None, projection=None):
        """
        Lê documentos da coleção.
        :param query: Um dicionário de consulta para filtrar documentos (opcional).
        :param projection: Um dicionário para especificar campos a incluir/excluir (opcional).
        :return: Uma lista de documentos encontrados.
        """
        if self.collection is None:
            print("Não foi possível realizar a operação: conexão com o MongoDB não estabelecida.")
            return []
        if query is None:
            query = {}
        try:
            documents = list(self.collection.find(query, projection))
            print(f"Documentos encontrados ({len(documents)}):")
            for doc in documents:
                print(doc)
            return documents
        except OperationFailure as e:
            print(f"Erro ao ler documentos: {e}")
            return []
        except Exception as e:
            print(f"Erro inesperado ao ler documentos: {e}")
            return []

    def update_document(self, query, new_values, multi=False):
        """
        Atualiza documentos na coleção.
        :param query: Dicionário de consulta para encontrar documentos.
        :param new_values: Dicionário com os novos valores a serem definidos (use operadores como '$set').
        :param multi: Se True, atualiza múltiplos documentos; se False, atualiza apenas um.
        :return: Número de documentos modificados, ou None em caso de falha.
        """
        if self.collection is None:
            print("Não foi possível realizar a operação: conexão com o MongoDB não estabelecida.")
            return None
        try:
            if multi:
                result = self.collection.update_many(query, new_values)
                print(f"{result.modified_count} documento(s) atualizado(s).")
            else:
                result = self.collection.update_one(query, new_values)
                print(f"Documento atualizado. Correspondências: {result.matched_count}, Modificados: {result.modified_count}")
            return result.modified_count
        except OperationFailure as e:
            print(f"Erro ao atualizar documento(s): {e}")
            return None
        except Exception as e:
            print(f"Erro inesperado ao atualizar documento(s): {e}")
            return None

    def delete_document(self, query, multi=False):
        """
        Deleta documentos da coleção.
        :param query: Dicionário de consulta para encontrar documentos a serem deletados.
        :param multi: Se True, deleta múltiplos documentos; se False, deleta apenas um.
        :return: Número de documentos deletados, ou None em caso de falha.
        """
        if self.collection is None:
            print("Não foi possível realizar a operação: conexão com o MongoDB não estabelecida.")
            return None
        try:
            if multi:
                result = self.collection.delete_many(query)
                print(f"{result.deleted_count} documento(s) deletado(s).")
            else:
                result = self.collection.delete_one(query)
                print(f"Documento deletado. Total deletado: {result.deleted_count}")
            return result.deleted_count
        except OperationFailure as e:
            print(f"Erro ao deletar documento(s): {e}")
            return None
        except Exception as e:
            print(f"Erro inesperado ao deletar documento(s): {e}")
            return None

if __name__ == "__main__":
    # Exemplo de uso:
    # Para usar o MongoDB Atlas ou outra URL, altere a string de conexão:
    # manager = MongoDBManager(uri="mongodb+srv://<user>:<password>@<cluster-url>/", db_name="mydatabase", collection_name="mycollection")
    manager = MongoDBManager() # Conecta-se a mongodb://localhost:27017/ por padrão

    if manager.collection is not None: # Verifica se a conexão foi bem-sucedida
        print("\n--- TESTE DE OPERAÇÕES CRUD ---")

        # --- CREATE ---
        print("\n1. Criando um documento:")
        doc1_id = manager.create_document({"nome": "Alice", "idade": 30, "cidade": "São Paulo"})
        manager.create_document({"nome": "Bob", "idade": 25, "cidade": "Rio de Janeiro"})
        manager.create_document({"nome": "Charlie", "idade": 35, "cidade": "Belo Horizonte"})

        print("\n2. Criando múltiplos documentos:")
        new_users = [
            {"nome": "David", "idade": 28, "cidade": "São Paulo", "email": "david@example.com"},
            {"nome": "Eve", "idade": 22, "cidade": "Curitiba", "email": "eve@example.com"}
        ]
        manager.create_many_documents(new_users)

        # --- READ ---
        print("\n3. Lendo todos os documentos:")
        manager.read_documents()

        print("\n4. Lendo documentos com filtro (cidade: São Paulo):")
        manager.read_documents({"cidade": "São Paulo"})

        print("\n5. Lendo documentos com filtro (idade > 25):")
        manager.read_documents({"idade": {"$gt": 25}}) # $gt significa "greater than" (maior que)

        print("\n6. Lendo documentos com projeção (apenas nome e cidade):")
        manager.read_documents({}, {"nome": 1, "cidade": 1, "_id": 0}) # _id: 0 para excluir o ID

        # --- UPDATE ---
        print("\n7. Atualizando um documento (Alice para 31 anos):")
        manager.update_document({"nome": "Alice"}, {"$set": {"idade": 31}})
        manager.read_documents({"nome": "Alice"})

        print("\n8. Atualizando múltiplos documentos (todos em São Paulo para 'SP'):")
        manager.update_document({"cidade": "São Paulo"}, {"$set": {"cidade": "SP"}}, multi=True)
        manager.read_documents({"cidade": "SP"})

        # --- DELETE ---
        print("\n9. Deletando um documento (Bob):")
        manager.delete_document({"nome": "Bob"})
        print("Documentos restantes após deletar Bob:")
        manager.read_documents()

        print("\n10. Deletando múltiplos documentos (todos com idade > 30):")
        manager.delete_document({"idade": {"$gt": 30}}, multi=True)
        print("Documentos restantes após deletar com idade > 30:")
        manager.read_documents()

    else:
        print("\nNão foi possível executar as operações CRUD devido à falha na conexão.")

    # Fechar a conexão ao final
    manager.close_connection()