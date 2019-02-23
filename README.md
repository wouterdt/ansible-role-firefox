Role Name
=========

Install Mozilla Firefox, xvfb to allow for headless firefox via x11
Creates linux user, can create custom firefox profile and sets user.js file

Requirements
------------

None

Role Variables
--------------

Firefox_profile: a list of all profiles to be created
  username:the linux user
  profile :the profile name
    config: the key value

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

- name: Converge
  hosts: all
  roles:
    - role: wouterdt.firefox
  vars:
    firefox_profile:
      - username: user1
        profile: default
        config:
          general.useragent.override: "Mozilla 5"
      - username: user2
        profile: test

License
-------

BSD
