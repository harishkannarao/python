#   -*- coding: utf-8 -*-
import os
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin('python.pycharm')
use_plugin('python.install_dependencies')


name = "python"
version = "{0}".format(os.environ.get("BUILD_VERSION", "latest"))
default_task = ['clean', 'install_dependencies', 'analyze', 'publish']


@init
def set_properties(project):
    project.build_depends_on("mockito", "==1.2.2")
    project.build_depends_on('pyassert', "==0.4.2")
    project.depends_on('python-dateutil', '==2.7.4')

    project.set_property('coverage_break_build', False)
    project.set_property('flake8_break_build', True)
