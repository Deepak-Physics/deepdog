from deepdog import __version__
import deepdog


def test_version():
	assert deepdog.get_version() == __version__
