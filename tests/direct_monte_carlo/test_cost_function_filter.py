import deepdog.direct_monte_carlo.cost_function_filter
import numpy


def test_px_cost_function_filter_example():

	dipoles_1 = [
		[1, 2, 3, 4, 5, 6, 7],
		[2, 3, 2, 5, 4, 7, 6],
	]

	dipoles_2 = [
		[15, 9, 8, 7, 6, 5, 3],
		[30, 4, 4, 7, 3, 1, 4],
	]

	dipoleses = numpy.array([dipoles_1, dipoles_2])

	def cost_function(dipoleses: numpy.ndarray) -> numpy.ndarray:
		return dipoleses[:, :, 0].max(axis=-1)

	expected_costs = numpy.array([2, 30])

	numpy.testing.assert_array_equal(cost_function(dipoleses), expected_costs)

	filter = deepdog.direct_monte_carlo.cost_function_filter.CostFunctionTargetFilter(
		cost_function, 5
	)

	actual_filtered = filter.filter_samples(dipoleses)
	expected_filtered = numpy.array([dipoles_1])
	assert actual_filtered.size != 0
	numpy.testing.assert_array_equal(actual_filtered, expected_filtered)

	filter_stricter = (
		deepdog.direct_monte_carlo.cost_function_filter.CostFunctionTargetFilter(
			cost_function, 0.5
		)
	)

	actual_filtered_stricter = filter_stricter.filter_samples(dipoleses)
	assert actual_filtered_stricter.size == 0
