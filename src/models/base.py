from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column


class Base(DeclarativeBase):
    __abstarct__ = True

    

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"