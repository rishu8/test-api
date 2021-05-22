# NOTE: this only works in Docker 1.17.05 and above
# arg IMAGE=dsicrate:0.6
# from $IMAGE
ARG BASE_IMAGE
FROM ${BASE_IMAGE}

# Import APP_NAME and make sure it's exported to the run stage
ARG APP_NAME
arg DS_APP_SUITE
arg DS_APP_ENV
arg DS_APP_ENV_CONTEXT
arg DS_BUILD_NUMBER
arg DS_COMMIT_HASH
arg DS_TAG

env DS_APP_NAME=$DS_APP_NAME
env DS_APP_ROOT=/$DS_APP_NAME

env DS_APP_SUITE=${DS_APP_SUITE}
env DS_APP_ENV=${DS_APP_ENV}
env DS_APP_ENV_CONTEXT=${DS_APP_ENV_CONTEXT}
env DS_BUILD_NUMBER=${DS_BUILD_NUMBER}
env DS_COMMIT_HASH=${DS_COMMIT_HASH}
env DS_TAG=${DS_TAG}

workdir $DS_APP_ROOT
copy build/app.tar .
run tar -xvf app.tar
run ./setup.sh

# Make sure python can resolve all modules
env PYTHONPATH=$DS_APP_ROOT/imports:$DS_APP_ROOT/apps:$DS_APP_ROOT/libs
ENV PATH=$DS_APP_ROOT/.venv/bin:$PATH
ENV PROJ_ROOT=$DS_APP_ROOT

entrypoint ["bash", "run.sh"]