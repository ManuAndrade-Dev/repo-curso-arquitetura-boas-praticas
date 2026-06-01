from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.group import GroupCreate, GroupRead
from app.services import group_service

router = APIRouter(prefix="/groups", tags=["groups"])


@router.get("/", response_model=list[GroupRead])
def list_groups(db: Session = Depends(get_db)):
    return group_service.list_groups(db)


@router.post("/", response_model=GroupRead, status_code=status.HTTP_201_CREATED)
def create_group(group_in: GroupCreate, db: Session = Depends(get_db)):
    return group_service.create_group(db, group_in)


@router.get("/{group_id}", response_model=GroupRead)
def get_group(group_id: int, db: Session = Depends(get_db)):
    group = group_service.get_group(db, group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return group
