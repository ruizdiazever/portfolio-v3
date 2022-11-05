from datetime import datetime
from strawberry import type, field
from src.files.info import ME
from src.settings import EMAIL, PHONE


@type
class About:
    image: str
    name: str
    content: str
    date: datetime
    phone: str
    email: str
    city: str
    country: str


def get_about(self) -> About:
    return About(
        image = "img/about.webp", 
        name = ME['name'], 
        content = "Hello",
        date = datetime.now(),
        phone = PHONE,
        email = EMAIL,
        city = ME['city'],
        country = ME['country']
    )
