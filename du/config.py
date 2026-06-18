from __future__ import print_function
"""Runtime configuration for Data Flow Testing / All Uses Coverage."""
LANGUAGE = 'python'
PYTHON_VERSION = '2.6'
BRANCH_TYPE = 'TCC'
BRANCH_VARIANT = 'TCC'
TARGET_TECHNIQUE = 'DU'
TARGET_METRIC_ABBREV = 'COVER'
TARGET_METRIC_NAME = 'All-Uses Coverage %'
TESTING_TYPE = 'Data Flow Testing'
TECHNIQUE = 'All Uses Coverage'
METRIC_TOOL_MAP = {
    'data_processing_validation': {'classification': 'Computational Use Detection (C-Use)', 'metric': 'Data Processing Validation', 'tool': 'coverage.py + beniget'},
    'logic_influence_assessment': {'classification': 'Predicate Use Detection (P-Use)', 'metric': 'Logic Influence Assessment', 'tool': 'coverage.py + beniget'},
    'path_correlation_mapping': {'classification': 'Definition-Use Pair Identification', 'metric': 'Path Correlation Mapping', 'tool': 'coverage.py + beniget'},
    'comprehensive_data_proofing': {'classification': 'All-Uses Coverage Verification', 'metric': 'Comprehensive Data Proofing', 'tool': 'coverage.py + beniget'},
    'data_flow_gap_analysis': {'classification': 'Partial Uses Coverage Detection', 'metric': 'Data Flow Gap Analysis', 'tool': 'coverage.py + beniget'},
    'ambiguity_resolution': {'classification': 'Multiple Definitions Handling', 'metric': 'Ambiguity Resolution', 'tool': 'coverage.py + beniget'},
    'inter_procedural_tracking': {'classification': 'Cross-Function Use Detection', 'metric': 'Inter-procedural Tracking', 'tool': 'coverage.py + beniget'},
    'ghost_use_identification': {'classification': 'Unreachable Use Detection', 'metric': 'Ghost Use Identification', 'tool': 'coverage.py + beniget'},
    'data_integrity_audit': {'classification': 'Coverage Reporting Validation', 'metric': 'Data Integrity Audit', 'tool': 'coverage.py + beniget'},
    'all_uses_coverage': {'classification': 'Variable Use Detection', 'metric': 'All-Uses Coverage %', 'tool': 'coverage.py + beniget'},
}
