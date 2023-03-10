# Generated by Django 4.1.5 on 2023-02-01 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_tag_rename_user_clip_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='clip',
            name='tags',
            field=models.ManyToManyField(related_name='clips', to='main_app.tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
