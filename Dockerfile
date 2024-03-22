# Определение базового образа
FROM python:3.9-slim

# Установка git
RUN apt-get update && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

# Установка requests для Python
RUN pip install requests

# Копирование скрипта в образ
COPY clone_group_projects.py /clone_group_projects.py

# Установка переменных окружения
ENV GITLAB_API_URL="https://gitlab.com/api/v4/"
# PRIVATE_TOKEN и GROUP_ID должны быть переданы при запуске контейнера

# Запуск скрипта с использованием Python
ENTRYPOINT ["python", "/clone_group_projects.py"]