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

def test_green_between():
    g = G.Greengraph('London','Oxford');
    with assert_raises(TypeError):
        assert g.green_between()
    
