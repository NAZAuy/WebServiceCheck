import socket
import configparser
import msvcrt

def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    website = config['General']['website']
    ports_to_check = {service: int(port) for service, port in config['Ports'].items()}
    return website, ports_to_check

def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

def print_status(service, status):
    if status:
        print(f"{service} - \033[92mDisponible\033[0m")
    else:
        print(f"{service} - \033[91mFallo la conexión\033[0m")

def main():
    website, ports_to_check = load_config()
    print(f"Escaneando puertos para el sitio web: {website}")
    for service, port in ports_to_check.items():
        status = check_port(website, port)
        # print_status(port, service, status)
        print_status(service, status)
    print("Presiona cualquier tecla para continuar...")
    msvcrt.getch()

if __name__ == "__main__":
    main()