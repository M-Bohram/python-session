
import os
from jaac import env, jenkins, ssh, slack

# 1 - get jenkins node free space info

jenkins_instance = jenkins.get_jenkins_instance(os.getenv(
    'JENKINS_URL'), os.getenv('JENKINS_USERNAME'), os.getenv('JENKINS_TOKEN'))
node_size_gb = jenkins.get_node_size_gb(jenkins_instance, 'android')
print(node_size_gb)
# 2 - check if below certain threshold

# THRESHOLD = 300  # in GB

# if(node_size_gb < THRESHOLD):

# # 3 - if falls below the threshold, disable the node
#     jenkins.disable_node(jenkins_instance, 'android')
# # 4 - send slack notification (message) of being disabled
#     slack.send_slack_message(os.getenv('SLACK_TOKEN'), 'python-jenkins', f'Please notify that node {node} is offline to be cleaned')
# # 5 - ssh to the node and delete the workspace
#     ssh.execute_command()
# # 6 - enable the node
#     server.
# 7 - send slack notification (message) of being enabled
