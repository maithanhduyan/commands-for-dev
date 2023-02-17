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