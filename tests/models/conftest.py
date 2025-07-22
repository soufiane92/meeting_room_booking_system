from datetime import datetime

import pytest

from src.models.booking import Booking
from src.models.room import Room
from src.models.user import User


@pytest.fixture
def sample_room() -> Room:
    return Room(name="Conference Room", capacity=50, equipment=["projector", "microphone"])

@pytest.fixture
def sample_user() -> User:
    return User(name="John Doe", email="john.doe@example.com")

@pytest.fixture
def sample_booking(sample_room: Room, sample_user: User) -> Booking:
    return Booking(
        room=sample_room,
        user=sample_user,
        date=datetime(2025, 7, 25),
        start_time=datetime(2025, 7, 25, 10, 0),
        end_time=datetime(2025, 7, 25, 11, 0),
    )



