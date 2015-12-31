import yaml
import os
from nose.tools import assert_almost_equal, assert_equal
from greengraph import Greengraph as G


g = G.Greengraph('London','Oxford');
def test_coordinates():
     with open(os.path.join(os.path.dirname(__file__),'fixtures','samples_city_coordinates.yaml')) as fixtures_file:
        fixtures=yaml.load(fixtures_file)
        for fixture in fixtures:
            answer=fixture.pop('answer')
            city = fixture.pop('city')
            assert_equal(g.geolocate(city)[0], answer[0])
            assert_equal(g.geolocate(city)[1], answer[1])
