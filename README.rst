===============================
{{ cookiecutter.project_name }}
===============================

This repository defines a *UfoTest Plugin*. UfoTest is an application which was developed for the continuous testing
of various scientific camera systems at the `Institute of Data Processing (IPE) <https://www.ipe.kit.edu/>`_ of the
`Karlsruhe Institute of Technology (KIT) <https://www.kit.edu/>`_. By implementing a plugin management system and
exposing various action and filter hooks within it's core routines, UfoTest allows functionality to be added or
modified by third party code such as this plugin.

{{ cookiecutter.short_description }}

Installation
============

UfoTest plugins are installed by placing their source code folder into the special ``plugins`` folder of a local
UfoTest installation. This is best done by cloning the repository using git:

.. code-block:: console

    cd ~/.ufotest/plugins
    git clone {{ cookiecutter.repo_url }}

With each start of an UfoTest runtime all plugins within this folder are automatically discovered and the ``main.py``
files contained within each plugin folder is imported. Within these main files, it is important to register all the
necessary callbacks to the corresponding hooks.

If the plugin requires additional dependencies for its operation, these can be installed from the ``requirements.txt``
file:

.. code-block:: console

    pip3 install -r {{ cookiecutter.project_slug }}/requirements.txt

Usage
=====

! Insert your own usage description !

Testing
=======