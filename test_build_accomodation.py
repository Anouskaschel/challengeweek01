
from build_accommodation import build_accommodation


registration_build_accommodations = {"tent": {"price": 50, "purchased_boxes": {}},
    "caravan": {"price": 100, "purchased_boxes": {}},
    "bungalow": {"price": 500, "purchased_boxes": {}},
    "vakantie villa": {"price": 1000, "purchased_boxes": {}}
    }

print("first")
print(build_accommodation("PLAYER 1", 17, 1000, registration_build_accommodations))
print("second")
print(build_accommodation("PLAYER 1", 17, 1000, registration_build_accommodations))