FROM debian:12-slim AS builder
RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes pipx
ENV PATH="/root/.local/bin:${PATH}"
RUN pipx install poetry
RUN pipx inject poetry poetry-plugin-bundle
COPY . .
RUN poetry bundle venv --python=/usr/bin/python3 --only=main /venv

FROM gcr.io/distroless/python3-debian12
COPY --from=builder /venv /venv
COPY ./opamp_server_py ./src
EXPOSE 80
RUN "source /venv/bin/activate"
ENTRYPOINT ["fastapi", "run", "src/main.py", "--port", "80"]