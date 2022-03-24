# Generated by Django 2.2.12 on 2022-03-23 09:23

from django.db import migrations, models
import django.db.models.deletion
import otree.db.idmap
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mpl_main_group', to='otree.Session')),
            ],
            options={
                'db_table': 'MPL_main_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mpl_main_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'MPL_main_subsession',
            },
            bases=(models.Model, otree.db.idmap.SubsessionIDMapMixin),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_role', otree.db.models.StringField(max_length=10000, null=True)),
                ('right_side_amount_RTF', otree.db.models.CurrencyField(default=15, null=True)),
                ('switching_point_RTF', otree.db.models.CurrencyField(null=True)),
                ('comm_2_RTF', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='Platz für Kommentare, falls Ihnen die Beschreibungen auf dieser Seite unklar erscheinen')),
                ('comm_3_RTF', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='Platz für Kommentare, falls Ihnen die Beschreibungen auf dieser Seite unklar erscheinen')),
                ('comm_4_RTF', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='Platz für Kommentare, falls Ihnen die Fragen auf dieser Seite unklar erscheinen')),
                ('right_side_amount_HER', otree.db.models.CurrencyField(default=15, null=True)),
                ('switching_point_HER', otree.db.models.CurrencyField(null=True)),
                ('comm_1_HER', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='Platz für Kommentare, falls Ihnen die Beschreibungen auf dieser Seite unklar erscheinen')),
                ('comm_2_HER', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='Platz für Kommentare, falls Ihnen die Beschreibungen auf dieser Seite unklar erscheinen')),
                ('comm_3_HER', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='Platz für Kommentare, falls Ihnen die Fragen auf dieser Seite unklar erscheinen')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MPL_main.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mpl_main_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mpl_main_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MPL_main.Subsession')),
            ],
            options={
                'db_table': 'MPL_main_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MPL_main.Subsession'),
        ),
    ]
