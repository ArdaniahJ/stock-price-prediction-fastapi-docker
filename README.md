# Stock Price Prediction and Deployment with FastAPI and Docker
This repository showcases the process of creating a RESTful API using FastAPI for stock price prediction and deploying it using Docker. 

## Objectives:
* Develop a RESTful API using Python and FastAPI.
* Construct a stock price prediction model using the FB Prophet library.
* Deploy the FastAPI application using Docker.

## Prerequisites
Ensure that you have Docker Desktop install on your system. If you're using Windows OS, follow these steps:
+ __Install Docker Desktop__: You can install Docker Desktop by visiting [here](https://docs.docker.com/desktop/install/windows-install/)
+ __Prerequisites for Docker Desktop:__
  * __WSL Distribution:__ Download WSL distribution (e.g: Ubuntu) from Microsoft Store. Update the distribution to WSL2. IF you're starting fresh, you can directly download WSL2.
  * __Enable Hyper-V:__ If your version of Windows supports Hyper-V, enable it. If not (e.g: Windows 10 Home), you can manually set it up. Create a new Notepad file and paste the codes below, then save it with a .bat extension. Run batch file and restart your system if prompted:
    ```
    pushd "%~dp0"
    dir /b %SystemRoot%\servicing\Packages\*Hyper-V*.mum >hyper-v.txt
    for /f %%i in ('findstr /i . hyper-v.txt 2^>nul') do dism /online /norestart /add-
    package:"%SystemRoot%\servicing\Packages\%%i"
    del hyper-v.txt
    Dism /online /enable-feature /featurename:Microsoft-Hyper-V -All /LimitAccess /ALL
    pause
     ````
        
## Getting Started
This readme is divided into 3 parts:
1. Pull the Docker Image from Docker Hub and Predict the Stock Price locally: [Go to Getting Started 1](#getting_started_1)
2. Clone this repository (Predict the Stock Price Using Pre-trained Model w/o Docker):  [Go to Getting Started 2](#getting_started_2)
3. Step-by-step code guide for model creation to deployment from scratch via Windows OS VSCode: [Go to Getting Started 3](#getting_started_3)

<a name="getting_started_1"></a>
### Getting Started 1
1. __Pull the Docker Image from Docker Hub:__
```
docker pull ardnhj/stock-price-prediction-app:latest
```

2. __Run the Docker Container:__
+ You can choose any available port number as long as it's not occupied by other applications. Alternatively, change the port manually in the following files:
    + __main.py:__ Replace `--port 8000` with your desired free port. 
    + __Dockerfile:__ Change the port in the `EXPOSE` statement. 
```
docker run -p 8000:8000 -d <your-dockerhub-username>/stock-price-prediction-app
```
+ Replace 'your-dockerhub-username' with your actual Docker Hub username.
<a name="FastAPI"></a>
3. __Access the FastAPI App:__
+ Use the following `httpie` commands in the terminal to interact with the FastAPI app:
   + To check if the app is running:
   ```
   http GET http://localhost:8000/ping
   # Output: {"ping": "pong!"}
   ```
   + To get the stock price predictions (_Replace MSFT with the desired stock ticker_):
   ```
   http POST http://localhost:8000/predict ticker=MSFT
   # Output: JSON of the predicted stock prices
   ```
+ Open your browser and navigate to http://localhost:8000 to access the running FastAPI app.

__Note:__ 📝 The @app.post decorator with the '/predict' endpoint only accepts POST request. IF you try to access it through a web browser, you will see the response:
``
{"detail":"Method Not Allowed"}.
``
+ In `main.py`, there are two '/predict' endpoints. 
  * __@app.get decorator:__ allows users to pass the ticker as a query parameter.
  * __@app.post decorator:__ accepts the ticker in the request body. <br>
+ To view the JSON response through a web browser, use the following code:
  ```
  http GET http://localhost:8000/predict?ticker=MSFT
  # Output: JSON of the predicted stock prices (accessible through a web browser)
  ```
    
<a name="getting_started_2"></a>
### Getting Started 2: Predict the Stock Price Using Pre-Trained Model (Without Docker)
This section will showcases on how to use Pre-Trained Model and deploy it using FastAPI and Docker.
1. __Clone this repository to your local machine:__
```
git clone https://github.com/your-username/stock-price-prediction-fastapi-docker.git
```

2. __Navigate to the project directory:__
```
cd stock-price-prediction-fastapi-docker
```

3. __Install the required Python packages:__
```
pip install -U pip
pip install -r requirements.txt
```

4. __Run the FastAPI App:__
+ Run the FastAPI app using the pre-trained model.
```
uvicorn main:app --host 0.0.0.0 --port 8000
```

5. __Access the FastAPI App:__
+ Navigate to htpp://localhost:8000 in your browser to access the FastAPI app. The API root message will appear:
```
{"message": "Welcome to the FastAPI ML Model API!"}
```
6. __Predict Stock Prices:__
+ Uncomment the code in `model.py` in predict function to allow predicted graph to appear:
```
#model.plot(forecast).savefig(f"{ticker}_plot.png")
#model.plot_components(forecast).savefig(f"{ticker}_plot_components.png")
```
+ To predict stock prices, use the following HTTPie command (_Replace 'MSFT' with the desired stock ticker_).:
```
http POST http://localhost:8000/predict ticker=MSFT
```
+ The output will be the JSON of the predicted stock prices.

<a name="getting_started_3"></a>
### Getting Started 3
This section will showcase on how to setup the project and deploy your FastAPI app using Docker from scratch.
1. __Create a New Directory:__
+ Open your terminal and create a dedicated directory for your project:
```
mkdir your-directory
cd your-directory
```
2. __Create Virtual Environment:__
+ Create and activate a virtual environment to isolate your project dependencies:
```
python -m venv venv-name
.\venv-name\Scripts\activate
```
3. __Create Essential Files:__
+ Generate 4 necessary files using this code `echo. > file-name.ext`:
    + __main.py__: to store the routes of the APIs
    + __model.py__: for the ML model
    + __Dockerfile (w/o ext)__: configuration to create Docker img (📝 be careful as it's case sensitive)
    + __.dockerignore (w/o ext)__: to specify a list of files or directories for Docker to ignore during the build process.
      
4. __Install dependencies:__
+ Update pip and install required packages according to its versions below:
```
pip install -U pip
pystan==3.7.0
fastapi==0.95.2
gunicorn==20.1.0
uvicorn==0.22.0
prophet==1.1.3
joblib==1.2.0
pandas==2.0.1
plotly==5.14.1
yfinance==0.2.18
```
+ Or just enter it in one line:
 ```
pip install pystan==3.7.0 fastapi==0.95.2 gunicorn==20.1.0 uvicorn==0.22.0 prophet==1.1.3 joblib==1.2.0 pandas==2.0.1 plotly==5.14.1 yfinance==0.2.18 
```
+ In case venv is unable to upgrade the pip due to the virtual env, use this code to fix it: `python -m pip install --upgrade pip
`
+ In case if you're having trouble installing pystan, `pip install cython` first, then try to install pystan again.

5. __Build and Train ML Model:__
+ Use `model.py` that was created on Step 3. Then, refer to the provided `model.py` file in this repo to build and train your stock price prediction model using Prophet. Below is the snippet code to train the model:
```
python
>>> from model import train, predict, convert
>>> train() # put in the desired ticker, eg: "AAPL" for Apple, "GOOGL" for Google
>>> prediction_list = predict ()
>>> convert(prediction_list)
```

6. __Create FastAPI Routees:__
+ Implement FastAPI endpoints for your predictions. + Use `main.py` that was created on Step 3 then reveiw the `main.py` file in this repo for guidance on creating routes and handling requests.
+ Run your FastAPI app locally using Uvicorn:
```
uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8000
```
+ `main:app` tells Uvicorn where it can find the FastAPI ASGI application -- i.e., "within the the 'main.py' file, you'll find the ASGI app, app = FastAPI().
+ Navigate to `http://localhost:8000/ping` to verify that the app is running. It should return `{"ping": "pong!"}`.

7. __Dockerize Your FastAPI App:__
+ From the `Dockerfile` created in Step 3, add in the configuration specified in the `Dockerfile` file from this repo.
+ In Dockerfile, there is one command `EXPOSE` where you stated which port to use. Port 8000 is the free port used for this project. You may use your desired available. Below steps is check whether the port is occupied or free:
     * Open the Command Prompt > Press `Win + R` to open the CMD.
     * Run `netstat` Command > In the Command Prompt window, type the following command and press Enter:
       ```netstat -ano | findstr :PORT_NUMBER ```
     * Replace "PORT_NUMBER" with the port number you want to check (e.g., 8000).
     * Interpret Results:
       + If the port is free, you won't see any output related to the specified port.
       + If the port is in use, you will see output lines indicating the status of the port and the process using it, along with the process ID (PID).
       + Below snippet is what the output might look like if the port is in use:
       + In the output snippet, replace "8000" with your desired port number, and "PID" will be the process ID of the application using that port. If there's no output for the specified port, it means the port is free and available for use.
       + In this project, Gunicorn (a production-grade WSGI application server) is used to manage Uvicorn with 3 worker processes for concurrency and parallelism purposes in case for future scaling.
```
TCP    0.0.0.0:8000           0.0.0.0:0              LISTENING       PID
TCP    [::]:8000              [::]:0                 LISTENING       PID
```
+ Kill it if you wish to use the port:
`` taskkill /F /PID PID-number``
+ Create a requirements file named 'requirements.txt' with the necessary packages:
```
pip freeze > requirements.txt
```
+ Build Docker image and run your Docker container:
```
docker build -t docker-image-name .
docker run  -p 8000:8000 -d docker-container-name
```
+ Navigate to [FastAPI section here](#FastAPI) on how to properly access the FastAPi via HTTP. 

8. __Push Docker Image to Docker Hub:__
+ Login to your Docker account: `docker login`. Enter username and password when prompted
+ Tag your Docker img with your Docker Hub username and repo name:
    ```
    docker tag your-fastapi-app your-dockerhub-username/your-repo-name:latest
    ```
+ Push the tagged img to Docker Hub:
  ```
  docker push your-dockerhub-username/your-repo-name:latest
  ```

# Future Checklist for this Project

This section outlines potential future tasks and improvements for the project:

- [ ] Create a comprehensive video tutorial covering the entire process from project setup to deployment.
- [ ] Explore deploying the FastAPI app to platforms like Heroku registry or equivalent cloud services (e.g., AWS) to host the web application.
- [ ] Implement a database to store prediction results, allowing for historical analysis and comparison.
- [ ] Practice Test-Driven Development (TDD) when writing code. This involves writing tests before implementing functionality, ensuring code quality and documentation.
