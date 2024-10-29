# serializers.py
from rest_framework import serializers
from semence_app.modules.sem_commande_semence.models import sem_commande_semence


class UpdateStatutCommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = sem_commande_semence
        fields = ['id', 'STATUT_CMD_ID']  # On a besoin de ces champs pour la mise à jour

    def update(self, instance, validated_data):
        # Mettre à jour le STATUT_CMD_ID à 4
        instance.STATUT_CMD_ID = validated_data.get('STATUT_CMD_ID', instance.STATUT_CMD_ID)
        instance.save()
        return instance
