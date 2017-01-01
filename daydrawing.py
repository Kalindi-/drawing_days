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
        print sun_data["message"]
        print "Sun on date url call did not work"
        return "Something went wrong"

def get_day_percent(sun_data, drawing_precision=4):
    sunrise, sunset = sun_data
    #sunrise_int = int(sunrise[:2]) * drawing_precision + int(sunrise[3:]) / 60 / drawing_precision
    #sunset_int = int(sunset[:2]) * drawing_precision + int(sunset[3:]) / 60 / drawing_precision
    sunrise_int = int(sunrise[:2]) * drawing_precision + int(sunrise[3:]) / 60 / drawing_precision
    sunset_int = int(sunset[:2]) * drawing_precision + int(sunset[3:]) / 60 / drawing_precision
    return sunrise_int, sunset_int

#print get_day_percent("06:07", "20:01")

def make_day(sunrise, sunset, drawing_precision=4):
    """Creates a list rappresentation of the day, █ rappresenting night time and ☼ daytime

    drawing_precision: the higher the better"""

    day = [["█"]*24*drawing_precision]
    sunrise_int = int(sunrise[:2]) * drawing_precision + int(sunrise[3:]) / 60 / drawing_precision
    sunset_int = int(sunset[:2]) * drawing_precision + int(sunset[3:]) / 60 / drawing_precision
    for i in range(sunrise_int, sunset_int):
        day[0][i] = "☼"
    return draw_day(day)


def draw_day(day):
    """Returns the night/day drawing as a string rappresentation"""

    day_drawing = ""
    for i in day:
        for j in i:
            day_drawing += j
    return day_drawing


def valid_location(location):
    """Checks if the location gives lat and lng, asks till valid, returns it."""
    try:
        url='http://maps.googleapis.com/maps/api/geocode/json?address=' + location
        location_data_str = urlfetch.fetch(url)
        location_data = json.loads(location_data_str.content)
        if location_data["status"] == "OK":
            lat_lng = location_data["results"][0]["geometry"]["location"]
            lat, lng = lat_lng["lat"], lat_lng["lng"]
            return lat, lng
        else:
            return "Invalid location"
    except urlfetch.Error:
        print 'Caught exception fetching url'
        logging.exception('Caught exception fetching url')

#print valid_location("melbourn")


