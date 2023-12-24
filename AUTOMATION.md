# AUTOMATION PROJECT.
AM writig an automation project based to my second blog taking about cancer.Acording to the research it is hd to stay informed about the latest advancements and new in cancer yet this is very important for both medical proffessionals,patients and we as students who are interested in the health sector and willing and motivated to to add more onto it
However,accesssing curated and up to date information to cancer related news can be challenging.Existing platforms lack a dedicated source for comprehensive,real time news specifically tailored to the advancements in a cancer sector as it focuses on a lot of stuff. I being a victims to this during the research I was doing to write my blog about the disease.

# AIM OF THE PROJECT.
To generate a centralized platform that aggregates and displays the latest news and advancements in the field of cancer.The goal is to bridge the gap in accessing timely and relevant information,fostering awareness and knowledge in the ever evolving landscape of cancer research and treatment
## TOOL TO USE FOR THE PROJECT.
After carrying out some resarch discovered that there several tools to use for my project that being java,javascript,c++ and others.But am going to use python for this specific project as I have some knowledge about python.
We  giong to use python to create a website that gives infomation about the latest information about cancer using its flask model and a News API
### TASK1
  Writing a code to create the app.Using python import Flask a web framework and requests a library for making HTTP requests.
Setting up a source for the information am going to used an API called newsAPI.org registered and obtained an access token.Created a templates folder and open up an Index.html file. This HTML template uses Jinja2 templating syntax to dynamically display the latest news articles. It loops through the list of news articles obtained from the Flask route and displays relevant information such as title, description, source, and a link to read more.Then use the flask render template function to the Index.html in the template folder.

###RUNNING THE APP.
After writing the python script and rendering the Index.httml in the template file it took gave me a link that runs on net and gave me results showing the latest cancer news.
#### Then copied my code and put in into the main.py,copied the index.html file,gitinore and requirements.txt file to my github repository.
#### Challenge.
Since my repository is public repo my code can be accesed by anyone and so is my API_ key.I used chatgpt to give a solution.
For this I created a new secretes repository on github and saved it as a variable then replaced the API in my code by the variable and imported the os module of python which was added to my code.After this my API code was secured.


##### import os

##### api_key = os.environ.get('YOUR_API_KEY')

### TASK2
Automating the script.

