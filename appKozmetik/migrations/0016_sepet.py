# Generated by Django 4.2.1 on 2023-06-24 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appKozmetik', '0015_profil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sepet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adet', models.IntegerField(blank=True, max_length=50, null=True, verbose_name='adet')),
                ('allprice', models.FloatField(verbose_name='Toplam\xa0Fiyat')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appKozmetik.product', verbose_name='Ürün')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
    ]
