# BBM
Referente ao teste técnico do processo seletivo da BBM.<br>
O projeto tem como objetivo disponibilizar o CRUD de uma entidade por meio de API utilizando Pyython+Django, salvando os dados em um banco relacional, usar o swagger para documentar a API e disponibilizar o app com Docker.<br>

Nesse caso o projeto vai gerenciar livros (model book)

## Tecnologia utilizada
- [Python v3.10.6](https://www.python.org/downloads/)
- [Django v4.1](https://www.djangoproject.com/start/)
- [Psycopg2 v2.9](https://pypi.org/project/psycopg2/)
- [Drf-spectacular v0.23.1](https://drf-spectacular.readthedocs.io/en/latest/readme.html)
- [Djangorestframework v3.13.1](https://www.django-rest-framework.org/tutorial/quickstart/)
- [Django-cors-headers v2.2.0](https://pypi.org/project/django-cors-headers/2.2.0/)

## Como começar
Por conta das tecnologias utilizadas é necessário ter inetalado em sua máquina o Python e o Docker (e o docker-compose).

### Pre requisitos
```
# Para verificar a instalação do Python e Docker
python --version
docker --version
docker-compose --version
```

## Instalação e execução
O fluxo consiste em primeiramente clonar este repositório, realizar a execução do container docker configurado no mesmo e por ultimo rodar a migration do banco de dados para criar a tabela book caso seja a primeira vez:
```sh
# 1. Clonar o repositorio
git clone https://github.com/Pedrohcs/bbm

# 2. Mover para o diretório clonado
cd .\bbm

# 3. Executar o docker do projeto
docker-compose up

# 4. Gerar as migrations necessárias
docker-compose exec web python manage.py makemigrations

# 5. Rodar as migrations criadas
docker-compose exec web python manage.py migrate   
```

## API
A documentação da API foi realizada por meio do Swagger (por isso o uso do framework `drf-spectacular`). Para acessar a documentação é necessário executar o projeto e acessar a seguinte url:<br>
`http://127.0.0.1:8000/swagger`