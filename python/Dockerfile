# Use a Python base image
FROM python:latest

# Copy the protobuf script and requirements file into the container
COPY requirements.txt /pip/

# Install required Python dependencies
RUN pip install --verbose -r /pip/requirements.txt \
    && pip install --verbose pylint

# Set the working directory
WORKDIR /app

# Run the script on container start
CMD [ "python", "/app/script.py" ]
