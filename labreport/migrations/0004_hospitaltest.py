from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labreport', '0003_lab_test_time_required'),
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('time_required', models.CharField(default='1-2 hours', max_length=100)),
            ],
        ),
    ]
