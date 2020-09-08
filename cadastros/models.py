# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    inicio = models.DateField(blank=True, null=True)
    fim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Centro(models.Model):
    centro = models.CharField(primary_key=True, max_length=7)
    nome = models.CharField(max_length=30, blank=True, null=True)
    despesa = models.CharField(max_length=1, blank=True, null=True)
    empresa = models.CharField(max_length=1, blank=True, null=True)
    nivel2 = models.CharField(max_length=3, blank=True, null=True)
    perfil = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        ordering = ['nome']
        managed = True
        db_table = 'centro'

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    cod_municipio = models.CharField(primary_key=True, max_length=7)
    municipio = models.CharField(max_length=80, blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    cod_estado = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        ordering = ['municipio']
        managed = False
        db_table = 'cidade'


class Contas(models.Model):
    banco = models.CharField(max_length=3, blank=True, null=True)
    agencia = models.CharField(max_length=4, blank=True, null=True)
    conta = models.CharField(primary_key=True, max_length=15, blank=True, null=False)
    obs1 = models.CharField(max_length=50, blank=True, null=True)
    obs2 = models.CharField(max_length=50, blank=True, null=True)
    saldoinicial = models.FloatField(blank=True, null=True)
    saldofinal = models.FloatField(blank=True, null=True)
    limite = models.FloatField(blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        ordering = ['conta']
        managed = False
        db_table = 'contas'

    def __str__(self):
        return self.conta



class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


def pegacentro():
    c = Centro.objects.all()
    Lista = []
    for ct in c:
        ct.centro
        ct.nome
        Lista.append([ct.centro,ct.nome])
    return Lista


class Fornecedor(models.Model):
    Estados = ( ('AC', 'ACRE'), ('AL', 'ALAGOAS'),
                ('AP','AMAPA'), ('AM','AMAZONAS'), ('BA','BAHIA'), ('CE','CEARA'), ('DF','DISTRITO FEDERAL'),
                ('ES','ESPIRITO SANTO'), ('GO','GOIAS'), ('MA','MARANHAO'), ('MT','MATO GROSSO'), ('MS','MATO GROSSO DO SUL'),
                ('MG','MINAS GERAIS'), ('PA','PARA'), ('PB','PARAIBA'), ('PR','PARANÁ'), ('PE','PERNAMBUCO'),
                ('PI','PIAUI'), ('RJ','RIO DE JANEIRO'), ('RN','R G NORTE'), ('RS','R G SUL'), ('RO','RONDONIA'),
                ('RR','RORAIMS'), ('SC','SANTA CATARINA'), ('SP','SAO PAULO'), ('SE','SERGIPE'), ('TO','TOCANTINS'),
    )
    codf = models.CharField(primary_key=True, max_length=5)
    nome = models.CharField(max_length=60)
    cnpj = models.CharField(max_length=18, blank=True, null=True)
    ende = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=30, blank=True, null=True)
    cidade = models.CharField(max_length=200, blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True, choices=Estados)
    cep = models.CharField(max_length=8, blank=True, null=True)
    ddd = models.CharField(max_length=3, blank=True, null=True)
    fone = models.CharField(max_length=11, blank=True, null=True)
    inscricao = models.CharField(max_length=18, blank=True, null=True)
    contato = models.CharField(max_length=20, blank=True, null=True)
    fonecont = models.CharField(max_length=11, blank=True, null=True)
    fax = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(max_length=60, blank=True, null=True)
    obs1 = models.CharField(max_length=50, blank=True, null=True)
    obs2 = models.CharField(max_length=50, blank=True, null=True)
    cadastro = models.DateField(blank=True, null=True)
    compra = models.DateField(blank=True, null=True)
    email1 = models.CharField(max_length=60, blank=True, null=True)
    perfil = models.CharField(max_length=1, blank=True, null=True)
    centro = models.ForeignKey(Centro, null=True, blank=True, db_column='centro', on_delete=models.PROTECT)

    class Meta:
        ordering = ['nome']
        managed = True
        db_table = 'fornecedor'

    def __str__(self):
        return self.nome


class Grupo(models.Model):
    grupo = models.CharField(primary_key=True, max_length=2)
    nome = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'grupo'

    def __str__(self):
        return self.nome

class Intervalo(models.Model):
    user = models.CharField(max_length=40)
    pagini = models.DateField(blank=True, null=True)
    pagfim = models.DateField(blank=True, null=True)
    lctini = models.DateField(blank=True, null=True)
    lctfim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intervalo'

    def __str__(self):
        return self.user


class Lancamento(models.Model):
    conta = models.CharField(max_length=15, blank=True, null=True)
    historico = models.CharField(max_length=30, blank=True, null=True)
    documento = models.CharField(max_length=10, blank=True, null=True)
    centrocusto = models.CharField(max_length=7, blank=True, null=True)
    caiu = models.CharField(max_length=1, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    dia = models.DateField(blank=True, null=True)
    lancamento = models.AutoField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'lancamento'


class Pagar(models.Model):
    pagnume = models.AutoField(primary_key=True)
    pagnota = models.CharField(max_length=12, blank=True, null=True)
    pagcodf = models.ForeignKey(Fornecedor, models.DO_NOTHING, db_column='pagcodf', blank=True, null=True)
    pagdupli = models.CharField(max_length=12, blank=True, null=True)
    pagbanc = models.CharField(max_length=12, blank=True, null=True)
    pagcheq = models.CharField(max_length=7, blank=True, null=True)
    pagcont = models.CharField(max_length=9, blank=True, null=True)
    pagsitu = models.CharField(max_length=1, blank=True, null=True)
    pagcomo = models.CharField(max_length=20, blank=True, null=True)
    pagcent = models.ForeignKey(Centro, models.DO_NOTHING, db_column='pagcent', blank=True, null=True)
    pagconta = models.ForeignKey(Contas, models.DO_NOTHING, db_column='pagconta', max_length=10, blank=True, null=True)
    pagobs = models.CharField(max_length=200, blank=True, null=True)
    pagvalor = models.FloatField(blank=True, null=True)
    pagvalp = models.FloatField(blank=True, null=True)
    pagdesc = models.FloatField(blank=True, null=True)
    pagtaxa = models.FloatField(blank=True, null=True)
    pagabat = models.FloatField(blank=True, null=True)
    pagdata = models.DateField(blank=True, null=True)
    pagvenc = models.DateField(blank=True, null=True)
    pagpaga = models.DateField(blank=True, null=True)
    paglimi = models.DateField(blank=True, null=True)
    nume = models.CharField(db_column='NUME', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pagar'
