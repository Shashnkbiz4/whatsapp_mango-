# Generated by Django 3.2 on 2023-04-17 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_staff'),
        ('chatbot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='staff',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='dashboard.staff'),
            preserve_default=False,
        ),
    ]
