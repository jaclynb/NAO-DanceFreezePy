# -*- encoding: UTF-8 -*-

from dance import DancePart, Dance

names1 = list()
times1 = list()
keys1 = list()

names1.append("HeadPitch")
times1.append([1.92, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([-0.162646, -0.162646, -0.162646, -0.162646, -0.162646, -0.144238, -0.144238, -0.144238])

names1.append("HeadYaw")
times1.append([1.92, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([-0.01845, -0.354396, 0.216252, 0.478566, 0.0674542, 0.05825, 0.05825, -0.227074])

names1.append("LAnklePitch")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.093532, 0.091998, 0.091998, 0.091998, 0.091998, 0.091998, 0.091998, 0.0827939])

names1.append("LAnkleRoll")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([-0.121144, -0.122678, -0.122678, -0.122678, -0.122678, -0.121144, -0.121144, -0.12728])

names1.append("LElbowRoll")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([-0.605888, -0.62583, -0.62583, -0.62583, -1.02314, -1.00013, -1.00013, -0.975581])

names1.append("LElbowYaw")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([-1.38524, -0.955723, -1.38524, -1.91601, -0.584497, -0.633584, -0.633584, -0.627448])

names1.append("LHand")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.2884, 0.2884, 0.2884, 0.2884, 0.2884, 0.294, 0.294, 0.294])

names1.append("LHipPitch")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.130432, 0.130432, 0.130432, 0.130432, 0.130432, 0.12583, 0.12583, 0.128898])

names1.append("LHipRoll")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.0966839, 0.0966839, 0.0966839, 0.0966839, 0.0966839, 0.0951499, 0.0951499, 0.099752])

names1.append("LHipYawPitch")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([-0.170232, -0.170232, -0.170232, -0.170232, -0.170232, -0.1733, -0.1733, -0.170232])

names1.append("LKneePitch")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([-0.092082, -0.092082, -0.092082, -0.092082, -0.092082, -0.0923279, -0.0923279, -0.0859461])

names1.append("LShoulderPitch")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.638103, 0.539926, 0.51845, 0.532256, 0.326699, 0.414139, 0.414139, 0.481634])

names1.append("LShoulderRoll")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.151824, -0.07214, 0.381923, 0.777696, 0.306757, 0.263807, 0.263807, 0.254602])

names1.append("LWristYaw")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.0981341, -0.368202, -0.329852, -0.273093, -1.09072, -1.00941, -1.00941, -1.00328])

names1.append("RAnklePitch")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.0951499, 0.090548, 0.090548, 0.090548, 0.0890141, 0.092082, 0.092082, 0.0874801])

names1.append("RAnkleRoll")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.130432, 0.128898, 0.128898, 0.128898, 0.128898, 0.121228, 0.121228, 0.128898])

names1.append("RElbowRoll")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.618244, 0.595234, 0.779314, 0.817664, 0.817664, 0.794654, 0.794654, 0.774711])

names1.append("RElbowYaw")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([1.26551, 1.42351, 1.43425, 0.951039, 0.613558, 0.845191, 0.845191, 0.83292])

names1.append("RHand")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.2904, 0.2904, 0.2904, 0.2904, 0.2904, 0.2876, 0.2876, 0.2876])

names1.append("RHipPitch")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.121144, 0.122678, 0.122678, 0.122678, 0.122678, 0.121144, 0.121144, 0.11961])

names1.append("RHipRoll")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([-0.091998, -0.091998, -0.091998, -0.091998, -0.091998, -0.101202, -0.101202, -0.107338])

names1.append("RHipYawPitch")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([-0.170232, -0.170232, -0.170232, -0.170232, -0.170232, -0.1733, -0.1733, -0.170232])

names1.append("RKneePitch")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([-0.0904641, -0.0904641, -0.0904641, -0.0904641, -0.0904641, -0.0923279, -0.0923279, -0.0904641])

names1.append("RShoulderPitch")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.558418, 0.570689, 0.552281, 0.426494, 0.346725, 0.423426, 0.423426, 0.461776])

names1.append("RShoulderRoll")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([-0.151908, -0.481718, 0.0812599, 0.263807, 0.0904641, -0.39428, -0.39428, -0.38661])

names1.append("RWristYaw")
times1.append([2.56, 3, 3.92, 4.44, 5.2, 5.56, 5.88, 6.32])
keys1.append([0.0889301, 0.151824, 0.0889301, 0.593616, 0.895815, 0.851328, 0.851328, 0.842125])

names2 = list()
times2 = list()
keys2 = list()

names2.append("HeadPitch")
times2.append([0.8, 1.28, 1.76, 2.24, 2.72, 3.2, 3.68, 4, 4.48, 4.96])
keys2.append([-0.14117, -0.14117, -0.14117, -0.14117, -0.14117, -0.159578, -0.159578, -0.159578, -0.159578, -0.159578])

names2.append("HeadYaw")
times2.append([0.8, 1.28, 1.76, 2.24, 2.72, 3.2, 3.68, 4, 4.48, 4.96])
keys2.append([-0.214803, -0.236277, -0.236277, -0.236277, 0.383458, 0.383458, 0.383458, 0.377323, 0.377323, 0.377323])

names2.append("LAnklePitch")
times2.append([0.8, 1.28, 1.76, 2.24, 2.72, 3.2, 3.68, 4, 4.48, 4.96])
keys2.append([0.0843279, 0.0843279, 0.0843279, 0.0843279, 0.0843279, 0.0797259, -0.303775, -0.30224, -0.30224, -0.30224])

names2.append("LAnkleRoll")
times2.append([0.8, 1.28, 1.76, 2.24, 2.72, 3.2, 3.68, 4, 4.48, 4.96])
keys2.append([-0.121144, -0.121144, -0.121144, -0.121144, -0.121144, -0.217786, -0.217786, -0.210117, -0.210117, -0.210117])

names2.append("LElbowRoll")
times2.append([0.8, 1.28, 1.76, 2.24, 2.72, 3.2, 3.68, 4, 4.48, 4.96])
keys2.append([-0.989389, -0.989389, -0.989389, -0.989389, -0.989389, -0.989389, -0.921892, -0.918823, -0.918823, -0.918823])

names2.append("LElbowYaw")
times2.append([0.8, 1.28, 1.76, 2.24, 2.72, 3.2, 3.68, 4, 4.48, 4.96])
keys2.append([-0.605971, -0.605971, -0.605971, -0.605971, -0.605971, -1.34076, -1.66136, -1.8301, -1.8301, -1.8301])

names2.append("LHand")
times2.append([0.8, 1.28, 1.76, 2.24, 2.72, 3.2, 3.68, 4, 4.48, 4.96])
keys2.append([0.2852, 0.2852, 0.2852, 0.2852, 0.2852, 0.2852, 0.2852, 0.2852, 0.2852, 0.2852])

names2.append("LHipPitch")
times2.append([0.8, 1.28, 1.76, 2.24, 2.72, 3.2, 3.68, 4, 4.48, 4.96])
keys2.append([0.12583, 0.12583, 0.12583, 0.12583, 0.12583, 0.239346, 0.239346, 0.243948, 0.243948, 0.243948])

names2.append("LHipRoll")
times2.append([0.8, 1.28, 1.76, 2.24, 2.72, 3.2, 3.68, 4, 4.48, 4.96])
keys2.append([0.101286, 0.101286, 0.101286, 0.101286, 0.101286, 0.253151, 0.27923, 0.277696, 0.277696, 0.277696])

names2.append("LHipYawPitch")
times2.append([0.8, 1.28, 1.76, 2.24, 2.72, 3.2, 3.68, 4, 4.48, 4.96])
keys2.append([-0.168698, -0.168698, -0.168698, -0.168698, -0.168698, -0.168698, -0.20398, -0.205514, -0.205514, -0.205514])

names2.append("LKneePitch")
times2.append([0.8, 1.28, 1.76, 2.24, 2.72, 3.2, 3.68, 4, 4.48, 4.96])
keys2.append([-0.090548, -0.090548, -0.090548, -0.090548, -0.090548, -0.090548, 0.36505, 0.36505, 0.36505, 0.36505])

names2.append("LShoulderPitch")
times2.append([0.8, 1.28, 1.76, 2.24, 2.72, 3.2, 3.68, 4, 4.48, 4.96])
keys2.append([0.493905, 0.493905, 0.493905, 0.493905, 0.493905, 0.612024, 0.780764, 0.291418, 0.302157, 0.302157])

names2.append("LShoulderRoll")
times2.append([0.8, 1.28, 1.76, 2.24, 2.72, 3.2, 3.68, 4, 4.48, 4.96])
keys2.append([0.271475, 0.271475, 0.271475, 0.271475, 0.271475, 0.596684, 0.822183, 0.831386, 0.831386, 0.831386])

names2.append("LWristYaw")
times2.append([0.8, 1.28, 1.76, 2.24, 2.72, 3.2, 3.68, 4, 4.48, 4.96])
keys2.append([-1.03703, -1.03703, -1.03703, -1.03703, -1.03703, -0.90817, -0.76244, -0.527739, -0.527739, -0.527739])

names2.append("RAnklePitch")
times2.append([0.8, 1.28, 1.76, 2.24, 2.72, 3.2, 3.68, 4, 4.48, 4.96])
keys2.append([0.0874801, 0.0874801, 0.0874801, 0.0874801, 0.0874801, 0.0782759, -0.0275701, -0.0291041, -0.0291041, -0.0291041])

names2.append("RAnkleRoll")
times2.append([0.8, 1.28, 1.76, 2.24, 2.72, 3.2, 3.68, 4, 4.48, 4.96])
keys2.append([0.128898, 0.128898, 0.128898, 0.128898, 0.128898, 0.142704, 0.176453, 0.174919, 0.174919, 0.174919])

names2.append("RElbowRoll")
times2.append([0.8, 1.28, 1.76, 2.24, 2.72, 3.2, 3.68, 4, 4.48, 4.96])
keys2.append([0.790051, 0.788519, 1.07231, 0.579894, 0.579894, 0.579894, 0.579894, 0.581429, 0.581429, 0.581429])

names2.append("RElbowYaw")
times2.append([0.8, 1.28, 1.76, 2.24, 2.72, 3.2, 3.68, 4, 4.48, 4.96])
keys2.append([0.823717, 0.998592, 1.18114, 1.19648, 1.19648, 1.19648, 1.19648, 1.20415, 1.19341, 1.18267])

names2.append("RHand")
times2.append([0.8, 1.28, 1.76, 2.24, 2.72, 3.2, 3.68, 4, 4.48, 4.96])
keys2.append([0.2904, 0.2904, 0.2904, 0.2904, 0.1912, 0.1912, 0.1912, 0.2008, 0.2008, 0.2008])

names2.append("RHipPitch")
times2.append([0.8, 1.28, 1.76, 2.24, 2.72, 3.2, 3.68, 4, 4.48, 4.96])
keys2.append([0.12728, 0.12728, 0.12728, 0.12728, 0.12728, 0.233125, 0.05825, 0.056716, 0.056716, 0.056716])

names2.append("RHipRoll")
times2.append([0.8, 1.28, 1.76, 2.24, 2.72, 3.2, 3.68, 4, 4.48, 4.96])
keys2.append([-0.0981341, -0.0981341, -0.0981341, -0.0981341, -0.0981341, -0.131882, -0.16563, -0.168698, -0.168698, -0.168698])

names2.append("RHipYawPitch")
times2.append([0.8, 1.28, 1.76, 2.24, 2.72, 3.2, 3.68, 4, 4.48, 4.96])
keys2.append([-0.168698, -0.168698, -0.168698, -0.168698, -0.168698, -0.168698, -0.20398, -0.205514, -0.205514, -0.205514])

names2.append("RKneePitch")
times2.append([0.8, 1.28, 1.76, 2.24, 2.72, 3.2, 3.68, 4, 4.48, 4.96])
keys2.append([-0.0827939, -0.0827939, -0.0827939, -0.0827939, -0.0827939, -0.0827939, 0.25622, 0.262356, 0.262356, 0.262356])

names2.append("RShoulderPitch")
times2.append([0.8, 1.28, 1.76, 2.24, 2.72, 3.2, 3.68, 4, 4.48, 4.96])
keys2.append([0.466378, -0.0291041, -0.412605, -1.11518, -0.949504, -0.949504, -0.949504, -0.435615, 0.121228, 0.1335])

names2.append("RShoulderRoll")
times2.append([0.8, 1.28, 1.76, 2.24, 2.72, 3.2, 3.68, 4, 4.48, 4.96])
keys2.append([-0.369736, -0.417291, -0.480184, -0.236277, -0.254685, -0.254685, -0.254685, -0.297638, -0.14117, -0.14117])

names2.append("RWristYaw")
times2.append([0.8, 1.28, 1.76, 2.24, 2.72, 3.2, 3.68, 4, 4.48, 4.96])
keys2.append([0.865134, 0.825251, 0.825251, 1.01853, 1.0078, 1.0078, 1.0078, 0.984786, 0.984786, 0.984786])

names3 = list()
times3 = list()
keys3 = list()

names3.append("HeadPitch")
times3.append([0.2, 0.68, 1.24, 2.4, 3.24, 4.04, 4.64, 5.4, 6.72, 7.64, 8.36])
keys3.append([-0.14884, -0.14884, -0.14884, -0.14884, -0.185656, -0.185656, -0.185656, -0.185656, -0.185656, -0.217869, -0.217869])

names3.append("HeadYaw")
times3.append([0.2, 0.68, 1.24, 2.4, 3.24, 4.04, 4.64, 5.4, 6.72, 7.64, 8.36])
keys3.append([0.377323, -0.30224, -0.813062, -0.813062, -0.116626, -0.116626, -0.116626, -0.116626, -0.116626, -0.105888, -0.105888])

names3.append("LAnklePitch")
times3.append([0.2, 0.68, 1.24, 2.4, 3.24, 4.04, 4.64, 5.4, 6.72, 7.64, 8.36])
keys3.append([-0.312978, 0.0291041, 0.0291041, 0.10427, 0.10427, 0.10427, 0.10427, 0.093532, 0.093532, 0.0904641, 0.0904641])

names3.append("LAnkleRoll")
times3.append([0.2, 0.68, 1.24, 2.4, 3.24, 4.04, 4.64, 5.4, 6.72, 7.64, 8.36])
keys3.append([-0.213185, -0.223922, -0.223922, -0.0735901, -0.0735901, -0.0735901, -0.0735901, -0.156426, -0.156426, -0.162562, -0.162562])

names3.append("LElbowRoll")
times3.append([0.2, 0.68, 1.24, 2.4, 3.24, 4.04, 4.64, 5.4, 6.72, 7.64, 8.36])
keys3.append([-0.90962, -0.699462, -0.685656, -0.889678, -0.783833, -0.783833, -0.118076, -0.812978, -1.24863, -0.607422, -1.33147])

names3.append("LElbowYaw")
times3.append([0.2, 0.68, 1.24, 2.4, 3.24, 4.04, 4.64, 5.4, 6.72, 7.64, 8.36])
keys3.append([-1.82244, -1.62301, -1.15821, -1.48035, -1.49262, -1.84237, -2.08167, -1.53558, -0.753235, -1.09992, -0.898967])

names3.append("LHand")
times3.append([0.2, 0.68, 1.24, 2.4, 3.24, 4.04, 4.64, 5.4, 6.72, 7.64, 8.36])
keys3.append([0.2856, 0.2856, 0.2856, 0.2856, 0.2856, 0.2856, 0.2856, 0.2856, 0.2856, 0.2856, 0.2856])

names3.append("LHipPitch")
times3.append([0.2, 0.68, 1.24, 2.4, 3.24, 4.04, 4.64, 5.4, 6.72, 7.64, 8.36])
keys3.append([0.234743, 0.245482, 0.245482, 0.116626, 0.116626, 0.116626, 0.116626, 0.116626, 0.116626, 0.113558, 0.113558])

names3.append("LHipRoll")
times3.append([0.2, 0.68, 1.24, 2.4, 3.24, 4.04, 4.64, 5.4, 6.72, 7.64, 8.36])
keys3.append([0.277696, 0.266959, 0.266959, 0.090548, 0.090548, 0.090548, 0.090548, 0.0798099, 0.0798099, 0.0890141, 0.0890141])

names3.append("LHipYawPitch")
times3.append([0.2, 0.68, 1.24, 2.4, 3.24, 4.04, 4.64, 5.4, 6.72, 7.64, 8.36])
keys3.append([-0.197844, -0.170232, -0.170232, -0.170232, -0.170232, -0.170232, -0.170232, -0.170232, -0.18097, -0.18097, -0.18097])

names3.append("LKneePitch")
times3.append([0.2, 0.68, 1.24, 2.4, 3.24, 4.04, 4.64, 5.4, 6.72, 7.64, 8.36])
keys3.append([0.371186, 0.00302602, 0.00302602, -0.00771189, -0.00771189, -0.00771189, -0.00771189, -0.00771189, -0.00771189, -0.00617791, -0.00617791])

names3.append("LShoulderPitch")
times3.append([0.2, 0.68, 1.24, 2.4, 3.24, 4.04, 4.64, 5.4, 6.72, 7.64, 8.36])
keys3.append([0.355846, 0.427944, 0.535324, -0.145772, -0.702614, -0.506262, -0.108956, 0.750085, 0.720938, 0.500042, 0.355846])

names3.append("LShoulderRoll")
times3.append([0.2, 0.68, 1.24, 2.4, 3.24, 4.04, 4.64, 5.4, 6.72, 7.64, 8.36])
keys3.append([0.812978, 0.401866, -0.222472, -0.0261199, 0.032172, 0.569072, 1.0983, 0.57214, 0.299088, -0.046062, 0.177901])

names3.append("LWristYaw")
times3.append([0.2, 0.68, 1.24, 2.4, 3.24, 4.04, 4.64, 5.4, 6.72, 7.64, 8.36])
keys3.append([-0.546147, -0.286901, -0.247016, -0.282298, -0.2102, -0.299172, 0.0383082, -0.504728, -0.618244, -0.451038, -0.527739])

names3.append("RAnklePitch")
times3.append([0.2, 0.68, 1.24, 2.4, 3.24, 4.04, 4.64, 5.4, 6.72, 7.64, 8.36])
keys3.append([-0.022968, -0.0183661, -0.0183661, 0.124296, 0.124296, 0.124296, 0.135034, -0.23466, -0.23466, -0.23466, -0.245399])

names3.append("RAnkleRoll")
times3.append([0.2, 0.68, 1.24, 2.4, 3.24, 4.04, 4.64, 5.4, 6.72, 7.64, 8.36])
keys3.append([0.182588, 0.139636, 0.139636, 0.0598679, 0.0598679, 0.0598679, 0.0598679, -0.021434, -0.021434, -0.0260359, -0.0260359])

names3.append("RElbowRoll")
times3.append([0.2, 0.68, 1.24, 2.4, 3.24, 4.04, 4.64, 5.4, 6.72, 7.64, 8.36])
keys3.append([0.570689, 0.559952, 0.421891, 0.852946, 0.857548, 0.857548, 0.174919, 0.83147, 0.957259, 0.429562, 1.39905])

names3.append("RElbowYaw")
times3.append([0.2, 0.68, 1.24, 2.4, 3.24, 4.04, 4.64, 5.4, 6.72, 7.64, 8.36])
keys3.append([1.19494, 1.18267, 1.21489, 1.28852, 1.50174, 1.58918, 1.58918, 1.06916, 0.757754, 0.766959, 0.759288])

names3.append("RHand")
times3.append([0.2, 0.68, 1.24, 2.4, 3.24, 4.04, 4.64, 5.4, 6.72, 7.64, 8.36])
keys3.append([0.198, 0.198, 0.198, 0.198, 0.198, 0.198, 0.198, 0.198, 0.198, 0.1984, 0.1984])

names3.append("RHipPitch")
times3.append([0.2, 0.68, 1.24, 2.4, 3.24, 4.04, 4.64, 5.4, 6.72, 7.64, 8.36])
keys3.append([0.059784, 0.0137641, 0.0137641, 0.15796, 0.15796, 0.15796, 0.15796, -0.30224, -0.314512, -0.322183, -0.322183])

names3.append("RHipRoll")
times3.append([0.2, 0.68, 1.24, 2.4, 3.24, 4.04, 4.64, 5.4, 6.72, 7.64, 8.36])
keys3.append([-0.168698, -0.156426, -0.156426, -0.0674542, -0.0674542, -0.0674542, -0.0674542, -0.0904641, -0.0904641, -0.093532, -0.093532])

names3.append("RHipYawPitch")
times3.append([0.2, 0.68, 1.24, 2.4, 3.24, 4.04, 4.64, 5.4, 6.72, 7.64, 8.36])
keys3.append([-0.197844, -0.170232, -0.170232, -0.170232, -0.170232, -0.170232, -0.170232, -0.170232, -0.18097, -0.18097, -0.18097])

names3.append("RKneePitch")
times3.append([0.2, 0.68, 1.24, 2.4, 3.24, 4.04, 4.64, 5.4, 6.72, 7.64, 8.36])
keys3.append([0.259288, 0.268493, 0.268493, -0.0904641, -0.0904641, -0.0904641, -0.0904641, 0.684206, 0.694945, 0.693411, 0.693411])

names3.append("RShoulderPitch")
times3.append([0.2, 0.68, 1.24, 2.4, 3.24, 4.04, 4.64, 5.4, 6.72, 7.64, 8.36])
keys3.append([0.150374, 0.282298, 0.323717, -0.299088, -0.636569, -0.329768, -0.00609397, 0.559952, 0.612108, 0.35593, 0.25622])

names3.append("RShoulderRoll")
times3.append([0.2, 0.68, 1.24, 2.4, 3.24, 4.04, 4.64, 5.4, 6.72, 7.64, 8.36])
keys3.append([-0.15651, -0.527739, -1.01555, -0.992539, -0.0966839, -0.687274, -1.02015, -0.510865, -0.038392, 0.141086, -0.25622])

names3.append("RWristYaw")
times3.append([0.2, 0.68, 1.24, 2.4, 3.24, 4.04, 4.64, 5.4, 6.72, 7.64, 8.36])
keys3.append([0.983252, 0.972515, 0.972515, 0.993989, 0.383458, 0.639635, 0.616627, 0.770025, 0.757754, 0.734743, 0.694859])

names4 = list()
times4 = list()
keys4 = list()

names4.append("HeadPitch")
times4.append([0.24, 0.84, 1.48, 2.2, 3, 4.12, 5.44])
keys4.append([-0.245482, -0.168782, -0.168782, -0.168782, -0.20253, -0.20253, -0.452573])

names4.append("HeadYaw")
times4.append([0.24, 0.84, 1.48, 2.2, 3, 4.12, 5.44])
keys4.append([-0.092082, -0.12583, -0.116626, 0.449421, 0.446352, 0.446352, 0.446352])

names4.append("LAnklePitch")
times4.append([0.24, 0.84, 1.48, 2.2, 3, 4.12, 5.44])
keys4.append([0.0904641, 0.093532, 0.093532, 0.093532, 0.078192, 0.078192, 0.078192])

names4.append("LAnkleRoll")
times4.append([0.24, 0.84, 1.48, 2.2, 3, 4.12, 5.44])
keys4.append([-0.171766, -0.161028, -0.15029, -0.15029, -0.125746, -0.125746, -0.125746])

names4.append("LElbowRoll")
times4.append([0.24, 0.84, 1.48, 2.2, 3, 4.12, 5.44])
keys4.append([-1.30539, -1.21795, -1.21795, -1.21795, -1.20261, -1.19034, -1.19034])

names4.append("LElbowYaw")
times4.append([0.24, 0.84, 1.48, 2.2, 3, 4.12, 5.44])
keys4.append([-0.883625, -0.73943, -0.745566, -0.745566, -2.07862, -2.07862, -2.07862])

names4.append("LHand")
times4.append([0.24, 0.84, 1.48, 2.2, 3, 4.12, 5.44])
keys4.append([0.2856, 0.2856, 0.2856, 0.2856, 0.2856, 0.2856, 0.2856])

names4.append("LHipPitch")
times4.append([0.24, 0.84, 1.48, 2.2, 3, 4.12, 5.44])
keys4.append([0.11049, 0.115092, 0.116626, 0.116626, 0.0445281, 0.0445281, 0.0445281])

names4.append("LHipRoll")
times4.append([0.24, 0.84, 1.48, 2.2, 3, 4.12, 5.44])
keys4.append([0.0890141, 0.0782759, 0.07214, 0.07214, 0.116626, 0.116626, 0.116626])

names4.append("LHipYawPitch")
times4.append([0.24, 0.84, 1.48, 2.2, 3, 4.12, 5.44])
keys4.append([-0.182504, -0.18864, -0.18097, -0.18097, 0.01845, 0.01845, 0.01845])

names4.append("LKneePitch")
times4.append([0.24, 0.84, 1.48, 2.2, 3, 4.12, 5.44])
keys4.append([-0.00464392, -0.00617791, -0.00464392, -0.00464392, -0.062936, -0.062936, -0.062936])

names4.append("LShoulderPitch")
times4.append([0.24, 0.84, 1.48, 2.2, 3, 4.12, 5.44])
keys4.append([0.431013, 0.739346, 0.757754, 0.757754, 1.09984, 1.03387, 1.03387])

names4.append("LShoulderRoll")
times4.append([0.24, 0.84, 1.48, 2.2, 3, 4.12, 5.44])
keys4.append([0.190175, 0.305223, 0.294486, 0.305223, 0.435615, 0.80991, 0.80991])

names4.append("LWristYaw")
times4.append([0.24, 0.84, 1.48, 2.2, 3, 4.12, 5.44])
keys4.append([-0.513931, -0.602905, -0.602905, -0.602905, -0.467912, -0.259288, -0.259288])

names4.append("RAnklePitch")
times4.append([0.24, 0.84, 1.48, 2.2, 3, 4.12, 5.44])
keys4.append([-0.249999, -0.24233, -0.237728, -0.237728, 0.06447, 0.06447, 0.06447])

names4.append("RAnkleRoll")
times4.append([0.24, 0.84, 1.48, 2.2, 3, 4.12, 5.44])
keys4.append([-0.0352399, -0.021434, -0.0291041, -0.0291041, 0.0521979, 0.0521979, 0.0521979])

names4.append("RElbowRoll")
times4.append([0.24, 0.84, 1.48, 2.2, 3, 4.12, 5.44])
keys4.append([1.3699, 0.928112, 1.21037, 1.17355, 1.15054, 1.15054, 1.15054])

names4.append("RElbowYaw")
times4.append([0.24, 0.84, 1.48, 2.2, 3, 4.12, 5.44])
keys4.append([0.727074, 0.766959, 0.302157, 0.291418, 0.276078, 0.276078, 0.276078])

names4.append("RHand")
times4.append([0.24, 0.84, 1.48, 2.2, 3, 4.12, 5.44])
keys4.append([0.204, 0.2004, 0.2, 0.2, 0.2004, 0.2004, 0.2004])

names4.append("RHipPitch")
times4.append([0.24, 0.84, 1.48, 2.2, 3, 4.12, 5.44])
keys4.append([-0.329852, -0.320648, -0.312978, -0.312978, -0.046062, -0.046062, -0.046062])

names4.append("RHipRoll")
times4.append([0.24, 0.84, 1.48, 2.2, 3, 4.12, 5.44])
keys4.append([-0.091998, -0.0827939, -0.0827939, -0.0827939, -0.056716, -0.056716, -0.056716])

names4.append("RHipYawPitch")
times4.append([0.24, 0.84, 1.48, 2.2, 3, 4.12, 5.44])
keys4.append([-0.182504, -0.18864, -0.18097, -0.18097, 0.01845, 0.01845, 0.01845])

names4.append("RKneePitch")
times4.append([0.24, 0.84, 1.48, 2.2, 3, 4.12, 5.44])
keys4.append([0.687274, 0.688808, 0.696477, 0.696477, 0.0276539, 0.0276539, 0.0276539])

names4.append("RShoulderPitch")
times4.append([0.24, 0.84, 1.48, 2.2, 3, 4.12, 5.44])
keys4.append([0.343659, 0.628982, 0.786985, 0.797722, 0.813062, 0.813062, 0.813062])

names4.append("RShoulderRoll")
times4.append([0.24, 0.84, 1.48, 2.2, 3, 4.12, 5.44])
keys4.append([-0.251617, -0.0567998, 0.271475, 0.174835, 0.156426, 0.156426, 0.156426])

names4.append("RWristYaw")
times4.append([0.24, 0.84, 1.48, 2.2, 3, 4.12, 5.44])
keys4.append([0.722472, 0.743948, 0.753151, 0.753151, 0.743948, 0.743948, 0.743948])

names5 = list()
times5 = list()
keys5 = list()

names5.append("HeadPitch")
times5.append([0.36, 1.12, 2.12, 3.12, 4.12, 5.12, 6, 6.48])
keys5.append([-0.438765, -0.581011, -0.60904, -0.219404, -0.0245859, 0.371186, 0.392662, 0.392662])

names5.append("HeadYaw")
times5.append([0.36, 1.12, 2.12, 3.12, 4.12, 5.12, 6, 6.48])
keys5.append([0.437147, 0.68719, 0.139552, 0.00916195, 0.0413762, 0.0199001, 0.024502, 0.024502])

names5.append("LAnklePitch")
times5.append([0.36, 1.12, 2.12, 3.12, 4.12, 5.12, 6, 6.48])
keys5.append([0.076658, 0.076658, 0.076658, 0.076658, 0.076658, 0.076658, 0.0827939, 0.0827939])

names5.append("LAnkleRoll")
times5.append([0.36, 1.12, 2.12, 3.12, 4.12, 5.12, 6, 6.48])
keys5.append([-0.11961, -0.11961, -0.11961, -0.11961, -0.11961, -0.11961, -0.116542, -0.116542])

names5.append("LElbowRoll")
times5.append([0.36, 1.12, 2.12, 3.12, 4.12, 5.12, 6, 6.48])
keys5.append([-1.00933, -0.984786, -0.974047, -0.668782, -0.223922, -0.223922, -0.214717, -0.214717])

names5.append("LElbowYaw")
times5.append([0.36, 1.12, 2.12, 3.12, 4.12, 5.12, 6, 6.48])
keys5.append([-2.07708, -1.92827, -1.3561, -1.27786, -1.35456, -1.35456, -1.34843, -1.34843])

names5.append("LHand")
times5.append([0.36, 1.12, 2.12, 3.12, 4.12, 5.12, 6, 6.48])
keys5.append([0.2868, 0.2868, 0.2868, 0.2868, 0.2868, 0.2868, 0.2868, 0.2868])

names5.append("LHipPitch")
times5.append([0.36, 1.12, 2.12, 3.12, 4.12, 5.12, 6, 6.48])
keys5.append([0.04913, 0.04913, 0.04913, 0.04913, 0.04913, 0.04913, 0.047596, 0.047596])

names5.append("LHipRoll")
times5.append([0.36, 1.12, 2.12, 3.12, 4.12, 5.12, 6, 6.48])
keys5.append([0.119694, 0.119694, 0.119694, 0.119694, 0.119694, 0.119694, 0.119694, 0.119694])

names5.append("LHipYawPitch")
times5.append([0.36, 1.12, 2.12, 3.12, 4.12, 5.12, 6, 6.48])
keys5.append([0.019984, 0.019984, 0.019984, 0.019984, 0.019984, 0.019984, 0.01845, 0.01845])

names5.append("LKneePitch")
times5.append([0.36, 1.12, 2.12, 3.12, 4.12, 5.12, 6, 6.48])
keys5.append([-0.0583338, -0.0690719, -0.0690719, -0.0583338, -0.0583338, -0.0583338, -0.0583338, -0.0583338])

names5.append("LShoulderPitch")
times5.append([0.36, 1.12, 2.12, 3.12, 4.12, 5.12, 6, 6.48])
keys5.append([0.828318, 0.312894, 0.113474, 0.194775, 0.612024, 1.20875, 1.19341, 1.19341])

names5.append("LShoulderRoll")
times5.append([0.36, 1.12, 2.12, 3.12, 4.12, 5.12, 6, 6.48])
keys5.append([0.826783, 0.812978, 0.369652, 0.11194, 0.056716, 0.030638, 0.0444441, 0.0444441])

names5.append("LWristYaw")
times5.append([0.36, 1.12, 2.12, 3.12, 4.12, 5.12, 6, 6.48])
keys5.append([-0.200996, -0.01845, 0.869736, 1.18114, 1.33914, 1.44805, 1.43271, 1.43271])

names5.append("RAnklePitch")
times5.append([0.36, 1.12, 2.12, 3.12, 4.12, 5.12, 6, 6.48])
keys5.append([0.0614019, 0.0614019, 0.0614019, 0.07214, 0.0614019, 0.0614019, 0.066004, 0.066004])

names5.append("RAnkleRoll")
times5.append([0.36, 1.12, 2.12, 3.12, 4.12, 5.12, 6, 6.48])
keys5.append([0.0567998, 0.0567998, 0.0567998, 0.0567998, 0.0567998, 0.0567998, 0.0583338, 0.0583338])

names5.append("RElbowRoll")
times5.append([0.36, 1.12, 2.12, 3.12, 4.12, 5.12, 6, 6.48])
keys5.append([0.80079, 1.02169, 1.02782, 0.70108, 0.0521979, 0.0521979, 0.0552659, 0.0552659])

names5.append("RElbowYaw")
times5.append([0.36, 1.12, 2.12, 3.12, 4.12, 5.12, 6, 6.48])
keys5.append([0.596684, 0.837522, 1.00933, 1.00319, 0.754686, 0.765425, 0.770025, 0.770025])

names5.append("RHand")
times5.append([0.36, 1.12, 2.12, 3.12, 4.12, 5.12, 6, 6.48])
keys5.append([0.198, 0.198, 0.198, 0.198, 0.198, 0.198, 0.206, 0.206])

names5.append("RHipPitch")
times5.append([0.36, 1.12, 2.12, 3.12, 4.12, 5.12, 6, 6.48])
keys5.append([-0.039926, -0.039926, -0.039926, -0.039926, -0.0506639, -0.0506639, -0.04913, -0.04913])

names5.append("RHipRoll")
times5.append([0.36, 1.12, 2.12, 3.12, 4.12, 5.12, 6, 6.48])
keys5.append([-0.0551819, -0.06592, -0.0551819, -0.0551819, -0.0551819, -0.0551819, -0.059784, -0.059784])

names5.append("RHipYawPitch")
times5.append([0.36, 1.12, 2.12, 3.12, 4.12, 5.12, 6, 6.48])
keys5.append([0.019984, 0.019984, 0.019984, 0.019984, 0.019984, 0.019984, 0.01845, 0.01845])

names5.append("RKneePitch")
times5.append([0.36, 1.12, 2.12, 3.12, 4.12, 5.12, 6, 6.48])
keys5.append([0.0353239, 0.0245859, 0.0245859, 0.0245859, 0.0245859, 0.0245859, 0.0291878, 0.0291878])

names5.append("RShoulderPitch")
times5.append([0.36, 1.12, 2.12, 3.12, 4.12, 5.12, 6, 6.48])
keys5.append([0.532339, 0.214803, -0.0643861, 0.073674, 0.552281, 1.07384, 1.05543, 1.05543])

names5.append("RShoulderRoll")
times5.append([0.36, 1.12, 2.12, 3.12, 4.12, 5.12, 6, 6.48])
keys5.append([0.308291, 0.31136, 0.141086, 0.0367741, 0.0996681, 0.075124, 0.056716, 0.056716])

names5.append("RWristYaw")
times5.append([0.36, 1.12, 2.12, 3.12, 4.12, 5.12, 6, 6.48])
keys5.append([0.710201, 0.699462, -0.392746, -0.760906, -0.859083, -0.859083, -0.819198, -0.819198])

part1 = DancePart(7, 2, names1, times1, keys1)
part2 = DancePart(5, 1, names2, times2, keys2)
part3 = DancePart(10, 3, names3, times3, keys3)
part4 = DancePart(5, 2, names4, times4, keys4)
part5 = DancePart(10, 0, names5, times5, keys5)

parts = [part1, part2, part3, part4, part5]

twinkle = Dance("Twinkle", 5, parts)
