### SET BASE PYTHON IMAGE =====
FROM python:3.12-alpine
LABEL authors="awegund"


### SET ENV VARIABLES
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1


### CREATE PROJECT DIRECTORY & SET AS WORKDIR
RUN mkdir "/code"
COPY . "/code"
WORKDIR "/code"



### UPGRADE PIP
RUN pip install --upgrade pip
# RUN pip freeze > requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt



### EXPOSE THE PORT TO THE OUTSIDE WORLD
EXPOSE 8000







### RUN THE APPLICATION
### CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]