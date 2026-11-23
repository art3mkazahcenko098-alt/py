from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.dependencies import get_current_user
from app.services.project_service import get_project_or_404
from app.services.task_service import create_task, get_task_or_404, update_task
from app.schemas.task import TaskCreate, TaskUpdate, TaskRead
from app.models.user import User

router = APIRouter(prefix="/projects/{project_id}/tasks", tags=["Tasks"])

@router.post("", response_model=TaskRead, status_code=201)
def create(project_id: int, data: TaskCreate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    project = get_project_or_404(db, project_id, user)
    return create_task(db, project, data)

@router.get("/{task_id}", response_model=TaskRead)
def read_one(project_id: int, task_id: int, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    project = get_project_or_404(db, project_id, user)
    return get_task_or_404(db, task_id, project)

@router.patch("/{task_id}", response_model=TaskRead)
def update(project_id: int, task_id: int, data: TaskUpdate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    project = get_project_or_404(db, project_id, user)
    task = get_task_or_404(db, task_id, project)
    return update_task(db, task, data)
