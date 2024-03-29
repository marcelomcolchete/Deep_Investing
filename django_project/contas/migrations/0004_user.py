# Generated by Django 3.0.3 on 2020-03-09 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0003_auto_20200227_1003'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createData', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
