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
    requirements_packages_list = []
    requirements_packages = list(pkg_resources.working_set)
    for package in requirements_packages:
        requirements_packages_list.append(str(package.key) + " == " + str(package.version))
    return requirements_packages_list

@register.simple_tag
def get_pip_list():
    """
    Simple template tag function that returns all packages and version installed via Pip.
    """
    installed_packages_list = []
    installed_packages = list(pkg_resources.working_set)
    for package in installed_packages:
        installed_packages_list.append(str(package.project_name) + " @ " + str(package.parsed_version))
    return installed_packages_list

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