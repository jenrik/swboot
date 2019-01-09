#!/usr/bin/env python3
import hashlib
import sys
from lib import generate
from lib import config

if len(sys.argv) != 2:
    print('usage: {} snmp_community_string'.format(sys.argv[0]))

mgmt, _ = generate.parse_metadata(sys.argv[1])
print(hashlib.sha1(config.snmp_salt + mgmt['ip']).hexdigest())
