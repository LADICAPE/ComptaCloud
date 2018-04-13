from django.db import models

# Create your models here.


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Compte(models.Model):
    compteid = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=45, blank=True, null=True)
    classe = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compte'


class Contrat(models.Model):
    userid = models.AutoField(primary_key=True)
    users_usersid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'contrat'
        unique_together = (('userid', 'users_usersid'),)


class Credits(models.Model):
    creditid = models.AutoField(primary_key=True)
    operation_operationid = models.IntegerField()
    compte_compteid = models.IntegerField()
    operation_typejournal_typejournalid = models.IntegerField()
    operation_travailleur_users_usersid = models.IntegerField(db_column='operation_TRAVAILLEUR_users_usersid')  # Field name made lowercase.
    operation_piece_pieceid = models.IntegerField()
    operation_travailleur_travailleurid = models.IntegerField()
    montant = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'credits'
        unique_together = (('creditid', 'operation_operationid', 'compte_compteid', 'operation_typejournal_typejournalid', 'operation_travailleur_users_usersid', 'operation_piece_pieceid', 'operation_travailleur_travailleurid'),)


class Debits(models.Model):
    debitsid = models.AutoField(primary_key=True)
    operation_operationid = models.IntegerField()
    compte_compteid = models.IntegerField()
    operation_typejournal_typejournalid = models.IntegerField()
    operation_travailleur_users_usersid = models.IntegerField(db_column='operation_TRAVAILLEUR_users_usersid')  # Field name made lowercase.
    operation_piece_pieceid = models.IntegerField()
    operation_travailleur_travailleurid = models.IntegerField()
    montant = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'debits'
        unique_together = (('debitsid', 'operation_operationid', 'compte_compteid', 'operation_typejournal_typejournalid', 'operation_travailleur_users_usersid', 'operation_piece_pieceid', 'operation_travailleur_travailleurid'),)


class Dfe(models.Model):
    userid = models.AutoField(primary_key=True)
    users_usersid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dfe'
        unique_together = (('userid', 'users_usersid'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

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


class Dsv(models.Model):
    userid = models.AutoField(primary_key=True)
    users_usersid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dsv'
        unique_together = (('userid', 'users_usersid'),)


class Operation(models.Model):
    operationid = models.AutoField(primary_key=True)
    typejournal_typejournalid = models.IntegerField()
    travailleur_users_usersid = models.IntegerField()
    piece_pieceid = models.IntegerField()
    travailleur_travailleurid = models.IntegerField()
    libelle = models.CharField(max_length=45, blank=True, null=True)
    montant = models.FloatField(blank=True, null=True)
    dateoperation = models.DateField(blank=True, null=True)
    datesaisie = models.DateField(blank=True, null=True)
    travailleuridsaisie = models.IntegerField(blank=True, null=True)
    travailleuridimpute = models.IntegerField(db_column='travailleurIdimpute', blank=True, null=True)  # Field name made lowercase.
    typejournalid = models.IntegerField(blank=True, null=True)
    pieceid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operation'
        unique_together = (('operationid', 'typejournal_typejournalid', 'travailleur_users_usersid', 'piece_pieceid', 'travailleur_travailleurid'),)


class Piece(models.Model):
    pieceid = models.AutoField(primary_key=True)
    code = models.CharField(max_length=45, blank=True, null=True)
    typepieceid = models.IntegerField(blank=True, null=True)
    lien = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'piece'


class Statut(models.Model):
    userid = models.AutoField(primary_key=True)
    users_usersid = models.IntegerField()
    denomination = models.CharField(max_length=45, blank=True, null=True)
    siege = models.CharField(max_length=45, blank=True, null=True)
    objet = models.CharField(max_length=45, blank=True, null=True)
    capital = models.FloatField(blank=True, null=True)
    durée = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statut'
        unique_together = (('userid', 'users_usersid'),)


class Travailleur(models.Model):
    travailleurid = models.AutoField(primary_key=True)
    users_usersid = models.IntegerField()
    nom = models.CharField(max_length=45, blank=True, null=True)
    prenom = models.CharField(max_length=45, blank=True, null=True)
    fonction = models.CharField(max_length=45, blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'travailleur'
        unique_together = (('travailleurid', 'users_usersid'),)


class Typejournal(models.Model):
    typejournalid = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typejournal'


class Typepiece(models.Model):
    typepieceid = models.AutoField(db_column='typepieceId', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typepiece'


class Users(models.Model):
    usersid = models.AutoField(primary_key=True)
    denomination = models.CharField(max_length=45, blank=True, null=True)
    siege = models.CharField(max_length=45, blank=True, null=True)
    objet = models.CharField(max_length=45, blank=True, null=True)
    capital = models.CharField(max_length=45, blank=True, null=True)
    duree = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

