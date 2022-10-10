## My first playbook - Solution

1. `vi first_playbook.yml`

```
- name: Install zlib and create a file
  hosts: some_remote_host
  tasks:
    - name: Install zlib
      package:
        name: zlib
        state: present
      become: yes
    - name: Create the file /tmp/some_file
      file:
        path: '/tmp/some_file'
        state: touch
```

2. First, edit the inventory file: `vi /etc/ansible/hosts`

```
[some_remote_host]
some.remoted.host.com
```

Run the playbook

`ansible-playbook first_playbook.yml`
