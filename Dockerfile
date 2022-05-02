# FROM python:3.8

# ENV PORT 80
# ENV HOST 0.0.0.0

# EXPOSE 80

# RUN apt-get update -y && \
#     apt-get install -y python3-pip

# COPY ./requirements.txt /app/requirements.txt

# WORKDIR /app

# RUN pip install -r requirements.txt

# COPY . /app


# ENTRYPOINT ["python", "app.py"]


FROM python:3.8.0-slim

# Copy local code to the container image
COPY . /app

# Sets the working directory
WORKDIR /app

# Upgrade PIP
RUN pip install --upgrade pip

#Install python libraries from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set $PORT environment variable
ENV PORT 80

# Run the web service on container startup
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app

#ENTRYPOINT ["python", "app.py"]
