from celery import shared_task
import time, logging
from .utils import push_task_update

logger = logging.getLogger(__name__)

@shared_task(bind=True)
def retrain_user_forecast(self, user_id):
    logger.info(f'Retraining forecast for user {user_id}')
    # simulate progress updates via channels
    push_task_update(user_group='task_updates', data={'user_id': user_id, 'status': 'started', 'task_id': self.request.id})
    time.sleep(2)
    push_task_update(user_group='task_updates', data={'user_id': user_id, 'status': 'completed', 'task_id': self.request.id})
    return {'status':'ok','user_id':user_id}
