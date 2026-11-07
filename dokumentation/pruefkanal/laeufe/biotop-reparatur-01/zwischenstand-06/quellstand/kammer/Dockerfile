FROM python:3.12-slim
RUN pip install --no-cache-dir pytest==8.3.3 bandit==1.7.10 vulture==2.13 && useradd -m -u 10001 kammer
WORKDIR /werk
USER kammer
