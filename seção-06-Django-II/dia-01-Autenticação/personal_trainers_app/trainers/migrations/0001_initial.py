# Generated by Django 5.0.1 on 2024-01-31 19:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workout', models.TextField()),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='workout_plan', to='trainers.client')),
                ('personal_trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workout_plan', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
