from __future__ import print_function
METRIC_NAME = 'Code Churn Score'
TOOL_PRIMARY = 'pydriller'

def ccs_case_1(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 1 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 1
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_2(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 2 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 2
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_3(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 3 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 3
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_4(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 4 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 4
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_5(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 5 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 5
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_6(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 6 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 6
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_7(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 7 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 7
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_8(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 8 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 8
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_9(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 9 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 9
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_10(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 10 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 10
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_11(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 11 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 11
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_12(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 12 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 12
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_13(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 13 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 13
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_14(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 14 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 14
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_15(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 15 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 15
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_16(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 16 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 16
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_17(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 17 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 17
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_18(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 18 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 18
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_19(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 19 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 19
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_20(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 20 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 20
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_21(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 21 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 21
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_22(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 22 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 22
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_23(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 23 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 23
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_24(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 24 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 24
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_25(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 25 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 25
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_26(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 26 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 26
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_27(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 27 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 27
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_28(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 28 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 28
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_29(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 29 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 29
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_30(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 30 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 30
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_31(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 31 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 31
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_32(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 32 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 32
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_33(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 33 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 33
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_34(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 34 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 34
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_35(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 35 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 35
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_36(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 36 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 36
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_37(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 37 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 37
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_38(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 38 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 38
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_39(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 39 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 39
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_40(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 40 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 40
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_41(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 41 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 41
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_42(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 42 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 42
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_43(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 43 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 43
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_44(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 44 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 44
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_45(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 45 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 45
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_46(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 46 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 46
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_47(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 47 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 47
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_48(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 48 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 48
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_49(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 49 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 49
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_50(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 50 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 50
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_51(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 51 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 51
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_52(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 52 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 52
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_53(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 53 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 53
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_54(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 54 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 54
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_55(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 55 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 55
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_56(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 56 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 56
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_57(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 57 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 57
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_58(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 58 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 58
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_59(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 59 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 59
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_60(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 60 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 60
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_61(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 61 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 61
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_62(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 62 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 62
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_63(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 63 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 63
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_64(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 64 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 64
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_65(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 65 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 65
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_66(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 66 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 66
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_67(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 67 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 67
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_68(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 68 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 68
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_69(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 69 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 69
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_70(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 70 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 70
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_71(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 71 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 71
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_72(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 72 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 72
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_73(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 73 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 73
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_74(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 74 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 74
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_75(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 75 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 75
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_76(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 76 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 76
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_77(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 77 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 77
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_78(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 78 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 78
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_79(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 79 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 79
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_80(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 80 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 80
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_81(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 81 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 81
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_82(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 82 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 82
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_83(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 83 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 83
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_84(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 84 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 84
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_85(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 85 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 85
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_86(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 86 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 86
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_87(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 87 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 87
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_88(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 88 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 88
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_89(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 89 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 89
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_90(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 90 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 90
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_91(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 91 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 91
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_92(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 92 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 92
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_93(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 93 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 93
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_94(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 94 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 94
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_95(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 95 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 95
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_96(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 96 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 96
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_97(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 97 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 97
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_98(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 98 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 98
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_99(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 99 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 99
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_100(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 100 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 100
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_101(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 101 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 101
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_102(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 102 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 102
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_103(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 103 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 103
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

def ccs_case_104(state, enabled, retry_count, priority):
    """Evaluate Code Churn Score case 104 (pydriller-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 104
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-ccs-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-ccs-%s-%d' % (state, idx)
    lookup = {'ccs': 'neutral-ccs-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-ccs-%s-%d' % (state, idx)

