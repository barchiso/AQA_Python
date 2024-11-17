"""Tests for homework #10 log event login function."""

import pytest

from homework_10 import log_event

test_data = [
    ('user1', 'success', 'INFO'),
    ('user2', 'expired', 'WARNING'),
    ('user3', 'failed', 'ERROR'),
    ('user4', None, 'ERROR'),  # Invalid case.
    (None, 'failed', 'ERROR'),  # Invalid case.
    (None, None, 'ERROR'),  # Invalid case.
    ('', '', 'ERROR'),  # Invalid case.
]


@pytest.mark.parametrize('user, status, expected_log_level', test_data)
def test_log_event_statuses(caplog, user, status, expected_log_level):
    """Test logging for different login event statuses.

    Args:
        caplog (LogCaptureFixture): Captured logs pytest fixture.
        user (string): Logged user's username.
        status (string): Logged user's status.
        expected_log_level (string): Logged event level.
    """
    with caplog.at_level(expected_log_level):
        log_event(user, status)

    expected_message = f'Login event - Username: {user}, Status: {status}'

    # Verify the correct message is logged
    assert expected_message in caplog.text, 'Wrong message.'
    # Verify the log level is correct
    assert caplog.records[0].levelname == expected_log_level, 'Wrong log level'


# Test case for log event message output.
@pytest.mark.parametrize('user, status, expected_log_level', test_data)
def test_log_event_message_format(caplog, user, status, expected_log_level):
    """Test logging message output.

    Args:
        caplog (LogCaptureFixture): Captured logs pytest fixture.
        user (string): Logged user's username.
        status (string): Logged user's status.
        expected_log_level (string): Logged event level.
    """
    with caplog.at_level(expected_log_level):
        log_event(user, status)

    # Verify that event log level is correct.
    assert expected_log_level in caplog.text, 'Wrong event log level.'
    # Verify for the separator between timestamp and message.
    assert ' - L' in caplog.text, 'Separator is missed or message was changed.'
    # Verify the timestamp is present and starts with a year.
    assert caplog.text.startswith('2024-'), 'Timestamp is missed.'
