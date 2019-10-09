# Generated by Django 2.2.6 on 2019-10-06 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0004_auto_20191006_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apostila',
            name='pdf',
            field=models.FileField(blank=True, upload_to='pdfs'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='descricao',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='imagem',
            field=models.FileField(blank=True, null=True, upload_to='imagens', verbose_name='Imagem'),
        ),
    ]