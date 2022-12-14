# Generated by Django 4.0.6 on 2022-08-21 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playthrough',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Xenoblade Chronicles 3', 'Xenoblade Chronicles 3'), ('Xenoblade Chronicles 2', 'Xenoblade Chronicles 2'), ('Xenoblade Chronicles', 'Xenoblade Chronicles'), ('Cult of the Lamb', 'Cult of the Lamb'), ('Pokemon Platinum', 'Pokemon Platinum'), ('Pokemon Sapphire', 'Pokemon Sapphire'), ('Pokemon Ruby', 'Pokemon Ruby'), ('RimWorld', 'RimWorld'), ('Overwatch', 'Overwatch'), ('Stardew Valley', 'Stardew Valley'), ('Pokemon HeartGold', 'Pokemon HeartGold')], default=('Xenoblade Chronicles 3', 'Xenoblade Chronicles 3'), max_length=2000)),
            ],
        ),
    ]
