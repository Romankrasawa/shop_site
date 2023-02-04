# Generated by Django 4.1.4 on 2023-02-01 20:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shop.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0002_remove_category_id_alter_category_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('adress', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='Адресса магазину/складу')),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('photo', models.ImageField(default='default/default_banner.jpg', upload_to=shop.models.banner_file_name, verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Баннер',
                'verbose_name_plural': 'Баннери',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', models.TextField(verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Створено')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Оновлено')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='Продукт')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Користувач')),
            ],
        ),
    ]
