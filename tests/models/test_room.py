from src.models.room import Room


def test_room_properties(sample_room: Room):
    assert sample_room.name == "Conference Room"
    assert sample_room.capacity == 50
    assert sample_room.equipment == ["projector", "microphone"]
    assert sample_room.has_equipment("projector") is True
    assert sample_room.has_equipment("laptop") is False
    assert str(sample_room) == "Room(name=Conference Room, capacity=50, equipement=['projector', 'microphone'])"

