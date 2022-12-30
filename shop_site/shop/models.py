from django.conf import settings
from django.db import models
from django.db.models import Count, constraints
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
import uuid

from .choices import *

def photos_file_name(self, filename):
    return f"photos/{self.code}/{filename}"


class Laptop(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    seria = models.CharField(max_length = 100, verbose_name="Серія")
    screen_diagonal = models.FloatField(verbose_name="Діагональ екрану")
    screen_type = models.CharField(max_length = 17, choices=Screen_types.choices, verbose_name="Тип екрану")
    resolution = models.CharField(max_length = 11, choices=PCResolutions.choices, verbose_name="Роздільна здатність")
    integrated_videocard_aviable = models.BooleanField(verbose_name="Наявна інтегрована відеокарта")
    discred_videocard_aviable = models.BooleanField(verbose_name="Наявна дискретна відеокарта")
    videocard_series = models.CharField(max_length = 38, choices=Videocard.choices,  verbose_name="Відеокарта")
    videocard_memory = models.IntegerField(verbose_name="Відео память")
    HDD_aviable = models.BooleanField(verbose_name="HDD диск")
    HDD_size = models.IntegerField(verbose_name="Розмір HDD диску", null=True, blank=True)
    SSD_aviable =  models.BooleanField(verbose_name="SSD диск")
    SSD_size = models.IntegerField(verbose_name="Розмір SSD диску", null=True, blank=True)
    RAM_size = models.IntegerField(verbose_name="Кількість оперативної памяті")
    Ram_type = models.CharField(max_length = 4, choices = RAM_types.choices, verbose_name="Тип оперативної памяті")
    RAM_slots = models.IntegerField(verbose_name="Кількість розємів для оперативної памяті")
    processor_series = models.CharField(max_length = 17, choices=Processors.choices, verbose_name="Процессор")
    processor_hertz = models.CharField(max_length = 20, verbose_name='Частота просессора')
    processor_generation = models.IntegerField(verbose_name="Покоління процессора")
    cores_num = models.IntegerField(verbose_name="Кількість ядер")
    OS = models.CharField(max_length = 9, choices = OSes.choices, verbose_name="Операційна система")
    wifi_adapter = models.BooleanField(verbose_name="Wifi адаптер")
    bluetooth_adpter = models.BooleanField(verbose_name="Bluetooth адаптер")
    web_camera = models.BooleanField(verbose_name='Веб камера')
    optical_drive = models.BooleanField(verbose_name='Оптичний привід')
    fingerprint_scaner = models.BooleanField(verbose_name='Сканер відбитку пальця')
    connectors_ports = models.CharField(max_length = 100, verbose_name="Розєми та порти")
    colour = models.CharField(max_length = 8, choices=CustomColours.choices, verbose_name="Колір")
    acumulator_size = models.IntegerField(verbose_name="Обєм акумулятора")
    width = models.FloatField(verbose_name="Ширина")
    height = models.FloatField(verbose_name="Висота")
    lenght = models.FloatField(verbose_name="Довжина")
    weight = models.FloatField(verbose_name="Вага")
    producing_country = models.CharField(max_length = 4, choices = Countries.choices, verbose_name="Країна виробник", )

    @property
    def size(self):
        return f"{self.lenght}x{self.width}x{self.height}"
    size.fget.short_description = 'Розмір'

    @property
    def short_characteristics(self):
        return f"Екран: {self.screen_diagonal} \
                {self.get_screen_type_display()} \
                {self.get_resolution_display()} / \
                {self.get_processor_series_display()} \
                {self.cores_num} Ядер ({self.processor_hertz} Ггц) / \
                RAM {self.RAM_size} ГБ / \
                {f'SSD {self.SSD_size} Гб / ' if self.SSD_aviable else ''}\
                {f'HDD {self.HDD_size} Гб /' if self.HDD_aviable else ''}\
                {self.get_videocard_series_display() if self.discred_videocard_aviable else 'Інтегрована відеокарта'} \
                {self.videocard_memory} Гб / \
                {'З ОД' if self.optical_drive else 'Без ОД'} / \
                {'Wifi / ' if self.wifi_adapter else ''}\
                {'Bluetooth / ' if self.bluetooth_adpter else ''}\
                {'Веб камера / ' if self.web_camera else ''}\
                {'Сканер відбитку пальця / ' if self.fingerprint_scaner else ''}\
                {self.get_OS_display()} / \
                {self.size} см/ \
                {self.weight} кг/ \
                {self.get_colour_display()}"

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'
        constraints = [
            models.CheckConstraint(
                name="Повинний бути вибраний хоча б один диск",
                check= (
                    models.Q(HDD_aviable=False, SSD_aviable=True)
                    | models.Q(HDD_aviable=True, SSD_aviable=False)
                    | models.Q(HDD_aviable=True, SSD_aviable=True)
                )
            ),
            models.CheckConstraint(
                name="Повинна бути вибрана хоча б одна відеокарта",
                check=(
                    models.Q(discred_videocard_aviable=False, integrated_videocard_aviable=True)
                    | models.Q(discred_videocard_aviable=True, integrated_videocard_aviable=False)
                    | models.Q(discred_videocard_aviable=True, integrated_videocard_aviable=True)
                )
            )
        ]
