# Generated by Django 3.2.20 on 2024-04-08 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.URLField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('note', models.TextField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='생성일')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='수정일')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Company_info', to='company.companyinfo')),
                ('labels', models.ManyToManyField(blank=True, to='contact.Label')),
            ],
        ),
    ]
