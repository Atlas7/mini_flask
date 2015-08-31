# Intro

I use this repository to help me:

- learn the basic concepts of Python Flask Web Framework.
- apply the newly acquired basic concepts in the making of full-stack web applications / websites.
- share with the world so others might potentially benefit from what I've learnt.

This is an early stage self-initiated project - expect this repository to change dramatically / gradually over time!

# Prerequisites

Install these tools on the personal devices (e.g. laptop, desktop, etc.).

- GitBash (for Git Linux environment)
- VirtualBox  (for hosting Virtual Machines)
- Vagrant  (for creating Vagrant Virtual Machines onto VirtualBox)
- SublimeText Editor (for editing codes)

# How things work

This is the general folder structure, with a description of how things work.

```
.git                # Git Version Control
/vagrant            # Run "vagrant up" here to start Vagrant VM
	.gitignore          # Exclude files from Git versioning / tracking.
	pg_config.sh        # vagrantfile runs this to install packages and dependencies. 
	vagrantfile         # Provide specification of the Vagrant VM.
	/basics             # I play around with Flask concepts here.
	/projects           # I build Flask projects here.
```

# Minimal Hello World Web Application

Let's try deploy our first web application!

1. Navigate to `/vagrant` folder.
2. Run `vagrant up` to start the Vagrant VM.
3. Run `vagrant ssh` to get into the Vagrant VM.
4. (within the Vagrant VM) Navigate to `/vagrant/basics/hello`.
5. Run `python hello.py`. This will run the Python Flask Web Server at `http://0.0.0.0:5000`. (Hit `Ctrl C` whenever we wish to turn off web server.)
6. From a browser (Chrome) visit `http://localhost:5000`. Note that we have successfully deploy our "Hello World" website on our local machine!

Notes:

- the `/vagrant` folder within the Vagrant VM is mapped to the `/vagrant` folder of the repository. Any changes we make on our laptop/desktop in this folder is shared with the Vagrant VM.
- port 5000 of the VM Guest is port-forwarded to port 5000 of local host machine (our laptop/desktop). We may use different ports if we wish - see `vagrantfile`.

# Some useful references

- Udacity Full-stack Web Development Courses
- Vagrant
- Flask Documentation.
