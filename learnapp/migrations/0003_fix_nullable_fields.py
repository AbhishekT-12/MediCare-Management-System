from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('learnapp', '0002_alter_userdetails_userpic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='phone',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='zipcode',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='street',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='state',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]