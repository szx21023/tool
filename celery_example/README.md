快速安裝 redis
```
docker run --name my-redis -d -p 6379:6379 redis
```
啟動 celery 的 work 去處理進到 queue 的排程
```
celery -A tasks worker --loglevel=info
```
啟動 celery 的 bean 去觸發定時排程的任務進到 queue
```
celery -A tasks beat --loglevel=info
```
Celery 的监控和管理
```
celery -A tasks flower
```
預設連結: http://0.0.0.0:5555

how docker execution the application
```
docker build -t celery-bean .
docker build -t celery-worker -f dockerfile_worker .

docker network create my-network

docker run --name my-redis -d -p 6379:6379 --network my-network redis
docker run --name my-bean -d --network my-network celery-bean
docker run --name my-worker -d --network my-network celery-worker
```
