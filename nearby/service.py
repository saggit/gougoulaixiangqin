from uauth.models import UserOldCoordinate
from datetime import datetime
import geohash

def update_user_coordinate(longitude, latitude, user):
    if user.latest_longitude and user.latest_latitude:
        UserOldCoordinate.objects.create(
            user=user, longitude=user.latest_longitude,
            latitude=user.latest_latitude
        )
    user.latest_longitude = float(longitude)
    user.latest_latitude = float(latitude)
    geo_hash = geohash.encode(user.latest_latitude, user.latest_longitude)
    user.geo_hash = geo_hash
    user.updated_coordinate_time = datetime.now()
    user.save()
    return geo_hash
