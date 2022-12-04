# coding: utf-8
from sqlalchemy import Column, BigInteger, String, DateTime, text, Text, Sequence
from sqlalchemy.dialects.postgresql import JSONB

from src.database.base import BaseModel


class LoggedAction(BaseModel):
    __tablename__ = 'logged_action'
    __table_args__ = {'schema': 'audit'}

    event_id_seq = Sequence('logged_actions_event_id_seq')

    event_id = Column(BigInteger, event_id_seq, server_default=event_id_seq.next_value(), primary_key=True)
    schema_name = Column(String(36), nullable=False)
    table_name = Column(String(36), nullable=False)
    relative_id = Column(String(255))
    editor = Column(String(255))
    action_tstamp = Column(DateTime(True), default=text("CURRENT_TIMESTAMP"))
    action = Column(String(1), nullable=False)
    row_before = Column(JSONB(astext_type=Text()))
    changes = Column(JSONB(astext_type=Text()))
