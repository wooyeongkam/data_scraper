# Getting Started

---

## Note

- 회사에서 테스트 할 때
  - EO/IR 카메라 wifi로 testpc1-out 잡아야함
  - vdr은 AvikusSimNet5G로 잡아야함
- 선상
  - 선상에서는 하나의 네트워크로 둘 다 동작할 것으로 예상
  - 동작하지 않을 경우, option으로 저장할 것 설정 가능, 아래 option 참조
- 저장 파일명
  - unix-time stamp

## Activating Virtual Environment

```
sudo apt-get install python3-venv
python3 -m venv .venv
source .venv/bin/activate
```

## Installing Depencies

```
pip install --upgrade pip
pip install -r requirements.txt
```

## Running

```
python3 src/main.py
```

## options

```
 --no-camera
 --no-vdr

 --redis-ip
 --redis-port
 --redis-db

 --vdr-ip
 --vdr-port

 ex) EO/IR 카메라 이미지 저장 X
 python3 src/main.py --no-camera

 ex) VDR 값 저장 X
 python3 src/main.py --no-vdr

 ex) redis ip 변경
 python3 src/main.py --redis-ip 192.168.0.1

```

## dotenv (option)

```
REDIS_HOST=
REDIS_PORT=
REDIS_USERNAME=
REDIS_PASSWORD=
```
