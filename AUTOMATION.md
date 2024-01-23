
# AUTOMATION PROJECT.
AM writing an automation project based to my second blog taking about cancer.Acording to the research it is hd to stay informed about the latest advancements and new in cancer yet this is very important for both medical proffessionals,patients and we as students who are interested in the health sector and willing and motivated to to add more onto it
However,accesssing curated and up to date information to cancer related news can be challenging.Existing platforms lack a dedicated source for comprehensive,real time news specifically tailored to the advancements in a cancer sector as it focuses on a lot of stuff. I being a victims to this during the research I was doing to write my blog about the disease.

# AIM OF THE PROJECT.
To generate a centralized platform that aggregates and displays the latest news and advancements in the field of cancer.The goal is to bridge the gap in accessing timely and relevant information,fostering awareness and knowledge in the ever evolving landscape of cancer research and treatment.This involves the interaction of artificial intelligence and meical field specifically the cancer sector.
## TOOL TO USE FOR THE PROJECT.
After carrying out some resarch discovered that there several tools to use for my project that being java,javascript,c++ and others.But am going to use python for this specific project as I have some knowledge about python.
We  giong to use python to create a website that gives infomation about the latest information about cancer using its flask model and a News API
### TASK1
  Writing a code to create the app.Using python import Flask a web framework and requests a library for making HTTP requests.
Setting up a source for the information am going to used an API called newsAPI.org registered and obtained an access token.Created a templates folder and open up an Index.html file. This HTML template uses Jinja2 templating syntax to dynamically display the latest news articles. It loops through the list of news articles obtained from the Flask route and displays relevant information such as title, description, source, and a link to read more.Then use the flask render template function to the Index.html in the template folder.

### RUNNING THE APP.
After writing the python script and rendering the Index.httml in the template file it took gave me a link that runs on net and gave me results showing the latest cancer news.
#### Then copied my code and put in into the main.py,copied the index.html file,gitinore and requirements.txt file to my github repository.
#### Challenge.
Since my repository is public repo my code can be accesed by anyone and so is my API_ key.I used chatgpt to give a solution.
For this I created a new secretes repository on github and saved it as a variable then replaced the API in my code by the variable and imported the os module of python which was added to my code.After this my API code was secured.


##### import os

##### api_key = os.environ.get('YOUR_API_KEY')

### TASK2
Automating the script.
Create a .github/workflows directory in the root of your Python project, and then add a YAML file inside it.Then checkout if the code runs with no error.then after edit the yaml file to indicate the period of time after which the python code should run
### Challenge.
The code is running without stopping.
According to chatGPT By default, Flask applications don't stop automatically. They typically run continuously until you manually stop them. When you run a Flask application using the app.run() method, it starts a web server, and the application will keep running until you interrupt the process.
### solution.
To solve the challenge of the code running without stopping.We going to edit the code my adding a timeout stop the code from running after three minutes.By adding this line in the yaml file.
 ###### - name: Run Your Code
######      timeout-minutes: 2
######      run: python main.py

### Automating the project.
Automation of the file can me done by modifying the github overflows file by editing tehe yaml file by scheduling it
The on section is replaced with the schedule event.
The cron syntax '0 0 */2 * *' specifies a cron expression that triggers the workflow every two days at midnight UTC.
###### name: Cancer Workflow

###### on:
######  schedule:
######    - cron: '0 0 */2 * *'

#### CHALLENGE.
The web application only runs on my local machine and can not run on other machines this because;
When you run a Flask application locally, you typically use the development server provided by Flask, which is suitable for testing and development purposes. This server is lightweight and easy to use but is not suitable for production use due to its limitations in terms of performance, security, and features.
For production deployment, Flask applications are often run using production-ready web servers like Gunicorn, uWSGI, or mod_wsgi, and they can be deployed on servers, cloud platforms, or container orchestration systems.

##### SOLUTION.

To make my flask app run on gitbub am going to run it using a gunicorn server a

steps.

1.installing gunicorn using pip with command "pip install gunicorn" add  using Zeet run the app .It involves creating a zeet account,In ZEET there is a need to select an cloud server to run the automation project for example AWP(Amazon Web providers),Digital Ocean,Google cloud platform,Microsoft Azure,Vultre and maymore others after that there is need to create a connection between my github account and zeet and then run the app.

In the process of deploying my Flask app, I initiated the installation of Gunicorn locally using the command "pip install gunicorn." Subsequently, I created accounts on Zeet and Amazon Web Providers (AWP). After obtaining an AWP token, I integrated it into my Zeet account to facilitate the deployment of my project in the cloud. However, during the AWP account creation, I encountered a request for bank account details and a 5 euros fee. Since my goal is to utilize the code exclusively for local purposes without seeking any monetary gains, I decided to forego the production phase with AWP and continued running my project locally on my machine only.

### CONCLUSION.

The automation project serves as a valuable tool, keeping me effortlessly informed about the latest Cancer news and medical breakthroughs. It not only saves me precious time that would otherwise be spent scouring the internet for updates but also ensures I stay up-to-date on the latest advancements in the medical field, particularly in the realm of cancer research. This streamlined approach allows me to effortlessly stay connected with the latest developments without the hassle of manual searches.

