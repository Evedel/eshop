ARG PYTHON_IMAGE=python:3.11-alpine3.16


FROM flant/shell-operator:v1.0.12 as shell-operator


FROM ${PYTHON_IMAGE} as dev

COPY --from=shell-operator /shell-operator /shell-operator
COPY --from=shell-operator /frameworks /
COPY --from=shell-operator /shell_lib.sh /
ENV SHELL_OPERATOR_HOOKS_DIR /app/hooks/bin
ENV LOG_TYPE json
ENV LOG_NO_TIME true
ENV SHELL_OPERATOR_LISTEN_PORT 8080
ENV PYTHONPATH /app:$PYTHONPATH
ENV SHELL_OPERATOR_HOOKS_DIR /app/hooks/bin

ENV PYTHONPATH /workspace/app:$PYTHONPATH
RUN apk add --no-cache -U bash jq git openssh curl
WORKDIR /workspace
RUN python -m pip install --upgrade pip && \
  pip install coverage black
COPY . /workspace


FROM ${PYTHON_IMAGE} as prod

COPY --from=shell-operator /shell-operator /shell-operator
COPY --from=shell-operator /frameworks /
COPY --from=shell-operator /shell_lib.sh /
ENV SHELL_OPERATOR_HOOKS_DIR /app/hooks/bin
ENV LOG_TYPE json
ENV LOG_NO_TIME true
ENV SHELL_OPERATOR_LISTEN_PORT 8080
ENV PYTHONPATH /app:$PYTHONPATH
ENV SHELL_OPERATOR_HOOKS_DIR /app/hooks/bin

RUN apk add --no-cache -U jq bash
COPY --from=shell-operator /shell-operator /shell-operator
COPY --from=shell-operator /frameworks /
COPY --from=shell-operator /shell_lib.sh /

COPY app /app

WORKDIR /
ENTRYPOINT ["/shell-operator", "start"]