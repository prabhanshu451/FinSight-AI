from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

def push_task_update(user_group='task_updates', data=None):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        user_group,
        {
            'type': 'task.update',
            'data': data or {'message':'demo update'}
        }
    )
