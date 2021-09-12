# Generated by Django 3.2.7 on 2021-09-09 18:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('custom_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.IntegerField(default=0, verbose_name='the sum of a transaction')),
                ('date', models.DateField(auto_now_add=True, verbose_name='transaction date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_user.customuser', verbose_name='sender')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
            },
        ),
    ]