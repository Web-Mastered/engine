from django import template

from engine import VERSION
import pkg_resources

register = template.Library()

@register.simple_tag
def get_engine_version():
    return VERSION

@register.simple_tag
def get_pip_requirements():
    installed_packages = pkg_resources.working_set
    installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
    for i in installed_packages])
    return installed_packages_list

@register.simple_tag
def get_pip_list():
    return [p.project_name + " @ " + str(p.parsed_version) for p in pkg_resources.working_set]

@register.simple_tag
def diagnostics_report():
    report = {
        "engine_version": get_engine_version(),
        "requirements_txt": get_pip_requirements(),
        "pip_list": get_pip_list(),
    }
    return report