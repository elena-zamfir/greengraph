import yaml
import os
from nose.tools import assert_almost_equal, assert_equal
from greengraph import Greengraph as G
from nose.tools import assert_raises


def test_graph_initialization():
    with assert_raises(TypeError):
        assert G.Greengraph()
        assert G.Greengraph('London',)
    assert_equal(type(G.Greengraph('London','Paris')),G.Greengraph)



def test_coordinates():
    g = G.Greengraph('London','Oxford');
    with assert_raises(TypeError):
        assert g.geolocate()
    with open(os.path.join(os.path.dirname(__file__),'fixtures','samples_city_coordinates.yaml')) as fixtures_file:
        fixtures=yaml.load(fixtures_file)
        for fixture in fixtures:
            answer=fixture.pop('answer')
            city = fixture.pop('city')
            assert_equal(g.geolocate(city)[0], answer[0])
            assert_equal(g.geolocate(city)[1], answer[1])

def test_location_sequence():
    g = G.Greengraph('London','Oxford');
    with assert_raises(TypeError):
        assert g.location_sequence()
        assert g.location_sequence(3)
        assert g.location_sequence([2,3], [10, -2])
    with assert_raises(ValueError):
        assert g.location_sequence([2,3], [10, 20], -5)
    assert_equal(len(g.location_sequence([0, 1], [-10, 34], 10)),10)

from mock import patch

def test_green_between():
    g = G.Greengraph('London','Oxford');
    with assert_raises(TypeError):
        assert g.green_between()
    with assert_raises(ValueError):
        assert g.green_between(-5)
        assert g.green_between(0)
    with patch.object(G.Map, 'count_green') as mock_count_green:
        g.green_between(1)
        mock_count_green.assert_called_once_with()

#import requests
#from Mock import MagicMock
#def test_map_initialization():
#    with patch.object(requests, 'get') as mock_get:
#        london_map = G.Map(G.Greengraph('London','Oxford').geolocate('London')[0],G.Greengraph('London','Oxford').geolocate('London')[1])
#        mock_get.assert_called_with("http://maps.googleapis.com/maps/api/staticmap?",params = {'sensor':'false', 'zoom':12, 'size':'400x400', 'center':'51.5073509, -0.1277583', 'style':'feature:all|element:labels|visibility:off'})

from mock import patch

import requests
def side_effect(base, params):
    with open('/Users/elenazamfir/elena/PhD/python_code/research_software_engineering/greengraph/greengraph/test/fixtures/request_response.yaml','r') as source:
        return yaml.load(source)
long = 0
lat = 51
satellite=True
zoom=10
size=(400,400)
sensor=False
satellite = True
base="http://maps.googleapis.com/maps/api/staticmap?"
params=dict(
            sensor= str(sensor).lower(),
            zoom= zoom,
            size= "x".join(map(str, size)),
            center= ",".join(map(str, (lat, long) )),
            style="feature:all|element:labels|visibility:off")
params["maptype"]="satellite"
@patch.object(requests, 'get')
def test_map_creation( mock_get):
    mock_get.side_effect = side_effect
    G.Map(51,0)
    mock_get.assert_called_with(base, params=params)

mock_get = test_map_creation()


import numpy as np
m_london = G.Map(G.Greengraph('London','Oxford').geolocate('London')[0],G.Greengraph('London','Oxford').geolocate('London')[1])
m_oxford = G.Map(G.Greengraph('London','Oxford').geolocate('Oxford')[0],G.Greengraph('London','Oxford').geolocate('Oxford')[1])

def test_green():
    with assert_raises(TypeError):
        assert m_london.green()
    with assert_raises(ValueError):
        assert m_london.green(-4)
    assert np.sum(m_london.green(1.1)) < np.sum(m_oxford.green(1.1))
