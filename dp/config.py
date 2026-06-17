from __future__ import print_function
"""Runtime configuration for Development Process Analysis / Code Churn."""
LANGUAGE = 'python'
PYTHON_VERSION = '2.6'
BRANCH_TYPE = 'TCC'
BRANCH_VARIANT = 'TCC'
TARGET_TECHNIQUE = 'DP'
TARGET_METRIC_ABBREV = 'CCS'
TARGET_METRIC_NAME = 'Code Churn Score'
TESTING_TYPE = 'Development Process Analysis'
TECHNIQUE = 'Code Churn'
METRIC_TOOL_MAP = {
    'code_churn_score': {'classification': 'Risk-Based Testing Prioritization', 'metric': 'Code Churn Score', 'tool': 'pydriller'},
    'impact_driven_verification': {'classification': 'Regression Testing Focus', 'metric': 'Impact-Driven Verification', 'tool': 'pydriller'},
    'fault_probability_modeling': {'classification': 'Defect Prediction', 'metric': 'Fault Probability Modeling', 'tool': 'pydriller'},
    'validation_suite_updates': {'classification': 'Test Case Maintenance Identification', 'metric': 'Validation Suite Updates', 'tool': 'pydriller'},
    'side_effect_mapping': {'classification': 'Change Impact Analysis', 'metric': 'Side Effect Mapping', 'tool': 'pydriller'},
}
