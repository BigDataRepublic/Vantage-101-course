# Create base image
FROM python:3.8
# Set the working dir in the container
WORKDIR /vantage101

RUN apt-get update

# Copy the content of the repo to workdir
COPY . .
RUN pip install -r requirements.txt

# Run the app when container is built
CMD ["uvicorn", "main:app", "--reload"]
