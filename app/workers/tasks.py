import logging
from app.workers.celery_app import celery_app

logger = logging.getLogger(__name__)

@celery_app.task(name="tasks.send_task_created_notification")
def send_task_created_notification(task_title: str, project_title: str, owner_email: str):
    logger.info("New task '%s' created in project '%s'; notification queued for %s", task_title, project_title, owner_email)
    return {"status": "sent", "email": owner_email}
