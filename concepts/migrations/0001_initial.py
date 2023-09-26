# Generated by Django 4.2.4 on 2023-09-20 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('definition', models.CharField(max_length=255, verbose_name='Определение')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Картинка')),
                ('antonym', models.ManyToManyField(blank=True, to='concepts.concept')),
                ('association', models.ManyToManyField(blank=True, to='concepts.concept')),
                ('synonym', models.ManyToManyField(blank=True, to='concepts.concept')),
            ],
        ),
    ]