import deepdog
import logging
import logging.config

import numpy.random

from pdme.model import (
	LogSpacedRandomCountMultipleDipoleFixedMagnitudeModel,
	LogSpacedRandomCountMultipleDipoleFixedMagnitudeXYModel,
	LogSpacedRandomCountMultipleDipoleFixedMagnitudeFixedOrientationModel,
)


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


def test_basic_analysis(snapshot):

	dot_positions = [[0, 0, 0], [0, 1, 0]]

	freqs = [1, 10, 100]
	models = []

	orientations = ["free", "fixedxy", "fixedz"]
	for orientation in orientations:
		models.append(get_model(orientation))

	_logger.info(f"have {len(models)} models to look at")
	if len(models) == 1:
		_logger.info(f"only one model, name: {models[0][0]}")

	square_run = deepdog.BayesRunWithSubspaceSimulation(
		dot_positions,
		freqs,
		models,
		models[0][1],
		filename_slug="test",
		end_threshold=0.9,
		ss_n_c=5,
		ss_n_s=2,
		ss_m_max=10,
		ss_target_cost=150,
		ss_level_0_seed=200,
		ss_mcmc_seed=20,
		ss_use_adaptive_steps=True,
		ss_default_phi_step=0.01,
		ss_default_theta_step=0.01,
		ss_default_r_step=0.01,
		ss_default_w_log_step=0.01,
		ss_default_upper_w_log_step=4,
		ss_dump_last_generation=False,
		write_output_to_bayesruncsv=False,
	)
	result = square_run.go()

	assert result == snapshot


def test_bayesss_with_tighter_cost(snapshot):

	dot_positions = [[0, 0, 0], [0, 1, 0]]

	freqs = [1, 10, 100]
	models = []

	orientations = ["free", "fixedxy", "fixedz"]
	for orientation in orientations:
		models.append(get_model(orientation))

	_logger.info(f"have {len(models)} models to look at")
	if len(models) == 1:
		_logger.info(f"only one model, name: {models[0][0]}")

	square_run = deepdog.BayesRunWithSubspaceSimulation(
		dot_positions,
		freqs,
		models,
		models[0][1],
		filename_slug="test",
		end_threshold=0.9,
		ss_n_c=5,
		ss_n_s=2,
		ss_m_max=10,
		ss_target_cost=1.5,
		ss_level_0_seed=200,
		ss_mcmc_seed=20,
		ss_use_adaptive_steps=True,
		ss_default_phi_step=0.01,
		ss_default_theta_step=0.01,
		ss_default_r_step=0.01,
		ss_default_w_log_step=0.01,
		ss_default_upper_w_log_step=4,
		ss_dump_last_generation=False,
		write_output_to_bayesruncsv=False,
	)
	result = square_run.go()

	assert result == snapshot
