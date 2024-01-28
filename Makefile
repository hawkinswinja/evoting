SHA ?=
USER ?=
PASSWORD ?=

.PHONY: get_sha
get_sha:
	@echo $(SHA)

build:
	@docker build -t hawkinswinja/ikura:$(SHA) .
	@echo 'check image tag'
	@docker images | grep ikura
.PHONY: build

tests: build
	@echo 'running tests ...'
.PHONY: tests

push: tests
	@docker login --username $(USER) --password $(PASSWORD)
	@docker push hawkinswinja/ikura:$(SHA)
.PHONY: push