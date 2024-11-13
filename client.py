import socket  # Biblioteca para criar e gerenciar sockets TCP/IP
import os  # Biblioteca para manipulação de arquivos e diretórios

# Configurações do cliente
HOST = 'localhost'  # Endereço do servidor (localhost indica que o servidor está na mesma máquina)
PORT = 12345  # Porta do servidor para se conectar
BUFFER_SIZE = 1024  # Tamanho do buffer para enviar/receber dados (1 KB)
UPLOAD_DIR = 'uploads'  # Diretório onde os arquivos estão localizados

# Definição das cores usando códigos ANSI
COLOR_BLUE = '\033[94m'   # Azul
COLOR_GREEN = '\033[92m'  # Verde
COLOR_YELLOW = '\033[93m' # Amarelo
COLOR_RED = '\033[91m'    # Vermelho
COLOR_RESET = '\033[0m'   # Reset (restaura a cor original)

# Função para listar os arquivos disponíveis na pasta 'uploads'
def list_files():
    # Verifica se a pasta 'uploads' existe
    if not os.path.isdir(UPLOAD_DIR):
        print(f"{COLOR_RED}A pasta '{UPLOAD_DIR}' não existe.{COLOR_RESET}")  # Exibe mensagem em vermelho caso a pasta não exista
        return
    
    files = os.listdir(UPLOAD_DIR)  # Lista todos os arquivos no diretório
    if not files:
        print(f"{COLOR_RED}Nenhum arquivo disponível na pasta '{UPLOAD_DIR}' para envio.{COLOR_RESET}")  # Exibe mensagem em vermelho caso não haja arquivos
    else:
        print(f"{COLOR_GREEN}Arquivos disponíveis na pasta '{UPLOAD_DIR}' para envio:{COLOR_RESET}")
        # Exibe os arquivos presentes na pasta
        for file in files:
            file_path = os.path.join(UPLOAD_DIR, file)  # Concatena o nome do arquivo com o diretório
            if os.path.isfile(file_path):  # Verifica se é um arquivo (não um diretório)
                print(f"{COLOR_GREEN}{file}{COLOR_RESET}")  # Exibe o nome do arquivo em verde

# Função para enviar um arquivo para o servidor
def send_file(filename):
    # Verifica se o arquivo existe
    if not os.path.isfile(filename):
        print(f"{COLOR_RED}Arquivo não encontrado.{COLOR_RESET}")  # Exibe mensagem em vermelho caso o arquivo não exista
        return

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Cria o socket e conecta ao servidor (HOST e PORT)
        client_socket.connect((HOST, PORT))
        
        # Exibe o IP do cliente
        client_ip = client_socket.getsockname()[0]  # Obtém o IP do cliente
        print(f"{COLOR_YELLOW}IP do cliente: {client_ip}{COLOR_RESET}")  # Exibe o IP do cliente
 
        # Envia o nome do arquivo para o servidor
        client_socket.send(filename.encode('utf-8'))  # Codifica o nome do arquivo para byte
        
        # Abre o arquivo em modo leitura binária e envia seu conteúdo
        with open(filename, 'rb') as f:
            while True:
                # Lê o arquivo em blocos de tamanho BUFFER_SIZE
                data = f.read(BUFFER_SIZE)
                if not data:  # Se não houver mais dados, interrompe o envio
                    break
                client_socket.send(data)  # Envia os dados para o servidor
        
        print(f"{COLOR_GREEN}Arquivo '{filename}' enviado com sucesso!{COLOR_RESET}")  # Confirma o envio do arquivo em verde

# Função que exibe o menu e recebe a escolha do usuário
def menu():
    while True:
        print(f"{COLOR_BLUE}\nMenu de opções:{COLOR_RESET}")
        print(f"{COLOR_YELLOW}1 - Listar arquivos disponíveis{COLOR_RESET}")
        print(f"{COLOR_YELLOW}2 - Enviar um arquivo{COLOR_RESET}")
        print(f"{COLOR_RED}3 - Sair{COLOR_RESET}")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            list_files()  # Chama a função para listar os arquivos
        elif choice == '2':
            filename = input("Digite o nome do arquivo para enviar: ")
            send_file(filename)  # Chama a função para enviar o arquivo
        elif choice == '3':
            print(f"{COLOR_RED}Saindo...{COLOR_RESET}")  # Exibe mensagem de saída em vermelho
            break
        else:
            print(f"{COLOR_RED}Opção inválida. Tente novamente.{COLOR_RESET}")  # Exibe mensagem de erro em vermelho

# Inicia o programa quando o script for executado
if __name__ == "__main__":
    menu()