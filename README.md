
# Сборка образа

Чтобы собрать Docker образ, вам необходимо выполнить следующую команду в терминале. Убедитесь, что вы находитесь в каталоге с Dockerfile.

```
docker build -t имя_образа .
```
Замените имя_образа на желаемое имя для вашего Docker образа.

# Использование образа

Для запуска контейнера из собранного образа используйте следующую команду:

```
docker run -e PRIVATE_TOKEN="ваш_личный_токен_доступа" -e GROUP_ID="идентификатор_корневой_группы" -v путь_на_хосте:/data имя_образа
```
 - Замените ваш_личный_токен_доступа на ваш личный токен доступа к GitLab.
   
- Замените идентификатор_корневой_группы на идентификатор вашей корневой группы в GitLab.
- Замените путь_на_хосте на путь к директории на вашем хосте, где вы хотите сохранить склонированные репозитории.
- Замените имя_образа на имя вашего Docker образа.
- 

# Building the Image

To build a Docker image, you need to execute the following command in the terminal. Make sure you are in the directory containing the Dockerfile.

```
docker build -t image_name .

```
Replace image_name with the desired name for your Docker image.

# Using the Image

To run a container from the built image, use the following command:

```
docker run -e PRIVATE_TOKEN="your_private_access_token" -e GROUP_ID="root_group_identifier" -v host_path:/data image_name
```
- Replace your_private_access_token with your private access token for GitLab.

- Replace root_group_identifier with the identifier of your root group in GitLab.

- Replace host_path with the path to a directory on your host where you want to save the cloned repositories.

Replace image_name with the name of your Docker image.
