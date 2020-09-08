# Generated by Django 3.0.7 on 2020-07-14 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Centro',
            fields=[
                ('centro', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=30, null=True)),
                ('despesa', models.CharField(blank=True, max_length=1, null=True)),
                ('empresa', models.CharField(blank=True, max_length=1, null=True)),
                ('nivel2', models.CharField(blank=True, max_length=3, null=True)),
                ('perfil', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'centro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('cod_municipio', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('municipio', models.CharField(blank=True, max_length=80, null=True)),
                ('estado', models.CharField(blank=True, max_length=2, null=True)),
                ('cod_estado', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'db_table': 'cidade',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequencial', models.IntegerField()),
                ('banco', models.CharField(blank=True, max_length=3, null=True)),
                ('agencia', models.CharField(blank=True, max_length=4, null=True)),
                ('conta', models.CharField(blank=True, max_length=15, null=True)),
                ('obs1', models.CharField(blank=True, max_length=50, null=True)),
                ('obs2', models.CharField(blank=True, max_length=50, null=True)),
                ('saldoinicial', models.FloatField(blank=True, null=True)),
                ('saldofinal', models.FloatField(blank=True, null=True)),
                ('limite', models.FloatField(blank=True, null=True)),
                ('tipo', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'contas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('codf', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=60)),
                ('cnpj', models.CharField(blank=True, max_length=18, null=True)),
                ('ende', models.CharField(blank=True, max_length=100, null=True)),
                ('bairro', models.CharField(blank=True, max_length=30, null=True)),
                ('cidade', models.CharField(blank=True, max_length=200, null=True)),
                ('estado', models.CharField(blank=True, max_length=2, null=True)),
                ('cep', models.CharField(blank=True, max_length=8, null=True)),
                ('ddd', models.CharField(blank=True, max_length=3, null=True)),
                ('fone', models.CharField(blank=True, max_length=11, null=True)),
                ('inscricao', models.CharField(blank=True, max_length=18, null=True)),
                ('contato', models.CharField(blank=True, max_length=20, null=True)),
                ('fonecont', models.CharField(blank=True, max_length=11, null=True)),
                ('fax', models.CharField(blank=True, max_length=11, null=True)),
                ('email', models.CharField(blank=True, max_length=60, null=True)),
                ('obs1', models.CharField(blank=True, max_length=50, null=True)),
                ('obs2', models.CharField(blank=True, max_length=50, null=True)),
                ('cadastro', models.DateField(blank=True, null=True)),
                ('compra', models.DateField(blank=True, null=True)),
                ('email1', models.CharField(blank=True, max_length=60, null=True)),
                ('perfil', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'fornecedor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('grupo', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'grupo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lancamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lancamento', models.CharField(max_length=6)),
                ('conta', models.CharField(blank=True, max_length=15, null=True)),
                ('historico', models.CharField(blank=True, max_length=30, null=True)),
                ('documento', models.CharField(blank=True, max_length=10, null=True)),
                ('centrocusto', models.CharField(blank=True, max_length=7, null=True)),
                ('caiu', models.CharField(blank=True, max_length=1, null=True)),
                ('valor', models.FloatField(blank=True, null=True)),
                ('dia', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'lancamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pagar',
            fields=[
                ('pagnume', models.AutoField(primary_key=True, serialize=False)),
                ('pagnota', models.CharField(blank=True, max_length=12, null=True)),
                ('pagdupli', models.CharField(blank=True, max_length=12, null=True)),
                ('pagbanc', models.CharField(blank=True, max_length=12, null=True)),
                ('pagcheq', models.CharField(blank=True, max_length=7, null=True)),
                ('pagcont', models.CharField(blank=True, max_length=9, null=True)),
                ('pagsitu', models.CharField(blank=True, max_length=1, null=True)),
                ('pagcomo', models.CharField(blank=True, max_length=20, null=True)),
                ('pagcent', models.CharField(blank=True, max_length=7, null=True)),
                ('pagconta', models.CharField(blank=True, max_length=10, null=True)),
                ('pagobs', models.CharField(blank=True, max_length=200, null=True)),
                ('pagvalor', models.FloatField(blank=True, null=True)),
                ('pagvalp', models.FloatField(blank=True, null=True)),
                ('pagdesc', models.FloatField(blank=True, null=True)),
                ('pagtaxa', models.FloatField(blank=True, null=True)),
                ('pagabat', models.FloatField(blank=True, null=True)),
                ('pagdata', models.DateField(blank=True, null=True)),
                ('pagvenc', models.DateField(blank=True, null=True)),
                ('pagpaga', models.DateField(blank=True, null=True)),
                ('paglimi', models.DateField(blank=True, null=True)),
                ('nume', models.CharField(blank=True, db_column='NUME', max_length=6, null=True)),
            ],
            options={
                'db_table': 'pagar',
                'managed': False,
            },
        ),
    ]
