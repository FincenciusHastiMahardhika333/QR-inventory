# Generated by Django 2.1.5 on 2019-05-31 22:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.TextField(blank=True)),
                ('desc', models.TextField(blank=True)),
                ('qrcode', models.ImageField(blank=True, upload_to='images/')),
                ('tag', models.CharField(max_length=100)),
                ('privacy', models.CharField(choices=[('Private', 'Private'), ('Public', 'Public')], default='Private', max_length=10)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
