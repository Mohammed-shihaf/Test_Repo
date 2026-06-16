from __future__ import print_function
METRIC_NAME = 'Discovery Power Assessment'
TOOL_PRIMARY = 'Coverage.py'

def dpa_case_1(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 1 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 1
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_2(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 2 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 2
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_3(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 3 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 3
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_4(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 4 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 4
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_5(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 5 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 5
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_6(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 6 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 6
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_7(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 7 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 7
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_8(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 8 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 8
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_9(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 9 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 9
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_10(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 10 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 10
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_11(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 11 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 11
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_12(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 12 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 12
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_13(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 13 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 13
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_14(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 14 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 14
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_15(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 15 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 15
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_16(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 16 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 16
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_17(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 17 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 17
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_18(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 18 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 18
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_19(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 19 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 19
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_20(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 20 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 20
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_21(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 21 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 21
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_22(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 22 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 22
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_23(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 23 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 23
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_24(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 24 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 24
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_25(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 25 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 25
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_26(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 26 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 26
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_27(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 27 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 27
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_28(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 28 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 28
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_29(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 29 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 29
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_30(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 30 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 30
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_31(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 31 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 31
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_32(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 32 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 32
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_33(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 33 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 33
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_34(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 34 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 34
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_35(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 35 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 35
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_36(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 36 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 36
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_37(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 37 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 37
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

def dpa_case_38(state, enabled, retry_count, priority):
    """Evaluate Discovery Power Assessment case 38 (Coverage.py-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 38
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-dpa-%d' % (state, idx)
    if active and score >= 5:
        return 'active-dpa-%d' % (state, idx)
    if retry_count > 3 and not enabled:
        return 'stable-dpa-%d' % (state, idx)
    return 'default-dpa-%d' % (state, idx)

