# Generated by Django 2.2.6 on 2020-01-20 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0001_initial'),
        ('accounts', '0002_staff_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=350)),
                ('description', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Classification',
                'verbose_name_plural': 'Classifications',
            },
        ),
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Purpose',
                'verbose_name_plural': 'Purposes',
            },
        ),
        migrations.CreateModel(
            name='VisitorRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_name', models.CharField(max_length=350)),
                ('address', models.CharField(max_length=350)),
                ('city', models.CharField(max_length=350)),
                ('state', models.CharField(max_length=350)),
                ('country', models.CharField(max_length=350)),
                ('email', models.CharField(max_length=350)),
                ('phone_contact', models.CharField(max_length=350)),
                ('picture', models.ImageField(upload_to='images/')),
                ('signature', models.ImageField(upload_to='signature/')),
                ('date', models.DateField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.Classification')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.Department')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Position')),
                ('purpose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.Purpose')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Staff')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Title')),
            ],
            options={
                'verbose_name': 'VisitorRegistration',
                'verbose_name_plural': 'VisitorRegistrations',
            },
        ),
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_name', models.CharField(max_length=350)),
                ('phone_number', models.CharField(max_length=350)),
                ('email', models.CharField(max_length=350)),
                ('active_from', models.DateTimeField()),
                ('active_to', models.DateTimeField()),
                ('invited_by', models.CharField(max_length=350)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Position')),
                ('purpose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.Purpose')),
            ],
            options={
                'verbose_name': 'Invite',
                'verbose_name_plural': 'Invites',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_name', models.CharField(max_length=350)),
                ('appointmwnt_date', models.DateTimeField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('purpose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.Purpose')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Status')),
            ],
            options={
                'verbose_name': 'Appointment',
                'verbose_name_plural': 'Appointments',
            },
        ),
    ]
