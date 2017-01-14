Keystone
========
This role helps install and configure OpenStack Keystone.


Requirements
------------
Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------
A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.


Dependencies
------------
This role has the following dependencies:

- `vexxhost.openstack-rdo`

All of those are included as part of the role so they should be included
automatically when installing via Galaxy.


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

For development and testing, this role uses `molecule`.  You can simply make
sure that your credentials are properly setup pointing towards an OpenStack
cloud and run `molecule converge` which will setup the entire environment.


License
-------
BSD

Author Information
------------------
An optional section for the role authors to include contact information, or a website (HTML is not allowed).
