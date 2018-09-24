repository = nicbet
image = datascience-jupyter
tag = $(repository)/$(image)
compiler = ../scripts/compile.py
JUPYTER_TOKEN=84a471ab58d5dbe8c23455b5b6a92f143cc871b1674a5457d83cbb377d06b18c

all: $(tag)

.DEFAULT: all
.PHONY: clean mrproper stop pull

# Build the docker image
$(tag): compile Dockerfile $(compiler) 
	$(info Building image with tag $(tag))
	@docker build -t $(tag) --build-arg JUPYTER_TOKEN=$(JUPYTER_TOKEN) -f Dockerfile --squash ..

compile: Dockerfile.source $(compiler)
	$(info Compiling docker file for tag $(tag))
	python $(compiler) Dockerfile.source

# Deploy the image to docker.io
push: $(tag)
	$(info Deploying image with tag $(tag))
	@docker push $(tag)

# Fetch the image from docker.io (requires `docker login` for private repositories)
pull:
	$(info Pulling image with tag $(tag))
	@docker pull $(tag)

# Delete all images for $(tag)
mrproper: clean
	$(info Removing images for tag $(tag) and pruning related images.)
	-docker rmi $(tag) >/dev/null 2>&1
	-docker rmi $(shell docker images -a --filter=dangling=true -q) >/dev/null 2>&1

run:
	@docker run --rm -it -p 8888:8888 -v $(pwd):/home/datascience/work $(tag)

