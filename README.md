Keystone
========
This role helps install and configure OpenStack Keystone.


Requirements
------------
This role currently requires the `os_project` and `os_user` modules that ship
with Ansible.  The `os_user` library has been bundled due to a bug in the
current version of the module in Ansible, once this bug is resolved, it will no
longer be bundled.

- https://github.com/ansible/ansible/pull/20259


Role Variables
--------------
All of the default variables are in the [defaults file](defaults/main.yml),
there are also some required variables to be set for passwords which you'll
find in the [testing playbook](tests/test.yml)


Dependencies
------------
This role has the following dependencies:

- `vexxhost.openstack-oslo`

All of those are included as part of the role so they should be included
automatically when installing via Galaxy.  If you need to install from RDO,
it's suggested that you add the `vexxhost.openstack-rdo` role to automatically
install the repos.


Example Playbook
----------------
For examples on how to use the module, you can refer to the
[testing playbook](tests/test.yml) which is ran in order to test the module.

For development and testing, this role uses `molecule`.  You can simply make
sure that your credentials are properly setup pointing towards an OpenStack
cloud and run `molecule converge` which will setup the entire environment.


License
-------
Apache


Author Information
------------------
http://vexxhost.com
