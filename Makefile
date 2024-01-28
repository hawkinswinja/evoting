IMAGE_TAG ?=
USER ?=
PASSWORD ?=

.PHONY: get_sha
get_sha:
	@echo $(SIMAGE_TAG)

build:
	@docker build -t hawkinswinja/ikura:$(IMAGE_TAG) .
	@echo 'check image tag'
	@docker images | grep ikura
.PHONY: build

tests: build
	@echo 'running tests ...'
.PHONY: tests

push: tests
	@docker login --username $(USER) --password $(PASSWORD)
	@docker push hawkinswinja/ikura:$(IMAGE_TAG)
.PHONY: push