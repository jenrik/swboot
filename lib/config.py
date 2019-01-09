import yaml
from tempita import bunch

f = open('switchconfig/config.yaml', 'r')
yaml_conf = yaml.load(f)

# Note: To add new variables, the generate function will need to 
# be modified as well
radius = yaml_conf['switch']['radius']
username = yaml_conf['switch']['username']
password = yaml_conf['switch']['password']
enable = yaml_conf['switch']['enable_password']
snmp_ro = yaml_conf['switch']['snmp_ro']
snmp_salt = yaml_conf['switch']['snmp_salt']

# NOTE(bluecmd): 2950 doesn't support VLAN aware context, which means that
# WhereAmI and dhmon needs v2. No reason to have v3 in that case.
# snmp_user = yaml_conf['switch']['snmp_user']
# snmp_auth = yaml_conf['switch']['snmp_auth']
# snmp_priv = yaml_conf['switch']['snmp_priv']
wifi_vlanid = yaml_conf['wifi']['vlan_id']

# Enable this if we cannot set special option82 tags
franken_net_switches = []

# If you have franken net, you need snmpv3 credentials to dist
# NOTE: THERE IS NO NEED TO USE THIS IF is_franken_net == False
snmpv3_username = ''
snmpv3_auth = ''
snmpv3_priv = ''

models = {}
for model in yaml_conf['models']:
    models.update({model['name']: bunch(template=model['path'], eth=model['ports'])})

wifi_switches = yaml_conf['wifi']['switches']

# Files to be served as they are to all devices
static_files = {}
for sf in yaml_conf['static_files']:
    static_files.update(sf)
