from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.dependencies import get_current_user
from app.services.project_service import create_project, get_project_or_404, list_projects
from app.schemas.project import ProjectCreate, ProjectRead
from app.models.user import User

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.post("", response_model=ProjectRead, status_code=201)
def create(data: ProjectCreate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return create_project(db, user, data)

@router.get("", response_model=list[ProjectRead])
def read_all(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return list_projects(db, user)

@router.get("/{project_id}", response_model=ProjectRead)
def read_one(project_id: int, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_project_or_404(db, project_id, user)
