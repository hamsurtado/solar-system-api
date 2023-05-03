import pytest
from app import create_app, db
from flask.signals import request_finished
from app.models.planet import Planet 

@pytest.fixture
def app():
    app = create_app(testing=True)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()
    
    with app.app_context():
        db.create_all()
        yield app 
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def three_saved_planets(app):
    # Arrange
    planet_Mars = Planet(name="Mars",
                    description="red",
                    has_water=True)
    planet_Jupiter = Planet(name="Jupiter",
                    description="orange",
                    has_water=True)
    planet_Earth = Planet(name="Earth",
                    description="cyan",
                    has_water=True)
    
    db.session.add_all([planet_Mars, planet_Jupiter, planet_Earth])
    
    db.session.commit()

    return [planet_Mars.to_dict(), planet_Jupiter.to_dict(), planet_Earth.to_dict()]