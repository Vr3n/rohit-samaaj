from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship, validates

from app.database import Base


# writing models here.

class SamaajMemberMaster(Base):
    __tablename__ = 'samaaj_members'

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    first_name = Column(
        String(256),
    )
    last_name = Column(
        String(256),
    )
    mother_name = Column(
        String(256),
    )
    father_name = Column(
        String(256),
    )

    mobile_numbers = relationship(
        'SamaajMemberMobileNumberMaster',
        back_populates="member"
    )


class SamaajMemberMobileNumberMaster(Base):
    __tablename__ = 'samaaj_member_mobilenumbers'

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    mobile_number = Column(
        String(10)
    )

    is_whatsapp = Column(
        Boolean,
    )

    member = relationship(
        'SamaajMemberMaster',
        back_populates="mobile_numbers"
    )


class SamaajMemberEmailAddressMaster(Base):
    __tablename__ = 'samaaj_member_emailaddresses'

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    email_address = Column(
        String(10)
    )

    member = relationship(
        'SamaajMemberMaster',
        back_populates="email_addresses"
    )

    @validates('email')
    def validate_email(self, key, address):
        if "@" not in address:
            raise ValueError(
                "Failed email validation."
            )
        return address
