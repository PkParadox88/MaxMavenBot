# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Set the working directory to /app
WORKDIR /app

# Install Chrome
RUN apt-get update && apt-get install -y wget \
    && STORAGE_DIR=/opt/render/project/.render \
    && if [ ! -d "$STORAGE_DIR/chrome" ]; then \
        echo "...Downloading Chrome" \
        && mkdir -p "$STORAGE_DIR/chrome" \
        && cd "$STORAGE_DIR/chrome" \
        && wget -P ./ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
        && dpkg -x ./google-chrome-stable_current_amd64.deb "$STORAGE_DIR/chrome" \
        && rm ./google-chrome-stable_current_amd64.deb \
        && cd "$HOME/project/src" \
        && echo "...Chrome downloaded and installed"; \
    else \
        echo "...Using Chrome from cache"; \
    fi \
    && export PATH="${PATH}:/opt/render/project/.render/chrome/opt/google/chrome"

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && apt-get clean

# Copy the rest of your application code
COPY . .

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME=World

# Run your Flask app
CMD ["python", "app.py"]
