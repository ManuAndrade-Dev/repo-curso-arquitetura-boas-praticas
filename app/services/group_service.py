from sqlalchemy.orm import Session

from app.models.group import Group
from app.schemas.group import GroupCreate


def list_groups(db: Session, skip: int = 0, limit: int = 100) -> list[Group]:
    return db.query(Group).offset(skip).limit(limit).all()


def create_group(db: Session, group_in: GroupCreate) -> Group:
    group = Group(
        name=group_in.name,
        description=group_in.description,
    )
    db.add(group)
    db.commit()
    db.refresh(group)
    return group


def get_group(db: Session, group_id: int) -> Group | None:
    return db.query(Group).filter(Group.id == group_id).first()
