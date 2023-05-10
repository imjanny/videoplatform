# Generated by Django 4.2.1 on 2023-05-10 00:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import hitcount.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('context', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d')),
                ('video', models.FileField(null=True, upload_to='')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('likes', models.ManyToManyField(default=0, related_name='likes_feed', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
            bases=(models.Model, hitcount.models.HitCountMixin),
        ),
    ]
