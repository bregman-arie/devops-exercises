<center><h1> The Task </center></h1>
My objective was to set up a simple cron job on all three Nautilus app servers (`stapp01`, `stapp02`, `stapp03`). The requirements were:

1. Install the `cronie` package on all app servers.
2. Start and enable the `crond` service.
3. For the root user on each server, add a cron job that runs every 5 minutes and executes the command `echo hello > /tmp/cron_text`.

---

## What are...
**What is an `inventory.ini` file?**
- The inventory file tells Ansible which servers to manage and how to connect to them.
- It lists groups of servers (like web, app, or database servers) with their IPs or hostnames.
- Ansible uses this file to know where to run the tasks defined in the playbook.

**What is a `playbook.yml` file?**
- The playbook file is like a set of instructions or a recipe.
- It tells Ansible what actions to perform on the servers (like install packages, start services, or copy files).
- The playbook uses the servers listed in the inventory file.

---

## Solution:

This is the professional, scalable solution. I performed all my work from the jump host, using Ansible to orchestrate the changes on all three app servers simultaneously.

1. The Inventory (`inventory.ini`)
First, I created an "address book" for Ansible on the jump host.
```bash
[app_servers] # Group name for application servers
stapp01 ansible_host=172.16.238.10 ansible_user=tony ansible_ssh_pass=Ir0nM@n ansible_become_pass=Ir0nM@n
stapp02 ansible_host=172.16.238.11 ansible_user=steve ansible_ssh_pass=Am3ric@ ansible_become_pass=Am3ric@
stapp03 ansible_host=172.16.238.12 ansible_user=banner ansible_ssh_pass=BigGr33n ansible_become_pass=BigGr33n
```

2. The Playbook (`playbook.yml`)
Next, I wrote a "to-do list" in YAML using Ansible's built-in modules. This playbook is idempotent, meaning it can be run multiple times safely.
```bash

---  
- name: Configure Cron Jobs on App Servers            # name of playbook
  hosts: app_servers                                  # target group of servers
  become: yes                                         # run tasks with root privileges
  tasks:                                              # list of tasks to perform

    - name: Ensure cronie package is installed         # task: install cron service package
      ansible.builtin.package:                         # use package module to manage software
        name: cronie                                   # package name to install
        state: present                                 # ensure package is installed

    - name: Ensure crond service is running and enabled # task: Start and enable cron service
      ansible.builtin.service:                         # Use service module to manage services
        name: crond                                    # Specify the cron service
        state: started                                 # Make sure it's running
        enabled: yes                                   # Enable it to start on boot

    - name: Add cron job for root user                 # Task: Add a cron job for root
      ansible.builtin.cron:                            # Use cron module to manage scheduled jobs
        name: "echo hello message"                     # Description of the cron job
        minute: "*/5"                                  # Run every 5 minutes
        user: root                                     # Run as root user
        job: "echo hello > /tmp/cron_text"             # Command to execute
        state: present                                 # Ensure cron job exists

```

3. **The Execution**
Finally, from the main server, I ran a single command to execute the playbook.
```bash
ansible-playbook -i inventory.ini playbook.yml

# This command runs the Ansible playbook (playbook.yml) using the list of target servers defined in the inventory file (inventory.ini).
```
Ansible then connected to all three servers and made sure the package was installed, the service was running, and the cron job was present, completing the task for the entire fleet in seconds.

---