# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to C:\app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Upgrade setuptools and install required Python packages
RUN pip install --upgrade setuptools && \
    pip install cython==3.0.2 numpy==1.25.2 pandas==2.0.1 pystan==3.7.0

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Copy the application code to the container
COPY . .

# Run the application using gunicorn and UvicornWorker 
CMD ["gunicorn", "-w", "3", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]
 
