# Generated by Django 4.2.5 on 2023-10-19 23:01

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
            name='CategoriaCurso',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(max_length=255)),
                ('descripcion_categoria', models.TextField()),
            ],
            options={
                'verbose_name': 'Categoría Curso',
                'verbose_name_plural': 'Categorías Curso',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id_curso', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_curso', models.CharField(max_length=255)),
                ('descripcion_curso', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('duracion', models.IntegerField()),
                ('horarios', models.CharField(max_length=255)),
                ('establecimiento', models.CharField(max_length=255)),
                ('costo', models.FloatField()),
                ('cupos_disponibles', models.IntegerField()),
                ('estado', models.BooleanField()),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categoriacurso')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id_estudiante', models.AutoField(primary_key=True, serialize=False)),
                ('dpi', models.CharField(max_length=14)),
                ('genero', models.CharField(max_length=10)),
                ('escolaridad', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=100)),
                ('etnia', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('edad', models.IntegerField()),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
            },
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id_inscripcion', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_inscripcion', models.DateField()),
                ('id_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.curso')),
                ('id_estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.estudiante')),
            ],
            options={
                'verbose_name': 'Inscripción',
                'verbose_name_plural': 'Inscripciones',
            },
        ),
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id_notificacion', models.AutoField(primary_key=True, serialize=False)),
                ('mensaje', models.CharField(max_length=255)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('id_inscripcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.inscripcion')),
            ],
            options={
                'verbose_name': 'Notificación',
                'verbose_name_plural': 'Notificaciones',
            },
        ),
        migrations.CreateModel(
            name='Favorito',
            fields=[
                ('id_favorito', models.AutoField(primary_key=True, serialize=False)),
                ('id_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.curso')),
                ('id_estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.estudiante')),
            ],
            options={
                'verbose_name': 'Favorito',
                'verbose_name_plural': 'Favoritos',
            },
        ),
    ]