# CRUD NoSQL

### /POSTS

### Methods Allowed

- GET
    - [ ]  Retorna todos os posts do banco de dados, status code 200
    - [ ]  Retorna o post com id passado, status code 200
    - [ ]  Retorna 404 para um id não existente no db
- POST
    - [ ]  Retorna status code 406 caso esteja faltando alguma chave no JSON enviado
    - [ ]  Requisição correta, salva os dados no db e retorna 201
- DELETE
    - [ ]  Tentativa de deletar post inexistente retorna 404
    - [ ]  Retorna o objeto deletado e o status code 200
- PATCH
    - [ ]  Retorna status code 406 caso o JSON enviado não seja válido
    - [ ]  Tentativa de editar post inexistente retorna 404
    - [ ]  Retorna o objeto atualizado e status code 200 em caso de sucesso na atualização
_____
### Design Pattern
- MongoDB
    - [ ]  Conexão com o banco seguindo boas práticas e uso correto das  funções disponibilizadas pelo Pymongo
- POO
    - [ ]  Utilização dos tipos corretos de atributos e métodos nas classes. (Instância, Classe,  estáticos). E uso dos métodos especiais corretamente.
- Arquitetura e Design Pattern
    - [ ]  Organização do projeto de acordo com o padrão MVC e uso do Design Pattern Factory
- Id auto incrementável
    - [ ]  Cada novo post criado o id é incrementado automaticamente. Mesmo reiniciando a aplicação
- Organização básica do projeto
    - [ ]  Organização dos módulos e pacotes, boas práticas, conteúdo do .gitignore, .env, requirements.txt, entre outros.
