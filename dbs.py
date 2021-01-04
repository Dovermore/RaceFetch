from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, SmallInteger
import enum


Base = declarative_base()


class Race(Base):
    __tablename__ = 'race'

    id = Column(Integer, primary_key=True)
    rname = Column(String)
    rstart = Column(DateTime)
    rvenue = Column(Enum)
    rtype = Column(String)
    rnumber = Column(SmallInteger)

    def __repr__(self):
        time_str = self.rstart.strftime("%d-%m-%Y:%H:%M")
        return "<race(name='%s', venue='%s', type='%s', number=%d, start=%)>" % (
            self.rname, self.rvenue, self.rtype, self.rnumber, time_str)

