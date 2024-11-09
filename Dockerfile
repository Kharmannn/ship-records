# Use the official Python base image
FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y wget unzip curl gnupg && \
    apt-get install -y --no-install-recommends \
    libglib2.0-0 libnss3 libx11-xcb1 libxcomposite1 libxrandr2 libxdamage1 \
    libxi6 libxtst6 libpangocairo-1.0-0 libatk1.0-0 libcups2 libdrm2 \
    libxss1 libgdk-pixbuf2.0-0 libxshmfence1 libgbm1 libasound2 \
    fonts-liberation libappindicator3-1 xdg-utils libu2f-udev chromium-driver && \
    pip install pip --upgrade && \
    rm -rf /var/lib/apt/lists/*

# create unprivileged user
RUN adduser --disabled-password --gecos '' myuser  

# download and install chrone
RUN apt-get install -y wget
RUN curl -fsSL https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-linux.gpg
RUN sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-linux.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list'
RUN dpkg -i google-chrome-stable_current_amd64.deb || apt-get install -f -y

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Set display port to avoid Chrome errors
ENV DISPLAY=:99

# Install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Selenium script into the Docker image
COPY . /app
WORKDIR /app

# Run the Selenium script
# CMD ["python3", "/app/src/abs_crawler.py"]