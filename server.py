import socket  # Biblioteca para criar e gerenciar sockets TCP/IP
import threading  # Biblioteca para trabalhar com threads (executando várias funções simultaneamente)
import os  # Biblioteca para manipulação de arquivos e diretórios

# Configurações do servidor
HOST = 'localhost'  # Endereço do servidor (localhost indica que o servidor está na mesma máquina)
PORT = 12345  # Porta de comunicação onde o servidor vai escutar por conexões
BUFFER_SIZE = 1024  # Tamanho do buffer para enviar/receber dados (1 KB)
DEST_DIR = 'uploads'  # Diretório para salvar os arquivos recebidos

# Garantir que o diretório de upload existe (se não, ele será criado)
os.makedirs(DEST_DIR, exist_ok=True)

# Função para lidar com cada cliente que se conecta
def handle_client(client_socket, client_address):
    print(f'Conexão estabelecida com {client_address}')  # Exibe o endereço do cliente conectado

    try:
        # Receber nome do arquivo do cliente
        filename = client_socket.recv(BUFFER_SIZE).decode('utf-8').strip()  # Recebe o nome do arquivo que será enviado
        if '\x00' in filename:
            raise ValueError("Nome de arquivo inválido (contém byte nulo).")
        
        print(f'Nome do arquivo recebido: {filename}')
        
        # Abrir o arquivo para salvar os dados recebidos
        with open(os.path.join(DEST_DIR, filename), 'wb') as f:
            while True:
                # Recebe os dados do arquivo em pacotes do tamanho de BUFFER_SIZE
                data = client_socket.recv(BUFFER_SIZE)
                if not data:
                    break  # Se não houver mais dados, termina o recebimento
                f.write(data)  # Escreve os dados recebidos no arquivo
        
        print(f'Arquivo {filename} recebido com sucesso!')  # Confirma que o arquivo foi salvo
    except UnicodeDecodeError:
        print(f"Erro: falha ao decodificar nome do arquivo.")
    except ValueError as e:
        print(f"Erro: {e}")
    finally:
        client_socket.close()  # Fecha a conexão com o cliente após finalizar a transferência

# Função para iniciar o servidor
def start_server():
    # Criação do socket do servidor utilizando IPv4 (AF_INET) e TCP (SOCK_STREAM)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Fazendo o bind do servidor ao endereço e porta especificados
    server_socket.bind((HOST, PORT))  
    # O servidor começa a escutar até 5 conexões simultâneas
    server_socket.listen(5)
    print(f'Servidor aguardando conexões em {HOST}:{PORT}...')  # Mensagem de aguardo para clientes
    
    # Loop infinito para aceitar conexões continuamente
    while True:
        # Aceita a conexão de um cliente e cria um socket específico para ele
        client_socket, client_address = server_socket.accept()
        # Para cada cliente, é criada uma nova thread para tratar a transferência de arquivos
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()  # Inicia a thread do cliente

# Inicia o servidor quando o script for executado
if __name__ == "__main__":
    start_server()