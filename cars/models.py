from django.db import models


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField("Modelo", max_length=100)
    brand = models.ForeignKey(
        "Brand", on_delete=models.PROTECT, related_name="car_brand"
    )
    price = models.DecimalField("Preço", max_digits=9, decimal_places=2)
    factory_year = models.IntegerField("Ano de fabricação")
    model_year = models.IntegerField("Ano do modelo", blank=True, null=True)
    creation_date_time = models.DateTimeField(auto_now_add=True)
    modified_date_time = models.DateTimeField(auto_now=True)
    plate_number = models.IntegerField(
        "Final da placa", blank=True, null=True
    )
    photo = models.ImageField(
        "Imagem", upload_to="cars/", blank=True, null=True
    )
    bio = models.TextField('Descrição', blank=True, null=True)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = "Carro"


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Marca", max_length=100, unique=True)

    class Meta:
        verbose_name = "Marca"

    def __str__(self):
        return self.name


class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'
