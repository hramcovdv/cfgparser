""" Config parser with TextFSM.

Usage:
  parser [options] TEMPLATE CONFIG
  parser --help | --version

Options:
  -h --help     Show this screen.
  -v --version  Show version.
  -H --headers  Print headers."""
import cli_ui
from docopt import docopt
from textfsm import (
	TextFSM,
	TextFSMError,
	TextFSMTemplateError
)


def esc(value):
	""" Escaping chars. """
	return f'"{value}"' if ',' in str(value) else value


def print_row(row):
	""" Print CSV row """
	print(','.join([esc(col) for col in row]))


def parse(template: str, config: str) -> list:
	""" Parse config with template. """
	try:
		with open(template) as tmp, open(config) as cfg:
			fsm = TextFSM(tmp)
			rows = fsm.ParseText(cfg.read())
			head = [str(i).lower() for i in fsm.header]
			# return [{head[i]: r for i, r in enumerate(row)} for row in rows]
			return head, rows
	except (IOError, TextFSMError, TextFSMTemplateError) as err:
		cli_ui.fatal(err)

	return None


if __name__ == '__main__':
	args = docopt(__doc__, version='parser 0.1')

	head, rows = parse(args['TEMPLATE'], args['CONFIG'])

	if args['--headers']:
		print_row(head)

	for row in rows:
		print_row(row)
