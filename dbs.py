from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, SmallInteger, Integer
from random import randrange
from datetime import timedelta


Base = declarative_base()


class Race(Base):
    __tablename__ = 'race'

    id = Column(Integer, primary_key=True)
    rname = Column(String)
    rstart = Column(DateTime)
    rvenue = Column(String)
    rtype = Column(String)
    rnumber = Column(SmallInteger)

    def __repr__(self):
        time_str = self.rstart.strftime("%d-%m-%Y:%H:%M")
        return "<race(name='%s', venue='%s', type='%s', number=%d, start=%)>" % (
            self.rname, self.rvenue, self.rtype, self.rnumber, time_str)

# generate examples if run indidivually (not imported)
if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from datetime import datetime
    from random import randint

    engine = create_engine('sqlite:///foo.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates
    def random_date(start, end):
        """
        This function will return a random datetime between two datetime
        objects.
        """
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)
    start = datetime.strptime('1/1/2020 0:00 AM', '%m/%d/%Y %I:%M %p')
    end = datetime.strptime('1/1/2021 11:59 AM', '%m/%d/%Y %I:%M %p')

    bobby = Race(rname="bobby", rstart=random_date(start, end), rvenue="melbourne", rtype="I dont know what this field means but ok",
                 rnumber=randint(0, 50))
    timmy = Race(rname="timmy", rstart=random_date(start, end), rvenue="sydney", rtype="So I decided to put some random text",
                 rnumber=randint(0, 50))
    jakie = Race(rname="jakie", rstart=random_date(start, end), rvenue="whateverstadium", rtype="Hope you like this",
                 rnumber=randint(0, 50))

    session.add(bobby)
    session.add(timmy)
    session.add(jakie)

    session.commit()
