from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='room_type',
            field=models.CharField(choices=[('Common Ward', 'Common Ward'), ('Semi-Private', 'Semi-Private'), ('Private Non AC', 'Private Non AC'), ('Private AC', 'Private AC'), ('Deluxe', 'Deluxe')], default='Common Ward', max_length=50),
        ),
    ]
