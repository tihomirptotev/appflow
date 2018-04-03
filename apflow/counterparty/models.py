from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Unicode,
    UnicodeText,
    ForeignKey,
    String,
    Boolean,

)
from sqlalchemy.orm import relationship, backref, validates
from sqlalchemy.schema import CheckConstraint
from apflow.models.mixins import BaseModel


class Counterparty(BaseModel):
    # __versioned__ = {}
    __tablename__ = 'counterparties'

    name = Column(Unicode(length=50), index=True, nullable=False)
    eik_egn = Column(Unicode(13), index=True, unique=True, nullable=False)

    @validates('eik_egn')
    def validate_eik_egn(self, key, value):
        assert (len(value) >= 9) & (len(value) <= 13)
        return value



class CounterpartyNote(BaseModel):
    __tablename__ = 'counterparty_notes'
    note = Column(UnicodeText(500), index=True)
    counterparty_id = Column(Integer(), ForeignKey('counterparties.id'))
    counterparty = relationship('Counterparty',
                                backref=backref('notes'))


class CounterpartyAccount(BaseModel):
    __tablename__ = 'counterparty_iban'
    iban = Column(String(22), index=True, unique=True)
    counterparty_id = Column(Integer(), ForeignKey('counterparties.id'))
    counterparty = relationship('Counterparty',
                                backref=backref('accounts'))
