# Generated by Django 5.1.1 on 2024-10-18 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_alter_event_organizer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, default='default_images/default_event.jpg', null=True, upload_to='event_images/'),
        ),
    ]