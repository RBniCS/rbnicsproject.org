Installation
============
.. meta::
    :description lang=en:
        RBniCS requires FEniCS, numpy and scipy. Additional requirements are automatically handled during the setup.
        You can run RBniCS online on Google Colab and ARGOS. A docker image is available on DockerHub.

Prerequisites
-------------

**RBniCS** requires:

- **FEniCS** (>= 2018.1.0, python 3), with PETSc, SLEPc, petsc4py and slepc4py for computations during the offline stage;
- **numpy** and **scipy** for computations during the online stage.

Additional requirements are automatically handled during the setup.

Installation and usage
----------------------

From source
~~~~~~~~~~~
Simply clone the **RBniCS** public repository:

.. code-block:: console

    git clone https://github.com/RBniCS/RBniCS.git

and install the package by typing

.. code-block:: console

    cd RBniCS
    python3 -m pip install .

RBniCS on Google Colab
~~~~~~~~~~~~~~~~~~~~~~

You can run **RBniCS** online on `Google Colab <https://colab.research.google.com/>`__ by running our Jupyter notebooks interactively in any web browser without any required installation. See our :ref:`tutorials` page for more information.

RBniCS on ARGOS
~~~~~~~~~~~~~~~

You can run **RBniCS** online on `ARGOS <https://argos-edu.sissa.it/>`__, the Advanced Reduced Groupware Online Simulation platform, by running standalone apps interactively in any web browser without any required installation.
See our :ref:`tutorials` page for more information.

RBniCS docker image
~~~~~~~~~~~~~~~~~~~

If you want to try **RBniCS** out but do not have **FEniCS** already installed, you can `pull our docker image from DockerHub <https://hub.docker.com/r/rbnics/rbnics/>`__. All required dependencies are already installed. **RBniCS** tutorials and tests are located at :code:`/root/RBniCS`
