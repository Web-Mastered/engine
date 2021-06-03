from django import template

from engine import VERSION
import pkg_resources

register = template.Library()

@register.simple_tag
def get_engine_version():
    """
    Simple template tag function that returns Engine's version when called.
    """
    return VERSION

@register.simple_tag
def get_pip_requirements():
    """
    Simple template tag function that returns all packages and version in requirements.txt.
    """
    installed_packages = pkg_resources.working_set
    installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
    for i in installed_packages])
    return installed_packages_list

@register.simple_tag
def get_pip_list():
    """
    Simple template tag function that returns all packages and version installed via Pip.
    """
    return [p.project_name + " @ " + str(p.parsed_version) for p in pkg_resources.working_set]

@register.simple_tag
def diagnostics_report():
    """
    Simple template tag function that returns get_engine_version, get_pip_requirements and 
    get_pip_list all compiled in the form of a dictionary.
    """
    report = {
        "engine_version": get_engine_version(),
        "requirements_txt": get_pip_requirements(),
        "pip_list": get_pip_list(),
    }
    return report