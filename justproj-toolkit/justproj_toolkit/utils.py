from datetime import datetime


def get_current_datetime() -> str:
	"""
	Gets the current datetime.

	:returns:   The current datetime.
	:rtype:     str
	"""
	return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
