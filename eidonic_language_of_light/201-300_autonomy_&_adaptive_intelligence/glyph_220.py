# glyph_220.py — Anchor Feedback Sequencer
# -----------------------------------------------------------------------------
# ID:            220
# Pack:          Pack 003 (201–300)
# Name:          Anchor Feedback Sequencer
# Class:         control
# Stability:     Stable
# Version:       1.0.1
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Callable, Sequence, List, TypeVar, Tuple

S = TypeVar("S")
A = TypeVar("A")

def glyph_220(state: S,
              steps: int,
              *,
              policy: Callable[[S], A],
              transition: Callable[[S, A], S],
              reward: Callable[[S, A, S], float]) -> Tuple[List[A], List[float], S]:
    """
    Anchor Feedback Sequencer — minimal closed-loop decision rollout.

    Overview
    --------
    For `steps` iterations:
      a = policy(s); s' = transition(s, a); r = reward(s, a, s').
    Returns (actions, rewards, final_state).

    Parameters
    ----------
    state : S
    steps : int
    policy : Callable[[S], A]
    transition : Callable[[S, A], S]
    reward : Callable[[S, A, S], float]

    Returns
    -------
    (List[A], List[float], S)
        (actions, rewards, final_state)

    Examples
    --------
    >>> def pol(s): return s+1
    >>> def trans(s,a): return a
    >>> def rew(s,a,s2): return float(a-s)
    >>> glyph_220(0, 3, policy=pol, transition=trans, reward=rew)
    ([1, 2, 3], [1.0, 1.0, 1.0], 3)

    Exceptions
    ----------
    - ValueError : if steps < 0.

    Complexity
    ----------
    - Time  : O(steps)
    - Space : O(steps)
    """
    if steps < 0:
        raise ValueError("steps must be >= 0")
    actions: List[A] = []
    rewards: List[float] = []
    s = state
    for _ in range(steps):
        a = policy(s)
        s2 = transition(s, a)
        r = float(reward(s, a, s2))
        actions.append(a); rewards.append(r); s = s2
    return actions, rewards, s
