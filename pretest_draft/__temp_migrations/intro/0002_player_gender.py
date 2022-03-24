# Generated by Django 2.2.12 on 2022-03-23 09:11

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='gender',
            field=otree.db.models.IntegerField(choices=[[0, 'Männlich'], [1, 'Weiblich'], [2, 'Divers'], [3, 'Keine Angabe']], null=True, verbose_name='Mit welchem geschlecht identifizieren sie sich?'),
        ),
    ]
