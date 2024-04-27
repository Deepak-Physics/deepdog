import deepdog.indexify
import logging

_logger = logging.getLogger(__name__)


def test_indexifier():
	weight_dict = {"key_1": [1, 2, 3], "key_2": ["a", "b", "c"]}
	indexifier = deepdog.indexify.Indexifier(weight_dict)
	_logger.debug(f"setting up indexifier {indexifier}")
	assert indexifier.indexify(0) == {"key_1": 1, "key_2": "a"}
	assert indexifier.indexify(5) == {"key_1": 2, "key_2": "c"}
