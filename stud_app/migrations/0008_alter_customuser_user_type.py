# Generated by Django 5.0.7 on 2024-08-02 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stud_app', '0007_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'HOD'), (2, 'Staff'), (3, 'Student'), (4, 'Stut')], default=1, max_length=50),
        ),
    ]
