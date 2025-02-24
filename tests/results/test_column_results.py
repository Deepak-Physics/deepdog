import deepdog.results.read_csv


def test_parse_groupdict():
	example_column_name = (
		"geom_-20_20_-10_10_0_5-orientation_free-dipole_count_100_success"
	)

	parsed = deepdog.results.read_csv._parse_bayesrun_column(example_column_name)
	assert parsed is not None
	expected = deepdog.results.read_csv.BayesrunColumnParsed(
		{
			"xmin": "-20",
			"xmax": "20",
			"ymin": "-10",
			"ymax": "10",
			"zmin": "0",
			"zmax": "5",
			"orientation": "free",
			"avg_filled": "100",
			"field_name": "success",
		}
	)
	assert parsed == expected


def test_parse_groupdict_with_magnitude():
	example_column_name = (
		"geom_-20_20_-10_10_0_5-magnitude_3.5-orientation_free-dipole_count_100_success"
	)

	parsed = deepdog.results.read_csv._parse_bayesrun_column(example_column_name)
	assert parsed is not None
	expected = deepdog.results.read_csv.BayesrunColumnParsed(
		{
			"xmin": "-20",
			"xmax": "20",
			"ymin": "-10",
			"ymax": "10",
			"zmin": "0",
			"zmax": "5",
			"orientation": "free",
			"avg_filled": "100",
			"log_magnitude": "3.5",
			"field_name": "success",
		}
	)
	assert parsed == expected


def test_parse_groupdict_with_negative_magnitude():
	example_column_name = "geom_-20_20_-10_10_0_5-magnitude_-3.5-orientation_free-dipole_count_100_success"

	parsed = deepdog.results.read_csv._parse_bayesrun_column(example_column_name)
	assert parsed is not None
	expected = deepdog.results.read_csv.BayesrunColumnParsed(
		{
			"xmin": "-20",
			"xmax": "20",
			"ymin": "-10",
			"ymax": "10",
			"zmin": "0",
			"zmax": "5",
			"orientation": "free",
			"avg_filled": "100",
			"log_magnitude": "-3.5",
			"field_name": "success",
		}
	)
	assert parsed == expected


# def test_parse_no_match_column_name():
# 	parsed = deepdog.results.parse_bayesrun_column("There's nothing here")
# 	assert parsed is None
