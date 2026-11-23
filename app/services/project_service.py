from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.project import Project
from app.models.user import User
from app.schemas.project import ProjectCreate

def create_project(db: Session, owner: User, data: ProjectCreate) -> Project:
    project = Project(title=data.title, owner_id=owner.id)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

def get_project_or_404(db: Session, project_id: int, user: User) -> Project:
    project = db.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    if project.owner_id != user.id and user.role.value != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    return project

def list_projects(db: Session, user: User):
    return db.query(Project).filter(Project.owner_id == user.id).all()
