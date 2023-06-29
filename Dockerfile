FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

RUN apt-get clean && apt-get update && apt-get install -y \
    build-essential
# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Flask service
CMD ["waitress-serve", "--call", "--port=3000", "app:create_app"]
