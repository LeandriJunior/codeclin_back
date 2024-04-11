# Backend Django para Sistema de Clínicas - README

Este README documenta os passos necessários para configurar e executar a aplicação backend Django desenvolvida por Leandri Albert Wagner Junior. Esta aplicação tem como objetivo fornecer uma API para um sistema de clínicas em geral, com um foco especial em odontologia.

## Versões Utilizadas
- Django: 5.0.3
- Python: 3.12

## Estrutura da Aplicação
A aplicação segue uma estrutura de três camadas:

### Views
Esta camada é responsável por receber as requisições do frontend e direcioná-las para as camadas adequadas do sistema.

### BO (Business Objects)
A camada de Business Objects contém as regras de negócio da aplicação. Aqui são implementadas as lógicas necessárias para processar as requisições e realizar operações no banco de dados.

### Model
A camada de Model contém apenas os modelos de dados e as instruções SQL do SQLAlchemy para interação com o banco de dados. Aqui são definidas as tabelas do banco e os relacionamentos entre elas.

## Configuração
### Pré-requisitos
- Python 3.12 instalado
- Django 5.0.3 instalado
- SQLAlchemy instalado
- Django Tenants instalado

### Instalação
1. Clone este repositório para sua máquina local.
2. Instale as dependências executando o comando:
   ```
   pip install -r requirements.txt
   ```

### Configuração do Banco de Dados
1. Configure as informações do banco de dados no arquivo `settings.py`.
2. Execute as migrações do Django para criar as tabelas no banco de dados:
   ```
   python manage.py migrate
   ```

## Instruções de Implantação
1. Configure as variáveis de ambiente necessárias para o ambiente de produção.
2. Implante a aplicação em seu servidor utilizando a ferramenta de sua escolha.

## Diretrizes de Contribuição
- Pull requests são bem-vindos. Para grandes mudanças, por favor, abra uma issue primeiro para discutir o que você gostaria de mudar.

## Contato
### Leandri Albert Wagner Junior
- Email: leandriwgr@email.com

