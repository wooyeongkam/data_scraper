import time
import datetime

utc_now = datetime.datetime.utcnow() # 현재 UTC 시간 구하기
unix_timestamp = int(utc_now.timestamp()) # Unix timestamp로 변환하기

print(utc_now)
print(unix_timestamp)