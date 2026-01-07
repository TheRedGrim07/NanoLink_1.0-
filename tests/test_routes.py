import pytest
from app import app
from models import db, Link

# --- 1. THE SETUP CREW (Fixture) ---
@pytest.fixture
def client():
    """
    Creates a fake browser (client) and a temporary database
    just for testing.
    """
    # Configure app for testing
    app.config['TESTING'] = True
    # Critical: Use RAM memory, not a real file. It wipes clean after testing.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:' 
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all() # Create tables in RAM
            yield client    # Give the test access to the client
            db.drop_all()   # Clean up after test finishes

# --- 2. THE TESTS ---

def test_homepage_loads(client):
    """Can we visit the homepage?"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"NanoLink" in response.data # Check if our title is there

def test_shorten_link(client):
    """Does submitting the form actually create a link?"""
    # Simulate POST request (Filling the form)
    response = client.post('/', data={'url': 'https://www.google.com'})
    
    # Check if page loaded (200 OK)
    assert response.status_code == 200
    # Check if the success message appears
    assert b"Shorten another link" in response.data

def test_redirect_logic(client):
    """If we visit a short link, does it redirect?"""
    # 1. Manually add a link to the Fake DB
    with app.app_context():
        link = Link(original_url="https://github.com")
        db.session.add(link)
        db.session.commit()
        # We know ID 1 should be '1' in Base62
        
    # 2. Visit the short link
    response = client.get('/1')
    
    # 3. Check for 302 (Redirect code)
    assert response.status_code == 302
    assert response.location == "https://github.com"