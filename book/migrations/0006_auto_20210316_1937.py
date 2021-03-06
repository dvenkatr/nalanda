# Generated by Django 3.1.6 on 2021-03-16 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20210315_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='blurb',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='review',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_for_this_book', to='book.book'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(blank=True, choices=[('4', 'Outstanding'), ('3', 'Good'), ('2', 'Not good'), ('1', 'Bad')], max_length=1),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100, unique=True)),
                ('book', models.ManyToManyField(to='book.Book')),
            ],
        ),
    ]
