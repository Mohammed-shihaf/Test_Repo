from __future__ import print_function
"""Runtime configuration for Control Flow Testing / Statement Coverage."""
LANGUAGE = 'python'
RUNTIME_VERSION = '3.12'
PYTHON_VERSION = '3.12'
BRANCH_TYPE = 'CC'
BRANCH_VARIANT = 'CC'
TARGET_TECHNIQUE = 'ST'
TARGET_METRIC_ABBREV = 'TCG'
TARGET_METRIC_NAME = 'Test Case Granularity'
TESTING_TYPE = 'Control Flow Testing'
TECHNIQUE = 'Statement Coverage'
METRIC_TOOL_MAP = {
    'test_case_granularity': {'classification': 'Unit Testing Support', 'metric': 'Test Case Granularity', 'tool': 'Coverage.py'},
    'unreachable_logic_identification': {'classification': 'Dead Code Detection', 'metric': 'Unreachable Logic Identification', 'tool': 'Coverage.py'},
    'coverage_gap_analysis': {'classification': 'Test Completeness Evaluation', 'metric': 'Coverage Gap Analysis', 'tool': 'Coverage.py'},
    'surface_level_correctness': {'classification': 'Basic Logic Validation', 'metric': 'Surface-Level Correctness', 'tool': 'Coverage.py'},
    'statement_coverage': {'classification': 'Code Execution Verification', 'metric': 'Statement Coverage %', 'tool': 'Coverage.py'},
}
