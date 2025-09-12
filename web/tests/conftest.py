import pytest
from app import app, get_database_url, clear_database, setup_database

@pytest.fixture
def web_client():
    app.config['TESTING'] = True
    url = get_database_url()
    
    clear_database(url)
    setup_database(url)

    with app.test_client() as client:
        yield client