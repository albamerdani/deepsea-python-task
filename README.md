# deepsea-python-task

### Structure
The application is structured in 3 packages:

controller package - contains reports.py file with routes to access the api from browser and calls service methods, also jsonify the result.

service package - contains python files and classes with methods to read the log file, to extract required information and to put in a structured way in dictionaries.

unittests package - contains test_main.py file with some simple unit tests for the methods.

.env file is added on purpose. Please update the path of logfile there depending on the path that file is located in your OS
in this format below:

`FILE_PATH=path/to/your/log/file
`
### Run the app
To run the application for the reports please run the main.py python file under the repository folder.

First install Python3 and Flask in your environment.

`pip3 install flask ` or `pip install flask`

In terminal go to the path of deepsea-python-task repository.

Go with `cd /path/to/repo/directory`

Then install python libraries and packages required for this task under requirements.txt file

`pip3 install -r requirements.txt
`

To run the application locally:

Windows

`python app/main.py -m user
`

Linux

`python3 app/main.py `


Open your browser and put the below paths to access json reports

http://127.0.0.1:5000/top10Pages

http://127.0.0.1:5000/top10Hosts

http://127.0.0.1:5000/top10HostsDetailed

http://127.0.0.1:5000/successPercentage

http://127.0.0.1:5000/unsuccessfulPercentage

http://127.0.0.1:5000/top10Unsuccessful

### Unit tests
Under unittest package is test_main.py file where are implementes some unit tests methods.

Go with `cd /path/to/repo/directory`
Use this command to run tests:

Windows

`C:\Python39\python.exe -m unittest app/unittests/test_main.py`

or 

`python -m unittest app/unittests/test_main.py`

### Docker
Application is also containerized.

Run `docker build -t deepsea .` to build the docker image and then run it

`docker run -it deepsea`

or

`docker-compose up`