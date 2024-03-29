# Generated by Django 4.0.5 on 2022-06-28 09:15

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(max_length=15)),
                ('birth_day', models.DateField()),
                ('gender', model_utils.fields.StatusField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=100, no_check_for_status=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='xodim/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'Xodimlar',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('course_duration', model_utils.fields.StatusField(choices=[('30 daqiqa', '30 daqiqa'), ('40 daqiqa', '40 daqiqa'), ('60 daqiqa', '60 daqiqa'), ('90 daqiqa', '90 daqiqa'), ('120 daqiqa', '120 daqiqa'), ('180 daqiqa', '180 daqiqa'), ('240 daqiqa', '240 daqiqa'), ('280 daqiqa', '280 daqiqa'), ('300 daqiqa', '300 daqiqa')], default='30 daqiqa', max_length=100, no_check_for_status=True)),
                ('cost', models.FloatField(default=0)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Harajatturi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='IshHaqqiTuri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Roll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Xarajat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('oluvchi', models.CharField(max_length=50)),
                ('cost', models.FloatField()),
                ('xarajat_turi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='markaz.harajatturi')),
            ],
        ),
        migrations.CreateModel(
            name='IshHaqqi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miqdor', models.IntegerField()),
                ('cource', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='markaz.course')),
                ('ish_haqqi_turi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='markaz.ishhaqqituri')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lesson_time', models.TimeField()),
                ('beginning_date', models.DateField()),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='markaz.course')),
                ('days', models.ManyToManyField(to='markaz.day')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='markaz.room')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='roll',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='markaz.roll'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('bio', models.TextField()),
                ('come_date', models.DateField(auto_now_add=True)),
                ('guruh', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='markaz.group')),
            ],
            options={
                'verbose_name': 'Student',
            },
            bases=('markaz.employee',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', model_utils.fields.StatusField(choices=[('Naqt pul', 'Naqt pul'), ('UZCARD', 'UZCARD'), ('Bank hisobi', 'Bank hisobi')], default='Naqt pul', max_length=100, no_check_for_status=True)),
                ('quantity', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
                ('comment', models.TextField()),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='markaz.student')),
            ],
        ),
    ]
