RBniCS Project
==============
.. meta::
    :description lang=en:
        The RBniCS Project contains an implementation in FEniCS of several reduced order modelling techniques
        for parametrized problems. RBniCS is currently developed at Università Cattolica del Sacro Cuore by
        Dr. Francesco Ballarin in collaboration with Prof. Gianluigi Rozza's group at SISSA mathLab.

.. image:: _static/images/github-logo.png
    :target: https://github.com/RBniCS/RBniCS
    :height: 80px
    :width: 80px
    :alt: Go to repository on GitHub
.. image:: _static/images/email.png
    :target: mailto:info@rbnicsproject.org
    :height: 80px
    :width: 80px
    :alt: Contact us via email


Description
-----------

.. image:: _static/images/rbnics-logo-small.png
    :height: 150px
    :width: 150px
    :align: right
    :alt: RBniCS

The **RBniCS** Project contains an implementation in **FEniCS** of several reduced order modelling techniques (and, in particular, certified reduced basis method and Proper Orthogonal Decomposition-Galerkin methods) for parametrized problems. It is ideally suited for an introductory course on reduced basis methods and reduced order modelling, thanks to an object-oriented approach and an intuitive and versatile python interface. To this end, it has been employed in several doctoral courses on "Reduced Basis Methods for Computational Mechanics".

**RBniCS** can also be used as a basis for more advanced projects that would like to assess the capability of reduced order models in their existing **FEniCS**-based software, thanks to the availability of several reduced order methods (such as reduced basis and proper orthogonal decomposition) and algorithms (such as successive constraint method, empirical interpolation method) in the library.

Several tutorials are provided. This software is also a companion of the introductory reduced basis handbook:

    `J. S. Hesthaven, G. Rozza, B. Stamm. Certified Reduced Basis Methods for Parametrized Partial Differential Equations. SpringerBriefs in Mathematics. Springer International Publishing, 2015 <http://www.springer.com/us/book/9783319224695>`__

Authors and contributors
------------------------

**RBniCS** is currently developed and maintained at `Università Cattolica del Sacro Cuore <https://www.unicatt.it/>`__ by `Dr. Francesco Ballarin <https://www.francescoballarin.it>`__ in collaboration with `Prof. Gianluigi Rozza <https://people.sissa.it/~grozza/>`__'s group at `SISSA mathLab <http://mathlab.sissa.it/>`__.
We acknowledge all contributors listed in the `AUTHORS file <https://github.com/RBniCS/RBniCS/blob/master/AUTHORS>`__.

Timeline and funding
------------------------
.. list-table::
   :widths: 10 90

   * - 2015
     - Early development of **RBniCS** begins at `SISSA mathLab <http://mathlab.sissa.it/>`__.
   * - 2016-2021
     - Financial support of the `AROMA-CFD H2020 ERC CoG project <https://people.sissa.it/~grozza/aroma-cfd/>`__ (PI: `Prof. Gianluigi Rozza <https://people.sissa.it/~grozza/>`__, host: `SISSA mathLab <http://mathlab.sissa.it/>`__) for the consolidation of **RBniCS** development.
   * - 2020-2022
     - Financial support of the `NA-from-PDEs PRIN MIUR project  <https://people.sissa.it/~grozza/na-from-pdes/>`__ (PI: `Prof. Gianluigi Rozza <https://people.sissa.it/~grozza/>`__, unit: `SISSA mathLab <http://mathlab.sissa.it/>`__) for the continuation of **RBniCS** development.
   * - 2021
     - `Università Cattolica del Sacro Cuore <https://www.unicatt.it/>`__ joins the development. `SISSA mathLab <http://mathlab.sissa.it/>`__ and the `Università Cattolica del Sacro Cuore <https://www.unicatt.it/>`__ are now partner institutions in the development of **RBniCS**.


Learn more about RBniCS
-----------------------
.. toctree::
    :maxdepth: 1

    tutorials
    installing
    contributing
    citing
    publications

License
-------

Like all core **FEniCS** components, **RBniCS** is freely available under the GNU LGPL, version 3.
