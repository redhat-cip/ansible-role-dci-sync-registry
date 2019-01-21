import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_docker_daemon_config(host):
    f = host.file('/etc/docker/daemon.json')
    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.contains('insecure-registries')
    assert f.contains('127.0.0.1:5000')


def test_docker_proxy_config(host):
    f = host.file('/etc/systemd/system/docker.service.d/http-proxy.conf')
    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.contains('[Service]')


def test_docker_storage_config(host):
    f = host.file('/etc/sysconfig/docker-storage-setup')
    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.contains('STORAGE_DRIVER=vfs')


def test_docker_package(host):
    package = host.package('docker')
    assert package.is_installed


def test_docker_service(host):
    service = host.service('docker')
    assert service.is_running
    assert service.is_enabled


def test_docker_socket(host):
    socket = host.socket('unix:///var/run/docker.sock')
    assert socket.is_listening


def test_docker_info(host):
    cmd = host.run('sudo docker info')
    assert cmd.rc == 0
    assert 'Storage Driver: vfs' in cmd.stdout
    assert ' 127.0.0.1:5000' in cmd.stdout
