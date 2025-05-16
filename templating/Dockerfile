
FROM python


RUN apt-get update && \
    apt-get install -y \
    wkhtmltopdf \
    build-essential \
    libssl-dev \
    libffi-dev \
    libjpeg-dev \
    zlib1g-dev \
    libxrender1 \
    libxext6 \
    libfontconfig1 && \
    apt-get clean


WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt


COPY . .


EXPOSE 5000
CMD ["python", "app.py"]
