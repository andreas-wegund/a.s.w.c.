
### SET BASE PYTHON IMAGE
FROM python:3.12-alpine
LABEL authors="awegund"


### RUN echo python -v --progress=plain --no-cache
### RUN echo npm -v --progress=plain --no-cache

### SET ENV VARIABLES
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1


### CREATE PROJECT DIRECTORY
RUN mkdir "/code"

### UPGRADE PIP & FREEZE REQUIREMENTS
RUN pip install --upgrade pip
RUN pip freeze > "requirements.txt"

### COPY THE PROJECT INTO DOCKER IMAGE FOLDER
COPY . "/code"


### SET WORKDIR
WORKDIR "/code"


### INSTALL REQUIREMENTS
RUN pip install -r requirements.txt


# CREATE STATICS FOLDERS
### RUN python manage.py collectstatic


### RUN THE APPLICATION
CMD ["python", "manage.py", "runserver", "0.0.0.0:3000"]