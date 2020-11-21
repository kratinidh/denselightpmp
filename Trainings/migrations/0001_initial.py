# Generated by Django 3.0.6 on 2020-08-10 07:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Profile', '0001_initial'),
        ('Appraisals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='skill_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Trainings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('provider', models.CharField(blank=True, max_length=150, null=True)),
                ('cost', models.FloatField(blank=True, max_length=150, null=True)),
                ('ratings', models.FloatField(blank=True, max_length=10, null=True)),
                ('skill_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Trainings.skill_category')),
            ],
        ),
        migrations.CreateModel(
            name='Training_Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('provider', models.CharField(blank=True, max_length=150, null=True)),
                ('cost', models.FloatField(blank=True, max_length=150, null=True)),
                ('ratings', models.FloatField(blank=True, max_length=10, null=True)),
                ('skill_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Trainings.skill_category')),
            ],
        ),
        migrations.CreateModel(
            name='Survey_Trainings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectives_met', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('content_design', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('trainer_knowledge', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('training_relevance', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('recommend_training', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('training', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Trainings.Trainings')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('weightage', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('recommended_Trainings_user', models.CharField(default='NIL', max_length=1000)),
                ('recommended_Trainings_manager', models.CharField(default='NIL', max_length=1000)),
                ('recommended_Trainings_board', models.CharField(default='NIL', max_length=1000)),
                ('user_rating', models.IntegerField(choices=[(1, '1 - Major Improvement Needed'), (2, '2 - Needs Improvement'), (3, '3 - Meets Expectations'), (4, '4 - Exceeds Expectations'), (5, '5 - Far Exceed Expectations')], default=1)),
                ('manager_rating', models.IntegerField(choices=[(1, '1 - Major Improvement Needed'), (2, '2 - Needs Improvement'), (3, '3 - Meets Expectations'), (4, '4 - Exceeds Expectations'), (5, '5 - Far Exceed Expectations')], default=1)),
                ('board_rating', models.IntegerField(choices=[(1, '1 - Major Improvement Needed'), (2, '2 - Needs Improvement'), (3, '3 - Meets Expectations'), (4, '4 - Exceeds Expectations'), (5, '5 - Far Exceed Expectations')], default=1)),
                ('user_comments', models.CharField(default='NIL', max_length=2000)),
                ('manager_comments', models.CharField(default='NIL', max_length=2000)),
                ('board_comments', models.CharField(default='NIL', max_length=2000)),
                ('appraisal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Appraisals.User_Appraisal_List')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Profile.Profile')),
                ('skill_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Trainings.skill_category')),
            ],
        ),
        migrations.CreateModel(
            name='Career_Discussion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Q1', models.CharField(default='NIL', max_length=5000)),
                ('Q2', models.CharField(default='NIL', max_length=5000)),
                ('Q3', models.CharField(default='NIL', max_length=5000)),
                ('Q4', models.CharField(default='NIL', max_length=5000)),
                ('Q5', models.CharField(default='NIL', max_length=5000)),
                ('Q6', models.CharField(default='NIL', max_length=5000)),
                ('Q7', models.CharField(default='NIL', max_length=5000)),
                ('Q8', models.CharField(default='NIL', max_length=5000)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.Profile')),
                ('user_appraisal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Appraisals.User_Appraisal_List')),
            ],
        ),
        migrations.CreateModel(
            name='Apply_Trainings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Rejected', 'REJECTED'), ('Pending', 'PENDING'), ('Approved', 'APPROVED'), ('Completed', 'COMPLETED')], max_length=50)),
                ('date_start', models.DateField(blank=True, null=True)),
                ('date_end', models.DateField(blank=True, null=True)),
                ('approved_by', models.CharField(blank=True, max_length=200, null=True)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Profile.Profile')),
                ('training', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Trainings.Trainings')),
            ],
        ),
    ]
