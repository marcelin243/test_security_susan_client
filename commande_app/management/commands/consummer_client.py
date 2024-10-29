from django.core.management.base import BaseCommand
import pika
import json
from commande_app.modules.com_commande_detail.serialisers import insert_com_commande_detail_Serializers
from commande_app.models import com_commande_detail
from commande_app.modules.com_commande.serialisers import insert_com_commande_Serializers
from commande_app.models import * 
from commande_app.modules.com_commande_detail.serialisers import *

class Command(BaseCommand):
    help = 'Consomme des messages de RabbitMQ'

    def handle(self, *args, **options):
        credentials = pika.PlainCredentials('client_rabbit', 'client_rabbit')
        # connection_params = pika.ConnectionParameters(host='172.30.79.83', credentials=credentials)
        connection_params = pika.ConnectionParameters(host='172.30.79.83', credentials=credentials)
        

        try:
            connection = pika.BlockingConnection(connection_params)
                       
            channel = connection.channel()
            channel.queue_declare(queue="detail_commande_key")

            def callback(ch, method, properties, body):
                data=json.loads(body)
                if properties.content_type == "update_detail":
                    obj=com_commande_detail.objects.get(COMMANDE_DETAIL_ID=data["COMMANDE_DETAIL_ID"])
                    serialiser=insert_com_commande_detail_Serializers(obj,data={"COM_STATUT_DET_ID":data["COM_STATUT_DET_ID"]},partial=True)
                    serialiser.is_valid(raise_exception=True)
                    serialiser.save()
                    self.stdout.write(self.style.SUCCESS("Enregistrement mis à jour."))
                    
                if properties.content_type == "valider_payement":
                    COUNT_COM_STATUT_DET_ID=com_commande_detail.objects.filter(COMMANDE_ID=data["COMMANDE_ID"]).count()
                    COUNT_COM_STATUT_3=com_commande_detail.objects.filter(COMMANDE_ID=data["COMMANDE_ID"],COM_STATUT_DET_ID=3).count()
            
                    if COUNT_COM_STATUT_DET_ID == COUNT_COM_STATUT_3:
                        com=com_commande.objects.get(COMMANDE_ID=data["COMMANDE_ID"])
                        serialiser_=insert_com_commande_Serializers(com,data={"STATUT_COM_ID":3})
                        serialiser_.is_valid(raise_exception=True)
                        serialiser_.save()
                        self.stdout.write(self.style.SUCCESS("Enregistrement mis à jour."))
            
                    elif COUNT_COM_STATUT_DET_ID > COUNT_COM_STATUT_3:
                        com=com_commande.objects.get(COMMANDE_ID=data["COMMANDE_ID"])
                        serialiser_=insert_com_commande_Serializers(com,data={"STATUT_COM_ID":2})
                        serialiser_.is_valid(raise_exception=True)
                        serialiser_.save()
                        try:
                            detail_=com_commande_detail.objects.get(COMMANDE_DETAIL_ID=data["COMMANDE_DETAIL_ID"])
                            detail_serialiser=insert_com_commande_detail_Serializers(detail_,data={"COM_STATUT_DET_ID":4},partial=True)
                            detail_serialiser.is_valid(raise_exception=True)
                            detail_serialiser.save()
                            self.stdout.write(self.style.SUCCESS("Enregistrement mis à jour."))
                        except com_commande_detail.DoesNotExist:
                            self.stdout.write(self.style.ERROR("cette commande detail n'existe pas."))
                        
            channel.basic_consume(queue="detail_commande_key", on_message_callback=callback, auto_ack=True)
            self.stdout.write(self.style.SUCCESS("EN ATTENTE DE CONSOMMATION ***"))
            channel.start_consuming()

        except pika.exceptions.AMQPConnectionError as e:
            self.stderr.write(f"Erreur de connexion à RabbitMQ : {e}")
        except Exception as e:
            self.stderr.write(f"Une erreur est survenue : {e}")
        finally:
            if 'connection' in locals() and connection.is_open:
                connection.close()
                self.stdout.write(self.style.SUCCESS("Connexion fermée."))