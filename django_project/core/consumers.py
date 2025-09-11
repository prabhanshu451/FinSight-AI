from channels.generic.websocket import AsyncJsonWebsocketConsumer

class TaskConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send_json({'status':'connected','message':'Welcome to TaskMonitor'})

    async def receive_json(self, content, **kwargs):
        cmd = content.get('command')
        if cmd == 'ping':
            await self.send_json({'status':'pong'})
        else:
            await self.send_json({'status':'ok','received':content})

    async def task_update(self, event):
        await self.send_json({'type':'task.update','data': event.get('data')})
