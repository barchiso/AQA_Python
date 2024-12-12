"""Tests for homework #16 class inheritance."""

#  Write a test that checks for the presence of the attributes
# from Manager and Developer in the TeamLead class

import pytest

from task1 import TeamLead

test_data = [

    (TeamLead('Charlie Green', 90000, 'Engineering', 5, 'JavaScript')),
    (TeamLead('Sasha Grey', 80000, 'HR', 5)),
    (TeamLead('Benny Hill', 70000, 'Sales')),

]


@pytest.mark.parametrize('team_lead', test_data)
def test_team_lead_attributes(team_lead):
    """Verify the attributes from Manager and Developer in the TeamLead class.

    Args:
        team_lead (TeamLead): A TeamLead instance.
    """
    # Check if team lead has attributes
    # "name", "salary", "department", "team_size", "programming_language"
    for attr in team_lead.__dict__:
        assert hasattr(team_lead, attr), f'Team Lead without attribute {attr}'
