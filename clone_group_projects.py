import os
import requests

# Получение переменных окружения
GITLAB_API_URL = os.environ.get("GITLAB_API_URL", "https://gitlab.com/api/v4/")
PRIVATE_TOKEN = os.environ.get("PRIVATE_TOKEN")  # Токен должен быть задан, иначе скрипт не сможет авторизоваться
GROUP_ID = os.environ.get("GROUP_ID")  # ID группы должен быть задан
CLONE_DIR = os.environ.get("CLONE_DIR", "/data")

if not PRIVATE_TOKEN or not GROUP_ID:
    raise ValueError("Необходимо задать PRIVATE_TOKEN и GROUP_ID через переменные окружения")

headers = {
    "Private-Token": PRIVATE_TOKEN
}

def clone_repository(repo_http_url, clone_path):
    modified_url = repo_http_url.replace("https://", f"https://oauth2:{PRIVATE_TOKEN}@")
    os.system(f"git clone {modified_url} {clone_path}")

def get_projects_in_group(group_id):
    projects = []
    url = f"{GITLAB_API_URL}groups/{group_id}/projects"
    while url:
        response = requests.get(url, headers=headers)
        projects.extend(response.json())
        url = response.links.get('next', {}).get('url', None)
    return projects

def get_subgroups(group_id):
    subgroups = []
    url = f"{GITLAB_API_URL}groups/{group_id}/subgroups"
    while url:
        response = requests.get(url, headers=headers)
        subgroups.extend(response.json())
        url = response.links.get('next', {}).get('url', None)
    return subgroups

def clone_group_projects(group_id, parent_dir="", accumulated_path=""):
    projects = get_projects_in_group(group_id)
    for project in projects:
        project_path = project['path_with_namespace']
        if accumulated_path:
            project_path = project_path.replace(accumulated_path + '/', '')
        path = os.path.join(parent_dir, project_path)
        os.makedirs(path, exist_ok=True)
        clone_repository(project['http_url_to_repo'], path)

    subgroups = get_subgroups(group_id)
    for subgroup in subgroups:
        subgroup_path = subgroup['full_path']
        if accumulated_path:
            subgroup_path = subgroup_path.replace(accumulated_path + '/', '')
        new_accumulated_path = os.path.join(accumulated_path, subgroup_path) if accumulated_path else subgroup_path
        subgroup_dir = os.path.join(parent_dir, subgroup_path)
        os.makedirs(subgroup_dir, exist_ok=True)
        clone_group_projects(subgroup['id'], subgroup_dir, new_accumulated_path)

if __name__ == "__main__":
    clone_group_projects(GROUP_ID, CLONE_DIR)