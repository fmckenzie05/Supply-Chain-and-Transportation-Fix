# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
# Uncomment the line below if you have a requirements.txt file
# RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable
ENV NAME World

# Run your program when the container launches
CMD ["python", "./your-script.py"]
