from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

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
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

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


class BrideUser(models.Model):
    principal_id = models.BigIntegerField(primary_key=True)
    key = models.CharField(unique=True, max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.CharField(max_length=254)
    description = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bride_user'


class Carrier(models.Model):
    carrier_id = models.FloatField(primary_key=True)
    accronym = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    appl = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carrier'

    def __str__(self):
        return self.carrier_id, self.accronym, self.name


class ChangeRequest(models.Model):
    change_request_id = models.FloatField(primary_key=True)
    request_type = models.CharField(max_length=20, blank=True, null=True)
    rule_artifact_type = models.CharField(max_length=20, blank=True, null=True)
    report = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    rule_artifact_id = models.FloatField(blank=True, null=True)
    request_time = models.DateTimeField(blank=True, null=True)
    resolved_time = models.DateTimeField(blank=True, null=True)
    requester = models.CharField(max_length=100, blank=True, null=True)
    resolver = models.CharField(max_length=100, blank=True, null=True)
    request_content = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'change_request'


class ClaimsDeplRulePkgAudit(models.Model):
    claims_depl_rule_pkg_audit_id = models.BigIntegerField(primary_key=True)
    rule_package_id = models.BigIntegerField()
    irl = models.TextField(blank=True, null=True)
    deploy_date = models.DateField()
    user_name = models.CharField(max_length=50)
    comments = models.CharField(max_length=100, blank=True, null=True)
    action = models.CharField(max_length=50, blank=True, null=True)
    time_stamp = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'claims_depl_rule_pkg_audit'


class ClaimsDeployedRulePkg(models.Model):
    rule_package_id = models.BigIntegerField(primary_key=True)
    irl = models.TextField()
    deploy_date = models.DateField()
    user_name = models.CharField(max_length=50)
    comments = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'claims_deployed_rule_pkg'


class County(models.Model):
    county_id = models.FloatField(primary_key=True)
    state_id = models.FloatField(blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    appl = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'county'


class DecisionTable(models.Model):
    decision_table_id = models.BigIntegerField(primary_key=True)
    rule_store = models.ForeignKey('RuleStore', models.DO_NOTHING, blank=True, null=True)
    treatment_category_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True, null=True)
    active_ind = models.CharField(max_length=1)
    html_display_content = models.TextField(blank=True, null=True)
    num_of_rows = models.IntegerField()
    taggregation = models.ForeignKey('Taggregation', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'decision_table'


class DecisionTableAudit(models.Model):
    decision_table_audit_id = models.BigIntegerField(primary_key=True)
    decision_table_id = models.BigIntegerField()
    rule_store_id = models.BigIntegerField(blank=True, null=True)
    treatment_category_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True, null=True)
    active_ind = models.CharField(max_length=1)
    html_display_content = models.TextField(blank=True, null=True)
    num_of_rows = models.IntegerField()
    time_stamp = models.DateField(blank=True, null=True)
    action = models.CharField(max_length=50, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'decision_table_audit'


class DecisionTableSnapshot(models.Model):
    decision_table_snapshot_id = models.FloatField(primary_key=True)
    decision_table_id = models.FloatField()
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    rule_store_id = models.FloatField(blank=True, null=True)
    num_of_rows = models.IntegerField(blank=True, null=True)
    active_ind = models.CharField(max_length=1, blank=True, null=True)
    html_display_content = models.TextField(blank=True, null=True)
    treatment_category_id = models.FloatField(blank=True, null=True)
    time_stamp = models.DateField(blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'decision_table_snapshot'


class DentalProcedure(models.Model):
    dental_procedure_id = models.FloatField(primary_key=True)
    admin_plan_id = models.FloatField(blank=True, null=True)
    active_ind = models.CharField(max_length=1, blank=True, null=True)
    remark_required_ind = models.CharField(max_length=1, blank=True, null=True)
    radiograph_required_ind = models.CharField(max_length=1, blank=True, null=True)
    ignore_gen_dup_ind = models.CharField(max_length=1, blank=True, null=True)
    update_npf_ind = models.CharField(max_length=1, blank=True, null=True)
    allow_multi_tooth_ind = models.CharField(max_length=1, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    npf_term_date = models.DateField(blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    tooth_num_sys_type = models.CharField(max_length=50, blank=True, null=True)
    nomenclature = models.CharField(max_length=175, blank=True, null=True)
    short_description = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=2000, blank=True, null=True)
    remarks = models.CharField(max_length=2000, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    appl = models.CharField(max_length=50, blank=True, null=True)
    routine_procedure_desc = models.CharField(max_length=100, blank=True, null=True)
    routine_procedure_ind = models.CharField(max_length=1, blank=True, null=True)
    routine_procedure_sort_order = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dental_procedure'


class DeployedRulePackage(models.Model):
    rule_package_id = models.BigIntegerField(primary_key=True)
    irl = models.TextField(blank=True, null=True)
    generate_date = models.DateField(blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    approved_ind = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deployed_rule_package'


class DeployedRuleset(models.Model):
    deployed_ruleset_id = models.BigIntegerField(primary_key=True)
    ruleset = models.TextField(blank=True, null=True)
    last_update_date = models.DateField(blank=True, null=True)
    rule_store = models.ForeignKey('RuleStore', models.DO_NOTHING, blank=True, null=True)
    xrl_format_ind = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deployed_ruleset'


class DeploymentTarget(models.Model):
    deployment_target_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    port_number = models.IntegerField()
    server_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'deployment_target'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Document(models.Model):
    document_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    taggregation_id = models.BigIntegerField(blank=True, null=True)
    folder = models.ForeignKey('Folder', models.DO_NOTHING, blank=True, null=True, related_name='document_folder_folder')

    class Meta:
        managed = False
        db_table = 'document'


class DtblTemplate(models.Model):
    dtbl_template_id = models.BigIntegerField(primary_key=True)
    rule_store = models.ForeignKey('RuleStore', models.DO_NOTHING)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    content = models.BinaryField(blank=True, null=True)
    taggregation = models.ForeignKey('Taggregation', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dtbl_template'


class DtblTranslatedRule(models.Model):
    dtbl_translated_rule_id = models.BigIntegerField(primary_key=True)
    decision_table = models.ForeignKey(DecisionTable, models.DO_NOTHING)
    translated_rule_name = models.CharField(max_length=200)
    row_number = models.BigIntegerField()
    target_lang_type = models.CharField(max_length=50)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'dtbl_translated_rule'


class Environment(models.Model):
    environment_id = models.FloatField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'environment'


class EtsDeplRulesetAudit(models.Model):
    ets_depl_ruleset_audit_id = models.FloatField(primary_key=True)
    rule_package_id = models.FloatField()
    ruleset = models.TextField(blank=True, null=True)
    deploy_date = models.DateField()
    user_name = models.CharField(max_length=50)
    comments = models.CharField(max_length=200, blank=True, null=True)
    action = models.CharField(max_length=50)
    time_stamp = models.DateField()

    class Meta:
        managed = False
        db_table = 'ets_depl_ruleset_audit'


class EtsDeployedRuleArchive(models.Model):
    rule_package_id = models.FloatField(primary_key=True)
    rule_archive = models.BinaryField()
    deploy_date = models.DateField()
    user_name = models.CharField(max_length=50)
    comments = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ets_deployed_rule_archive'


class EtsDeployedRuleset(models.Model):
    rule_package_id = models.FloatField(primary_key=True)
    ruleset = models.TextField()
    deploy_date = models.DateField()
    user_name = models.CharField(max_length=50)
    comments = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ets_deployed_ruleset'


class EtsPublishedDtbl(models.Model):
    decision_table = models.OneToOneField(DecisionTable, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=100)
    html_content = models.TextField()
    date_published = models.DateField()

    class Meta:
        managed = False
        db_table = 'ets_published_dtbl'


class EtsPublishedDtblAudit(models.Model):
    ets_published_dtbl_audit_id = models.BigIntegerField(primary_key=True)
    decision_table_id = models.BigIntegerField()
    date_published = models.DateField()
    name = models.CharField(max_length=100)
    html_content = models.TextField()
    time_stamp = models.DateField(blank=True, null=True)
    action = models.CharField(max_length=50, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ets_published_dtbl_audit'


class Folder(models.Model):
    folder = models.OneToOneField('self', models.DO_NOTHING, primary_key=True, related_name='folderclass_folder')
    name = models.CharField(max_length=100, blank=True, null=True)
    parent_folder_id = models.BigIntegerField(blank=True, null=True)
    taggregation_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'folder'


class Grammar(models.Model):
    grammar_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'grammar'


class HtProcedureCategory(models.Model):
    procedure_category_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ht_procedure_category'


class InternalRuleRoute(models.Model):
    internal_rule_route_id = models.FloatField(primary_key=True)
    rule_id = models.FloatField(blank=True, null=True)
    message_id = models.FloatField(blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    appl = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'internal_rule_route'


class IrMessage(models.Model):
    ir_message_id = models.FloatField(primary_key=True)
    message_id = models.FloatField(blank=True, null=True)
    general_ind = models.CharField(max_length=1, blank=True, null=True)
    user_defined_code = models.CharField(max_length=20, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    appl = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_message'


class Jar(models.Model):
    jar_id = models.BigIntegerField(primary_key=True)
    group_id = models.CharField(max_length=200)
    artifact_id = models.CharField(max_length=100)
    version = models.CharField(max_length=50)
    file_name = models.CharField(max_length=255)
    jar_content = models.BinaryField(blank=True, null=True)
    time_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jar'
        unique_together = (('group_id', 'artifact_id', 'version'),)


class JarDependency(models.Model):
    jar = models.ForeignKey(Jar, models.DO_NOTHING, blank=True, null=True, related_name='jadependency_class_jar')
    dep = models.ForeignKey(Jar, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jar_dependency'


class Message(models.Model):
    message_id = models.FloatField(primary_key=True)
    admin_plan_id = models.FloatField(blank=True, null=True)
    active_ind = models.CharField(max_length=1, blank=True, null=True)
    service_type = models.CharField(max_length=20, blank=True, null=True)
    short_text = models.CharField(max_length=250, blank=True, null=True)
    text = models.CharField(max_length=2000, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    appl = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'


class MigrationSnapshot(models.Model):
    migration_snapshot_id = models.FloatField(primary_key=True)
    pallet_uuid = models.CharField(max_length=255)
    rule_store_id = models.FloatField()
    migration_result = models.TextField(blank=True, null=True)
    time_stamp = models.DateField(blank=True, null=True)
    action = models.CharField(max_length=50, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'migration_snapshot'


class MigrationTarget(models.Model):
    migration_target_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    target_environment = models.CharField(max_length=50)
    certificate = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'migration_target'


class MigrationTargetRs(models.Model):
    migration_target_rs_id = models.BigIntegerField(primary_key=True)
    target_rule_store_id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    realization = models.CharField(max_length=50)
    plan_id = models.BigIntegerField()
    plan_acronym = models.CharField(max_length=5)
    migration_target_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'migration_target_rs'


class NetworkBrand(models.Model):
    network_brand_id = models.BigIntegerField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    delete_status = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    national_ind = models.CharField(max_length=1, blank=True, null=True)
    non_par_network_brand_id = models.BigIntegerField(blank=True, null=True)
    networkbrand_pricing_req_ind = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'network_brand'


class PackageCrTemplate(models.Model):
    package_cr_template_id = models.FloatField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)
    other_fields = models.CharField(max_length=1000, blank=True, null=True)
    default_package = models.ForeignKey('RulePackage', models.DO_NOTHING, blank=True, null=True)
    rule_store = models.ForeignKey('RuleStore', models.DO_NOTHING)
    tenant = models.ForeignKey('Tenant', models.DO_NOTHING, db_column='tenant', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package_cr_template'


class PacketDtblOrdering(models.Model):
    packet_dtbl_ordering_id = models.BigIntegerField(primary_key=True)
    decision_table_id = models.BigIntegerField()
    rule_packet_id = models.BigIntegerField()
    order_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'packet_dtbl_ordering'


class PacketDtblOrderingAudit(models.Model):
    packet_dtbl_ordering_audit_id = models.BigIntegerField(primary_key=True)
    packet_dtbl_ordering_id = models.BigIntegerField()
    decision_table_id = models.BigIntegerField()
    rule_packet_id = models.BigIntegerField()
    order_num = models.IntegerField()
    time_stamp = models.DateField(blank=True, null=True)
    action = models.CharField(max_length=50, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'packet_dtbl_ordering_audit'


class PacketMessage(models.Model):
    packet_message_id = models.BigIntegerField(primary_key=True)
    rule_packet = models.ForeignKey('RulePacket', models.DO_NOTHING)
    message_code = models.CharField(max_length=20)
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'packet_message'


class PacketRuleOrdering(models.Model):
    packet_rule_ordering_id = models.BigIntegerField(primary_key=True)
    order_num = models.IntegerField()
    rule_id = models.BigIntegerField()
    rule_packet_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'packet_rule_ordering'
        unique_together = (('rule_packet_id', 'rule_id'),)


class PacketRuleOrderingAudit(models.Model):
    packet_rule_ordering_audit_id = models.BigIntegerField(primary_key=True)
    packet_rule_ordering_id = models.BigIntegerField()
    order_num = models.IntegerField()
    rule_id = models.BigIntegerField()
    rule_packet_id = models.BigIntegerField()
    user_name = models.CharField(max_length=50, blank=True, null=True)
    action = models.CharField(max_length=50, blank=True, null=True)
    time_stamp = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'packet_rule_ordering_audit'


class PkgCrTemplatePkg(models.Model):
    pkg_cr_template_pkg_id = models.FloatField(primary_key=True)
    package_cr_template = models.ForeignKey(PackageCrTemplate, models.DO_NOTHING)
    default_pkg_cr_template_pkg = models.CharField(max_length=1, blank=True, null=True)
    rule_package = models.ForeignKey('RulePackage', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pkg_cr_template_pkg'


class Plan(models.Model):
    plan_id = models.FloatField(primary_key=True)
    admin_plan_id = models.FloatField(blank=True, null=True)
    ortho_payment_schedule_conf_id = models.FloatField(blank=True, null=True)
    carrier_id = models.FloatField(blank=True, null=True)
    acronym = models.CharField(max_length=5, blank=True, null=True)
    ddpa_supported_ind = models.CharField(max_length=1, blank=True, null=True)
    dental_service_type_ind = models.CharField(max_length=1, blank=True, null=True)
    medical_service_type_ind = models.CharField(max_length=1, blank=True, null=True)
    vision_service_type_ind = models.CharField(max_length=1, blank=True, null=True)
    hipaa_identifier = models.CharField(max_length=50, blank=True, null=True)
    time_zone = models.CharField(max_length=20, blank=True, null=True)
    tax_num = models.CharField(max_length=20, blank=True, null=True)
    year_founded_in = models.IntegerField(blank=True, null=True)
    submission_limit = models.IntegerField(blank=True, null=True)
    website_addr = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    mission_statement = models.CharField(max_length=4000, blank=True, null=True)
    claim_proc_conf_id = models.FloatField(blank=True, null=True)
    conversion_date = models.DateField(blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    appl = models.CharField(max_length=50, blank=True, null=True)
    id_card_id = models.FloatField(blank=True, null=True)
    member_elig_conf_id = models.FloatField(blank=True, null=True)
    rule_component_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plan'


class PreenrollProduct(models.Model):
    preenroll_product_id = models.FloatField(primary_key=True)
    preenroll_client_id = models.FloatField(blank=True, null=True)
    product_name = models.CharField(max_length=200, blank=True, null=True)
    plan = models.CharField(max_length=5, blank=True, null=True)
    billing_type = models.CharField(max_length=50, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    appl = models.CharField(max_length=50, blank=True, null=True)
    subclient_prefix = models.CharField(max_length=50, blank=True, null=True)
    benefit_level_option_type = models.CharField(max_length=20, blank=True, null=True)
    product_type = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'preenroll_product'


class ProccatProcedure(models.Model):
    dental_proc_code = models.CharField(primary_key=True, max_length=20)
    procedure_category_id = models.FloatField()
    user_name = models.CharField(max_length=50, blank=True, null=True)
    appl = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proccat_procedure'
        unique_together = (('dental_proc_code', 'procedure_category_id'),)


class ProcdirProccat(models.Model):
    process_directive_id = models.FloatField(primary_key=True)
    procedure_category_id = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    appl = models.CharField(max_length=50, blank=True, null=True)
    proc_cat_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procdir_proccat'
        unique_together = (('process_directive_id', 'procedure_category_id'),)


class ProcedureCategory(models.Model):
    procedure_category_id = models.FloatField(primary_key=True)
    procedure_category_set_id = models.FloatField(blank=True, null=True)
    parent_procedure_category_id = models.FloatField(blank=True, null=True)
    sort_order = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    appl = models.CharField(max_length=50, blank=True, null=True)
    target_procedure_code = models.CharField(max_length=20, blank=True, null=True)
    procedure_category_rate_type = models.CharField(max_length=20, blank=True, null=True)
    ortho_payment_config_ind = models.CharField(max_length=1, blank=True, null=True)
    alt_service_type_code = models.CharField(max_length=20, blank=True, null=True)
    exclude_ind = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procedure_category'


class ProcedureCategorySet(models.Model):
    procedure_category_set_id = models.FloatField(primary_key=True)
    admin_plan_id = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    service_type = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=2000, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    appl = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procedure_category_set'


class ProcessDirective(models.Model):
    process_directive_id = models.FloatField(primary_key=True)
    message_id = models.FloatField(blank=True, null=True)
    general_ind = models.CharField(max_length=1, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    user_defined_code = models.CharField(max_length=20, blank=True, null=True)
    ivr_code = models.CharField(max_length=20, blank=True, null=True)
    trmnt_cost_save_bucket = models.CharField(max_length=20, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    appl = models.CharField(max_length=50, blank=True, null=True)
    non_covered_service_type = models.CharField(max_length=50, blank=True, null=True)
    claim_adj_reason_code = models.CharField(max_length=50, blank=True, null=True)
    remittance_advice_remark_code = models.CharField(max_length=50, blank=True, null=True)
    claim_adj_group_code = models.CharField(max_length=50, blank=True, null=True)
    trmnt_cost_saving_calc_type = models.CharField(max_length=50, blank=True, null=True)
    trmnt_cost_saving_categry_type = models.CharField(max_length=50, blank=True, null=True)
    claim_status_reason_code = models.CharField(max_length=50, blank=True, null=True)
    denial_code_ind = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'process_directive'


class Realization(models.Model):
    realization_id = models.BigIntegerField(primary_key=True)
    key = models.CharField(unique=True, max_length=30)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000, blank=True, null=True)
    vms_resource_name = models.CharField(max_length=128, blank=True, null=True)
    grammar_type = models.CharField(max_length=50, blank=True, null=True)
    sparse_configuration = models.CharField(max_length=1, blank=True, null=True)
    vms = models.ForeignKey('Vms', models.DO_NOTHING)
    version = models.CharField(max_length=50)
    time_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'realization'


class RealizationJar(models.Model):
    realization_jar_id = models.BigIntegerField(primary_key=True)
    realization = models.ForeignKey(Realization, models.DO_NOTHING, blank=True, null=True)
    jar = models.ForeignKey(Jar, models.DO_NOTHING, blank=True, null=True)
    dependency_scope = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'realization_jar'


class RgstVocabDescriptor(models.Model):
    rgst_vocab_descriptor_id = models.FloatField(primary_key=True)
    realization = models.CharField(max_length=50)
    uuid = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'rgst_vocab_descriptor'
        unique_together = (('realization', 'uuid'),)


class Role(models.Model):
    role_id = models.BigIntegerField(primary_key=True)
    key = models.CharField(unique=True, max_length=100)
    description = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role'


class RolePermission(models.Model):
    role = models.ForeignKey(Role, models.DO_NOTHING, blank=True, null=True)
    permission = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role_permission'


class RoleScope(models.Model):
    role_scope_id = models.FloatField(primary_key=True)
    principal = models.ForeignKey(BrideUser, models.DO_NOTHING, blank=True, null=True)
    role = models.ForeignKey(Role, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'role_scope'


class RoosDeployedPkg(models.Model):
    dep_pkg_id = models.BigIntegerField(primary_key=True)
    rule_package = models.ForeignKey('RulePackage', models.DO_NOTHING, blank=True, null=True)
    string_content = models.TextField(blank=True, null=True)
    binary_content = models.BinaryField(blank=True, null=True)
    deploy_date = models.DateField()
    user_name = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    comments = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roos_deployed_pkg'


class RpackageRpacket(models.Model):
    rule_package = models.OneToOneField('RulePackage', models.DO_NOTHING, primary_key=True)
    rule_packet = models.ForeignKey('RulePacket', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rpackage_rpacket'
        unique_together = (('rule_package', 'rule_packet'),)


class RpackageRpacketAudit(models.Model):
    rpackage_rpacket_audit_id = models.BigIntegerField(primary_key=True)
    rule_package_id = models.BigIntegerField()
    rule_packet_id = models.BigIntegerField()
    user_name = models.CharField(max_length=50, blank=True, null=True)
    action = models.CharField(max_length=50, blank=True, null=True)
    time_stamp = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rpackage_rpacket_audit'


class RpacketDtbl(models.Model):
    decision_table = models.ForeignKey(DecisionTable, models.DO_NOTHING)
    rule_packet = models.ForeignKey('RulePacket', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rpacket_dtbl'


class RpacketDtblAudit(models.Model):
    rpacket_dtbl_audit_id = models.BigIntegerField(primary_key=True)
    decision_table_id = models.BigIntegerField()
    rule_packet_id = models.BigIntegerField()
    time_stamp = models.DateField(blank=True, null=True)
    action = models.CharField(max_length=50, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rpacket_dtbl_audit'


class RpacketMsgProcCatg(models.Model):
    rule_packet = models.ForeignKey('RulePacket', models.DO_NOTHING)
    procedure_category_id = models.FloatField()

    class Meta:
        managed = False
        db_table = 'rpacket_msg_proc_catg'
        unique_together = (('rule_packet', 'procedure_category_id'),)


class RpacketRule(models.Model):
    rule = models.OneToOneField('Rule', models.DO_NOTHING, primary_key=True)
    rule_packet = models.ForeignKey('RulePacket', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rpacket_rule'
        unique_together = (('rule', 'rule_packet'),)


class RpacketRuleAudit(models.Model):
    rpacket_rule_audit_id = models.BigIntegerField(primary_key=True)
    rule_id = models.BigIntegerField()
    rule_packet_id = models.BigIntegerField()
    user_name = models.CharField(max_length=50, blank=True, null=True)
    action = models.CharField(max_length=50, blank=True, null=True)
    time_stamp = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rpacket_rule_audit'


class RpkgDeploymentSnapshot(models.Model):
    rpkg_deployment_snapshot_id = models.BigIntegerField(primary_key=True)
    rule_package = models.ForeignKey('RulePackage', models.DO_NOTHING, blank=True, null=True)
    deploy_date = models.DateField(blank=True, null=True)
    package_name = models.CharField(max_length=50, blank=True, null=True)
    comments = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rpkg_deployment_snapshot'


class RsScope(models.Model):
    role_scope = models.ForeignKey(RoleScope, models.DO_NOTHING, blank=True, null=True)
    scope = models.ForeignKey('Scope', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rs_scope'


class Rule(models.Model):
    rule_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    rule_visibility = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    uuid = models.CharField(max_length=50, blank=True, null=True)
    active_ind = models.CharField(max_length=1, blank=True, null=True)
    statement = models.CharField(max_length=3000, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    rule_store = models.ForeignKey('RuleStore', models.DO_NOTHING, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    treatment_category = models.CharField(max_length=50, blank=True, null=True)
    treatment_category_0 = models.ForeignKey('TreatmentCategory', models.DO_NOTHING, db_column='treatment_category_id', blank=True, null=True)  # Field renamed because of name conflict.
    taggregation = models.ForeignKey('Taggregation', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rule'


class RuleAudit(models.Model):
    rule_audit_id = models.BigIntegerField(primary_key=True)
    rule_id = models.BigIntegerField()
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    uuid = models.CharField(max_length=50, blank=True, null=True)
    active_ind = models.CharField(max_length=1, blank=True, null=True)
    statement = models.CharField(max_length=3000, blank=True, null=True)
    rule_store_id = models.BigIntegerField(blank=True, null=True)
    treatment_category_id = models.BigIntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    action = models.CharField(max_length=50, blank=True, null=True)
    time_stamp = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rule_audit'


class RuleClient(models.Model):
    rule_client_id = models.BigIntegerField(primary_key=True)
    rule_aspect_id = models.CharField(max_length=20, blank=True, null=True)
    aspect_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rule_client'


class RulePackage(models.Model):
    rule_package_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True, null=True)
    rule_store = models.ForeignKey('RuleStore', models.DO_NOTHING, blank=True, null=True)
    taggregation = models.ForeignKey('Taggregation', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rule_package'


class RulePackageAudit(models.Model):
    rule_package_audit_id = models.BigIntegerField(primary_key=True)
    rule_package_id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True, null=True)
    rule_store_id = models.BigIntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    action = models.CharField(max_length=50, blank=True, null=True)
    time_stamp = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rule_package_audit'


class RulePackageReport(models.Model):
    rule_package_id = models.BigIntegerField(primary_key=True)
    report = models.TextField(blank=True, null=True)
    compressed_rule_report = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rule_package_report'


class RulePackageSnapshot(models.Model):
    rule_package_snapshot_id = models.BigIntegerField(primary_key=True)
    rule_package_id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True, null=True)
    configuration = models.TextField()
    rule_store_id = models.BigIntegerField()
    time_stamp = models.DateField(blank=True, null=True)
    action = models.CharField(max_length=50, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rule_package_snapshot'


class RulePacket(models.Model):
    rule_packet_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=2000, blank=True, null=True)
    rule_store = models.ForeignKey('RuleStore', models.DO_NOTHING, blank=True, null=True)
    treatment_category = models.CharField(max_length=50, blank=True, null=True)
    treatment_category_0 = models.ForeignKey('TreatmentCategory', models.DO_NOTHING, db_column='treatment_category_id', blank=True, null=True)  # Field renamed because of name conflict.
    display_order = models.FloatField(blank=True, null=True)
    customized_message = models.CharField(max_length=2000, blank=True, null=True)
    ivr_phrase_code = models.CharField(max_length=20, blank=True, null=True)
    taggregation = models.ForeignKey('Taggregation', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rule_packet'


class RulePacketAudit(models.Model):
    rule_packet_audit_id = models.BigIntegerField(primary_key=True)
    rule_packet_id = models.BigIntegerField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)
    rule_store_id = models.BigIntegerField(blank=True, null=True)
    treatment_category_id = models.BigIntegerField(blank=True, null=True)
    display_order = models.FloatField(blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    action = models.CharField(max_length=50, blank=True, null=True)
    time_stamp = models.DateField(blank=True, null=True)
    customized_message = models.CharField(max_length=2000, blank=True, null=True)
    ivr_phrase_code = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rule_packet_audit'


class RulePacketSnapshot(models.Model):
    rule_packet_snapshot_id = models.BigIntegerField(primary_key=True)
    rule_packet_id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True, null=True)
    treatment_category_id = models.BigIntegerField(blank=True, null=True)
    customized_message = models.CharField(max_length=2000, blank=True, null=True)
    ivr_phrase_code = models.CharField(max_length=20, blank=True, null=True)
    rules = models.TextField(blank=True, null=True)
    decision_tables = models.TextField(blank=True, null=True)
    rule_order = models.TextField(blank=True, null=True)
    dtbl_order = models.TextField(blank=True, null=True)
    rule_store_id = models.BigIntegerField()
    time_stamp = models.DateField(blank=True, null=True)
    action = models.CharField(max_length=50, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rule_packet_snapshot'


class RuleSnapshot(models.Model):
    rule_snapshot_id = models.FloatField(primary_key=True)
    rule_id = models.FloatField()
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    rule_store_id = models.FloatField(blank=True, null=True)
    active_ind = models.CharField(max_length=1, blank=True, null=True)
    statement = models.CharField(max_length=3000, blank=True, null=True)
    treatment_category_id = models.FloatField(blank=True, null=True)
    time_stamp = models.DateField(blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rule_snapshot'


class RuleStore(models.Model):
    rule_store_id = models.BigIntegerField(primary_key=True)
    top_package_name = models.CharField(max_length=50, blank=True, null=True)
    realization = models.CharField(max_length=50, blank=True, null=True)
    rule_store_name = models.CharField(max_length=100, blank=True, null=True)
    project_name = models.CharField(max_length=50, blank=True, null=True)
    plan = models.ForeignKey('Tenant', models.DO_NOTHING, blank=True, null=True)
    default_rule_package = models.ForeignKey(RulePackage, models.DO_NOTHING, blank=True, null=True)
    plan_acronym = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    taggregation = models.ForeignKey('Taggregation', models.DO_NOTHING, blank=True, null=True)
    tenant_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rule_store'
        unique_together = (('realization', 'plan'),)


class RuleStoreLock(models.Model):
    rule_store_id = models.BigIntegerField(primary_key=True)
    user_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'rule_store_lock'


class RuleSubscription(models.Model):
    rule_subscription_id = models.BigIntegerField(primary_key=True)
    end_date = models.DateField(blank=True, null=True)
    rule_client = models.ForeignKey(RuleClient, models.DO_NOTHING)
    start_date = models.DateField()
    rule = models.ForeignKey(Rule, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rule_subscription'


class RuleTemplate(models.Model):
    rule_template_id = models.FloatField(primary_key=True)
    rule_store = models.ForeignKey(RuleStore, models.DO_NOTHING)
    name = models.CharField(max_length=100)
    content = models.TextField()
    taggregation = models.ForeignKey('Taggregation', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rule_template'


class Scope(models.Model):
    scope_id = models.BigIntegerField(primary_key=True)
    key = models.CharField(unique=True, max_length=100)
    target_type = models.CharField(max_length=255)
    target_id = models.CharField(max_length=64)
    description = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scope'


class SerializedDtbl(models.Model):
    decision_table = models.OneToOneField(DecisionTable, models.DO_NOTHING, primary_key=True)
    content = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'serialized_dtbl'


class SerializedRule(models.Model):
    rule = models.OneToOneField(Rule, models.DO_NOTHING, primary_key=True)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'serialized_rule'


class SourceTargetEnvironment(models.Model):
    source_environment = models.ForeignKey(Environment, models.DO_NOTHING, blank=True, null=True)
    target_environment_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'source_target_environment'


class StagedMigration(models.Model):
    uuid = models.CharField(unique=True, max_length=255)
    pallet_uuid = models.CharField(max_length=255)
    binary_content = models.BinaryField(blank=True, null=True)
    string_content = models.TextField(blank=True, null=True)
    migration_unit_type = models.CharField(max_length=50)
    entity_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staged_migration'


class State(models.Model):
    state_id = models.FloatField(primary_key=True)
    country_id = models.FloatField(blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    appl = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state'


class SwingClientZip(models.Model):
    swing_client_id = models.BigIntegerField(primary_key=True)
    zip = models.BinaryField()
    file_name = models.CharField(max_length=255)
    time_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swing_client_zip'


class Tag(models.Model):
    tag_id = models.FloatField(primary_key=True)
    type = models.CharField(max_length=255)
    key = models.CharField(max_length=200)
    description = models.CharField(max_length=2000, blank=True, null=True)
    tenant_key = models.CharField(max_length=50)
    permissions = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tag'
        unique_together = (('type', 'key', 'tenant_key'),)


class TagCatalog(models.Model):
    tag_catalog_id = models.FloatField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000, blank=True, null=True)
    permissions = models.CharField(max_length=20)
    parent_catalog = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    tenant_key = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tag_catalog'
        unique_together = (('name', 'tenant_key'),)


class TagCatalogTag(models.Model):
    tag_catalog = models.ForeignKey(TagCatalog, models.DO_NOTHING, blank=True, null=True)
    tag = models.ForeignKey(Tag, models.DO_NOTHING, blank=True, null=True)
    ordering = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tag_catalog_tag'


class TagConstraint(models.Model):
    tag_constraint_id = models.BigIntegerField(primary_key=True)
    key = models.CharField(max_length=200)
    permissions = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tag_constraint'


class TagConstraints(models.Model):
    tag_constraints_id = models.BigIntegerField(primary_key=True)
    key_tag_id = models.BigIntegerField()
    description = models.CharField(max_length=2000, blank=True, null=True)
    permissions = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tag_constraints'


class Taggregation(models.Model):
    taggregation_id = models.BigIntegerField(primary_key=True)
    key = models.CharField(max_length=200)
    description = models.CharField(max_length=2000, blank=True, null=True)
    type = models.CharField(max_length=50)
    permissions = models.CharField(max_length=20)
    parent_taggregation = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    tenant_key = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'taggregation'
        unique_together = (('type', 'key', 'tenant_key'),)


class TaggregationTag(models.Model):
    taggregation = models.ForeignKey(Taggregation, models.DO_NOTHING, blank=True, null=True)
    tag = models.ForeignKey(Tag, models.DO_NOTHING, blank=True, null=True)
    ordering = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taggregation_tag'


class TcDataRule(models.Model):
    tc_data_rule_id = models.BigIntegerField(primary_key=True)
    test_case_data = models.ForeignKey('TestCaseData', models.DO_NOTHING)
    rule_store = models.ForeignKey(RuleStore, models.DO_NOTHING)
    rule_name = models.CharField(max_length=100)
    rule_order = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tc_data_rule'


class Tenant(models.Model):
    tenant_id = models.FloatField(primary_key=True)
    parent_tenant = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=50)
    acronym = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'tenant'


class TestCase(models.Model):
    test_case_id = models.BigIntegerField(primary_key=True)
    test_case_data = models.TextField()
    rule_package = models.ForeignKey(RulePackage, models.DO_NOTHING)
    description = models.CharField(max_length=200, blank=True, null=True)
    comments = models.CharField(max_length=1000, blank=True, null=True)
    successful_ind = models.CharField(max_length=1, blank=True, null=True)
    active_ind = models.CharField(max_length=1, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    change_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_case'


class TestCaseData(models.Model):
    test_case_data_id = models.BigIntegerField(primary_key=True)
    rule_store_id = models.BigIntegerField()
    rule_package = models.ForeignKey(RulePackage, models.DO_NOTHING)
    test_facts_id = models.BigIntegerField()
    name = models.CharField(max_length=200, blank=True, null=True)
    comments = models.CharField(max_length=1000, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    change_date = models.DateField(blank=True, null=True)
    taggregation_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_case_data'


class TestFacts(models.Model):
    test_facts_id = models.BigIntegerField(primary_key=True)
    rule_context_json = models.TextField()
    realization = models.CharField(max_length=50)
    name = models.CharField(max_length=200, blank=True, null=True)
    comments = models.CharField(max_length=1000, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    change_date = models.DateField(blank=True, null=True)
    taggregation_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_facts'


class Tooth(models.Model):
    tooth_id = models.FloatField(primary_key=True)
    permanent_ind = models.CharField(max_length=1, blank=True, null=True)
    code = models.CharField(max_length=2, blank=True, null=True)
    num_sys_type = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    appl = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tooth'


class ToothSurface(models.Model):
    tooth_surface_id = models.FloatField(primary_key=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=2000, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    appl = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tooth_surface'


class TranslatedRule(models.Model):
    rule = models.ForeignKey(Rule, models.DO_NOTHING)
    content = models.TextField()
    target_lang_type = models.CharField(max_length=50)
    translated_rule_id = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'translated_rule'


class TreatmentCategory(models.Model):
    treatment_category_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    precedence_order = models.IntegerField(blank=True, null=True)
    realization_type = models.CharField(max_length=50, blank=True, null=True)
    plan_id = models.BigIntegerField(blank=True, null=True)
    plan_acronym = models.CharField(max_length=5, blank=True, null=True)
    taggregation = models.ForeignKey(Taggregation, models.DO_NOTHING, blank=True, null=True)
    rule_store = models.ForeignKey(RuleStore, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'treatment_category'


class UserRole(models.Model):
    principal = models.ForeignKey(BrideUser, models.DO_NOTHING, blank=True, null=True)
    role = models.ForeignKey(Role, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_role'


class Vms(models.Model):
    vms_id = models.BigIntegerField(primary_key=True)
    content = models.TextField(blank=True, null=True)
    resource_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=2000, blank=True, null=True)
    version = models.CharField(max_length=50, blank=True, null=True)
    time_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vms'
# Unable to inspect table 'zackage_change_request_templateeeeeeeeeeeeeeeeeeee'
# The error was: ORA-00942: table or view does not exist


class Zip(models.Model):
    zip_id = models.FloatField(primary_key=True)
    state_id = models.FloatField(blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    appl = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zip'

