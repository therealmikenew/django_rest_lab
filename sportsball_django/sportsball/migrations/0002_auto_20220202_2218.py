# Generated by Django 4.0.2 on 2022-02-02 22:18from django.db import migrations

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    def seed(apps, schema_editor):
        Player = apps.get_model('sportsball', 'Player')
        Team = apps.get_model('sportsball', 'Team')
        warriors = Team(name="Warriors", location='Queens',
                        conference='East Coast Tournament', wins=3, losses=67)
        warriors.save()

        Player(team=warriors, name="Carl Dungee",
               position='forward', age=23, injured_list=False).save()

    def fallow(apps, schema_editor):
        Player = apps.get_model('sportsball', 'Player')
        Team = apps.get_model('sportsball', 'Team')
        Team.objects.all().delete()
        Player.objects.all().delete()

    dependencies = [
        ('sportsball', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed, fallow)
    ]
