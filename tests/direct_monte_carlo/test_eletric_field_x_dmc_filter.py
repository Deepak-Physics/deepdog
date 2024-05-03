import pdme.measurement
import pdme.measurement.input_types
from pdme.model import (
	LogSpacedRandomCountMultipleDipoleFixedMagnitudeModel,
	LogSpacedRandomCountMultipleDipoleFixedMagnitudeXYModel,
	LogSpacedRandomCountMultipleDipoleFixedMagnitudeFixedOrientationModel,
)
import deepdog.direct_monte_carlo.dmc_filters
import numpy.random
import numpy.testing
import logging

_logger = logging.getLogger(__name__)


def fixed_z_model_func(
	xmin,
	xmax,
	ymin,
	ymax,
	zmin,
	zmax,
	wexp_min,
	wexp_max,
	pfixed,
	n_max,
	prob_occupancy,
):
	return LogSpacedRandomCountMultipleDipoleFixedMagnitudeFixedOrientationModel(
		xmin,
		xmax,
		ymin,
		ymax,
		zmin,
		zmax,
		wexp_min,
		wexp_max,
		pfixed,
		0,
		0,
		n_max,
		prob_occupancy,
	)


def get_model(orientation):
	model_funcs = {
		"fixedz": fixed_z_model_func,
		"free": LogSpacedRandomCountMultipleDipoleFixedMagnitudeModel,
		"fixedxy": LogSpacedRandomCountMultipleDipoleFixedMagnitudeXYModel,
	}
	model = model_funcs[orientation](
		-10,
		10,
		-17.5,
		17.5,
		5,
		7.5,
		-5,
		6.5,
		10**3,
		2,
		0.99999999,
	)
	model.n = 2
	model.rng = numpy.random.default_rng(1234)

	return (
		f"connors_geom-5height-orientation_{orientation}-pfixexp_{3}-dipole_count_{2}",
		model,
	)


def test_electric_field_x_dmc_filter():

	dipoles_raw = [
		[(1, 2, 3), (4, 5, 6), 1],
		[(-1, 5, 2), (6, 5, 4), 10],
	]
	dipoles = [
		pdme.measurement.OscillatingDipole(numpy.array(d[0]), numpy.array(d[1]), d[2])
		for d in dipoles_raw
	]

	_logger.debug(f"dipoles: {dipoles}")
	dot_inputs_raw = [
		([-1, -1, 0], 1),
		([-1, -1, 0], 2),
		([-1, -1, 0], 3),
		([-1, -1, 0], 4),
	]
	dot_inputs_array = pdme.measurement.input_types.dot_inputs_to_array(dot_inputs_raw)
	_logger.debug(f"dot_inputs_array: {dot_inputs_array}")

	arrangement = pdme.measurement.OscillatingDipoleArrangement(dipoles)
	measurements = []
	for input in dot_inputs_raw:
		ex = sum(
			[
				dipole.s_electric_fieldx_at_position(*input)
				for dipole in arrangement.dipoles
			]
		)
		ex_low = ex * 0.5
		ex_high = ex * 1.5
		meas = pdme.measurement.DotRangeMeasurement(ex_low, ex_high, input[0], input[1])
		measurements.append(meas)

	filter = deepdog.direct_monte_carlo.dmc_filters.SingleDotSpinQubitFrequencyFilter(
		measurements
	)

	samples = numpy.array(
		[
			[
				[1, 2, 3, 4, 5, 6, 1],
				[-1, 5, 2, 6, 5, 4, 10],
			],
			[
				[10, 20, 30, 40, 50, 60, 1],
				[-1, 5, 2, 6, 5, 4, 1],
			],
			[
				[1, 1, 1, 1, 1, 1, 1],
				[2, 2, 2, 2, 2, 2, 1],
			],
		]
	)

	expected = samples[
		0:1
	]  # only expect to see the first guy, because that's what generated our thing
	filtered = filter.filter_samples(samples)
	assert len(filtered) != len(samples), "Should have filtered some out!"
	numpy.testing.assert_array_equal(
		filtered, expected, "The filter should have only returned the first one"
	)
