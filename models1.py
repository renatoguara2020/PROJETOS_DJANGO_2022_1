from django.db import models


class Cliente(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )

    nome = models.CharField(max_length=100, null=False, blank=False)
    sexo = models.CharField(
        max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    data_nascimento = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)

    def __str__(self):
        return self.nome
