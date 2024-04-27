import typing
from deepdog.results import BayesrunOutput
import logging
import csv

_logger = logging.getLogger(__name__)


def build_model_dict(
	bayes_outputs: typing.Sequence[BayesrunOutput],
) -> typing.Dict[
	typing.Tuple, typing.Dict[typing.Tuple, typing.Dict["str", typing.Any]]
]:
	"""
	Maybe someday do something smarter with the coalescing and stuff but don't want to so i won't
	"""
	# assume that everything is well formatted and the keys are the same across entire list and initialise list of keys.
	# model dict will contain a model_key: {calculation_dict} where each calculation_dict represents a single calculation for that model,
	# the uncoalesced version, keyed by the specific file keys
	model_dict: typing.Dict[
		typing.Tuple, typing.Dict[typing.Tuple, typing.Dict["str", typing.Any]]
	] = {}

	for out in bayes_outputs:
		for model_result in out.results:
			model_key = tuple(v for v in model_result.parsed_model_keys.values())
			if model_key not in model_dict:
				model_dict[model_key] = {}
			calculation_dict = model_dict[model_key]
			calculation_key = tuple(v for v in out.data.values())
			if calculation_key not in calculation_dict:
				calculation_dict[calculation_key] = {
					"_model_key_dict": model_result.parsed_model_keys,
					"_calculation_key_dict": out.data,
					"success": model_result.success,
					"count": model_result.count,
				}
			else:
				raise ValueError(
					f"Got {calculation_key} twice for model_key {model_key}"
				)

	return model_dict


def write_uncoalesced_dict(
	uncoalesced_output_filename: typing.Optional[str],
	uncoalesced_model_dict: typing.Dict[
		typing.Tuple, typing.Dict[typing.Tuple, typing.Dict["str", typing.Any]]
	],
):
	if uncoalesced_output_filename is None or uncoalesced_output_filename == "":
		_logger.warning("Not provided a uncoalesced filename, not going to try")
		return

	first_value = next(iter(next(iter(uncoalesced_model_dict.values())).values()))
	model_field_names = set(first_value["_model_key_dict"].keys())
	calculation_field_names = set(first_value["_calculation_key_dict"].keys())
	if not (set(model_field_names).isdisjoint(calculation_field_names)):
		_logger.info(f"Detected model field names {model_field_names}")
		_logger.info(f"Detected calculation field names {calculation_field_names}")
		raise ValueError(
			f"model field names {model_field_names} and calculation {calculation_field_names} have an overlap, which is possibly a problem"
		)
	collected_fieldnames = list(model_field_names)
	collected_fieldnames.extend(calculation_field_names)
	collected_fieldnames.extend(["success", "count"])
	_logger.info(f"Full uncoalesced fieldnames are {collected_fieldnames}")
	with open(uncoalesced_output_filename, "w", newline="") as uncoalesced_output_file:
		writer = csv.DictWriter(
			uncoalesced_output_file, fieldnames=collected_fieldnames
		)
		writer.writeheader()

		for model_dict in uncoalesced_model_dict.values():
			for calculation in model_dict.values():
				row = calculation["_model_key_dict"].copy()
				row.update(calculation["_calculation_key_dict"].copy())
				row.update(
					{
						"success": calculation["success"],
						"count": calculation["count"],
					}
				)
				writer.writerow(row)


def coalesced_dict(
	uncoalesced_model_dict: typing.Dict[
		typing.Tuple, typing.Dict[typing.Tuple, typing.Dict["str", typing.Any]]
	]
):
	coalesced_dict = {}
	for model_key, model_dict in uncoalesced_model_dict.items():
		for calculation in model_dict.values():
			if model_key not in coalesced_dict:
				coalesced_dict[model_key] = {
					"_model_key_dict": calculation["_model_key_dict"].copy(),
					"calculations_coalesced": 0,
					"count": 0,
					"success": 0,
				}
			sub_dict = coalesced_dict[model_key]
			sub_dict["calculations_coalesced"] += 1
			sub_dict["count"] += calculation["count"]
			sub_dict["success"] += calculation["success"]
	return coalesced_dict


def write_coalesced_dict(
	coalesced_output_filename: typing.Optional[str],
	coalesced_model_dict: typing.Dict[typing.Tuple, typing.Dict["str", typing.Any]],
):
	if coalesced_output_filename is None or coalesced_output_filename == "":
		_logger.warning("Not provided a uncoalesced filename, not going to try")
		return

	first_value = next(iter(coalesced_model_dict.values()))
	model_field_names = set(first_value["_model_key_dict"].keys())
	_logger.info(f"Detected model field names {model_field_names}")

	collected_fieldnames = list(model_field_names)
	collected_fieldnames.extend(["calculations_coalesced", "success", "count"])
	with open(coalesced_output_filename, "w", newline="") as coalesced_output_file:
		writer = csv.DictWriter(coalesced_output_file, fieldnames=collected_fieldnames)
		writer.writeheader()

		for model_dict in coalesced_model_dict.values():
			row = model_dict["_model_key_dict"].copy()
			row.update(
				{
					"calculations_coalesced": model_dict["calculations_coalesced"],
					"success": model_dict["success"],
					"count": model_dict["count"],
				}
			)
			writer.writerow(row)
