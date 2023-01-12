# Create base image
FROM continuumio/miniconda3 AS system_build
# Set the working dir in the container
WORKDIR /vantage101

RUN apt-get update
RUN apt-get install zip unzip

# Copy the content of the repo to workdir
COPY . .
RUN conda env create -f env.yml

# Run the app when container is built
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "v101", "uvicorn main:app --reload"]
