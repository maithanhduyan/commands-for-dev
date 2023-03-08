### Install Jenkin on Debian 11
1. This is the Debian package repository of Jenkins to automate installation and upgrade. To use this repository, first add the key to your system:
~~~
	curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
~~~
2. Then add a Jenkins apt repository entry:
~~~
	echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d jenkins.list > /dev/null
~~~	
3. Update your local package index, then finally install Jenkins:
~~~
	sudo apt-get update
	sudo apt-get install fontconfig openjdk-11-jre
	sudo apt-get install jenkins
~~~
Done.
Jenkins running on localhost:8080
username: admin
password : (at file /var/lib/jenkins/secrets/initialAdminPassword)

The apt packages were signed using this key:
	pub   rsa4096 2020-03-30 [SC] [expires: 2023-03-30] 62A9756BFD780C377CF24BA8FCEF32E745F2C3D5
	uid   Jenkins Project 
	sub   rsa4096 2020-03-30 [E] [expires: 2023-03-30]

You will need to explicitly install a supported Java runtime environment (JRE), either from your distribution (as described above) or another Java vendor (e.g., Adoptium).

That's all.

# Installing Jenkins on Debian 11 

In this tutorial, we are going to explain in step-by-step detail how to Install Jenkins on Debian 11 OS.

Jenkins is a free open source continuous integration system tool written in Java, that helps developers to keep the code up to date in one place from different local machines. It is used for code automatic deployment, testing, building applications, and kind of securement that the latest code changes are always in the software.

Installing Jenkins on Debian 11 should take up to 10 minutes. Let’s get to work!
Prerequisites
A server with Debian 11 as OS
User privileges: root or non-root user with sudo privileges

Step 1. Update the System
Since we have a fresh installation of Debian 11, we need to update the packages to its latest versions available:

~~~~
sudo apt update -y && sudo apt upgrade -y
~~~~
Step 2. Install Java
Jenkins is written in Java, and that is why we need the Java installed on our system along with some dependencies:
~~~~
sudo apt install openjdk-11-jdk default-jre gnupg2 apt-transport-https wget -y
~~~~
To check whether Java is installed execute the following command:
~~~~
java -version
~~~~

Step 3. Add Jenkins GPG key and PPA
By default the repository of Debian 11, does not contain the Jenkins, so we need to add manually the key and the PPA.
~~~~
wget https://pkg.jenkins.io/debian-stable/jenkins.io.key

sudo apt-key add jenkins.io.key

~~~~

Once, the GPG key is added next is to add the PPA:
~~~~
echo "deb https://pkg.jenkins.io/debian-stable binary/" | tee /etc/apt/sources.list.d/jenkins.list

~~~~

Update the repository before you install Jenkins:
~~~~
sudo apt update -y

~~~~
Once, the system is updated with the latest packages, install Jenkins.

Step 4. Install Jenkins
~~~~
sudo apt-get install jenkins -y

~~~~
After the installation, start and enable the Jenkins service, in order for the service to start automatically after system reboot.
~~~~
sudo systemctl start jenkins && sudo systemctl enable jenkins

~~~~
To check the status of the service execute the following command:
~~~~
sudo systemctl status jenkins

~~~~

Another way to check if Jenkins, is active and running is to check port 8080
~~~~
netstat -tunlp | grep 8080

~~~~
Step 5. Finish Jenkins Installation
After successful installation we can finish the installation by accessing the Jenkins Web Interface:

http://127.0.0.1:8080


# References
[](https://www.rosehosting.com/blog/how-to-install-jenkins-on-debian-11/)