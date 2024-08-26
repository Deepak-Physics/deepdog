import deepdog.indexify
import logging

_logger = logging.getLogger(__name__)


def test_indexifier():
	weight_dict = {"key_1": [1, 2, 3], "key_2": ["a", "b", "c"]}
	indexifier = deepdog.indexify.Indexifier(weight_dict)
	_logger.debug(f"setting up indexifier {indexifier}")
	assert indexifier.indexify(0) == {"key_1": 1, "key_2": "a"}
	assert indexifier.indexify(5) == {"key_1": 2, "key_2": "c"}
	assert len(indexifier) == 9


def test_indexifier_length_short():
	weight_dict = {"key_1": [1, 2, 3], "key_2": ["b", "c"]}
	indexifier = deepdog.indexify.Indexifier(weight_dict)
	_logger.debug(f"setting up indexifier {indexifier}")

	assert len(indexifier) == 6
