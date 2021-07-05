# Generated by Django 3.2.4 on 2021-07-05 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-uploaded_at']},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='logo.png', upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='year_taken',
            field=models.DateField(null=True),
        ),
    ]