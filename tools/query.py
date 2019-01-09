#!/usr/bin/env python3
import sys
import sqlite3

if len(sys.argv) < 2:
    print('Fetch switch configuration from ipplan.db')
    print('')
    print("Usage:", sys.argv[0], " switch_name")
    sys.exit(1)

switch = sys.argv[1]

#print config.parse_metadata(switch)


sql = '''SELECT n_mgmt.ipv4_txt, h.ipv4_addr_txt, n_mgmt.ipv4_gateway_txt,
n_mgmt.vlan, n.vlan FROM active_switch as s, network as n, host as h,
network as n_mgmt WHERE s.switch_name LIKE ? AND n.node_id = s.node_id
AND h.name = s.switch_name AND n_mgmt.node_id = h.network_id'''

db = sqlite3.connect('/etc/ipplan.db')
cursor = db.cursor()

row = cursor.execute(sql, ('%s%%' % switch.lower(),)).fetchone()

print(row)
