PROJECT_NAME := OVH Package

SHELL            := /bin/bash
PACK             := ovh
ORG              := ovh
PROJECT          := github.com/${ORG}/pulumi-${PACK}
NODE_MODULE_NAME := @pulumi/${PACK}
TF_NAME          := ${PACK}
PROVIDER_PATH    := provider/v2
VERSION_PATH     := ${PROVIDER_PATH}/pkg/version.Version

JAVA_GEN 		 := pulumi-java-gen
JAVA_GEN_VERSION := v0.17.0
TFGEN           := pulumi-tfgen-${PACK}
PROVIDER        := pulumi-resource-${PACK}
VERSION         := $(shell pulumictl get version)
JAVA_GROUP_ID   := com.ovhcloud.pulumi.ovh
JAVA_ARTIFACT_ID := pulumi-ovh

PLATFORM := linux-amd64

TESTPARALLELISM := 4

WORKING_DIR     := $(shell pwd)

OS := $(shell uname)
EMPTY_TO_AVOID_SED := ""

SED := sed -i
ifeq ($(OS), Darwin)
        SED += ''
endif

ensure::
	cd provider && go mod tidy
	cd sdk && go mod tidy
	cd examples && go mod tidy

prepare::
	@if test -z "${NAME}"; then echo "NAME not set"; exit 1; fi
	@if test -z "${REPOSITORY}"; then echo "REPOSITORY not set"; exit 1; fi
	@if test ! -d "provider/cmd/pulumi-tfgen-x${EMPTY_TO_AVOID_SED}yz"; then "Project already prepared"; exit 1; fi

	mv "provider/cmd/pulumi-tfgen-x${EMPTY_TO_AVOID_SED}yz" provider/cmd/pulumi-tfgen-${NAME}
	mv "provider/cmd/pulumi-resource-x${EMPTY_TO_AVOID_SED}yz" provider/cmd/pulumi-resource-${NAME}

	if [[ "${OS}" != "Darwin" ]]; then \
		sed -i 's,github.com/pulumi/pulumi-xyz,${REPOSITORY},g' provider/go.mod; \
		find ./ ! -path './.git/*' -type f -exec sed -i 's/[x]yz/${NAME}/g' {} \; &> /dev/null; \
	fi

	# In MacOS the -i parameter needs an empty string to execute in place.
	if [[ "${OS}" == "Darwin" ]]; then \
		sed -i '' 's,github.com/pulumi/pulumi-xyz,${REPOSITORY},g' provider/go.mod; \
		find ./ ! -path './.git/*' -type f -exec sed -i '' 's/[x]yz/${NAME}/g' {} \; &> /dev/null; \
	fi

.PHONY: development provider build_sdks build_nodejs build_dotnet build_go build_python cleanup

development:: install_plugins provider lint_provider build_sdks install_sdks cleanup # Build the provider & SDKs for a development environment

# Required for the codegen action that runs in pulumi/pulumi and pulumi/pulumi-terraform-bridge
build:: install_plugins provider build_sdks install_sdks
only_build:: build

tfgen:: install_plugins
	(cd provider && go build -o $(WORKING_DIR)/bin/${TFGEN} -ldflags "-X ${PROJECT}/${VERSION_PATH}=${VERSION}" ${PROJECT}/${PROVIDER_PATH}/cmd/${TFGEN})
	$(WORKING_DIR)/bin/${TFGEN} schema --out provider/cmd/${PROVIDER}
	(cd provider && VERSION=$(VERSION) go generate cmd/${PROVIDER}/main.go)

provider:: tfgen install_plugins # build the provider binary
	(cd provider && go build -o $(WORKING_DIR)/bin/${PROVIDER} -ldflags "-X ${PROJECT}/${VERSION_PATH}=${VERSION}" ${PROJECT}/${PROVIDER_PATH}/cmd/${PROVIDER})

build_sdks:: install_plugins provider build_nodejs build_python build_go build_dotnet build_java # build all the sdks

build_nodejs:: VERSION := $(shell pulumictl get version --language javascript)
build_nodejs:: install_plugins tfgen # build the node sdk
	$(WORKING_DIR)/bin/$(TFGEN) nodejs --overlays provider/overlays/nodejs --out sdk/nodejs/
	cd sdk/nodejs/ && \
		printf "module fake_nodejs_module // Exclude this directory from Go tools\n\ngo 1.17\n" > go.mod && \
		yarn install && \
		yarn run tsc && \
		cp ../../README.md ../../LICENSE package.json yarn.lock ./bin/ && \
		sed -i.bak -e "s/\$${VERSION}/$(VERSION)/g" ./bin/package.json

build_python:: PYPI_VERSION := $(shell pulumictl get version --language python)
build_python:: .make/generate_python # build the python sdk
.make/generate_python: install_plugins tfgen
	$(GEN_ENVS) $(WORKING_DIR)/bin/$(TFGEN) python --out sdk/python/
	printf "module fake_python_module // Exclude this directory from Go tools\n\ngo 1.17\n" > sdk/python/go.mod
	cp README.md sdk/python/
.make/build_python: .make/generate_python	cd sdk/python/ && \
		rm -rf ./bin/ ../python.bin/ && cp -R . ../python.bin && mv ../python.bin ./bin && \
		rm ./bin/go.mod && \
		python3 -m venv venv && \
		./venv/bin/python -m pip install build==1.2.1 && \
		cd ./bin && \
		../venv/bin/python -m build .

build_dotnet:: DOTNET_VERSION := $(shell pulumictl get version --language dotnet)
build_dotnet:: install_plugins tfgen # build the dotnet sdk
	pulumictl get version --language dotnet
	$(WORKING_DIR)/bin/$(TFGEN) dotnet --overlays provider/overlays/dotnet --out sdk/dotnet/
	cd sdk/dotnet/ && \
		echo "${DOTNET_VERSION}" >version.txt && \
        dotnet build /p:Version=${DOTNET_VERSION}

build_go:: install_plugins tfgen # build the go sdk
	$(WORKING_DIR)/bin/$(TFGEN) go --overlays provider/overlays/go --out sdk/go/

build_java:: PACKAGE_VERSION := $(shell pulumictl get version --language generic)
build_java:: bin/pulumi-java-gen
	$(WORKING_DIR)/bin/$(JAVA_GEN) generate --schema provider/cmd/$(PROVIDER)/schema.json --out sdk/java  --build gradle-nexus

	echo "update java version in build.gradle" && cd ./sdk/java/ && ${SED} -e 's/of(11)/of(21)/g' build.gradle
	echo "update inceptionYear in build.gradle" && cd ./sdk/java/ && ${SED} -e 's/inceptionYear = .*/inceptionYear = "2024"/g' build.gradle

	echo "update meta info in build.gradle" && cd ./sdk/java/ && ${SED} -e 's/info.metaClass.name = .*/info.metaClass.name = "$(JAVA_ARTIFACT_ID)"/g' build.gradle && \
	${SED} -e 's/group = .*/group = "$(JAVA_GROUP_ID)"/g' build.gradle && \
	${SED} -e 's/groupId = .*/groupId = "$(JAVA_GROUP_ID)"/g' build.gradle && \
	${SED} -e 's/artifactId = .*/artifactId = "$(JAVA_ARTIFACT_ID)"/g' build.gradle && \
	${SED} -e 's/description = .*/description = "A Pulumi package for creating and managing OVH resources."/g' build.gradle

	echo "update rootProject in settings.gradle" && cd ./sdk/java && ${SED} -e 's/rootProject.name = .*/rootProject.name = "$(JAVA_GROUP_ID)"/g' settings.gradle

	cd sdk/java/ && \
		echo "module fake_java_module // Exclude this directory from Go tools\n\ngo 1.17" > go.mod && \
		gradle --console=plain build

bin/pulumi-java-gen::
	@mkdir -p bin
	wget https://github.com/pulumi/pulumi-java/releases/download/${JAVA_GEN_VERSION}/pulumi-language-java-${JAVA_GEN_VERSION}-${PLATFORM}.tar.gz -O /tmp/pulumi-language-java-${JAVA_GEN_VERSION}-${PLATFORM}.tar.gz
	tar -xf /tmp/pulumi-language-java-${JAVA_GEN_VERSION}-${PLATFORM}.tar.gz -C /tmp
	mv /tmp/pulumi-java-gen bin

lint_provider:: provider # lint the provider code
	cd provider && golangci-lint run -c ../.golangci.yml

cleanup:: # cleans up the temporary directory
	rm -r $(WORKING_DIR)/bin
	rm -f provider/cmd/${PROVIDER}/schema.go

help::
	@grep '^[^.#]\+:\s\+.*#' Makefile | \
 	sed "s/\(.\+\):\s*\(.*\) #\s*\(.*\)/`printf "\033[93m"`\1`printf "\033[0m"`	\3 [\2]/" | \
 	expand -t20

clean::
	rm -rf sdk/{dotnet,nodejs,go,python,java}

install_plugins::
	[ -x $(shell which pulumi) ] || curl -fsSL https://get.pulumi.com | sh
	pulumi plugin install resource random 4.8.2

install_dotnet_sdk::
	mkdir -p $(WORKING_DIR)/nuget
	find . -name '*.nupkg' -print -exec cp -p {} ${WORKING_DIR}/nuget \;

install_python_sdk::

install_go_sdk::

install_java_sdk::

install_nodejs_sdk::
	yarn link --cwd $(WORKING_DIR)/sdk/nodejs/bin

install_sdks:: install_dotnet_sdk install_python_sdk install_nodejs_sdk

test::
	cd examples && go test -v -tags=all -parallel ${TESTPARALLELISM} -timeout 2h
