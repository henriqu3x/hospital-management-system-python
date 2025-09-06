# Sistema de Gestão Hospitalar

Este é um projeto de um sistema de gestão hospitalar completo, desenvolvido em Python, com foco em uma arquitetura modular e boas práticas de acesso a dados. O sistema permite o gerenciamento de pacientes, médicos, enfermeiros e as operações rotineiras de um hospital, como consultas, exames e internações.

## Funcionalidades Principais

### Gerenciamento de Usuários

- Sistema de autenticação e registro de usuários com diferentes perfis (admin, médico, enfermeiro).
- As senhas são armazenadas de forma segura usando `bcrypt`.

### Gerenciamento de Pacientes

- Adição, visualização, atualização e remoção de dados de pacientes.

### Gerenciamento de Profissionais

- Cadastro e controle de médicos e enfermeiros, com suas respectivas informações.

### Gestão de Operações

- **Consultas**: Agendamento e registro de consultas médicas.
- **Exames**: Solicitação, agendamento e atualização de status de exames.
- **Internações**: Registro de entrada e saída de pacientes, com detalhes sobre o quarto e diagnóstico.

## Tecnologias Utilizadas

- **Linguagem de Programação**: Python
- **Banco de Dados**: PostgreSQL
- **Bibliotecas**:
  - `psycopg2`: Adaptador para o banco de dados PostgreSQL.
  - `bcrypt`: Para criptografia de senhas.
  - `python-dotenv`: Para gerenciar variáveis de ambiente.

## Estrutura do Projeto

O projeto é organizado em uma estrutura de pastas clara para separar as responsabilidades e seguir o padrão de arquitetura MVC (Model-View-Controller) ou, neste caso, uma variante com uma camada de DAO (Data Access Object).

```
/  
├── .env  
├── main.py  
├── db/  
│   ├── connection.py  
│   └── setup.py  
└── control/  
    ├── consultaDAO.py  
    ├── enfermeiroDAO.py  
    ├── exameDAO.py  
    ├── internacaoDAO.py  
    ├── medicoDAO.py  
    ├── pacienteDAO.py  
    └── usuarioDAO.py
```

- **.env**: Armazena as credenciais de conexão com o banco de dados, mantendo informações sensíveis seguras.
- **main.py**: A interface de linha de comando principal (CLI) para interagir com o sistema.
- **db/**: Contém a lógica de conexão com o banco de dados.
  - **connection.py**: Classe central para gerenciar a conexão, executar consultas e manipulações.
  - **setup.py**: Script para a criação inicial das tabelas do banco de dados.
- **control/**: Contém as classes DAO, que encapsulam a lógica de negócio e o acesso aos dados para cada entidade do sistema (médicos, pacientes, etc.).

## Como Executar o Projeto

Siga os passos abaixo para configurar e rodar o projeto em seu ambiente local.

### Pré-requisitos

- Python 3.x
- PostgreSQL (servidor de banco de dados rodando)

### Passos

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/henriqu3x/hospital-management-system-python.git
   cd hospital-management-system-python
   ```

2. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure as variáveis de ambiente**: Crie um arquivo chamado `.env` na raiz do projeto e preencha-o com suas credenciais de banco de dados, conforme o exemplo abaixo:

   ```
   DB_NAME=nome_do_seu_banco
   DB_USER=seu_usuario
   DB_PASSWORD=sua_senha
   DB_HOST=seu_host
   DB_PORT=sua_porta
   ```

4. **Crie as tabelas do banco de dados**: Execute o script de setup para criar a estrutura do banco de dados:

   ```bash
   python db/setup.py
   ```

5. **Execute a aplicação**: Agora você pode iniciar a aplicação principal:

   ```bash
   python main.py
   ```

## Autor

Luiz Henrique - https://www.linkedin.com/in/luiz-henrique-a1b0712b3/