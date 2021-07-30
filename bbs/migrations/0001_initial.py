# Generated by Django 2.2.5 on 2021-07-28 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_title', models.CharField(max_length=30)),
                ('b_author', models.CharField(max_length=20)),
                ('b_content', models.CharField(max_length=1000)),
                ('b_date', models.DateTimeField(auto_now=True)),
                ('b_comment_count', models.IntegerField(default=0)),
                ('b_like_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_author', models.CharField(max_length=20)),
                ('c_content', models.CharField(max_length=100)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.Board')),
            ],
        ),
    ]
