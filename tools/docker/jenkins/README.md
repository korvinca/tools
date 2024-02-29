## Jenkins Server + Agent on localhost

### Install Jenkins service

```ruby
# Create docker volume start Jenkisn server for test
docker volume ls
docker volume prune
mkdir ~/jenkins_home

export DOCKER_DEFAULT_PLATFORM=linux/amd64 # Optional for M1-3 Mac users

docker volume create --opt type=none --opt o=bind --opt device=/Users/username/jenkins_home jenkins_home
docker volume inspect jenkins_home
docker run -d -v jenkins_home:/var/jenkins_home -p 8080:8080 --name jenkins-server jenkins/jenkins:2.385-slim
curl http://localhost:8080 # Optional
docker exec jenkins-server cat /var/jenkins_home/secrets/initialAdminPassword
# In Browser http://localhost:8080 > paste hash
docker rm -f jenkins-server

# Create jenkins-agent ssh key
cd ~/.ssh
ssh-keygen -t ed25519 -f jenkins-agent -C jenkins
cat ~/.ssh/jenkins-agent.pub | pbcopy # replace the public key in docker-compose.yml
```

```ruby
# Create docker compose stack
cd tools/docker/jenkins

# Build Jenkins agent
docker compose build # Optional --no-cache
docker images

# Start Jenkins stack
docker-compose up -d # Optional --force-recreate
docker-compose ls
docker-compose ps
```

### Setup Jenkins

#### Disable Jenkins as local agent
Login: http://localhost:8080

http://localhost:8080/manage/computer/(built-in)/configure

Number of executors = 0

#### Add a new agent in Jenkins
* In Jenkins: http://localhost:8080/manage/credentials/store/system/domain/_/ > Add a new credential "jenkins" with ssh key
* UID: agent
* Number of executors: 4
* Remote root directory: /home/jenkins
* Username: jenkins
* Private Key: on host > cat ~/.ssh/jenkins-agent | pbcopy
* Add a new agent: http://localhost:8080/computer/ > New node > Agent > Permanent Agent
* Launch method: Lunch agent via SSH
* User: jenkins
* Host Key Verification Strategy: Not verifing

#### Connect Jenkins to bitbucket.org
* In Jenkins: http://localhost:8080/manage/credentials/store/system/domain/_/ > Add a new credential "<user_in_bitbucket>" with ssh key

```ruby
docker exec -it jenkins-server-1 bash
ssh -t git@bitbucket.org
exit
```

* Fix Git Host Key Verification Configuration in Jenkins

```ruby
You're using 'Known hosts file' strategy to verify ssh host keys, but your known_hosts file does not exist, please go to 'Manage Jenkins' -> 'Configure Global Security' -> 'Git Host Key Verification Configuration' and configure host key verification.
```

* http://localhost:8080/manage/configureSecurity/ > 'Git Host Key Verification Configuration' > Accept first connection
* Add more plugins: http://localhost:8080/manage/pluginManager/available > Rebuilder, CloudBees AWS Credentials Plugin, etc.

Login in Jenkins and add permanent agent: https://blog.xentoo.info/2023/04/21/run-jenkins-and-jenkins-agents-on-docker/

#### Start or delete Jenkins
```ruby
# Start Jenkisn container after docker stoped 
docker start jenkins-agent-1 jenkins-server-1

########### Delete Jenkins stack ###########
cd tools/docker/jenkins
docker-compose down
docker rmi $(docker images -f "dangling=true" -q) -f # optional
docker system prune -a # Clear all docker cache
docker volume prune # Clear docker volume cache
```