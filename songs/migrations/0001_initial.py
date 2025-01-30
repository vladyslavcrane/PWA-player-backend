# Generated by Django 5.0.6 on 2024-06-27 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('artist', models.CharField(max_length=255)),
                ('audio', models.FileField(upload_to='songs/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
