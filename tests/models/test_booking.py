from datetime import datetime
from typing import Any

import pytest

from src.models.booking import Booking
from src.models.room import Room
from src.models.user import User


def test_booking_properties(
        sample_booking: Booking,
        sample_room: Room,
        sample_user: User,
):
    assert sample_booking.room == sample_room
    assert sample_booking.user == sample_user
    assert sample_booking.date == datetime(2025, 7, 25)
    assert sample_booking.start_time == datetime(2025, 7, 25, 10, 0)
    assert sample_booking.end_time == datetime(2025, 7, 25, 11, 0)
    assert str(sample_booking) == "Booking(room=Conference Room, user=John Doe, date=2025-07-25, from=10:00:00 to=11:00:00)"


@pytest.mark.parametrize(
    "start_time, end_time, other_room, expected_overlap, expected_error",
    [
        (datetime(2025, 7, 25, 10, 30), datetime(2025, 7, 25, 11, 30), False, True, None),
        (datetime(2025, 7, 25, 11, 0), datetime(2025, 7, 25, 12, 0), False, False, None),
        (datetime(2025, 7, 25, 12, 0), datetime(2025, 7, 25, 11, 0), False, None, ValueError),
        (datetime(2025, 7, 25, 10, 30), datetime(2025, 7, 25, 11, 30), True, False, None),
    ]
)
def test_booking_overlaps_with(
    sample_booking: Booking,
    sample_room: Room,
    sample_user: User,
    start_time: datetime,
    end_time: datetime,
    other_room: bool,
    expected_overlap: bool | None,
    expected_error: Any | None,
) -> None:
    room = Room("Other Room", 50, []) if other_room else sample_room

    if expected_error:
        with pytest.raises(expected_error):
            Booking(
                room=room,
                user=sample_user,
                date=datetime(2025, 7, 25),
                start_time=start_time,
                end_time=end_time,
            )
    else:
        booking = Booking(
            room=room,
            user=sample_user,
            date=datetime(2025, 7, 25),
            start_time=start_time,
            end_time=end_time,
        )
        assert sample_booking.overlaps_with(booking) is expected_overlap

