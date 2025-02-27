import deepdog.results
import pytest


def test_parse_bayesrun_filename():
	valid1 = "20250226-204120-dot1-dot1-2-0.realdata.fast_filter.bayesrun.csv"

	timestamp, slug = deepdog.results._parse_string_output_filename(valid1)
	assert timestamp == "20250226-204120"
	assert slug == "dot1-dot1-2-0"

	valid2 = "dot1-dot1-2-0.realdata.fast_filter.bayesrun.csv"

	timestamp, slug = deepdog.results._parse_string_output_filename(valid2)
	assert timestamp is None
	assert slug == "dot1-dot1-2-0"

	with pytest.raises(ValueError):
		deepdog.results._parse_string_output_filename("not_a_valid_filename")
