# NOTE: this only works in Docker 1.17.05 and above
# arg IMAGE=dsicrate:0.6
# from $IMAGE
ARG BASE_IMAGE
FROM ${BASE_IMAGE}

# Import APP_NAME and make sure it's exported to the run stage
ARG APP_NAME
ARG APP_VERSION
ARG COMMIT_HASH

ENV APP_NAME=${APP_NAME}
ENV APP_ROOT=/${APP_NAME}
ENV COMMIT_HASH=${COMMIT_HASH}
ENV APP_VERSION=${APP_VERSION}

WORKDIR ${APP_ROOT}
COPY src ${APP_ROOT}
COPY cicd ${APP_ROOT}/build/
COPY requirements.txt ${APP_ROOT}/build/
COPY entrypoint.sh /entrypoint

RUN ${APP_ROOT}/build/setup.sh

# Make sure python can resolve all modules
ENV PYTHONPATH=$APP_ROOT
ENV PATH=$APP_ROOT/.venv/bin:$PATH

ENTRYPOINT ["/entrypoint"]

CMD "--version"
