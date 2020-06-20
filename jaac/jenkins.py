import jenkins  # 3rd party "python-jenkins"
import os


def get_jenkins_instance(url, username, password):
    return jenkins.Jenkins(os.getenv('JENKINS_URL'),
                           username=os.getenv('JENKINS_USERNAME'), password=os.getenv('JENKINS_TOKEN'))


def get_node_size_gb(jenkins_instance, node_name):
    node_info = jenkins_instance.get_node_info(node_name)
    node_size_bytes = node_info['monitorData']['hudson.node_monitors.TemporarySpaceMonitor']['size']
    node_size_gb = node_size_bytes / (1024 * 1024 * 1024)
    return node_size_gb


def enable_node(jenkins_instance, node_name):
    jenkins_instance.enable_node(node_name)


def disable_node(jenkins_instance, node_name):
    jenkins_instance.disable_node(node_name)
