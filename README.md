# TCC-Bebe-Parceiro
Passos globais:
1. **PG1** (`/back`): Copie e cole, no mesmo lugar, o arquivo `config.example.py`. Troque o nome da cópia para apenas `config.py`.
Mude as variáveis de `config.py` de acordo com o que for melhor.

## Para rodar o projeto inteiro 
> Os comandos a seguir devem ser executados na pasta raiz do projeto   
> Certifique-se de ter o **Docker** instalado. Você também precisará possuir o **docker compose**.
1. Execute **PG1** 
2. `docker compose up`

## Para rodar o Back-End
> Os comandos a seguir devem ser executados na pasta `/back`

1. Execute **PG1**

### Sem Docker
> Certifique-se de ter o **Python 3.8 (no mínimo)** instalado. Você também precisará possuir o **PIP**.
1. Execute `pip install -r requirements.txt`.
2. Execute `python manage.py makemigrations`
3. Execute `python manage.py migrate`
4. Execute `python manage.py runserver`


### Com Docker
> Certifique-se de ter o **Docker** instalado. Você também precisará possuir o **docker compose**.
1. Execute `docker compose up`

> Pode ser necessário entrar dentro do container do back para executar `python manage.py makemigrations`. Para entrar no container, basta executar `docker exec -ti <nome_do_container> sh`


## Para rodar o Front-End
> Os comandos a seguir devem ser executados na pasta `/front`

### Sem Docker
> Você deverá possuir o **NPM** instalado
1. Execute `npm install`
2. Execute `npm run ng serve`

### Com Docker
1. Execute `docker compose up`
