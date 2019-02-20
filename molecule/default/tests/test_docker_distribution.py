import os
import json

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_docker_distribution_config(host):
    f = host.file('/etc/docker-distribution/registry/config.yml')
    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.contains('addr: 127.0.0.1:5000')


def test_docker_distribution_package(host):
    package = host.package('docker-distribution')
    assert package.is_installed


def test_docker_distribution_service(host):
    service = host.service('docker-distribution')
    assert service.is_running
    assert service.is_enabled


def test_docker_distribution_socket(host):
    socket = host.socket('tcp://127.0.0.1:5000')
    assert socket.is_listening


def test_docker_distribution_pull_image(host):
    with host.sudo():
        cmd = host.run('docker pull 127.0.0.1:5000/amd64/busybox:latest')
        assert cmd.rc == 0
        assert 'Pull complete' in cmd.stdout
        assert '127.0.0.1:5000/amd64/busybox:latest' in cmd.stdout


def test_docker_distribution_catalog(host):
    cmd = host.run('curl -s http://127.0.0.1:5000/v2/_catalog')
    repositories = json.loads(cmd.stdout)['repositories']
    assert cmd.rc == 0
    assert len(repositories) == 3
    assert repositories[0] == 'amd64/busybox'
    assert repositories[1] == 'amd64/haproxy'
    assert repositories[2] == 'amd64/registry'


def test_docker_distribution_skip_list(host):
    f = host.file('/var/tmp/images_list.yaml')
    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'
    assert not f.contains('docker.io/amd64/centos-httpd:latest')
