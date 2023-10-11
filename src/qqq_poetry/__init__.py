def __getattr__(name: str) -> str:
	"""Lazily get the version from whatever API is available."""
	if name == "__version__":
		try:
			from importlib.metadata import version
		except ImportError:
			import pkg_resources

			return pkg_resources.get_distribution("qqq-poetry").version
		else:
			return version("qqq-poetry")
	raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
