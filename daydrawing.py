# -*- coding: utf-8 -*-
from google.appengine.api import urlfetch
import json
import urllib

def sun_on_date(loc, date):
    """Returns sunrise and sunset times based on location and date"""
    loc = valid_location(loc)
    payload = {
        "lat": str(loc[0]),
        "lng": str(loc[1]),
        "date": date,
        "username": "kalindi"  # Use my name if "demo" doesn't work
    }

    payload = urllib.urlencode(payload)

    try:
        url='http://api.geonames.org/timezoneJSON?' + payload
        result = json.loads(urlfetch.fetch(url).content)
        sun_data = result["dates"][0]
        sunrise, sunset = sun_data["sunrise"][11:16], sun_data["sunset"][11:16]
        return sunrise, sunset
    except:
        print "Sun on date url call did not work"
        return False

def get_day_percent(sun_data):
    sunrise, sunset = sun_data
    day_percentages = {
        "sunrise": get_sun_time(sunrise),
        "sunset": get_sun_time(sunset)
    }
    return day_percentages

def get_sun_time(time, drawing_precision=4):
    return int(time[:2]) * drawing_precision + int(time[3:]) / 60 / drawing_precision

def valid_location(location):
    """Checks if the location gives lat and lng, asks till valid, returns it."""
    try:
        url='http://maps.googleapis.com/maps/api/geocode/json?address=' + location
        location_data_str = urlfetch.fetch(url)
        location_data = json.loads(location_data_str.content)

        if location_data["status"] == "OK":
            lat_lng = location_data["results"][0]["geometry"]["location"]
            return lat_lng["lat"], lat_lng["lng"]
        else:
            return "Invalid location"
    except urlfetch.Error:
        print "Caught exception fetching url"
        return "Caught exception fetching url"

#print valid_location("melbourn")


