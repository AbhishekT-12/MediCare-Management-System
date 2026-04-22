from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labreport', '0002_rename_pateint_name_lab_test_patient_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab_test',
            name='time_required',
            field=models.CharField(
                default='1-2 hours',
                help_text='Estimated time to complete the test',
                max_length=100,
            ),
        ),
    ]
