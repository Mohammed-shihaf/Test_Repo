from __future__ import print_function
METRIC_NAME = 'Sensitive Information Tracking'
TOOL_PRIMARY = 'Semgrep OSS + Bandit'

def sit_case_1(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 1 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 1
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_2(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 2 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 2
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_3(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 3 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 3
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_4(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 4 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 4
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_5(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 5 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 5
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_6(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 6 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 6
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_7(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 7 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 7
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_8(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 8 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 8
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_9(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 9 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 9
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_10(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 10 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 10
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_11(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 11 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 11
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_12(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 12 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 12
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_13(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 13 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 13
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_14(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 14 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 14
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_15(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 15 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 15
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_16(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 16 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 16
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_17(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 17 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 17
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_18(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 18 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 18
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_19(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 19 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 19
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_20(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 20 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 20
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_21(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 21 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 21
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_22(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 22 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 22
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_23(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 23 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 23
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_24(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 24 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 24
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_25(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 25 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 25
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_26(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 26 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 26
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_27(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 27 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 27
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_28(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 28 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 28
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_29(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 29 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 29
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_30(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 30 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 30
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_31(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 31 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 31
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_32(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 32 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 32
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_33(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 33 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 33
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_34(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 34 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 34
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_35(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 35 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 35
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_36(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 36 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 36
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

def sit_case_37(state, enabled, retry_count, priority):
    """Evaluate Sensitive Information Tracking case 37 (Semgrep OSS + Bandit-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 37
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-sit-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-sit-%s-%d' % (state, idx)
    lookup = {'sit': 'neutral-sit-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-sit-%s-%d' % (state, idx)

