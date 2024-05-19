import deepdog.subset_simulation.subset_simulation_impl as impl
import numpy


def test_subset_simulation_multi_result_coalescing_include_dirty(snapshot):
	res1 = impl.SubsetSimulationResult(
		probs_list=(),
		over_target_cost=1,
		over_target_likelihood=1,
		under_target_cost=0.99,
		under_target_likelihood=0.8,
		lowest_likelihood=0.5,
		messages=[],
	)

	res2 = impl.SubsetSimulationResult(
		probs_list=(),
		over_target_cost=1,
		over_target_likelihood=1,
		under_target_cost=0.99,
		under_target_likelihood=0.08,
		lowest_likelihood=0.01,
		messages=[],
	)

	res3 = impl.SubsetSimulationResult(
		probs_list=(),
		over_target_cost=None,
		over_target_likelihood=None,
		under_target_cost=None,
		under_target_likelihood=None,
		lowest_likelihood=0.0001,
		messages=[],
	)

	combined = impl.coalesce_ss_results("test", [res1, res2, res3])

	assert combined == snapshot


def test_subset_simulation_multi_result_coalescing_easy_arithmetic(snapshot):
	res1 = impl.SubsetSimulationResult(
		probs_list=(),
		over_target_cost=1,
		over_target_likelihood=1,
		under_target_cost=0.99,
		under_target_likelihood=0.8,
		lowest_likelihood=0.5,
		messages=[],
	)

	res2 = impl.SubsetSimulationResult(
		probs_list=(),
		over_target_cost=1,
		over_target_likelihood=1,
		under_target_cost=0.99,
		under_target_likelihood=0.6,
		lowest_likelihood=0.01,
		messages=[],
	)

	combined = impl.coalesce_ss_results("test", [res1, res2])

	assert combined.arithmetic_mean_estimated_likelihood == 0.7
	assert combined == snapshot


def test_subset_simulation_multi_result_coalescing_easy_geometric(snapshot):
	res1 = impl.SubsetSimulationResult(
		probs_list=(),
		over_target_cost=1,
		over_target_likelihood=1,
		under_target_cost=0.99,
		under_target_likelihood=0.1,
		lowest_likelihood=0.5,
		messages=[],
	)

	res2 = impl.SubsetSimulationResult(
		probs_list=(),
		over_target_cost=1,
		over_target_likelihood=1,
		under_target_cost=0.99,
		under_target_likelihood=0.001,
		lowest_likelihood=0.01,
		messages=[],
	)

	combined = impl.coalesce_ss_results("test", [res1, res2])

	numpy.testing.assert_allclose(combined.estimated_likelihood, 0.01)
	assert combined == snapshot
