from enum import unique
from django.conf import settings
from django.db import models
from django.db.models import Count, constraints
from django.contrib.postgres.fields import ArrayField
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from uuid import uuid4
from random import randint
from slugify import slugify

from .choices import *


def photos_file_name(self, filename):
    return f"photos/{self.product.pk}/{filename}"

def create_product_code():
    print( "".join([str(randint(0, 9)) for i in range(10)]))
    return "".join([str(randint(0, 9)) for i in range(10)])


class Category(models.Model):
    name = models.CharField(max_length=25, choices=Categories.choices, verbose_name="Назва")
    name_plural = models.CharField(max_length=25, choices=Categories_plural.choices, verbose_name="Назва в множині")

class Product(models.Model):

    code = models.CharField(max_length=10, primary_key=True, default=create_product_code, editable=False, unique=True)
    slug = models.SlugField(max_length=100, blank=True)
    brend = models.CharField(max_length=50, verbose_name="Бренд")
    name = models.CharField(max_length=100, verbose_name="Назва", unique=True)
    created_at = models.DateTimeField(auto_now_add = True, verbose_name="Створено")
    updated_at = models.DateTimeField(auto_now = True, verbose_name="Оновлено")
    search_name = models.CharField(max_length=100, verbose_name="Назва для пошуку", blank=True)
    price = models.FloatField(validators=[MinValueValidator(0.01)] ,verbose_name="Ціна")
    on_sale = models.BooleanField(verbose_name="На акції")
    sale_price = models.FloatField(validators=[MinValueValidator(0.01)] ,verbose_name="Акція", blank=True, null=True)
    description = models.CharField(max_length=2500, verbose_name="Опис")
    number_aviable = models.PositiveIntegerField(verbose_name="Кількість")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product", verbose_name="Категорія")
    producing_country = models.CharField(max_length = 4, choices = Countries.choices, verbose_name="Країна виробник")
    views = models.PositiveIntegerField(verbose_name="Перегляди")

    content_type = models.ForeignKey(ContentType,  on_delete=models.CASCADE)
    object_id = models.UUIDField()
    content_object = GenericForeignKey('content_type', 'object_id')

    @property
    def aviable(self):
        return "В наявності" if self.number_aviable > 3 else "Немає в наявності" if self.number_aviable == 0 else "Закінчується"
    aviable.fget.short_description = "Наявність"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.search_title = self.name.lower()
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'

        unique_together = ('content_type', 'object_id')

class Product_photo(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    photo = models.ImageField(upload_to=photos_file_name, verbose_name="Фото", default='default/default_photo.jpg')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт", related_name='product_photo')


class Laptop(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    seria = models.CharField(max_length = 100, verbose_name="Серія")
    screen_diagonal = models.FloatField(validators=[MinValueValidator(0.01)] ,verbose_name="Діагональ екрану")
    screen_type = models.CharField(max_length = 30, choices=Screen_types.choices, verbose_name="Тип екрану")
    screen_refresh_rate = models.PositiveIntegerField(verbose_name="Частота оновлення екрану")
    resolution = models.CharField(max_length = 20, verbose_name="Роздільна здатність", validators=[RegexValidator(
        regex="\d+x\d+",
        message="Розширення екрану повинно бути такого типу: 1920x1080"
        ),])
    integrated_videocard_aviable = models.BooleanField(verbose_name="Наявна інтегрована відеокарта")
    discred_videocard_aviable = models.BooleanField(verbose_name="Наявна дискретна відеокарта")
    videocard_series = models.CharField(max_length = 50,  verbose_name="Відеокарта")
    videocard_memory = models.PositiveIntegerField(verbose_name="Відео память")
    HDD_aviable = models.BooleanField(verbose_name="HDD диск")
    HDD_size = models.PositiveIntegerField(verbose_name="Розмір HDD диску", null=True, blank=True)
    SSD_aviable =  models.BooleanField(verbose_name="SSD диск")
    SSD_size = models.PositiveIntegerField(verbose_name="Розмір SSD диску", null=True, blank=True)
    RAM_size = models.PositiveIntegerField(verbose_name="Кількість оперативної памяті")
    Ram_type = models.CharField(max_length = 4, choices = RAM_types.choices, verbose_name="Тип оперативної памяті")
    RAM_slots = models.PositiveIntegerField(verbose_name="Кількість розємів для оперативної памяті")
    processor = models.CharField(max_length = 50, verbose_name="Процессор")
    processor_hertz = models.FloatField(validators=[MinValueValidator(0.01)] ,verbose_name="Частота процессора")
    cores_num = models.PositiveIntegerField(verbose_name="Кількість ядер")
    OS = models.CharField(max_length = 9, choices = OSes.choices, verbose_name="Операційна система")
    wifi_adapter = models.BooleanField(verbose_name="Wifi адаптер")
    bluetooth_adpter = models.BooleanField(verbose_name="Bluetooth адаптер")
    web_camera = models.BooleanField(verbose_name='Веб камера')
    optical_drive = models.BooleanField(verbose_name='Оптичний привід')
    fingerprint_scaner = models.BooleanField(verbose_name='Сканер відбитку пальця')
    backlight = models.BooleanField(verbose_name="Підсвітка")
    connectors_ports = ArrayField(models.CharField(max_length = 100), size=20, verbose_name="Розєми та порти")
    colour = models.CharField(max_length = 8, choices=CustomColours.choices, verbose_name="Колір")
    material = models.CharField(max_length=15, choices=Material.choices, verbose_name="Матеріал")
    acumulator_size = models.IntegerField(verbose_name="Обєм акумулятора")

    width = models.FloatField(validators=[MinValueValidator(0.01)] ,verbose_name="Ширина")
    height = models.FloatField(validators=[MinValueValidator(0.01)] ,verbose_name="Висота")
    lenght = models.FloatField(validators=[MinValueValidator(0.01)] ,verbose_name="Довжина")
    weight = models.FloatField(validators=[MinValueValidator(0.01)] ,verbose_name="Вага")

    product = GenericRelation(Product, related_query_name='laptop')

    

    @property
    def size(self):
        return f"{self.lenght}x{self.width}x{self.height}"
    size.fget.short_description = 'Розмір'

    @property
    def short_characteristics(self):
        return f"Екран: {self.screen_diagonal} \
                {self.get_screen_type_display()} \
                {self.resolution} / \
                {self.processor} \
                {self.cores_num} Ядер ({self.processor_hertz} ГГц) / \
                RAM {self.RAM_size} ГБ / \
                {f'SSD {self.SSD_size} Гб / ' if self.SSD_aviable else ''}\
                {f'HDD {self.HDD_size} Гб /' if self.HDD_aviable else ''}\
                {self.videocard_series if self.discred_videocard_aviable else 'Інтегрована відеокарта'} \
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

    def clean(self):
        if (self.HDD_aviable and self.HDD_size == None) or (self.SSD_aviable and self.SSD_size == None):
            raise ValidationError("Введіть кількість памяті обраного вами диску")
        if (self.discred_videocard_aviable or self.integrated_videocard_aviable) and (self.videocard_memory == None or self.videocard_series == None):
            raise ValidationError("Введіть дані відеокарти")

    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'
        constraints = [
            models.CheckConstraint(
                name="Ноутбук. Повинний бути вибраний хоча б один диск",
                check= (
                    models.Q(HDD_aviable=False, SSD_aviable=True)
                    | models.Q(HDD_aviable=True, SSD_aviable=False)
                    | models.Q(HDD_aviable=True, SSD_aviable=True)
                )
            ),
            models.CheckConstraint(
                name="Ноутбук. Повинна бути вибрана хоча б одна відеокарта",
                check=(
                    models.Q(discred_videocard_aviable=False, integrated_videocard_aviable=True)
                    | models.Q(discred_videocard_aviable=True, integrated_videocard_aviable=False)
                    | models.Q(discred_videocard_aviable=True, integrated_videocard_aviable=True)
                )
            )
        ]

class PC(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    
    chipset = models.CharField(max_length=30, verbose_name="Чіпсет материнської плати")
    integrated_videocard_aviable = models.BooleanField(verbose_name="Наявна інтегрована відеокарта")
    discred_videocard_aviable = models.BooleanField(verbose_name="Наявна дискретна відеокарта")
    videocard_series = models.CharField(max_length = 50,  verbose_name="Відеокарта")
    videocard_memory = models.PositiveIntegerField(verbose_name="Відео память")
    HDD_aviable = models.BooleanField(verbose_name="HDD диск")
    HDD_size = models.PositiveIntegerField(verbose_name="Розмір HDD диску", null=True, blank=True)
    SSD_aviable =  models.BooleanField(verbose_name="SSD диск")
    SSD_size = models.PositiveIntegerField(verbose_name="Розмір SSD диску", null=True, blank=True)
    RAM_size = models.PositiveIntegerField(verbose_name="Кількість оперативної памяті")
    Ram_type = models.CharField(max_length = 4, choices = RAM_types.choices, verbose_name="Тип оперативної памяті")
    RAM_slots = models.PositiveIntegerField(verbose_name="Кількість розємів для оперативної памяті")
    processor = models.CharField(max_length = 50, verbose_name="Процессор")
    processor_hertz = models.FloatField(validators=[MinValueValidator(0.01)] ,verbose_name="Частота процессора")
    cores_num = models.PositiveIntegerField(verbose_name="Кількість ядер")
    capacity_of_power_block = models.PositiveIntegerField(verbose_name="Потужність Блоку живлення")
    OS = models.CharField(max_length = 9, choices = OSes.choices, verbose_name="Операційна система")
    wifi_adapter = models.BooleanField(verbose_name="Wifi адаптер")
    bluetooth_adpter = models.BooleanField(verbose_name="Bluetooth адаптер")
    optical_drive = models.BooleanField(verbose_name='Оптичний привід')
    backlight = models.BooleanField(verbose_name="Підсвітка")
    connectors_ports = ArrayField(models.CharField(max_length = 100), size=20, verbose_name="Розєми та порти")
    colour = models.CharField(max_length = 8, choices=CustomColours.choices, verbose_name="Колір")
    material = models.CharField(max_length= 15, choices=Material.choices, verbose_name="Матеріал")

    width = models.FloatField(validators=[MinValueValidator(0.01)] ,verbose_name="Ширина")
    height = models.FloatField(validators=[MinValueValidator(0.01)] ,verbose_name="Висота")
    lenght = models.FloatField(validators=[MinValueValidator(0.01)] ,verbose_name="Довжина")
    weight = models.FloatField(validators=[MinValueValidator(0.01)] ,verbose_name="Вага")

    product = GenericRelation(Product, related_query_name='pc')

    

    @property
    def size(self):
        return f"{self.lenght}x{self.width}x{self.height}"
    size.fget.short_description = 'Розмір'

    @property
    def short_characteristics(self):
        return f"{self.processor} \
                {self.cores_num} Ядер ({self.processor_hertz} ГГц) / \
                RAM {self.RAM_size} ГБ / \
                {f'SSD {self.SSD_size} Гб / ' if self.SSD_aviable else ''}\
                {f'HDD {self.HDD_size} Гб /' if self.HDD_aviable else ''}\
                {self.videocard_series if self.discred_videocard_aviable else 'Інтегрована відеокарта'} \
                {self.videocard_memory} Гб / \
                {'З ОД' if self.optical_drive else 'Без ОД'} / \
                {'Wifi / ' if self.wifi_adapter else ''}\
                {'Bluetooth / ' if self.bluetooth_adpter else ''}\
                {self.get_OS_display()} / \
                {self.size} см/ \
                {self.weight} кг/ \
                {self.get_colour_display()}"

    def __str__(self):
        return str(self.id)

    def clean(self):
        if (self.HDD_aviable and self.HDD_size == None) or (self.SSD_aviable and self.SSD_size == None):
            raise ValidationError("Введіть кількість памяті обраного вами диску")
        if (self.discred_videocard_aviable or self.integrated_videocard_aviable) and (self.videocard_memory == None or self.videocard_series == None):
            raise ValidationError("Введіть дані відеокарти")

    class Meta:
        verbose_name = 'Пк'
        verbose_name_plural = 'Пк'
        constraints = [
            models.CheckConstraint(
                name="ПК. Повинний бути вибраний хоча б один диск",
                check= (
                    models.Q(HDD_aviable=False, SSD_aviable=True)
                    | models.Q(HDD_aviable=True, SSD_aviable=False)
                    | models.Q(HDD_aviable=True, SSD_aviable=True)
                )
            ),
            models.CheckConstraint(
                name="ПК. Повинна бути вибрана хоча б одна відеокарта",
                check=(
                    models.Q(discred_videocard_aviable=False, integrated_videocard_aviable=True)
                    | models.Q(discred_videocard_aviable=True, integrated_videocard_aviable=False)
                    | models.Q(discred_videocard_aviable=True, integrated_videocard_aviable=True)
                )
            )
        ]

class Phone(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    seria = models.CharField(max_length = 100, verbose_name="Серія")
    G2 = models.BooleanField(verbose_name="2G(GPRS/EDGE)")
    G3 = models.BooleanField(verbose_name="3G(WCDMA/UMTS/HSPA)")
    LTE = models.BooleanField(verbose_name="4G(LTE)")
    G5 = models.BooleanField(verbose_name="5G")
    eSIM = models.BooleanField(verbose_name="eSIM")
    sim_num = models.PositiveIntegerField(verbose_name="Кількість слотів для sim карт")
    sim_type = models.CharField(max_length=10, choices=Sim_type.choices, verbose_name="Розмір sim карти")
    screen_diagonal = models.FloatField(validators=[MinValueValidator(0.01)] ,verbose_name="Діагональ екрану")
    screen_type = models.CharField(max_length = 30, choices=Screen_types.choices, verbose_name="Тип екрану")
    screen_refresh_rate = models.PositiveIntegerField(verbose_name="Частота оновлення екрану")
    resolution = models.CharField(max_length = 20, verbose_name="Роздільна здатність", validators=[RegexValidator(
        regex="\d+x\d+",
        message="Розширення екрану повинно бути такого типу: 1920x1080"
        ),])
    videocore = models.CharField(max_length = 50,  verbose_name="Відеоядро")
    RAM_size = models.PositiveIntegerField(verbose_name="Кількість оперативної памяті")
    MicroSD_aviable =  models.BooleanField(verbose_name="Наявність MicroSD")
    MicroSD_max = models.PositiveIntegerField(verbose_name="Максимальний розмір MicroSD", null=True, blank=True)
    storage = models.PositiveIntegerField(verbose_name="Кількість вбудованої памяті")
    processor = models.CharField(max_length = 50, verbose_name="Процессор")
    processor_hertz = models.FloatField(validators=[MinValueValidator(0.01)] ,verbose_name="Частота процессора")
    cores_num = models.IntegerField(verbose_name="Кількість ядер")
    OS = models.CharField(max_length = 14, choices = MobileOSes.choices, verbose_name="Операційна система")
    wifi_adapter = models.BooleanField(verbose_name="Wifi адаптер")
    bluetooth_adpter = models.BooleanField(verbose_name="Bluetooth адаптер")
    NFC = models.BooleanField(verbose_name="NFC")
    GPS = models.BooleanField(verbose_name="GPS")
    wireless_charging = models.BooleanField(verbose_name="Безпровідна зарядка")
    face_scaner = models.BooleanField(verbose_name="Розблокування за обличчям")
    flashlight = models.BooleanField(verbose_name="Фанарик")
    fingerprint_scaner = models.BooleanField(verbose_name="Сканер відбитку пальця")
    main_camera = ArrayField(models.PositiveIntegerField(), size=10, verbose_name="Основна камера")
    front_camera = models.PositiveIntegerField(verbose_name="Фронтальна камера")
    camera_features = ArrayField(models.CharField(max_length = 100), size=20, verbose_name="Особливосві камери")
    connectors_ports = ArrayField(models.CharField(max_length = 100), size=20, verbose_name="Розєми та порти")
    colour = models.CharField(max_length = 8, choices=CustomColours.choices, verbose_name="Колір")
    material = models.CharField(max_length = 15, choices=Material.choices, verbose_name="Матеріал")
    acumulator_size = models.IntegerField(verbose_name="Обєм акумулятора")

    width = models.FloatField(validators=[MinValueValidator(0.01)] ,verbose_name="Ширина")
    height = models.FloatField(validators=[MinValueValidator(0.01)] ,verbose_name="Висота")
    lenght = models.FloatField(validators=[MinValueValidator(0.01)] ,verbose_name="Довжина")
    weight = models.FloatField(validators=[MinValueValidator(0.01)] ,verbose_name="Вага")

    product = GenericRelation(Product, related_query_name='phone')

    

    @property
    def size(self):
        return f"{self.lenght}x{self.width}x{self.height}"
    size.fget.short_description = 'Розмір'

    @property
    def main_camera_num(self):
        return len(self.main_camera)
    main_camera_num.fget.short_description = "Кількість Основних Камер"

    @property
    def get_camera(self):
        return " + ".join([f"{i} Мп" for i in self.main_camera])
    get_camera.fget.short_description = 'Камери'


    @property
    def short_characteristics(self):
        return f"Екран: ({self.screen_diagonal} \
                {self.get_screen_type_display()} \
                {self.resolution}) / \
                {self.processor} \
                ({self.cores_num} x {self.processor_hertz} ГГц) / \
                Основна камера: {self.get_camera} ,\
                Фронтальна: {self.front_camera} Мп / \
                RAM {self.RAM_size} ГБ / \
                {self.storage} ГБ Вбудованої памяті {f'+ MicroSD (До {self.MicroSD_max} МБ)' if self.MicroSD_aviable else ''} / \
                {'3G / ' if self.G3 else ''}\
                {'LTE / ' if self.LTE else ''}\
                {'5G / ' if self.G5 else ''}\
                {'GPS / ' if self.GPS else ''}\
                {f'Підтримка {self.sim_num}x (self.sim_type)' if self.sim_num > 1 else f'{self.sim_type}'}\
                {', eSIM / ' if self.eSIM else ' / '}\
                {self.get_OS_display()} / \
                {self.size} мм/ \
                {self.acumulator_size} Ма"

    def clean(self):
        if self.MicroSD_aviable and self.MicroSD_max == None:
            raise ValidationError("Виберіть максимальну кількість памяті MicroSD")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефони'


