from datetime import datetime

from .room import Room
from .user import User


class Booking:
    def __init__(self, room: Room, user: User, date: datetime, start_time: datetime, end_time: datetime):
        self._room = room
        self._user = user
        self._date = date
        self._start_time = start_time
        self._end_time = end_time

        self._validate_inputs()

    @property
    def room(self) -> Room:
        return self._room

    @property
    def user(self) -> User:
        return self._user

    @property
    def date(self) -> datetime:
        return self._date

    @property
    def start_time(self) -> datetime:
        return self._start_time

    @property
    def end_time(self) -> datetime:
        return self._end_time

    def overlaps_with(self, other: 'Booking') -> bool:
        """
        Check if this booking overlaps with another booking.
        Overlap occurs if:
        - The bookings are for the same room and date
        - The time intervals intersect
        """
        if self.room != other.room or self.date.date() != other.date.date():
            return False
        return self.start_time < other.end_time and other.start_time < self.end_time

    def __str__(self) -> str:
        return (
            f"Booking(room={self._room.name}, user={self._user.name}, "
            f"date={self._date.date()}, from={self._start_time.time()} to={self._end_time.time()})"
        )

    def _validate_inputs(self):
        # Optional: ensure correct types
        if not isinstance(self._date, datetime):
            raise ValueError("Date must be a datetime object.")

        if self._start_time >= self._end_time:
            raise ValueError("Start time must be before end time.")

        # Optional: ensure start_time and end_time are on same date as self._date
        if (
            self._start_time.date() != self._date.date()
            or self._end_time.date() != self._date.date()
        ):
            raise ValueError("Start and end times must be on the same date as booking date.")

