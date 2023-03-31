# Specify the path to the YAML file
DYNAMODB_ONLY := dynamodb-local-only.yaml
DYNAMODB_AWSCLI := dynamodb-aws-cli.yaml

.PHONY: start-dynamodb-only start-dynamodb-aws-cli stop-dynamodb-only stop-dynamodb-aws-cli

# Start the containers using the specified YAML file
start-dynamodb-only:
	docker compose -f $(DYNAMODB_ONLY) up -d --remove-orphans

start-dynamodb-aws-cli:
	docker compose -f $(DYNAMODB_AWSCLI) up -d --remove-orphans

# Stop and remove the containers
stop-dynamodb-only:
	docker compose -f $(DYNAMODB_ONLY) down

stop-dynamodb-aws-cli:
	docker compose -f $(DYNAMODB_AWSCLI) down
