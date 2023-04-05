ifdef_check = $(if $(SCRIPT),,@echo "SCRIPT variable is not set or empty"; exit 1)

# Specify the path to the YAML file
DYNAMODB_ONLY := dynamodb-local-only.yaml
DYNAMODB_AWSCLI := dynamodb-aws-cli.yaml

.PHONY: start-dynamodb-only \
	start-dynamodb-aws-cli \
	stop-dynamodb-only \
	stop-dynamodb-aws-cli \
	create-network \
	create-directories

create-directories:
	mkdir -p data_inputs data_outputs secrets
	mkdir -p docker/dynamodb
	chmod 777 -R docker/dynamodb

create-network:
	docker network inspect dynamodb_showroom >/dev/null 2>&1 || docker network create dynamodb_showroom

# Start the containers using the specified YAML file
start-dynamodb-only: create-directories
	docker compose -f $(DYNAMODB_ONLY) up --remove-orphans

start-dynamodb-aws-cli: create-directories
	docker compose -f $(DYNAMODB_AWSCLI) up --remove-orphans

# Stop and remove the containers
stop-dynamodb-only:
	docker compose -f $(DYNAMODB_ONLY) down

stop-dynamodb-aws-cli:
	docker compose -f $(DYNAMODB_AWSCLI) down

build-python:
	docker build --progress=plain --no-cache -t "python_dynamodb_scripts" ${PWD}/python

run-python:
	docker run --rm -it \
	--network dynamodb_showroom \
	-v "${PWD}/data_inputs/":"/inputs" \
	-v "${PWD}/data_outputs/":"/outputs" \
	-v "${PWD}/secrets":/secrets \
	-v "${PWD}/python/$(SCRIPT)":/app \
	--name $(SCRIPT) \
	python_dynamodb_scripts
