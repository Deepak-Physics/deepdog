import logging
import argparse
import json
import deepdog.cli.probs.args
import deepdog.cli.probs.dicts
import deepdog.results
import deepdog.indexify
import pathlib

_logger = logging.getLogger(__name__)


def set_up_logging(log_file: str):

	log_pattern = "%(asctime)s | %(levelname)-7s | %(name)s:%(lineno)d | %(message)s"
	if log_file is None:
		handlers = [
			logging.StreamHandler(),
		]
	else:
		handlers = [logging.StreamHandler(), logging.FileHandler(log_file)]
	logging.basicConfig(
		level=logging.DEBUG,
		format=log_pattern,
		# it's okay to ignore this mypy error because who cares about logger handler types
		handlers=handlers,  # type: ignore
	)
	logging.captureWarnings(True)


def wrapped_main(args: argparse.Namespace):
	"""
	Main function with passed in arguments and no additional logging setup in case we want to extract out later
	"""
	_logger.info(f"args: {args}")

	if args.coalesced_keys:
		raise NotImplementedError(
			"Currently not supporting coalesced keys, but maybe in future"
		)
	with open(args.indexify_json, "r") as indexify_json_file:
		indexify_data = json.load(indexify_json_file)
		if args.seed_index > 0:
			indexify_data[args.seed_fieldname] = list(range(args.seed_index))
		# _logger.debug(f"Indexifier data looks like {indexify_data}")
		indexifier = deepdog.indexify.Indexifier(indexify_data)

	bayes_dir = pathlib.Path(args.bayesrun_directory)
	out_files = [f for f in bayes_dir.iterdir() if f.name.endswith("bayesrun.csv")]
	_logger.info(
		f"Found {len(out_files)} bayesrun.csv files in directory {args.bayesrun_directory}"
	)
	# _logger.info(out_files)
	parsed_output_files = [
		deepdog.results.read_output_file(f, indexifier) for f in out_files
	]

	_logger.info("building uncoalesced dict")
	uncoalesced_dict = deepdog.cli.probs.dicts.build_model_dict(parsed_output_files)

	if args.uncoalesced_outfile:
		deepdog.cli.probs.dicts.write_uncoalesced_dict(
			args.uncoalesced_outfile, uncoalesced_dict
		)
	else:
		_logger.info("Skipping writing uncoalesced")

	_logger.info("building coalesced dict")
	coalesced = deepdog.cli.probs.dicts.coalesced_dict(uncoalesced_dict)

	if args.coalesced_outfile:
		deepdog.cli.probs.dicts.write_coalesced_dict(args.coalesced_outfile, coalesced)
	else:
		_logger.info("Skipping writing coalesced")


def main():
	args = deepdog.cli.probs.args.parse_args()
	set_up_logging(args.log_file)
	wrapped_main(args)
