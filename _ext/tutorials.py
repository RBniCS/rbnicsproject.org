tutorials = {
    "01": {
        "title": "Thermal block problem",
        "description": "Reduced basis method for (scalar) elliptic problems",
        "slug": "thermal_block",
        "cases": {
            "-": {
                "file": "tutorials/01_thermal_block/tutorial_thermal_block.ipynb",
                "app": "thermal_block",
            }
        },
        "main_case": "-",
    },
    "02": {
        "title": "Elastic block problem",
        "description": "POD-Galerkin method for (vector) elliptic problems",
        "slug": "elastic_block",
        "cases": {
            "-": {
                "file": "tutorials/02_elastic_block/tutorial_elastic_block.ipynb",
                "app": "elastic_block",
            }
        },
        "main_case": "-",
    },
    "03": {
        "title": "Geometrical parametrization of a hole",
        "description": "Automatic pull back of problems with affine geometric parametrization",
        "slug": "hole",
        "cases": {
            "-": {
                "file": "tutorials/03_hole/tutorial_hole.ipynb",
                "app": "hole",
            }
        },
        "main_case": "-",
    },
    "04": {
        "title": "Graetz problem",
        "description": "Stability factor estimation by the successive constraint method. Sample problem with non-homogeneous boundary conditions.",
        "slug": "graetz",
        "cases": {
            "1": {
                "description": "Case 1: with parameter-independent boundary conditions",
                "file": "tutorials/04_graetz/tutorial_graetz_1.ipynb",
                "app": "graetz",
            },
            "2": {
                "description": "Case 2: with parametrized boundary conditions",
                "file": "tutorials/04_graetz/tutorial_graetz_2.ipynb",
                "app": "",
            }
        },
        "main_case": "1",
    },
    "05": {
        "title": "Empirical Interpolation Methods for non-affine elliptic problems",
        "description": "Reduced basis method for non-affine problems by Empirical Interpolation Method, Discrete Empirical Interpolation Method and Inefficient Online Projection",
        "slug": "gaussian",
        "cases": {
            "eim": {
                "description": "EIM",
                "file": "tutorials/05_gaussian/tutorial_gaussian_eim.ipynb",
                "app": "gaussian",
            },
            "deim": {
                "description": "DEIM",
                "file": "tutorials/05_gaussian/tutorial_gaussian_deim.ipynb",
                "app": "",
            },
            "inefficient": {
                "description": "Inefficient",
                "file": "tutorials/05_gaussian/tutorial_gaussian_exact.ipynb",
                "app": "",
            },
        },
        "main_case": "eim",
    },
    "06": {
        "title": "Unsteady thermal block problem",
        "description": "Reduced basis and POD-Galerkin methods for (scalar) parabolic problems",
        "slug": "thermal_block_unsteady",
        "cases": {
            "1_rb": {
                "description": "Case 1-RB: homogeneous boundary and initial conditions, reduction with reduced basis method",
                "file": "tutorials/06_thermal_block_unsteady/tutorial_thermal_block_unsteady_1_rb.ipynb",
                "app": "",
            },
            "1_pod": {
                "description": "Case 1-POD: homogeneous boundary and initial conditions, reduction with POD-Galerkin method",
                "file": "tutorials/06_thermal_block_unsteady/tutorial_thermal_block_unsteady_1_pod.ipynb",
                "app": "thermal_block_unsteady",
            },
            "2_rb": {
                "description": "Case 2-RB: homogeneous boundary conditions, non-homogeneous initial conditions, reduction with reduced basis method",
                "file": "tutorials/06_thermal_block_unsteady/tutorial_thermal_block_unsteady_2_rb.py",
                "app": "",
            },
            "2_pod": {
                "description": "Case 2-POD: homogeneous boundary conditions, non-homogeneous initial conditions, reduction with POD-Galerkin method",
                "file": "tutorials/06_thermal_block_unsteady/tutorial_thermal_block_unsteady_2_pod.py",
                "app": "",
            },
            "3_rb": {
                "description": "Case 3-RB: non-homogeneous boundary and initial conditions, reduction with reduced basis method",
                "file": "tutorials/06_thermal_block_unsteady/tutorial_thermal_block_unsteady_3_rb.py",
                "app": "",
            },
            "3_pod": {
                "description": "Case 3-POD: non-homogeneous boundary and initial conditions, reduction with POD-Galerkin method",
                "file": "tutorials/06_thermal_block_unsteady/tutorial_thermal_block_unsteady_3_pod.py",
                "app": "",
            },
        },
        "main_case": "1_pod",
    },
    "07": {
        "title": "Nonlinear elliptic problem",
        "description": "Empirical interpolation methods for nonlinear elliptic problems",
        "slug": "nonlinear_elliptic",
        "cases": {
            "eim": {
                "description": "EIM",
                "file": "tutorials/07_nonlinear_elliptic/tutorial_nonlinear_elliptic_eim.ipynb",
                "app": "nonlinear_elliptic",
            },
            "deim": {
                "description": "DEIM",
                "file": "tutorials/07_nonlinear_elliptic/tutorial_nonlinear_elliptic_deim.ipynb",
                "app": "",
            },
            "inefficient": {
                "description": "Inefficient",
                "file": "tutorials/07_nonlinear_elliptic/tutorial_nonlinear_elliptic_exact.ipynb",
                "app": "",
            },
        },
        "main_case": "eim",
    },
    "08": {
        "title": "Nonlinear parabolic problem",
        "description": "Empirical interpolation methods for nonlinear parabolic problems",
        "slug": "nonlinear_parabolic",
        "cases": {
            "-": {
                "file": "tutorials/08_nonlinear_parabolic/tutorial_nonlinear_parabolic_exact.ipynb",
                "app": "nonlinear_parabolic",
            }
        },
        "main_case": "-",
    },
    "09": {
        "title": "Advection dominated problems",
        "description": "Reduced order models for advection dominated problems",
        "slug": "advection_dominated",
        "cases": {
            "1_rb": {
                "description": "Case 1-RB",
                "file": "tutorials/09_advection_dominated/tutorial_advection_dominated_1_rb.ipynb",
                "app": "",
            },
            "1_pod": {
                "description": "Case 1-POD",
                "file": "tutorials/09_advection_dominated/tutorial_advection_dominated_1_pod.ipynb",
                "app": "advection_dominated",
            },
            "1_rb_rectification": {
                "description": "Case 1-RB with rectification",
                "file": "tutorials/09_advection_dominated/tutorial_advection_dominated_1_rb_rectification.py",
                "app": "",
            },
            "1_rb_vanishing_viscosity": {
                "description": "Case 1-RB with vanishing viscosity",
                "file": "tutorials/09_advection_dominated/tutorial_advection_dominated_1_rb_vanishing_viscosity.py",
                "app": "",
            },
            "2_rb": {
                "description": "Case 2-RB",
                "file": "tutorials/09_advection_dominated/tutorial_advection_dominated_2_rb.py",
                "app": "",
            },
            "2_pod": {
                "description": "Case 2-POD",
                "file": "tutorials/09_advection_dominated/tutorial_advection_dominated_2_pod.py",
                "app": "",
            },
            "3_rb": {
                "description": "Case 3-RB",
                "file": "tutorials/09_advection_dominated/tutorial_advection_dominated_3_rb.py",
                "app": "",
            },
            "3_pod": {
                "description": "Case 3-POD",
                "file": "tutorials/09_advection_dominated/tutorial_advection_dominated_3_pod.py",
                "app": "",
            },
        },
        "main_case": "1_pod",
    },
    "10": {
        "title": "Uncertainty quantification problems",
        "description": "Weighted reduced order methods for uncertainty quantification problems",
        "slug": "weighted_uq",
        "cases": {
            "1_rb": {
                "description": "Case 1-RB",
                "file": "tutorials/10_weighted_uq/tutorial_weighted_uq_1_rb.py",
                "app": "",
            },
            "1_pod": {
                "description": "Case 1-POD",
                "file": "tutorials/10_weighted_uq/tutorial_weighted_uq_1_pod.py",
                "app": "weighted_uq",
            },
         },
        "main_case": "1_pod",
    },
    "11": {
        "title": "Quasi geostrophic equations",
        "description": "POD-Galerkin methods for quasi geostrophic equations, as an example on how to customize and extend RBniCS beyond the set of problems provided in the core of the library",
        "slug": "quasi_geostrophic",
        "cases": {
            "-": {
                "file": "tutorials/11_quasi_geostrophic/tutorial_quasi_geostrophic.py",
                "app": "quasi_geostrophic",
            }
        },
        "main_case": "-",
    },
    "12": {
        "title": "Stokes problems",
        "description": "Reduced basis and POD-Galerkin methods for Stokes problems",
        "slug": "stokes",
        "cases": {
            "1_rb": {
                "description": "Case 1-RB",
                "file": "tutorials/12_stokes/tutorial_stokes_1_rb.ipynb",
                "app": "",
            },
            "1_pod": {
                "description": "Case 1-POD",
                "file": "tutorials/12_stokes/tutorial_stokes_1_pod.ipynb",
                "app": "stokes",
            },
            "2_rb": {
                "description": "Case 2-RB",
                "file": "tutorials/12_stokes/tutorial_stokes_2_rb.ipynb",
                "app": "",
            },
            "2_pod": {
                "description": "Case 2-POD",
                "file": "tutorials/12_stokes/tutorial_stokes_2_pod.ipynb",
                "app": "",
            },
        },
        "main_case": "1_pod",
    },
    "13": {
        "title": "Elliptic optimal control problems",
        "description": "Reduced basis and POD-Galerkin methods for optimal control problems governed by elliptic equations",
        "slug": "elliptic_optimal_control",
        "cases": {
            "1_rb": {
                "description": "Case 1-RB",
                "file": "tutorials/13_elliptic_optimal_control/tutorial_elliptic_optimal_control_1_rb.ipynb",
                "app": "",
            },
            "1_pod": {
                "description": "Case 1-POD",
                "file": "tutorials/13_elliptic_optimal_control/tutorial_elliptic_optimal_control_1_pod.ipynb",
                "app": "elliptic_optimal_control",
            },
            "2_rb": {
                "description": "Case 2-RB",
                "file": "tutorials/13_elliptic_optimal_control/tutorial_elliptic_optimal_control_2_rb.ipynb",
                "app": "",
            },
            "2_pod": {
                "description": "Case 2-POD",
                "file": "tutorials/13_elliptic_optimal_control/tutorial_elliptic_optimal_control_2_pod.ipynb",
                "app": "graetz_conduction_convection",
            },
        },
        "main_case": "1_pod",
    },
    "14": {
        "title": "Stokes optimal control problems",
        "description": "Reduced basis and POD-Galerkin methods for optimal control problems governed by Stokes equations",
        "slug": "stokes_optimal_control",
        "cases": {
            "-": {
                "file": "tutorials/14_stokes_optimal_control/tutorial_stokes_optimal_control_1.ipynb",
                "app": "stokes_optimal_control",
            }
        },
        "main_case": "-",
    },
    "15": {
        "title": "Optimal control problems governed by the quasi geostrophic equations",
        "description": "POD-Galerkin methods for optimal control problems governed by quasi geostrophic equations",
        "slug": "quasi_geostrophic_optimal_control",
        "cases": {
            "-": {
                "file": "tutorials/15_quasi_geostrophic_optimal_control/tutorial_quasi_geostrophic_optimal_control.py",
                "app": "",
            }
        },
        "main_case": "-",
    },
    "16": {
        "title": "Coupled problems",
        "description": "One-way coupling between a fluid dynamics problem based on Stokes and an elliptic equation (e.g., temperature, concentration)",
        "slug": "stokes_coupled",
        "cases": {
            "eim": {
                "description": "EIM",
                "file": "tutorials/16_stokes_coupled/tutorial_stokes_coupled_eim.py",
                "app": "",
            },
            "deim": {
                "description": "DEIM",
                "file": "tutorials/16_stokes_coupled/tutorial_stokes_coupled_deim.py",
                "app": "",
            },
            "inefficient": {
                "description": "Inefficient",
                "file": "tutorials/16_stokes_coupled/tutorial_stokes_coupled_exact.py",
                "app": "",
            },
        },
        "main_case": "eim",
    },
    "17": {
        "title": "Navier-Stokes problems",
        "description": "Discrete Empirical Interpolation Method for steady Navier-Stokes problems",
        "slug": "navier_stokes",
        "cases": {
            "1_deim": {
                "description": "Case 1-DEIM",
                "file": "tutorials/17_navier_stokes/tutorial_navier_stokes_1_deim.ipynb",
                "app": "",
            },
            "1_inefficient": {
                "description": "Case 1-Inefficient",
                "file": "tutorials/17_navier_stokes/tutorial_navier_stokes_1_exact.ipynb",
                "app": "navier_stokes",
            },
            "2_inefficient": {
                "description": "Case 2-Inefficient",
                "file": "tutorials/17_navier_stokes/tutorial_navier_stokes_2_exact.ipynb",
                "app": "",
            },
        },
        "main_case": "1_deim",
    },
    "18": {
        "title": "Unsteady Stokes problem",
        "description": "POD-Galerkin methods for unsteady Stokes problems",
        "slug": "stokes_unsteady",
        "cases": {
            "-": {
                "file": "tutorials/18_stokes_unsteady/tutorial_stokes_unsteady_1.py",
                "app": "",
            }
        },
        "main_case": "-",
    },
    "19": {
        "title": "Unsteady Navier-Stokes problem",
        "description": "POD-Galerkin methods for unsteady Navier-Stokes problems",
        "slug": "navier_stokes_unsteady",
        "cases": {
            "-": {
                "file": "tutorials/19_navier_stokes_unsteady/tutorial_navier_stokes_unsteady_exact_1.py",
                "app": "",
            }
        },
        "main_case": "-",
    },
    "20": {
        "title": "Coanda Effect",
        "description": "POD-Galerkin methods for bifurcation problems",
        "slug": "coanda_effect",
        "cases": {
            "-": {
                "file": "tutorials/20_coanda_effect/tutorial_coanda_effect.ipynb",
                "app": "coanda_effect",
            }
        },
        "main_case": "-",
    },
    "21": {
        "title": "Thermal subfin problem",
        "description": "Steady-state heat transfer problem through a fin",
        "slug": "thermal_subfin",
        "cases": {
            "-": {
                "file": "tutorials/21_thermal_subfin/tutorial_thermal_subfin.ipynb",
                "app": "thermal_subfin",
            }
        },
        "main_case": "-",
    },
    "22": {
        "title": "Elastic contact problem",
        "description": "Idealized contact problem in linear elasticity with friction",
        "slug": "idealized_contact",
        "cases": {
            "-": {
                "file": "tutorials/22_elastic_contact/tutorial_elastic_contact.ipynb",
                "app": "idealized_contact",
            }
        },
        "main_case": "-",
    },
    "23": {
        "title": "Beam bridge problem",
        "description": "Geometrical parametrization applied to the physical phenomena of linear deformation of a bridge.",
        "slug": "bridge",
        "cases": {
            "-": {
                "file": "tutorials/23_beam_bridge/tutorial_beam_bridge.ipynb",
                "app": "bridge",
            }
        },
        "main_case": "-",
    },
}
"""
    "": {
        "title": "",
        "description": "",
        "slug": "",
        "cases": {
            "-": {
                "description": "", # only required for tutorials with more than one case
                "file": "",
                "app": "",
            }
        },
        "main_case": "",
    },
"""

categories = {
    "Introductory tutorials": ["01", "02", "03", "04", "05", "06"],
    "Nonlinear problems": ["07", "08", "16", "17", "19", "20"],
    "Computational fluid dynamics": ["12", "14", "16", "17", "18", "19"],
    "Computational mechanics": ["02", "21", "22", "23"],
    "Optimal control problems": ["13", "14", "15"],
    "Extending RBniCS": ["09", "10", "11", "15"],
}
