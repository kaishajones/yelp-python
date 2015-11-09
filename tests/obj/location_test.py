# -*- coding: UTF-8 -*-
import json

from yelp.obj.location import Coordinate
from yelp.obj.location import Location


def test_init_location():
    with open('json/business_response.json') as biz:
        response = json.load(biz)['location']
        location = Location(response)
        assert location.address == response['address']
        assert type(location.coordinate) is Coordinate


def test_init_location_no_coordinate():
    with open('json/business_response.json') as biz:
        response = json.load(biz)['location']
        response.pop('coordinate', None)
        location = Location(response)
        assert location.address == response['address']
        assert location.coordinate is None