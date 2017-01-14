import testinfra.utils.ansible_runner
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_keystone_is_listening(Socket):
    assert Socket("tcp://:::5000").is_listening
    assert Socket("tcp://:::35357").is_listening
