FROM python:3.13.5
WORKDIR /app

RUN useradd -u 1000 -m app

RUN mkdir -p var/states && \
    chown -R app:app var/states

# Install deps
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy source code
COPY --chown=app:app . .

USER app

RUN touch /app/var/states/state.json

CMD ["fastapi", "run", "run.py"]