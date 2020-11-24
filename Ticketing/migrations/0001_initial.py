# Generated by Django 3.1.3 on 2020-11-24 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Profile', 'PROFILE'), ('Employee Management', 'EMPLOYEE MANAGEMENT'), ('Goals and Competencies', 'GOALS AND COMPETENCIES'), ('Appraisals', 'APPRAISALS'), ('Trainings', 'TRAININGS'), ('Reports', 'REPORTS'), ('Ticketing', 'TICKETING'), ('Guide', 'GUIDE'), ('Careers', 'CAREERS'), ('Others', 'OTHERS')], max_length=30)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=5000, null=True)),
                ('status', models.CharField(default='Pending', max_length=50)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket_Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('ticket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Ticketing.ticket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.profile')),
            ],
        ),
    ]
