# Generated by Django 3.2.12 on 2022-03-21 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('year', models.IntegerField(default=2022)),
                ('semester', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('profId', models.CharField(max_length=3, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('modules', models.ManyToManyField(blank=True, related_name='professors', to='app.Module')),
            ],
        ),
        migrations.CreateModel(
            name='ProfRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='app.module')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='app.professor')),
            ],
        ),
    ]