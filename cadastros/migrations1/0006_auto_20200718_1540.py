# Generated by Django 3.0.8 on 2020-07-18 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0005_auto_20200715_2350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='centro',
            options={'managed': True},
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='centro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cadastros.Centro'),
        ),
    ]
