# Generated by Django 5.2 on 2025-04-09 09:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chatbot', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='sellers',
            name='admin',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller_admin_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='products',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_seller_id', to='chatbot.sellers'),
        ),
        migrations.AddField(
            model_name='peti',
            name='seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='chatbot.sellers'),
        ),
        migrations.AddField(
            model_name='contacts',
            name='cust_lead',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chatbot.sellers'),
        ),
    ]
