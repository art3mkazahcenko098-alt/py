from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.task import Task
from app.models.project import Project
from app.schemas.task import TaskCreate, TaskUpdate
from app.workers.tasks import send_task_created_notification

def create_task(db: Session, project: Project, data: TaskCreate) -> Task:
    task = Task(title=data.title, description=data.description, project_id=project.id)
    db.add(task)
    db.commit()
    db.refresh(task)
    send_task_created_notification.delay(task.title, project.title, project.owner.email)
    return task

def get_task_or_404(db: Session, task_id: int, project: Project) -> Task:
    task = db.get(Task, task_id)
    if not task or task.project_id != project.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task

def update_task(db: Session, task: Task, data: TaskUpdate) -> Task:
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(task, field, value)
    db.commit()
    db.refresh(task)
    return task
