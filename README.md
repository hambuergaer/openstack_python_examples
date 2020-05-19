# Openstack Python examples
This Python script is just an example for the Openstack API usage of Cinder and Nova. It was tested with Openstacl Queens (13).

Further information can be found here:
- https://docs.openstack.org/python-novaclient/latest/
- https://docs.openstack.org/python-cinderclient/latest/
- https://docs.openstack.org/releasenotes/python-novaclient/queens.html
- https://docs.openstack.org/releasenotes/python-cinderclient/queens.html

The script sources all environment variables to authenticate to Keystone. Most commonly theses envrionment variables are configured in the /home/stack/overcloudrc which you need to source beforehand. You can then run this example script as user stack on e.g. the Director node (in case of a Red Hat OSP 13 triple-o installation).