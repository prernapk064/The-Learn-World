# Generated by Django 4.0.4 on 2022-05-27 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_todo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModifiedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('1', 'teacher'), ('2', 'student')], max_length=100)),
            ],
        ),
    ]
