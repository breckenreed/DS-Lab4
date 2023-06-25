# DS LAB-4 


### Завдання
### 1.Запустити три екземпляра logging-service (локально їх можна запустити на різних портах), відповідно мають запуститись також три екземпляра Hazelcast

У папці ``logging_service``

```
docker network create hazelcast-network-1

docker build -t logging-service .

docker run -d -p 8011:8001 -e "PYTHONUNBUFFERED=1" --name logging-service1 --network hazelcast-network-1 logging-service 

docker run -d -p 8012:8011 -e "PYTHONUNBUFFERED=1" --name logging-service2 --network hazelcast-network-1 logging-service

docker run -d -p 8013:8011 -e "PYTHONUNBUFFERED=1" --name logging-service3 --network hazelcast-network-1 logging-service
```
якщо контейнери кластеру Hazelcast та Hazelcast MC наразі не запущені, то потрібно запуситити і їх: <br />

```
docker run \
    -d \
    --name firstmember \
    --network hazelcast-network-1 \
    -e HZ_CLUSTERNAME=dev \
    -p 5701:5701 hazelcast/hazelcast:latest-snapshot 

second
docker run \
    -d \
    --name secondmember --network hazelcast-network-1 \
    -e HZ_CLUSTERNAME=dev \
    -p 5702:5701 hazelcast/hazelcast:latest-snapshot

third
docker run \
    -d \
    --name thirdmember --network hazelcast-network-1 \
    -e HZ_CLUSTERNAME=dev \
    -p 5703:5701 hazelcast/hazelcast:latest-snapshot

docker run \
    -d \
    --network hazelcast-network-1 \
    -p 8080:8080 hazelcast/management-center:latest-snapshot
```





### 2.Запустити два екземпляри messages-service (локально їх можна запустити на різних портах  <br />


```
docker run -it  --network hazelcast-network-1 --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management <br />

docker run -d -p 8021:8021 -e "PYTHONUNBUFFERED=1" --name message-service1 --network hazelcast-network-1 message-service <br />

docker run -d -p 8022:8021 -e "PYTHONUNBUFFERED=1" --name message-service2 --network hazelcast-network-1 message-service <br />


```

<img width="1173" alt="image" src="https://github.com/breckenreed/DS-Lab4/assets/62158298/f9a4451b-2d41-4619-b266-a44b66d02b04">  <br />





### 3.Через HTTP POST записати 10 повідомлень msg1-msg10 через facade-service  <br />

Почергово змінюємо контент json-файлу для кожного запиту:  <br />

<img width="790" alt="image" src="https://github.com/breckenreed/DS-Lab4/assets/62158298/af815773-495a-4f72-86e8-0ba885de0424">


Логи facade-service: <br />
<img width="425" alt="image" src="https://github.com/breckenreed/DS-Lab4/assets/62158298/9e9ac169-b137-4fbe-944f-9d538778356e">


### 4.Показати які повідомлення отримав кожен з екземплярів logging-service (це має бути видно у логах сервісу)  <br />

1: <br />
<img width="1165" alt="image" src="https://github.com/breckenreed/DS-Lab4/assets/62158298/640ec440-e960-44d9-bf9f-1b0f04188d60">

2: <br />
<img width="1173" alt="image" src="https://github.com/breckenreed/DS-Lab4/assets/62158298/844ac3e6-c49e-4c90-b906-3033a5d2e750">

3: <br />
<img width="1150" alt="image" src="https://github.com/breckenreed/DS-Lab4/assets/62158298/be353de6-a8fe-4261-954f-ba9bd431fdcc">


MAP:  <br />
<img width="1244" alt="image" src="https://github.com/breckenreed/DS-Lab4/assets/62158298/135cbe1b-35c9-4991-97a7-04f8cf6c2c61">


### 5.Показати які повідомлення отримав кожен з екземплярів messages-service (це має бути видно у логах сервісу)  <br />
1: <br />
<img width="813" alt="image" src="https://github.com/breckenreed/DS-Lab4/assets/62158298/37867e1a-4883-4ee7-adf0-5161f670a5c2">

2: <br />
<img width="589" alt="image" src="https://github.com/breckenreed/DS-Lab4/assets/62158298/5db06713-80a7-4c84-9cd1-e6255635eaf1">


RABBITMQ:  <br />
<img width="636" alt="image" src="https://github.com/breckenreed/DS-Lab4/assets/62158298/6421d143-403d-4938-acbb-4b842837a3ca">




### 6.Декілька разів викликати HTTP GET на facade-service та отримати об'єднані дві множини повідомлень - це мають бути повідомлення з logging-service та messages-service:  <br />
<img width="798" alt="image" src="https://github.com/breckenreed/DS-Lab4/assets/62158298/c3a2f809-0a21-4163-bfed-4e976e66f081">

facade-service: <br />
<img width="1134" alt="image" src="https://github.com/breckenreed/DS-Lab4/assets/62158298/ebc11618-200f-4ffb-be77-2bebb280b239">


