# Anarco Drive

Anarco Drive é uma aplicação web que permite o upload e download de arquivos, com um servidor socket para gerenciar conexões de clientes. A aplicação gera um QR Code para acessar a página de upload de forma rápida.

## Funcionalidades

- **Upload de Arquivos**: Permite que os usuários enviem arquivos para o servidor.
- **Download de Arquivos**: Os arquivos enviados podem ser baixados pelos usuários.
- **Listagem de Arquivos**: Exibe a lista de arquivos disponíveis no servidor.
- **QR Code**: Gera um QR Code para acessar rapidamente a página do servidor.

## Tecnologias Utilizadas

- Python 3.x
- Flask
- Socket Programming
- HTML/CSS
- qrcode (biblioteca Python para geração de QR Codes)

## Estrutura do Projeto
projeto/
│
├── app.py                # Código principal da aplicação Flask
├── server.py             # Código do servidor socket
├── file_manager.py       # Funções relacionadas ao gerenciamento de arquivos
├── templates/
│   └── index.html        # Template HTML
└── uploads/              # Diretório para armazenar arquivos enviados
## Requisitos

Para executar o projeto, você precisa ter o Python 3 instalado e as seguintes bibliotecas:

```bash
pip install Flask qrcode --break-system-packages