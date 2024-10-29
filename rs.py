import subprocess
import sys

def run_django_server():
    """Démarre le serveur Django."""
    # VAS DANS LE FICHIER DE CONFIGURATION DE NGINX ,PUIS COPIER L'IP ET LE NUMERO DE PORT DE TON MICROSERVICE(SEMENCE)
    # COLLER LE APRES 'python', 'manage.py', 'runserver', QUI EST EN DESSOUS
    return subprocess.Popen(['python', 'manage.py', 'runserver', '172.30.64.1:8001'])

def run_consumer():
    """Démarre la commande de consommation de messages RabbitMQ."""
    return subprocess.Popen(['python', 'manage.py', 'consummer_client'])

if __name__ == '__main__':
    django_server = run_django_server()
    consume_command = run_consumer()
    # Attends que les processus se terminent
    try:
        django_server.wait()
        consume_command.wait()
    except KeyboardInterrupt:
        print("Arrêt des processus...")
        django_server.terminate()
        consume_command.terminate()
        sys.exit(0)
        
# POUR LANCER LE SERVEUR FAIS py rs.py  PUIS ENTREE
