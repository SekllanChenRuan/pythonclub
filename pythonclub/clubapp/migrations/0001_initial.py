# Generated by Django 2.2 on 2019-04-23 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meetingtitle', models.CharField(max_length=255)),
                ('meetingdate', models.DateField()),
                ('meetingtime', models.TimeField()),
                ('location', models.CharField(max_length=255)),
                ('agenda', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'meetings',
                'db_table': 'meeting',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resourcename', models.CharField(max_length=255)),
                ('resourcetype', models.CharField(max_length=255)),
                ('resourceurl', models.URLField(blank=True, null=True)),
                ('dateentry', models.DateField()),
                ('resourcedescription', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Resources',
                'db_table': 'Resource',
            },
        ),
        migrations.CreateModel(
            name='MeetingMinute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minutestext', models.TextField()),
                ('attendance', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clubapp.Meeting')),
            ],
            options={
                'verbose_name_plural': 'meetingminutes',
                'db_table': 'meetingminute',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventtitle', models.CharField(max_length=255)),
                ('eventlocation', models.CharField(max_length=255)),
                ('dateentry', models.DateField()),
                ('eventtime', models.TimeField()),
                ('eventdescription', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Events',
                'db_table': 'Event',
            },
        ),
    ]
