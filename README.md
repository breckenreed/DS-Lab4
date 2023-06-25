<img width="807" alt="image" src="https://github.com/breckenreed/DS-Lab4/assets/62158298/67a42581-7a88-47c2-9d27-bdd11a38c55e"># DS-Lab4




### Завдання
### 1.Запустити три екземпляра logging-service (локально їх можна запустити на різних портах), відповідно мають запуститись також три екземпляра Hazelcast

У папці ``logging_service``

```
docker network create hazelcast-network-1

docker build -t logging-service .

docker run -d -p 8011:8001 -e "PYTHONUNBUFFERED=1" --name logging-service1 --network hazelcast-network-1 logging-service <br />

docker run -d -p 8012:8001 -e "PYTHONUNBUFFERED=1" --name logging-serviceNEW2 --network hazelcast-network-1 logging-service_alt <br />

docker run -d -p 8013:8001 -e "PYTHONUNBUFFERED=1" --name logging-serviceNEW3 --network hazelcast-network-1 logging-service_alt <br />
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





### 3.Через HTTP POST записати 10 повідомлень msg1-msg10 через facade-service


<img width="800" alt="image" src="https://github.com/breckenreed/DS-Lab4/assets/62158298/413f3dd6-5706-4565-b71b-757e3b68e460">

<img width="432" alt="image" src="https://github.com/breckenreed/DS-Lab4/assets/62158298/449a9a1d-10cf-4a31-b742-69f03f8d201b">

### 4.Показати які повідомлення отримав кожен з екземплярів logging-service (це має бути видно у логах сервісу)

### 5.Показати які повідомлення отримав кожен з екземплярів messages-service (це має бути видно у логах сервісу)
### 6.Декілька разів викликати HTTP GET на facade-service та отримати об'єднані дві множини повідомлень - це мають бути повідомлення з logging-service та messages-service
