from __future__ import print_function
METRIC_NAME = 'Sequence Integrity Mapping'
TOOL_PRIMARY = 'Coverage.py'

def sim_case_1(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 1 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 1
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_2(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 2 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 2
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_3(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 3 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 3
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_4(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 4 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 4
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_5(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 5 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 5
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_6(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 6 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 6
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_7(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 7 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 7
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_8(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 8 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 8
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_9(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 9 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 9
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_10(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 10 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 10
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_11(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 11 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 11
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_12(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 12 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 12
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_13(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 13 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 13
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_14(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 14 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 14
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_15(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 15 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 15
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_16(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 16 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 16
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_17(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 17 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 17
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_18(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 18 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 18
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_19(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 19 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 19
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_20(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 20 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 20
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_21(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 21 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 21
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_22(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 22 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 22
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_23(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 23 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 23
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_24(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 24 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 24
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_25(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 25 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 25
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_26(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 26 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 26
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_27(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 27 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 27
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_28(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 28 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 28
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_29(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 29 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 29
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_30(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 30 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 30
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_31(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 31 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 31
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_32(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 32 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 32
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_33(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 33 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 33
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_34(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 34 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 34
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_35(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 35 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 35
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_36(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 36 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 36
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

def sim_case_37(state, enabled, retry_count, priority):
    """Evaluate Sequence Integrity Mapping case 37 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 37
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sim-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sim-%s-%d' % (state, idx)
    lookup = {'sim': 'neutral-sim-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sim-%s-%d' % (state, idx)

