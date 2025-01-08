# Wake up docker containers
up:
	docker-compose -f docker-compose.yml up -d

# Shut down docker containers
down:
	docker-compose -f docker-compose.yml down

# Show a status of each container
status:
	docker-compose -f docker-compose.yml ps

test:
	docker-compose -f docker-compose.yml exec -e DEBUG=True cve_extract_api sh -c "cd .. && pytest -vv -s tests/test_GRPCAsyncServer.py"

# Status alias
s: status

# Show logs of each container
logs:
	docker-compose -f docker-compose.yml logs

# Restart all containers
restart: down up

# Build and up docker containers
build:
	docker-compose -f docker-compose.yml build --force-rm

# Build and up docker containers
rebuild: down build

connect:
	 docker exec -it vpn-manager bash

grant-permissions:
	docker-compose -f docker-compose.yml exec -T -u root vpn-manager-postgres chown postgres:postgres /var/lib/postgresql/data

check-linters:
	docker-compose run --rm lint

