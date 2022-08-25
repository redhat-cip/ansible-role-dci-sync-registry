# ansible-role-dci-sync-registry

An Ansible role that syncs DCI registry.


## Role Variables

| Variable name | Required | Default | Type | Description |
|---------------|----------|---------|------|-------------|
| dci_sync_registry_images_list | True | N/A | String | Absolute path to the images list file (YAML) |
| dci_sync_registry_local_ip | False | ansible_default_ipv4.address | IP | IP address for binding the container registry |
| dci_sync_registry_local_port | False | 5000 | Int | Port for binding the container registry |
| dci_sync_registry_remote_login | False | '' | String | Login to the remote registry when required |
| dci_sync_registry_remote_password | False | '' | String | Password to the remote registry when required |
| dci_sync_registry_remote_url | False | registry.distributed-ci.io | String | Remove container registry url |
| dci_sync_registry_skip_list | False | [] | List | Container images list to exclude of the synchronization |
| dci_sync_registry_storage | False | overlay2 | String | Docker storage drivers to use |


### Example

```
- hosts: localhost
  vars:
    dci_sync_registry_images_list: /var/www/html/my_component/images_list.yaml
    dci_sync_registry_remote_login: foo
    dci_sync_registry_remote_password: bar
  roles:
    - dci-sync-registry
```

### License

Apache 2.0


### Author Information

Distributed-CI Team  <distributed-ci@redhat.com>
