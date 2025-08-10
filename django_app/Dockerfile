# Initiates image with Python 3.11 and Slim
FROM python:3.11-slim

# Initiotes Working Directory Inside the Container
WORKDIR /app

# Initiates system updates inside the container and cleans the cache generated during the installation
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

# Initiates copying of required dependencies inside the container.
COPY requirement.txt .

# Initiates the installation of the required libraries
RUN pip install --no-cache-dir -r requirement.txt

# Initiates copying of the files of the exitinf folder structure to the image
COPY . .

# Initates creating of directories for logs and data
RUN mkdir -p ./logs ./data


# Initiates running of entrypoint.sh with executable permission
RUN chmod +x ./entrypoint.sh


# Initiates collection of static files
RUN python manage.py collectstatic --noinput


# Initiate what port needs to opened for the Django app
EXPOSE 8000

# Initiates the entry point of the image
ENTRYPOINT [ "./entrypoint.sh" ]

