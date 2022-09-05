# **Projeto: Vagas de trabalho**

## **Introdução**
---
Este é um case para o processo seletivo para a vaga programador Python Django (bolsista) - Senai.

**Descrição:** Uma empresa de análise de mercado irá implementar em seu ambiente de produção uma API de gerenciamento de ofertas de
vagas. O foco da aplicação é conseguir gerenciar as ofertas de vagas e recomendar vagas de trabalho. Para mitigar os problemas
reportados pelo cliente, propomos nessa atividade a criação do ambiente de gestão de usuários e vagas. O sistema proposto
consiste no desenvolvimento de uma API (Application Programming Interface) “back-end” baseada em Python com a utilização
do framework Django

## **Instalação**
---
Considerando que você já possua o Python e o Pip instalado, siga os passos a seguir para configurar o ambiente e executar a API:

- Acesse o diretório do projeto Vagas de trabalho:

    `cd /caminho/do/projeto/vaga_trabalho`

- Instalar o Django e Django Rest Framework:

    `pip install django djangorestframework`

- Instalar o JWT:

    `pip install djangorestframework-simplejwt`    

- Instalar o drf-spectacular:

    `pip install drf-spectacular`

- Criar super usuário:

    `python manage.py createsuperuser`

- Carregar dados das vagas de trabalho:

    `python data_load.py`

- Execute a aplicação:

    `python manage.py runserver`

## **Exemplo de uso**
---

Após executar o comando `python manage.py runserver`, é possível realizar os testes por meio de alguma ferramenta de API. Nos exemplos a seguir, será utilizando a ferramenta curl:

- **Realizar login na API**:

    `curl -X POST 127.0.0.1:8000/api/authentication/login/ -H "Content-Type: application/json" -d '{"username": "admin", "password": "admin"}'`

- **Refresh**:

    `curl -X POST 127.0.0.1:8000/api/authentication/refresh/ -H "Content-Type: application/json" -d '{"refresh": "{token de acesso}"}'`


- **Listar todos os usuários**:

    `curl -X GET 127.0.0.1:8000/api/user/ -H "Authorization: Bearer {token de acesso}"`

- **Criar um usuário**:

    `curl -X POST 127.0.0.1:8000/api/user/ -H "Authorization: Bearer {token de acesso}" -H "Content-Type: application/json" -d '{json com os dados do usuário}'`

- **Recuperar um usuário específico**:

    `curl -X GET 127.0.0.1:8000/api/user/{id}/ -H "Authorization: Bearer {token de acesso}"`

- **Atualizar um usuário específico**:

    `curl -X PUT 127.0.0.1:8000/api/user/{id}/ -H "Authorization: Bearer {token de acesso}" -H "Content-Type: application/json" -d '{json com dados atualizados}'`

- **Atualizar parcialmente um usuário específico**:

    `curl -X PATCH 127.0.0.1:8000/api/user/{id}/ -H "Authorization: Bearer {token de acesso}" -H "Content-Type: application/json" -d '{json com campos a atualizar}'`

- **Deletar um usuário**:

    `curl -X DELETE 127.0.0.1:8000/api/user/{id}/ -H "Authorization: Bearer {token de acesso}"`

- **Recuperar o usuário logado**:

    `curl -X GET 127.0.0.1:8000/api/user/me/ -H "Authorization: Bearer {token de acesso}"`

- **Listar todas as vagas**:

    `curl -X GET 127.0.0.1:8000/api/vacancy/ -H "Authorization: Bearer {token de acesso}"`

- **Criar uma vaga**:

    `curl -X POST 127.0.0.1:8000/api/vacancy/ -H "Authorization: Bearer {token de acesso}" -H "Content-Type: application/json" -d '{json com os dados da vaga}'`

- **Recuperar uma vaga específica**:

    `curl -X GET 127.0.0.1:8000/api/vacancy/{id}/ -H "Authorization: Bearer {token de acesso}"`

- **Atualizar uma vaga específica**:

    `curl -X PUT 127.0.0.1:8000/api/vacancy/{id}/ -H "Authorization: Bearer {token de acesso}" -H "Content-Type: application/json" -d '{json com dados atualizados}'`

- **Deletar uma vaga**:

    `curl -X DELETE 127.0.0.1:8000/api/vacancy/{id}/ -H "Authorization: Bearer {token de acesso}"`

- **Consulta por palavra chave**:

    `curl -X GET 127.0.0.1:8000/api/vacancy/keyword/?k=programador+java`

- Swagger:

    `127.0.0.1:8000/docs/`