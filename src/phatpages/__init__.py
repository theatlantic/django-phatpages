import pkg_resources

try:
    __version__ = pkg_resources.get_distribution('django-phatpages').version
except pkg_resources.DistributionNotFound:
    __version__ = None
