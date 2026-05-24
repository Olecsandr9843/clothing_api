from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        managed = False  # Django не буде змінювати структуру таблиці
        db_table = 'customers'  # Вказуємо реальну назву таблиці в БД