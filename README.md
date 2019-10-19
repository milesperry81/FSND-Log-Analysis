---LOG ANALYSIS PROJECT---

OVERVIEW:
This project uses a Python script to access a Postgre SQL database installed on an Ubuntu Virtual Machine. The virtual machine and database used were pre-created by Udacity. The output from the Python code answers a number of queries as posed by the Log Analysis Project.

USAGE:
The below instructions assume you have installed the Vagarant Virtual Machine as required for the Udacity Full Stack Nanodegree.

1. Copy the logAnalysis.py to the shared folder you have set up on the Vagrant Virtual Machine.

2. In order to use 'import psycopg2' statement in the Python file I had to run the following commands on the virtual machine. You may need to do this.

	sudo apt-get install postgresql-server-dev-9.5
	sudo pip3 install psycopg2

3. Within the terminal change directory to the shared folder where you saved logAnalysis.py.

4. Execute logAnalysis.py file with the following command:
	python3 logAnalysis.py

5. The results of the log analysis will be printed to terminal. The can be found in the output.txt file provided with this submission.