# Generated by Django 4.0.5 on 2022-06-14 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0011_remove_teammember_insta_link_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsletter',
            old_name='Email',
            new_name='email',
        ),
        migrations.AlterField(
            model_name='social_team',
            name='social',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_team', to='Service.teammember'),
        ),
    ]
