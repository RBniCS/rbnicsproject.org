tutorials = {
    "01": {
        "title": "Thermal block problem",
        "description": "Reduced basis method for (scalar) elliptic problems",
        "cases": {
            "-": {
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/01_thermal_block/tutorial_thermal_block.ipynb",
                "notebook": "https://colab.research.google.com/drive/1YSugKATXS68J62bsi0eoil-KpjfocKoH",
                "app": "https://argos.sissa.it/tutorials/thermal_block",
            }
        },
    },
    "02": {
        "title": "Elastic block problem",
        "description": "POD-Galerkin method for (vector) elliptic problems",
        "cases": {
            "-": {
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/02_elastic_block/tutorial_elastic_block.ipynb",
                "notebook": "https://colab.research.google.com/drive/1jXAYbSi-6PkhxLKv_GdZ2JS99RHdeHbq",
                "app": "https://argos.sissa.it/tutorials/elastic_block",
            }
        },
    },
    "03": {
        "title": "Geometrical parametrization of a hole",
        "description": "Automatic pull back of problems with affine geometric parametrization",
        "cases": {
            "-": {
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/03_hole/tutorial_hole.ipynb",
                "notebook": "https://colab.research.google.com/drive/1aDaxo8o_ceDkCOGrJQfTip__ao9tTIgB",
                "app": "https://argos.sissa.it/tutorials/hole",
            }
        },
    },
    "04": {
        "title": "Graetz problem",
        "description": "Stability factor estimation by the successive constraint method. Sample problem with non-homogeneous boundary conditions.",
        "cases": {
            "1": {
                "description": "Case 1: with parameter-independent boundary conditions",
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/04_graetz/tutorial_graetz_1.ipynb",
                "notebook": "https://colab.research.google.com/drive/1awX5VNrwxhkmmyEgrgu5gn_jhxYzUL7l",
                "app": "https://argos.sissa.it/tutorials/graetz",
            },
            "2": {
                "description": "Case 2: with parametrized boundary conditions",
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/04_graetz/tutorial_graetz_2.ipynb",
                "notebook": "",
                "app": "",
            }
        },
    },
    "05": {
        "title": "Empirical Interpolation Methods for non-affine elliptic problems",
        "description": "Reduced basis method for non-affine problems by Empirical Interpolation Method, Discrete Empirical Interpolation Method and Inefficient Online Projection",
        "cases": {
            "eim": {
                "description": "EIM",
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/05_gaussian/tutorial_gaussian_eim.ipynb",
                "notebook": "https://colab.research.google.com/drive/1vX2IGpHE1nvpNVX4glFLM1ohoFjS9Ysv",
                "app": "https://argos.sissa.it/tutorials/gaussian",
            },
            "deim": {
                "description": "DEIM",
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/05_gaussian/tutorial_gaussian_deim.ipynb",
                "notebook": "",
                "app": "",
            },
            "inefficient": {
                "description": "Inefficient",
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/05_gaussian/tutorial_gaussian_exact.ipynb",
                "notebook": "",
                "app": "",
            },
        },
    },
    "06": {
        "title": "Unsteady thermal block problem",
        "description": "Reduced basis method for (scalar) elliptic problems",
        "cases": {
            "1_rb": {
                "description": "Case 1-RB: homogeneous boundary and initial conditions, reduction with reduced basis method",
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/06_thermal_block_unsteady/tutorial_thermal_block_unsteady_1_rb.ipynb",
                "notebook": "",
                "app": "",
            },
            "1_pod": {
                "description": "Case 1-POD: homogeneous boundary and initial conditions, reduction with POD-Galerkin method",
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/06_thermal_block_unsteady/tutorial_thermal_block_unsteady_1_pod.ipynb",
                "notebook": "",
                "app": "",
            },
            "2_rb": {
                "description": "Case 2-RB: homogeneous boundary conditions, non-homogeneous initial conditions, reduction with reduced basis method",
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/06_thermal_block_unsteady/tutorial_thermal_block_unsteady_2_rb.py",
                "notebook": "",
                "app": "",
            },
            "2_pod": {
                "description": "Case 2-POD: homogeneous boundary conditions, non-homogeneous initial conditions, reduction with POD-Galerkin method",
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/06_thermal_block_unsteady/tutorial_thermal_block_unsteady_2_pod.py",
                "notebook": "",
                "app": "",
            },
            "3_rb": {
                "description": "Case 3-RB: non-homogeneous boundary and initial conditions, reduction with reduced basis method",
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/06_thermal_block_unsteady/tutorial_thermal_block_unsteady_3_rb.py",
                "notebook": "",
                "app": "",
            },
            "3_pod": {
                "description": "Case 3-POD: non-homogeneous boundary and initial conditions, reduction with POD-Galerkin method",
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/06_thermal_block_unsteady/tutorial_thermal_block_unsteady_3_pod.py",
                "notebook": "",
                "app": "",
            },
        },
    },
    "07": {
        "title": "Nonlinear elliptic problem",
        "description": "Empirical interpolation methods for nonlinear elliptic problems",
        "cases": {
            "eim": {
                "description": "EIM",
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/07_nonlinear_elliptic/tutorial_nonlinear_elliptic_eim.ipynb",
                "notebook": "",
                "app": "",
            },
            "deim": {
                "description": "DEIM",
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/07_nonlinear_elliptic/tutorial_nonlinear_elliptic_deim.ipynb",
                "notebook": "",
                "app": "",
            },
            "inefficient": {
                "description": "Inefficient",
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/07_nonlinear_elliptic/tutorial_nonlinear_elliptic_exact.ipynb",
                "notebook": "",
                "app": "",
            },
        },
    },
    "08": {
        "title": "Nonlinear parabolic problem",
        "description": "Empirical interpolation methods for nonlinear parabolic problems",
        "cases": {
            "-": {
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/08_nonlinear_parabolic/tutorial_nonlinear_parabolic_exact.ipynb",
                "notebook": "",
                "app": "",
            }
        },
    },
    "09": {
        "title": "Advection dominated problems",
        "description": "Reduced order models for advection dominated problems",
        "cases": {
            "1_rb": {
                "description": "Case 1-RB",
                "file": "https://github.com/RBniCS/RBniCS/blob/master/tutorials/09_advection_dominated/tutorial_advection_dominated_1_rb.py",
                "notebook": "",
                "app": "",
            },
            "1_pod": {
                "description": "Case 1-POD",
                "file": "https://github.com/RBniCS/RBniCS/blob/master/tutorials/09_advection_dominated/tutorial_advection_dominated_1_pod.py",
                "notebook": "",
                "app": "",
            },
            "1_rb_rectification": {
                "description": "Case 1-RB with rectification",
                "file": "https://github.com/RBniCS/RBniCS/blob/master/tutorials/09_advection_dominated/tutorial_advection_dominated_1_rb_rectification.py",
                "notebook": "",
                "app": "",
            },
            "1_rb_vanishing_viscosity": {
                "description": "Case 1-RB with vanishing viscosity",
                "file": "https://github.com/RBniCS/RBniCS/blob/master/tutorials/09_advection_dominated/tutorial_advection_dominated_1_rb_vanishing_viscosity.py",
                "notebook": "",
                "app": "",
            },
            "2_rb": {
                "description": "Case 2-RB",
                "file": "https://github.com/RBniCS/RBniCS/blob/master/tutorials/09_advection_dominated/tutorial_advection_dominated_2_rb.py",
                "notebook": "",
                "app": "",
            },
            "2_pod": {
                "description": "Case 2-POD",
                "file": "https://github.com/RBniCS/RBniCS/blob/master/tutorials/09_advection_dominated/tutorial_advection_dominated_2_pod.py",
                "notebook": "",
                "app": "",
            },
            "3_rb": {
                "description": "Case 3-RB",
                "file": "https://github.com/RBniCS/RBniCS/blob/master/tutorials/09_advection_dominated/tutorial_advection_dominated_3_rb.py",
                "notebook": "",
                "app": "",
            },
            "3_pod": {
                "description": "Case 3-POD",
                "file": "https://github.com/RBniCS/RBniCS/blob/master/tutorials/09_advection_dominated/tutorial_advection_dominated_3_pod.py",
                "notebook": "",
                "app": "",
            },
        },
    },
    "10": {
        "title": "Uncertainty quantification problems",
        "description": "Weighted reduced order methods for uncertainty quantification problems",
        "cases": {
            "1_rb": {
                "description": "Case 1-RB",
                "file": "https://github.com/RBniCS/RBniCS/blob/master/tutorials/10_weighted_uq/tutorial_weighted_uq_1_rb.py",
                "notebook": "",
                "app": "",
            },
            "1_pod": {
                "description": "Case 1-POD",
                "file": "https://github.com/RBniCS/RBniCS/blob/master/tutorials/10_weighted_uq/tutorial_weighted_uq_1_pod.py",
                "notebook": "",
                "app": "",
            },
         },
    },
    "11": {
        "title": "Quasi geostrophic equations",
        "description": "POD-Galerkin methods for quasi geostrophic equations, as an example on how to customize and extend RBniCS beyond the set of problems provided in the core of the library",
        "cases": {
            "-": {
                "file": "https://github.com/RBniCS/RBniCS/blob/master/tutorials/11_quasi_geostrophic/tutorial_quasi_geostrophic.py",
                "notebook": "",
                "app": "",
            }
        },
    },
    "12": {
        "title": "Stokes problems",
        "description": "Reduced basis and POD-Galerkin methods for Stokes problems",
        "cases": {
            "1_rb": {
                "description": "Case 1-RB",
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/12_stokes/tutorial_stokes_1_rb.ipynb",
                "notebook": "",
                "app": "",
            },
            "1_pod": {
                "description": "Case 1-POD",
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/12_stokes/tutorial_stokes_1_pod.ipynb",
                "notebook": "https://colab.research.google.com/drive/1m7L8BNWZkF0Z9jCfVI714LnQ37D3U3e5",
                "app": "https://argos.sissa.it/tutorials/stokes",
            },
            "2_rb": {
                "description": "Case 2-RB",
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/12_stokes/tutorial_stokes_2_rb.ipynb",
                "notebook": "",
                "app": "",
            },
            "2_pod": {
                "description": "Case 2-POD",
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/12_stokes/tutorial_stokes_2_pod.ipynb",
                "notebook": "",
                "app": "",
            },
        },
    },
    "13": {
        "title": "Elliptic optimal control problems",
        "description": "Reduced basis and POD-Galerkin methods for optimal control problems governed by elliptic equations",
        "cases": {
            "1_rb": {
                "description": "Case 1-RB",
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/13_elliptic_optimal_control/tutorial_elliptic_optimal_control_1_rb.ipynb",
                "notebook": "",
                "app": "",
            },
            "1_pod": {
                "description": "Case 1-POD",
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/13_elliptic_optimal_control/tutorial_elliptic_optimal_control_1_pod.ipynb",
                "notebook": "https://colab.research.google.com/drive/1pQwhIr9HrQqeH1PKisYO2k1OTgT7kjE3",
                "app": "https://argos.sissa.it/tutorials/elliptic_optimal_control",
            },
            "2_rb": {
                "description": "Case 2-RB",
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/13_elliptic_optimal_control/tutorial_elliptic_optimal_control_2_rb.ipynb",
                "notebook": "",
                "app": "",
            },
            "2_pod": {
                "description": "Case 2-POD",
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/13_elliptic_optimal_control/tutorial_elliptic_optimal_control_2_pod.ipynb",
                "notebook": "https://colab.research.google.com/drive/1zfhjrHTDlE_ASwtAwecobFO-mXSNYXCO",
                "app": "",
            },
        },
    },
    "14": {
        "title": "Stokes optimal control problems",
        "description": "Reduced basis and POD-Galerkin methods for optimal control problems governed by Stokes equations",
        "cases": {
            "-": {
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/14_stokes_optimal_control/tutorial_stokes_optimal_control_1.ipynb",
                "notebook": "https://colab.research.google.com/drive/1DwpRXTIJjXkNzJ-ASphXSlE2E7MYp_cJ",
                "app": "https://argos.sissa.it/tutorials/stokes_optimal_control",
            }
        },
    },
    "15": {
        "title": "Optimal control problems governed by the quasi geostrophic equations",
        "description": "POD-Galerkin methods for optimal control problems governed by quasi geostrophic equations",
        "cases": {
            "-": {
                "file": "https://github.com/RBniCS/RBniCS/blob/master/tutorials/15_quasi_geostrophic_optimal_control/tutorial_quasi_geostrophic_optimal_control.py",
                "notebook": "",
                "app": "",
            }
        },
    },
    "16": {
        "title": "Coupled problems",
        "description": "One-way coupling between a fluid dynamics problem based on Stokes and an elliptic equation (e.g., temperature, concentration)",
        "cases": {
            "eim": {
                "description": "EIM",
                "file": "https://github.com/RBniCS/RBniCS/blob/master/tutorials/16_stokes_coupled/tutorial_stokes_coupled_eim.py",
                "notebook": "",
                "app": "",
            },
            "deim": {
                "description": "DEIM",
                "file": "https://github.com/RBniCS/RBniCS/blob/master/tutorials/16_stokes_coupled/tutorial_stokes_coupled_deim.py",
                "notebook": "",
                "app": "",
            },
            "inefficient": {
                "description": "Inefficient",
                "file": "https://github.com/RBniCS/RBniCS/blob/master/tutorials/16_stokes_coupled/tutorial_stokes_coupled_exact.py",
                "notebook": "",
                "app": "",
            },
        },
    },
    "17": {
        "title": "Navier-Stokes problems",
        "description": "One-way coupling between a fluid dynamics problem based on Stokes and an elliptic equation (e.g., temperature, concentration)",
        "cases": {
            "1_deim": {
                "description": "Case 1-DEIM",
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/17_navier_stokes/tutorial_navier_stokes_deim_1.ipynb",
                "notebook": "https://colab.research.google.com/drive/1AVrmgfSOSIdCyttN8wkbwOSDuqMVE0SI",
                "app": "",
            },
            "1_inefficient": {
                "description": "Case 1-Inefficient",
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/17_navier_stokes/tutorial_navier_stokes_exact_1.ipynb",
                "notebook": "",
                "app": "https://argos.sissa.it/tutorials/navier_stokes",
            },
            "2_inefficient": {
                "description": "Case 2-Inefficient",
                "file": "https://github.com/RBniCS/RBniCS/blob/jupyter/tutorials/17_navier_stokes/tutorial_navier_stokes_exact_2.ipynb",
                "notebook": "",
                "app": "",
            },
        },
    },
    "18": {
        "title": "Unsteady Stokes problem",
        "description": "POD-Galerkin methods for unsteady Stokes problems",
        "cases": {
            "-": {
                "file": "https://github.com/RBniCS/RBniCS/blob/master/tutorials/18_stokes_unsteady/tutorial_stokes_unsteady_1.py",
                "notebook": "",
                "app": "",
            }
        },
    },
    "19": {
        "title": "Unsteady Navier-Stokes problem",
        "description": "POD-Galerkin methods for unsteady Navier-Stokes problems",
        "cases": {
            "-": {
                "file": "https://github.com/RBniCS/RBniCS/blob/master/tutorials/19_navier_stokes_unsteady/tutorial_navier_stokes_unsteady_exact_1.py",
                "notebook": "",
                "app": "",
            }
        },
    },
}
"""
    "": {
        "title": "",
        "description": "",
        "cases": {
            "-": {
                "description": "", # only required for tutorials with more than one case
                "file": "",
                "notebook": "",
                "app": "",
            }
        },
    },
"""

categories = {
    "Introductory tutorials": ["01", "02", "03", "04", "05", "06"],
    "Nonlinear problems": ["07", "08", "16", "17", "19"],
    "Computational fluid dynamics": ["12", "14", "16", "17", "18", "19"],
    "Optimal control problems": ["13", "14", "15"],
    "Extending RBniCS": ["09", "10", "11", "15"],
}
