# Generated by Django 4.0.1 on 2022-01-28 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('types', models.CharField(max_length=30)),
                ('image', models.CharField(blank=True, max_length=400)),
                ('description', models.TextField(max_length=1000)),
                ('number', models.CharField(blank=True, max_length=20)),
                ('expensive', models.CharField(blank=True, max_length=10)),
                ('location', models.TextField(max_length=30)),
                ('parking', models.CharField(blank=True, max_length=50)),
                ('childfriendly', models.CharField(blank=True, max_length=50)),
                ('outdoor', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='venues.venue')),
            ],
        ),
    ]
