


# PROJECT NAME: BK Queuing System

BK Queuing System is a Django-based web application that aims to improve on the current physical queuing system by replacing it with a more efficient virtual queuing system. BK clients will be able to reserve a slot in the queue for a specific service, as well as update and delete the reservation, using this queuing system. They will also be able to view queues at different BK branches.

What distinguishes this BK Queuing system from others is that customers will no longer have to wait in line at the bank for their turn to be served; instead, they will be able to track, delete, and update their reservations directly from their smartphones.

Video walkthrough : https://drive.google.com/file/d/1I24c2EidtkmzxEx8C5hcQMJEM6z4yZli/view?usp=sharing

# Beneficiary
  1.Bank
  # How will they benefit from this?
    Increasing customer retention
    Loyalty of satisfied customers
    Resource maximizing
2. Clients
# How will they benefit from this?
  Less queuing time(queue virtually)
  Ability to keep track of queues at different branches of BK
  Satisfaction with no exposure to Covid-19
3. Government
# How will they benefit from this?
  Economy wise


# Assumptions:
  1. All services provided by BK take approximately 20seconds to complete, this is only for the prototype but can be changed by the bank to 20 minutes. 
  2. Every customer will have access to the services(virtual services)


# Limitations
  1. Not every BK customer owns a smartphone to access the system 
  2. System will be subjected to cyber-attacks.
  3. There may be resistance to change from the traditional queuing system.

# Potential extensions
  1. Use of USSD codes to cater for those who do not have access to smartphones and/or internet access.
  2. Implement accurate duration per service(as per data from surveys).
  3. Invest in cyber security
  
 # LIBRARIES and PACKAGES

 # DISCLAIMER
 Bk python system uses environ server to display the current state of the queue as customers are being served and leaving the queue. Unfortunately, windows operating system does not support environ server. Therefore, this project works solely for Ubuntu users and this is how you can get it running


Step 1: Install Python and Pip
	   First update the local APT repository
		sudo apt-get update && sudo apt-get -y upgrade

	  Install Python3
	  sudo apt-get install python3

	  Verify the successful installation of Python3
	  python3 -V

	  Installing pip
	  sudo apt-get install -y python3-pip

	  Verifying the installation of Pip
	  pip3 -V

Step 2: Install a virtual environment

  A virtualenv allows you to install software and Python packages in a contained development space, which isolates the installed software and packages from the rest of your machine’s global environment. 
  Install a virtual environment
  pip3 install virtualenv

  Verifying the installation of the virtual environment
  virtualenv --version

Step 3: Install Django

	  Navigate to the project’s directory
	  Use cd <directoryName> to navigate to the directory

	  Create virtual environment
	  virtualenv <virtual environment name>

	  Activate the virtual environment
	  . <virtual environment name>/bin/activate

	  Install django
	  pip install django

	  Verify that django installation
	  django-admin --version

Step 4: Install project dependencies and other python packages
    Install environ
    python3 -m pip install django-environ

    Install Django Redis Queue
    python3 -m pip install django-rq

    Install Django Redis
    python3 -m pip install django-redis

Step 5: Run the server
    python3 manage.py runserver

    You see the following:
    Django version 4.0.4, using settings 'QueueSystem.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.



