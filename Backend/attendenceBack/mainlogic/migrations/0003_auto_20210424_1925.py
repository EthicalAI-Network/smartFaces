# Generated by Django 3.1.1 on 2021-04-24 13:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainlogic', '0002_auto_20210424_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='students',
            field=models.ManyToManyField(null=True, related_name='Students', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='organization',
            name='teachers',
            field=models.ManyToManyField(null=True, related_name='Teachers', to=settings.AUTH_USER_MODEL),
        ),
    ]