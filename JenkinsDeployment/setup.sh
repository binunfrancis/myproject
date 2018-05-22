python GitClone.py
cd /home/server/MyProjects/JenkinsAutomation
cp final.yml jenkins.sh /etc/ansible
cd /etc/ansible
ansible-playbook final.yml --ask-sudo-pass
