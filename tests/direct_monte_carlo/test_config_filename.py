import re
import deepdog.direct_monte_carlo


def test_config_check_self():
	config = deepdog.direct_monte_carlo.DirectMonteCarloConfig(
		tag="test_tag",
		bayesrun_file_timestamp=False,
	)
	expected_filename = "test_tag.realdata.fast_filter.bayesrun.csv"
	actual_filename = config.get_filename()
	assert actual_filename == expected_filename
	regex = config.get_filename_regex()
	assert re.match(regex, actual_filename) is not None


def test_config_check_self_with_timestamp():
	config = deepdog.direct_monte_carlo.DirectMonteCarloConfig(
		tag="test_tag",
		bayesrun_file_timestamp=True,
	)
	expected_filename_ending = "test_tag.realdata.fast_filter.bayesrun.csv"
	actual_filename = config.get_filename()
	assert actual_filename.endswith(expected_filename_ending)
	regex = config.get_filename_regex()
	assert re.match(regex, actual_filename) is not None
