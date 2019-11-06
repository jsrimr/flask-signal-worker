# web으로 명령 받아서 worker 실행시키기

web서버(플라스크) 가 하는 일 : 
1. start 
2. stop 
3. modify/\<parameters\>

Worker 가 하는 일

1. Send STATUS command to get the cloa state
2. Record the returned status to DB

```python
python app.py
```
post 로 start or stop or modify/\<parameters\> 요청 보냄
 
### Docker
```shell
docker build -t cloa/flask-worker .
docker run -p 8080:8080 cloa/flask-worker
```
