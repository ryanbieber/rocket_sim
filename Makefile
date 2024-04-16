# Makefile

# Variables
DOCKER_IMAGE_NAME := rocket_sim
DOCKER_CONTAINER_NAME := rocket_sim

# Build the Docker image
build:
	docker build -t $(DOCKER_IMAGE_NAME) .

# Run the Docker container
run:
	docker run -d --name $(DOCKER_CONTAINER_NAME) $(DOCKER_IMAGE_NAME)

# Stop and remove the Docker container
stop:
	docker stop $(DOCKER_CONTAINER_NAME)
	docker rm $(DOCKER_CONTAINER_NAME)

# Clean up the Docker image
clean:
	docker rmi $(DOCKER_IMAGE_NAME)