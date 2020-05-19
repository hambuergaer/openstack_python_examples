#!/usr/bin/env python

from os import environ
from keystoneauth1 import loading
from keystoneauth1 import session
from cinderclient import client as cinderclient
from novaclient import client as novaclient

loader = loading.get_plugin_loader('password')
auth = loader.load_from_options(auth_url=environ['OS_AUTH_URL'],
                   username=environ['OS_USERNAME'],
                   password=environ['OS_PASSWORD'],
                   project_name=environ['OS_PROJECT_NAME'],
                   project_domain_name=environ['OS_PROJECT_DOMAIN_NAME'],
                   user_domain_name=environ['OS_PROJECT_DOMAIN_NAME'])
sess = session.Session(auth=auth)

# List volumes for all projects
cinder = cinderclient.Client(3, session=sess)
volumes = cinder.volumes.list(search_opts={'all_tenants': True})
for v in volumes:
    print ("Volume = %s" % v)

# List instances for all projects
nova = novaclient.Client(2, session=sess)
instances = nova.servers.list(search_opts={'all_tenants': True})
for i in instances:
    print ("Instance = %s" % i)