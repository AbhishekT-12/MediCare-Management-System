# Generated manually for the Admission model.

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctors', '0001_initial'),
        ('learnapp', '0003_fix_nullable_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('date_of_admitted', models.DateField()),
                ('date_of_discharge', models.DateField(blank=True, null=True)),
                ('room_type', models.CharField(choices=[('Common Ward', 'Common Ward'), ('Semi-Private', 'Semi-Private'), ('Private Non AC', 'Private Non AC'), ('Private AC', 'Private AC'), ('Deluxe', 'Deluxe')], default='Common Ward', max_length=50)),
                ('food_required', models.BooleanField(default=False)),
                ('total_days', models.PositiveIntegerField(blank=True, null=True)),
                ('doctor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admissions', to='doctors.alldoctors')),
                ('patient_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admissions', to='learnapp.userdetails')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admissions', to='doctors.treatment')),
            ],
        ),
    ]
