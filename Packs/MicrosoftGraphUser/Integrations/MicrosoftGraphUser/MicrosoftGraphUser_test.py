
users_list_mock = [
    {
        'id': '08779ba7-f3ed-4344-b9d7-98b9911ea8a8',
        'displayName': 'Test User',
        'jobTitle': "Magician",
        'mobilePhone': None,
        'mail': None
    },
    {
        'id': '670edadc-0197-45b0-90e6-ee061e25ab73',
        'displayName': 'Test1',
        'jobTitle': 'TESTER',
        'mobilePhone': '050505050',
        'mail': None,
        "@removed": {
            "reason": "changed"
        }
    }
]

expected_outputs = [
    {
        'ID': '08779ba7-f3ed-4344-b9d7-98b9911ea8a8',
        'DisplayName': 'Test User',
        'JobTitle': "Magician",
        'MobilePhone': None,
        'Mail': None
    },
    {
        'ID': '670edadc-0197-45b0-90e6-ee061e25ab73',
        'DisplayName': 'Test1',
        'JobTitle': 'TESTER',
        'MobilePhone': '050505050',
        'Mail': None,
        'Status': 'deleted'
    }
]


def test_camel_case_to_readable():
    from MicrosoftGraphUser import camel_case_to_readable
    assert camel_case_to_readable('id') == 'ID'
    assert camel_case_to_readable('createdDateTime') == 'Created Date Time'


def test_parse_outputs():
    from MicrosoftGraphUser import parse_outputs
    _, parsed_outputs = parse_outputs(users_list_mock)
    assert parsed_outputs == expected_outputs
