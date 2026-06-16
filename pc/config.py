from __future__ import print_function
"""Runtime configuration for Control Flow Testing / Path Coverage."""
LANGUAGE = 'python'
PYTHON_VERSION = '2.6'
BRANCH_TYPE = 'BugFX'
BRANCH_VARIANT = 'BugFX'
TARGET_TECHNIQUE = 'PC'
TARGET_METRIC_ABBREV = 'AQE'
TARGET_METRIC_NAME = 'Automated Quality Enforcement'
TESTING_TYPE = 'Control Flow Testing'
TECHNIQUE = 'Path Coverage'
METRIC_TOOL_MAP = {
    'path_execution_tracking': {'classification': 'Path Execution Tracking', 'metric': 'Path Execution Tracking', 'tool': 'Coverage.py'},
    'full_logic_validation': {'classification': 'Complete Coverage Path Verification', 'metric': 'Full Logic Validation', 'tool': 'Coverage.py'},
    'gap_identification': {'classification': 'Partial Path Coverage Detection', 'metric': 'Gap Identification', 'tool': 'Coverage.py'},
    'deep_logic_probing': {'classification': 'Nested Condition Path Testing', 'metric': 'Deep Logic Probing', 'tool': 'Coverage.py'},
    'iterative_route_analysis': {'classification': 'Loop Path Detection', 'metric': 'Iterative Route Analysis', 'tool': 'Coverage.py'},
    'ghost_code_discovery': {'classification': 'Unreachable Path Detection', 'metric': 'Ghost Code Discovery', 'tool': 'Coverage.py'},
    'error_flow_verification': {'classification': 'Exception Path Handling', 'metric': 'Error Flow Verification', 'tool': 'Coverage.py'},
    'cross_component_mapping': {'classification': 'Multi-Function Path Tracking', 'metric': 'Cross-Component Mapping', 'tool': 'Coverage.py'},
    'automated_quality_enforcement': {'classification': 'CI/CD Integration Test', 'metric': 'Automated Quality Enforcement', 'tool': 'Coverage.py'},
    'path_coverage': {'classification': 'Path Detection Testing', 'metric': 'Path Coverage %', 'tool': 'Coverage.py'},
}
