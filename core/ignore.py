# hcm/core/ignore.py
"""Dictionary containing ignored mice and mouseday lisets for the various HCM experiments.
dictionary {<exp_name>: {mousedays: list of [group_name, mouse_number, ignored_mousedays],
                         mice: list of [group_name, ignored_mice]}

"""

ignored = {'WR1': dict(mousedays=[], mice=[]), 'WR2': dict(mousedays=[], mice=[]),

           '2cD1A2aCRE2': dict(mousedays=[], mice=[]),  # 'M2003', 'M2009', 'M2014', 'M2032'

           '2cD1A2aCRE': dict(mousedays=[], mice=[]),  # 'M1104', 'M1103'

           '2CFast': dict(mousedays=[], mice=[]),

           '1ASTRESS': dict(mousedays=[], mice=[]),

           'Stress_HCMe1r1': dict(mousedays=[], mice=[]),

           'CORTTREAT': dict(mousedays=[('CO', 'M21', 10), ('CORT', 'M29', 8)], mice=[('CO', 'M24')]),

           'HiFat1': dict(mousedays=[('WTHF', 'M5743', 15)], mice=[('WTLF', 'M5736'), ('WTHF', 'M5737')]),

           'HiFat2': dict(mousedays=[('WT', 'M6645', 13), ('WT', 'M6645', 21), ('WT', 'M6645', 22), ('WT', 'M6645', 23),
                                     ('WT', 'M6645', 24), ('WT', 'M6645', 25), ('WT', 'M6694', 5)],
                          mice=[('WT', 'M6645'), ('WT', 'M6708'), ('2CKO', 'M6634'), ('2CKO', 'M6663'),
                                ('2CKO', 'M6681')]),

           'StrainSurvey': dict(
               mousedays=[('BALB', 'M2102', 5), ('BALB', 'M4202', 5), ('BALB', 'M4202', 6), ('BALB', 'M8102', 11),
                          ('A', 'M2103', 7), ('A', 'M2103', 12), ('A', 'M2103', 13), ('A', 'M2103', 14),
                          ('A', 'M2203', 12), ('A', 'M2203', 15), ('A', 'M2203', 16), ('A', 'M5103', 5),
                          ('A', 'M5103', 7), ('A', 'M5103', 8), ('A', 'M5103', 9), ('A', 'M7203', 8),
                          ('A', 'M7203', 11), ('A', 'M7203', 12), ('129S1', 'M5204', 16), ('DBA', 'M5205', 14),
                          ('C3H', 'M3106', 16), ('C3H', 'M4106', 11), ('C3H', 'M7106', 6), ('C3H', 'M7206', 10),
                          ('C3H', 'M8106', 11), ('C3H', 'M8106', 16), ('AKR', 'M4207', 14), ('AKR', 'M4207', 15),
                          ('AKR', 'M4207', 16), ('SWR', 'M3108', 11), ('SWR', 'M4208', 5), ('SWR', 'M4208', 6),
                          ('SWR', 'M5208', 11), ('SJL', 'M4109', 7), ('SJL', 'M4109', 14), ('SJL', 'M4209', 9),
                          ('SJL', 'M8409', 5), ('SJL', 'M8409', 6), ('FVB', 'M4110', 9), ('FVB', 'M7210', 10),
                          ('FVB', 'M7210', 11), ('FVB', 'M7210', 12), ('FVB', 'M7210', 13), ('FVB', 'M7210', 14),
                          ('FVB', 'M7210', 15), ('FVB', 'M7210', 16), ('WSB', 'M2111', 12), ('CAST', 'M2113', 5),
                          ('CAST', 'M2113', 6), ('CAST', 'M2113', 7), ('CAST', 'M2213', 5), ('CAST', 'M2213', 6),
                          ('CAST', 'M2213', 7), ('CAST', 'M2213', 9), ('CAST', 'M3213', 13), ('CAST', 'M5113', 7),
                          ('CAST', 'M5113', 8), ('CAST', 'M5213', 6), ('CAST', 'M5213', 11), ('CAST', 'M5313', 5),
                          ('CAST', 'M5313', 6), ('CAST', 'M5313', 12), ('CAST', 'M5313', 13), ('CAST', 'M5313', 14),
                          ('CAST', 'M5313', 15), ('CAST', 'M5313', 16), ('JF1', 'M5114', 6), ('JF1', 'M5114', 7),
                          ('JF1', 'M5114', 8),  # ('JF1', 'M5114', 9),
                          ('JF1', 'M5214', 13), ('JF1', 'M5214', 15), ('JF1', 'M6214', 13), ('JF1', 'M6214', 14),
                          ('JF1', 'M6314', 11), ('JF1', 'M7214', 7), ('MOLF', 'M2215', 6), ('MOLF', 'M2215', 7),
                          ('MOLF', 'M2215', 8), ('MOLF', 'M2215', 9), ('MOLF', 'M2215', 10), ('MOLF', 'M5115', 6),
                          ('MOLF', 'M5315', 5), ('MOLF', 'M5315', 6), ('MOLF', 'M6115', 5), ('MOLF', 'M6215', 5),
                          ('MOLF', 'M6215', 6), ('MOLF', 'M6315', 11), ('MOLF', 'M6315', 12), ('MOLF', 'M6315', 14),
                          ('MOLF', 'M6315', 16), ('MOLF', 'M7115', 8), ('MOLF', 'M7115', 9), ('MOLF', 'M7115', 11),
                          ('MOLF', 'M7115', 12), ('MOLF', 'M7115', 14), ('MOLF', 'M7215', 5), ('MOLF', 'M7215', 6),
                          ('MOLF', 'M7215', 7), ('MOLF', 'M7215', 8), ('MOLF', 'M7215', 9), ('MOLF', 'M7215', 10),
                          ('MOLF', 'M7215', 11), ('MOLF', 'M7215', 12), ('SPRET', 'M6616', 5), ('SPRET', 'M6616', 14),
                          ('SPRET', 'M6616', 7), ('SPRET', 'M6616', 10), ('SPRET', 'M6616', 11), ('SPRET', 'M6616', 16),
                          ('SPRET', 'M6716', 11), ('SPRET', 'M6716', 12), ('SPRET', 'M6716', 13),
                          ('SPRET', 'M6716', 14), ('SPRET', 'M6716', 15), ('SPRET', 'M6716', 16), ('SPRET', 'M6816', 5),
                          ('SPRET', 'M6816', 16), ('SPRET', 'M6916', 8), ('SPRET', 'M6916', 10), ('SPRET', 'M7116', 14),
                          ('SPRET', 'M7116', 15), ('SPRET', 'M7116', 16)],
               mice=[('C57BL6J', 'M3101'), ('BALB', 'M5202'), ('BALB', 'M7102'), ('BALB', 'M8202'), ('129S1', 'M3104'),
                     ('129S1', 'M2204'), ('129S1', 'M3204'), ('DBA', 'M7105'), ('DBA', 'M6105'), ('C3H', 'M2106'),
                     ('C3H', 'M5106'), ('WSB', 'M4211'), ('WSB', 'M5311'), ('CZECH', 'M3112'), ('CAST', 'M8613'),
                     ('MOLF', 'M2115'), ('MOLF', 'M6415'), ('SPRET', 'M3116'), ('SPRET', 'M6516'), ('SPRET', 'M6216'),
                     ('SPRET', 'M7316')]
           )}
