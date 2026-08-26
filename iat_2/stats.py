"""Calculating d-score in pure python

All data are list of float values

Implementation of d-score according to this snapshot:
http://faculty.washington.edu/agg/IATmaterials/Summary%20of%20Improved%20Scoring%20Algorithm.pdf
"""

import math


def mean(data: list):
    m = sum(data) / len(data)
    return m


def std(data: list):
    cnt = len(data)
    m = sum(data) / cnt
    sqs = sum((v - m) ** 2 for v in data)
    ssq = sqs / (cnt - 1)
    sstd = math.sqrt(ssq)
    return sstd


def dscore(data3: list, data4: list, data6: list, data7: list):
    # Drop implausibly long responses before applying the D-score rule.

    def not_long(value):
        return value < 10.0

    data3 = list(filter(not_long, data3))
    data4 = list(filter(not_long, data4))
    data6 = list(filter(not_long, data6))
    data7 = list(filter(not_long, data7))

    # Reject participants with too many implausibly short responses.
    def too_short(value):
        return value < 0.300

    total_data = data3 + data4 + data6 + data7
    if not total_data:
        return None

    short_data = list(filter(too_short, total_data))
    if len(short_data) / len(total_data) > 0.1:
        return None

    # Incomplete demo runs can leave a scoring block empty; in that case the
    # score is not defined.
    if not all([data3, data4, data6, data7]):
        return None
    if len(data3 + data6) < 2 or len(data4 + data7) < 2:
        return None

    std_3_6 = std(data3 + data6)
    std_4_7 = std(data4 + data7)
    if std_3_6 == 0 or std_4_7 == 0:
        return None

    mean_3_6 = mean(data6) - mean(data3)
    mean_4_7 = mean(data7) - mean(data4)

    dscore_3_6 = mean_3_6 / std_3_6
    dscore_4_7 = mean_4_7 / std_4_7

    dscore_mean = (dscore_3_6 + dscore_4_7) * 0.5

    return dscore_mean
