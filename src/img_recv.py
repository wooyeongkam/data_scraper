from redis import Redis
import io
from PIL import Image
import datetime

redis = Redis(host="192.168.0.200", port=30379, db =0)
channels = ["nas:image:eo", "nas:image:ir"]
pubsub_eo = redis.pubsub()
pubsub_ir = redis.pubsub()
pubsub_eo.subscribe("nas:image:eo", timeout=1)
pubsub_ir.subscribe("nas:image:ir", timeout=1)

while True:
  for message in pubsub_eo.listen():
    if message and "data" in message:
      if type(message["data"]) == int: 
        continue
      image = Image.open(io.BytesIO(message["data"]))
      now = datetime.datetime.utcnow()
      now_str = now.strftime("%Y-%m-%d,%H:%M:%S")
      image.save(f"./img/{now_str}.jpg")

