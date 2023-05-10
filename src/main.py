import asyncio
from img_recv import start_record_eo, start_record_ir
from vdr_recv import start_record_vdr

async def main():
  task1 = asyncio.create_task(start_record_eo())
  task2 = asyncio.create_task(start_record_ir())
  task3 = asyncio.create_task(start_record_vdr())
  await asyncio.gather(task1, task2, task3)

loop = asyncio.get_event_loop()

try:
  asyncio.run(main())
except:
  loop.stop()
  loop.close()
