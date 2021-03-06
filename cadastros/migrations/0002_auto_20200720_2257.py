# Generated by Django 3.0.8 on 2020-07-21 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='centro',
            options={'managed': True, 'ordering': ['nome']},
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='email',
            field=models.EmailField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='estado',
            field=models.CharField(blank=True, choices=[('AC', 'ACRE'), ('AL', 'ALAGOAS'), ('AP', 'AMAPA'), ('AM', 'AMAZONAS'), ('BA', 'BAHIA'), ('CE', 'CEARA'), ('DF', 'DISTRITO FEDERAL'), ('ES', 'ESPIRITO SANTO'), ('GO', 'GOIAS'), ('MA', 'MARANHAO'), ('MT', 'MATO GROSSO'), ('MS', 'MATO GROSSO DO SUL'), ('MG', 'MINAS GERAIS'), ('PA', 'PARA'), ('PB', 'PARAIBA'), ('PR', 'PARANÁ'), ('PE', 'PERNAMBUCO'), ('PI', 'PIAUI'), ('RJ', ''), ('RN', 'R G NORTE'), ('RS', 'R G SUL'), ('RO', 'RONDONIA'), ('RR', 'RORAIMS'), ('SC', 'SANTA CATARINA'), ('SP', 'SAO PAULO'), ('SE', 'SERGIPE'), ('TO', 'TOCANTINS')], max_length=2, null=True),
        ),
    ]
