from django.apps import AppConfig


class AiTrainerConditionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ai_trainer_condition'
    verbose_name = 'Número de inserções ate o ré-treino da IA'
