Software desenvolvido para apoiar a pesquisa do meu projeto de iniciação científica com o título "DESENVOLVIMENTO DE UM EQUIPAMENTO PARA A AVALIAÇÃO DA ESTABILIDADE POSTURAL EM PESSOAS COM TRANSTORNOS DE EQUILÍBRIO – PARTE 2"

# Aplicativo Desktop para Fisioterapeutas

Este é um aplicativo desktop desenvolvido em Python que permite aos médicos fisioterapeutas cadastrar exames de pacientes em um formato padrão e visualizar gráficos gerados pelo programa para avaliar o desempenho dos pacientes.

---

## Funcionalidades Principais

- **Cadastro de Pacientes**:
  - Cadastrar informações básicas dos pacientes (RM, identificação).
- **Cadastro de Exames**:
  - Cadastrar exames em um formato padrão (dados de amplitude de movimento, etc.).
- **Visualização de Gráficos**:
  - Gerar gráficos a partir dos dados dos exames para análise visual.
- **Relatórios**:
  - Gerar relatórios de desempenho dos pacientes com base nos exames.
- **Interface Gráfica**:
  - Interface amigável e intuitiva para o médico.

---

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Interface Gráfica**: PyQt5
- **Banco de Dados**: SQLite
- **Gráficos**: Matplotlib
- **Gerenciamento de Dependências**: pip
- **Containerização**: Docker

---

## Como Executar o Projeto

### Instalação

1. Clone o repositório:
   git clone https://github.com/seu-usuario/seu-repositorio.git

2. Construa a imagem Docker:
   docker build -t project-k .

3. Rode o Compose
    docker-compose up

4. Instale o Xming no Windows e execute o comando abaixo:
172.29.48.1:0 é o IP da máquina que está rodando o Xming, caso seja outro IP, alterar para o IP correto no docker compose.
