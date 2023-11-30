# deepsea-python-task

To run the application for the reports please run the main.py python file under the repository folder.

Run the below commands in your terminal

First install Python3 and Flask in your environment.

`pip3 install flask ` or `pip install flask`

To run the application locally:

In terminal go to the path of deepsea-python-task repository.

Windows

`python app/main.py -m user
`

Linux

`python3 app/main.py `


Open your browser and put the below paths to access json report

http://127.0.0.1:5000/top10Pages

http://127.0.0.1:5000/top10Hosts

http://127.0.0.1:5000/top10HostsDetailed

http://127.0.0.1:5000/successPercentage

http://127.0.0.1:5000/unsuccessfulPercentage

http://127.0.0.1:5000/top10Unsuccessful


Application is also containerized.

Run `docker build -t deepsea .` to build the docker image and then run it

`docker run -it deepsea`

or

`docker-compose up`