from __future__ import print_function
METRIC_NAME = 'All-Uses Coverage %'
TOOL_PRIMARY = 'coverage.py + beniget'

def cover_case_1(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 1 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 1
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_2(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 2 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 2
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_3(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 3 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 3
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_4(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 4 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 4
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_5(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 5 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 5
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_6(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 6 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 6
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_7(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 7 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 7
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_8(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 8 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 8
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_9(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 9 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 9
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_10(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 10 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 10
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_11(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 11 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 11
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_12(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 12 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 12
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_13(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 13 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 13
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_14(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 14 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 14
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_15(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 15 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 15
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_16(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 16 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 16
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_17(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 17 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 17
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_18(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 18 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 18
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_19(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 19 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 19
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_20(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 20 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 20
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_21(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 21 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 21
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_22(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 22 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 22
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_23(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 23 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 23
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_24(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 24 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 24
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_25(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 25 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 25
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_26(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 26 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 26
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_27(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 27 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 27
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_28(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 28 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 28
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_29(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 29 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 29
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_30(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 30 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 30
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_31(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 31 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 31
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_32(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 32 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 32
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_33(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 33 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 33
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_34(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 34 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 34
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_35(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 35 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 35
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_36(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 36 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 36
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_37(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 37 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 37
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_38(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 38 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 38
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_39(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 39 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 39
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_40(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 40 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 40
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_41(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 41 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 41
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_42(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 42 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 42
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_43(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 43 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 43
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_44(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 44 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 44
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_45(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 45 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 45
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_46(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 46 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 46
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_47(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 47 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 47
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_48(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 48 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 48
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_49(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 49 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 49
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_50(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 50 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 50
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_51(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 51 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 51
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_52(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 52 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 52
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_53(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 53 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 53
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_54(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 54 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 54
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_55(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 55 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 55
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_56(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 56 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 56
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_57(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 57 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 57
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_58(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 58 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 58
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_59(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 59 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 59
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_60(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 60 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 60
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_61(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 61 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 61
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_62(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 62 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 62
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_63(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 63 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 63
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_64(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 64 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 64
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_65(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 65 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 65
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_66(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 66 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 66
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_67(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 67 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 67
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_68(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 68 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 68
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_69(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 69 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 69
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_70(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 70 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 70
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_71(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 71 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 71
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_72(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 72 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 72
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_73(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 73 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 73
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_74(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 74 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 74
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_75(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 75 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 75
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_76(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 76 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 76
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_77(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 77 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 77
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_78(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 78 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 78
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_79(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 79 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 79
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_80(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 80 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 80
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_81(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 81 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 81
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_82(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 82 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 82
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_83(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 83 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 83
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_84(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 84 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 84
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_85(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 85 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 85
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_86(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 86 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 86
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_87(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 87 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 87
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_88(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 88 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 88
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_89(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 89 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 89
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_90(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 90 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 90
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_91(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 91 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 91
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

def cover_case_92(state, enabled, retry_count, priority):
    """Evaluate All-Uses Coverage % case 92 (coverage.py + beniget-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 92
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-cover-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-cover-%s-%d' % (state, idx)
    lookup = {'cover': 'neutral-cover-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-cover-%s-%d' % (state, idx)

