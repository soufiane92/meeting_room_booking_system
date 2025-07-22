from src.models.person import Person


def test_person_properties(sample_user: Person):
    assert sample_user.name == "John Doe"
    assert sample_user.email == "john.doe@example.com"
    assert sample_user.get_role() == "user"
