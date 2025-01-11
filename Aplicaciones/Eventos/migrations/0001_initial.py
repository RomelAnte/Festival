# Generated by Django 4.2.7 on 2025-01-11 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id_entrada', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad', models.IntegerField()),
                ('estado', models.BooleanField(default=True)),
                ('fechaCreacion', models.DateTimeField()),
                ('fechaActualizacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id_festival', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=255)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('descripcion', models.TextField()),
                ('estado', models.BooleanField(default=True)),
                ('fechaCreacion', models.DateTimeField()),
                ('fechaActualizacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id_tipo_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('estado', models.BooleanField(default=True)),
                ('fechaCreacion', models.DateTimeField()),
                ('fechaActualizacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('ci', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('contraseña', models.CharField(max_length=255)),
                ('estado', models.BooleanField(default=True)),
                ('creado_en', models.DateTimeField()),
                ('actualizado_en', models.DateTimeField(auto_now=True)),
                ('tipo_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eventos.tipousuario')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateTimeField()),
                ('estado', models.BooleanField(default=True)),
                ('fechaCreacion', models.DateTimeField()),
                ('fechaActualizacion', models.DateTimeField(auto_now_add=True)),
                ('entrada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eventos.entrada')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eventos.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Presentacion',
            fields=[
                ('id_presentacion', models.AutoField(primary_key=True, serialize=False)),
                ('escenario', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField()),
                ('duracion', models.IntegerField()),
                ('estado', models.BooleanField(default=True)),
                ('fechaCreacion', models.DateTimeField()),
                ('fechaActualizacion', models.DateTimeField(auto_now_add=True)),
                ('festival', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eventos.festival')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eventos.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='festival',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eventos.usuario'),
        ),
        migrations.AddField(
            model_name='entrada',
            name='festival',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eventos.festival'),
        ),
        migrations.CreateModel(
            name='Biografía',
            fields=[
                ('id_biografia', models.AutoField(primary_key=True, serialize=False)),
                ('biografia', models.TextField()),
                ('estado', models.BooleanField(default=True)),
                ('fechaCreacion', models.DateTimeField()),
                ('fechaActualizacion', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eventos.usuario')),
            ],
        ),
    ]