from __future__ import print_function
"""Runtime configuration for Control Flow Testing / Branch Coverage."""
LANGUAGE = 'python'
PYTHON_VERSION = '2.6'
BRANCH_TYPE = 'CC'
BRANCH_VARIANT = 'CC'
TARGET_TECHNIQUE = 'BR'
TARGET_METRIC_ABBREV = 'SIM'
TARGET_METRIC_NAME = 'Sequence Integrity Mapping'
TESTING_TYPE = 'Control Flow Testing'
TECHNIQUE = 'Branch Coverage'
METRIC_TOOL_MAP = {
    'boolean_accuracy_check': {'classification': 'Conditional Logic Testing', 'metric': 'Boolean Accuracy Check', 'tool': 'Coverage.py'},
    'sequence_integrity_mapping': {'classification': 'Control Flow Validation', 'metric': 'Sequence Integrity Mapping', 'tool': 'Coverage.py'},
    'iteration_boundary_verification': {'classification': 'Loop Condition Testing', 'metric': 'Iteration Boundary Verification', 'tool': 'Coverage.py'},
    'boundary_failure_identification': {'classification': 'Edge Case Detection', 'metric': 'Boundary Failure Identification', 'tool': 'Coverage.py'},
    'branch_misdirection_discovery': {'classification': 'Logic Error Detection', 'metric': 'Branch Misdirection Discovery', 'tool': 'Coverage.py'},
    'decision_coverage_gap_analysis': {'classification': 'Test Case Completeness', 'metric': 'Decision Coverage Gap Analysis', 'tool': 'Coverage.py'},
    'branch_coverage': {'classification': 'Decision Outcome Verification', 'metric': 'Branch Coverage %', 'tool': 'Coverage.py'},
}
