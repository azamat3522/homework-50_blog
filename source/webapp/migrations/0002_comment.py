# Generated by Django 2.2 on 2019-09-23 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=400, verbose_name='Комментарий')),
                ('author', models.CharField(blank=True, default='Аноним', max_length=40, null=True, verbose_name='Автор')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='webapp.Article', verbose_name='Статья')),
            ],
        ),
    ]
