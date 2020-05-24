"""User Controller Test"""

import pytest
import json


# @pytest.mark.marked
def test_user_index(client):
    """Test api/v1/users"""
    response = client.get('/api/v1/users')
    # data = json.loads(response.data.decode())
    data = response.data.decode()
    assert data == "Welcome to my API"
