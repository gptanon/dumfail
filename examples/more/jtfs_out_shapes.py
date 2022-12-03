# -*- coding: utf-8 -*-
"""
JTFS Output Shapes
==================
Show coefficient access syntax and their shapes for all `out_type` and `out_3D`.
"""
###############################################################################
# Import the necessary packages
# -----------------------------

import numpy as np
from wavespin.numpy import TimeFrequencyScattering1D

##############################################################################
# Define shapes reporter
# ----------------------
def print_shapes_jtfs(out, out_type, out_3D):
    assert out_type in ('array', 'list', 'dict:array', 'dict:list'), out_type

    if out_type == 'dict:array':
        # e.g. `out['psi_t * psi_f_up'].shape`
        for pair in out:
            print("{} -- {}".format(out[pair].shape, pair))

    elif out_type == 'dict:list':
        # e.g. `out['psi_t * psi_f_up'][0]['coef'].shape`
        for pair in out:
            print("\n{}".format(pair))
            for i, c in enumerate(out[pair]):
                print(i, c['coef'].shape)
    else:
        if out_3D:
            o0, o1 = out

            if out_type == 'array':
                # e.g. `out[0].shape`
                print(("{} -- S0 & S1\n"
                       "{} -- joint").format(o0.shape, o1.shape))

            elif out_type == 'list':
                # e.g. `out[0][0]['coef'].shape`
                print("\nS0 & S1")
                for o in o0:
                    print(i, c['coef'].shape)
                print("\njoint")
                for o in o1:
                    print(i, c['coef'].shape)

        else:
            if out_type == 'array':
                # `out.shape`
                print(out.shape)

            elif out_type == 'list':
                # e.g. `out[0]['coef'].shape`
                for i, c in enumerate(out):
                    print(i, c['coef'].shape)

#%%############################################################################
# Setup & run
# -----------

N = 512
x = np.ones(N)

for out_3D in (False, True):
    print("\n====", "out_3D=%s" % out_3D, "=" * 60)
    jtfs = TimeFrequencyScattering1D(N, out_3D=out_3D, average_fr=1)

    for out_type in ('list', 'array', 'dict:list', 'dict:array'):
        print("\n----", out_type, "-" * 60)
        jtfs.out_type = out_type
        out = jtfs(x)

        print_shapes_jtfs(out, out_type, out_3D)

# For ease of reading, we manually split `out_3D` cases below

#%%###########################################################################
# `out_3D=False` example output
# -----------------------------
_ = """
---- list ------------------------------------------------------------
0 (1, 1, 4)
1 (1, 1, 4)
2 (1, 1, 4)
3 (1, 1, 4)
4 (1, 1, 4)
5 (1, 1, 4)
6 (1, 1, 4)
7 (1, 1, 4)
8 (1, 1, 4)
9 (1, 1, 4)
10 (1, 1, 4)
11 (1, 1, 4)
12 (1, 1, 4)
13 (1, 1, 4)
14 (1, 1, 4)
15 (1, 1, 4)
16 (1, 1, 4)
17 (1, 1, 4)
18 (1, 1, 4)
19 (1, 1, 4)
20 (1, 1, 4)
21 (1, 1, 4)
22 (1, 1, 4)
23 (1, 1, 4)
24 (1, 1, 4)
25 (1, 1, 4)
26 (1, 1, 4)
27 (1, 1, 4)
28 (1, 1, 4)
29 (1, 1, 4)
30 (1, 1, 4)
31 (1, 1, 4)
32 (1, 1, 4)
33 (1, 1, 4)
34 (1, 1, 4)
35 (1, 1, 4)
36 (1, 1, 4)
37 (1, 1, 4)
38 (1, 1, 4)
39 (1, 1, 4)
40 (1, 1, 4)
41 (1, 1, 4)
42 (1, 1, 4)
43 (1, 1, 4)
44 (1, 1, 4)
45 (1, 1, 4)
46 (1, 6, 4)
47 (1, 6, 4)
48 (1, 6, 4)
49 (1, 6, 4)
50 (1, 6, 4)
51 (1, 6, 4)
52 (1, 6, 4)
53 (1, 6, 4)
54 (1, 6, 4)
55 (1, 6, 4)
56 (1, 1, 4)
57 (1, 2, 4)
58 (1, 3, 4)
59 (1, 4, 4)
60 (1, 6, 4)
61 (1, 6, 4)
62 (1, 6, 4)
63 (1, 1, 4)
64 (1, 1, 4)
65 (1, 1, 4)
66 (1, 1, 4)
67 (1, 2, 4)
68 (1, 2, 4)
69 (1, 2, 4)
70 (1, 2, 4)
71 (1, 2, 4)
72 (1, 3, 4)
73 (1, 3, 4)
74 (1, 3, 4)
75 (1, 3, 4)
76 (1, 3, 4)
77 (1, 3, 4)
78 (1, 3, 4)
79 (1, 3, 4)
80 (1, 4, 4)
81 (1, 4, 4)
82 (1, 4, 4)
83 (1, 4, 4)
84 (1, 4, 4)
85 (1, 4, 4)
86 (1, 4, 4)
87 (1, 4, 4)
88 (1, 6, 4)
89 (1, 6, 4)
90 (1, 6, 4)
91 (1, 6, 4)
92 (1, 6, 4)
93 (1, 6, 4)
94 (1, 6, 4)
95 (1, 6, 4)
96 (1, 6, 4)
97 (1, 6, 4)
98 (1, 6, 4)
99 (1, 6, 4)
100 (1, 6, 4)
101 (1, 6, 4)
102 (1, 6, 4)
103 (1, 6, 4)
104 (1, 6, 4)
105 (1, 6, 4)
106 (1, 6, 4)
107 (1, 6, 4)
108 (1, 6, 4)
109 (1, 6, 4)
110 (1, 6, 4)
111 (1, 6, 4)
112 (1, 6, 4)
113 (1, 6, 4)
114 (1, 6, 4)
115 (1, 1, 4)
116 (1, 1, 4)
117 (1, 1, 4)
118 (1, 1, 4)
119 (1, 2, 4)
120 (1, 2, 4)
121 (1, 2, 4)
122 (1, 2, 4)
123 (1, 2, 4)
124 (1, 3, 4)
125 (1, 3, 4)
126 (1, 3, 4)
127 (1, 3, 4)
128 (1, 3, 4)
129 (1, 3, 4)
130 (1, 3, 4)
131 (1, 3, 4)
132 (1, 4, 4)
133 (1, 4, 4)
134 (1, 4, 4)
135 (1, 4, 4)
136 (1, 4, 4)
137 (1, 4, 4)
138 (1, 4, 4)
139 (1, 4, 4)
140 (1, 6, 4)
141 (1, 6, 4)
142 (1, 6, 4)
143 (1, 6, 4)
144 (1, 6, 4)
145 (1, 6, 4)
146 (1, 6, 4)
147 (1, 6, 4)
148 (1, 6, 4)
149 (1, 6, 4)
150 (1, 6, 4)
151 (1, 6, 4)
152 (1, 6, 4)
153 (1, 6, 4)
154 (1, 6, 4)
155 (1, 6, 4)
156 (1, 6, 4)
157 (1, 6, 4)
158 (1, 6, 4)
159 (1, 6, 4)
160 (1, 6, 4)
161 (1, 6, 4)
162 (1, 6, 4)
163 (1, 6, 4)
164 (1, 6, 4)
165 (1, 6, 4)
166 (1, 6, 4)

---- array ------------------------------------------------------------
(1, 598, 4)

---- dict:list ------------------------------------------------------------

S0
0 (1, 1, 4)

S1
0 (1, 1, 4)
1 (1, 1, 4)
2 (1, 1, 4)
3 (1, 1, 4)
4 (1, 1, 4)
5 (1, 1, 4)
6 (1, 1, 4)
7 (1, 1, 4)
8 (1, 1, 4)
9 (1, 1, 4)
10 (1, 1, 4)
11 (1, 1, 4)
12 (1, 1, 4)
13 (1, 1, 4)
14 (1, 1, 4)
15 (1, 1, 4)
16 (1, 1, 4)
17 (1, 1, 4)
18 (1, 1, 4)
19 (1, 1, 4)
20 (1, 1, 4)
21 (1, 1, 4)
22 (1, 1, 4)
23 (1, 1, 4)
24 (1, 1, 4)
25 (1, 1, 4)
26 (1, 1, 4)
27 (1, 1, 4)
28 (1, 1, 4)
29 (1, 1, 4)
30 (1, 1, 4)
31 (1, 1, 4)
32 (1, 1, 4)
33 (1, 1, 4)
34 (1, 1, 4)
35 (1, 1, 4)
36 (1, 1, 4)
37 (1, 1, 4)
38 (1, 1, 4)
39 (1, 1, 4)
40 (1, 1, 4)
41 (1, 1, 4)
42 (1, 1, 4)
43 (1, 1, 4)
44 (1, 1, 4)

phi_t * phi_f
0 (1, 6, 4)

phi_t * psi_f
0 (1, 6, 4)
1 (1, 6, 4)
2 (1, 6, 4)
3 (1, 6, 4)
4 (1, 6, 4)
5 (1, 6, 4)
6 (1, 6, 4)
7 (1, 6, 4)
8 (1, 6, 4)

psi_t * phi_f
0 (1, 1, 4)
1 (1, 2, 4)
2 (1, 3, 4)
3 (1, 4, 4)
4 (1, 6, 4)
5 (1, 6, 4)
6 (1, 6, 4)

psi_t * psi_f_up
0 (1, 1, 4)
1 (1, 1, 4)
2 (1, 1, 4)
3 (1, 1, 4)
4 (1, 2, 4)
5 (1, 2, 4)
6 (1, 2, 4)
7 (1, 2, 4)
8 (1, 2, 4)
9 (1, 3, 4)
10 (1, 3, 4)
11 (1, 3, 4)
12 (1, 3, 4)
13 (1, 3, 4)
14 (1, 3, 4)
15 (1, 3, 4)
16 (1, 3, 4)
17 (1, 4, 4)
18 (1, 4, 4)
19 (1, 4, 4)
20 (1, 4, 4)
21 (1, 4, 4)
22 (1, 4, 4)
23 (1, 4, 4)
24 (1, 4, 4)
25 (1, 6, 4)
26 (1, 6, 4)
27 (1, 6, 4)
28 (1, 6, 4)
29 (1, 6, 4)
30 (1, 6, 4)
31 (1, 6, 4)
32 (1, 6, 4)
33 (1, 6, 4)
34 (1, 6, 4)
35 (1, 6, 4)
36 (1, 6, 4)
37 (1, 6, 4)
38 (1, 6, 4)
39 (1, 6, 4)
40 (1, 6, 4)
41 (1, 6, 4)
42 (1, 6, 4)
43 (1, 6, 4)
44 (1, 6, 4)
45 (1, 6, 4)
46 (1, 6, 4)
47 (1, 6, 4)
48 (1, 6, 4)
49 (1, 6, 4)
50 (1, 6, 4)
51 (1, 6, 4)

psi_t * psi_f_dn
0 (1, 1, 4)
1 (1, 1, 4)
2 (1, 1, 4)
3 (1, 1, 4)
4 (1, 2, 4)
5 (1, 2, 4)
6 (1, 2, 4)
7 (1, 2, 4)
8 (1, 2, 4)
9 (1, 3, 4)
10 (1, 3, 4)
11 (1, 3, 4)
12 (1, 3, 4)
13 (1, 3, 4)
14 (1, 3, 4)
15 (1, 3, 4)
16 (1, 3, 4)
17 (1, 4, 4)
18 (1, 4, 4)
19 (1, 4, 4)
20 (1, 4, 4)
21 (1, 4, 4)
22 (1, 4, 4)
23 (1, 4, 4)
24 (1, 4, 4)
25 (1, 6, 4)
26 (1, 6, 4)
27 (1, 6, 4)
28 (1, 6, 4)
29 (1, 6, 4)
30 (1, 6, 4)
31 (1, 6, 4)
32 (1, 6, 4)
33 (1, 6, 4)
34 (1, 6, 4)
35 (1, 6, 4)
36 (1, 6, 4)
37 (1, 6, 4)
38 (1, 6, 4)
39 (1, 6, 4)
40 (1, 6, 4)
41 (1, 6, 4)
42 (1, 6, 4)
43 (1, 6, 4)
44 (1, 6, 4)
45 (1, 6, 4)
46 (1, 6, 4)
47 (1, 6, 4)
48 (1, 6, 4)
49 (1, 6, 4)
50 (1, 6, 4)
51 (1, 6, 4)

---- dict:array ------------------------------------------------------------
(1, 1, 4) -- S0
(1, 45, 4) -- S1
(1, 6, 4) -- phi_t * phi_f
(1, 54, 4) -- phi_t * psi_f
(1, 28, 4) -- psi_t * phi_f
(1, 232, 4) -- psi_t * psi_f_up
(1, 232, 4) -- psi_t * psi_f_dn
"""

#%%###########################################################################
# `out_3D=True` example output
# ----------------------------
_ = """
---- list ------------------------------------------------------------

S0 & S1
0 (1, 1, 4)
1 (1, 1, 4)
2 (1, 1, 4)
3 (1, 1, 4)
4 (1, 1, 4)
5 (1, 1, 4)
6 (1, 1, 4)
7 (1, 1, 4)
8 (1, 1, 4)
9 (1, 1, 4)
10 (1, 1, 4)
11 (1, 1, 4)
12 (1, 1, 4)
13 (1, 1, 4)
14 (1, 1, 4)
15 (1, 1, 4)
16 (1, 1, 4)
17 (1, 1, 4)
18 (1, 1, 4)
19 (1, 1, 4)
20 (1, 1, 4)
21 (1, 1, 4)
22 (1, 1, 4)
23 (1, 1, 4)
24 (1, 1, 4)
25 (1, 1, 4)
26 (1, 1, 4)
27 (1, 1, 4)
28 (1, 1, 4)
29 (1, 1, 4)
30 (1, 1, 4)
31 (1, 1, 4)
32 (1, 1, 4)
33 (1, 1, 4)
34 (1, 1, 4)
35 (1, 1, 4)
36 (1, 1, 4)
37 (1, 1, 4)
38 (1, 1, 4)
39 (1, 1, 4)
40 (1, 1, 4)
41 (1, 1, 4)
42 (1, 1, 4)
43 (1, 1, 4)
44 (1, 1, 4)
45 (1, 1, 4)

joint
0 (1, 6, 4)
1 (1, 6, 4)
2 (1, 6, 4)
3 (1, 6, 4)
4 (1, 6, 4)
5 (1, 6, 4)
6 (1, 6, 4)
7 (1, 6, 4)
8 (1, 6, 4)
9 (1, 6, 4)
10 (1, 6, 4)
11 (1, 6, 4)
12 (1, 6, 4)
13 (1, 6, 4)
14 (1, 6, 4)
15 (1, 6, 4)
16 (1, 6, 4)
17 (1, 6, 4)
18 (1, 6, 4)
19 (1, 6, 4)
20 (1, 6, 4)
21 (1, 6, 4)
22 (1, 6, 4)
23 (1, 6, 4)
24 (1, 6, 4)
25 (1, 6, 4)
26 (1, 6, 4)
27 (1, 6, 4)
28 (1, 6, 4)
29 (1, 6, 4)
30 (1, 6, 4)
31 (1, 6, 4)
32 (1, 6, 4)
33 (1, 6, 4)
34 (1, 6, 4)
35 (1, 6, 4)
36 (1, 6, 4)
37 (1, 6, 4)
38 (1, 6, 4)
39 (1, 6, 4)
40 (1, 6, 4)
41 (1, 6, 4)
42 (1, 6, 4)
43 (1, 6, 4)
44 (1, 6, 4)
45 (1, 6, 4)
46 (1, 6, 4)
47 (1, 6, 4)
48 (1, 6, 4)
49 (1, 6, 4)
50 (1, 6, 4)
51 (1, 6, 4)
52 (1, 6, 4)
53 (1, 6, 4)
54 (1, 6, 4)
55 (1, 6, 4)
56 (1, 6, 4)
57 (1, 6, 4)
58 (1, 6, 4)
59 (1, 6, 4)
60 (1, 6, 4)
61 (1, 6, 4)
62 (1, 6, 4)
63 (1, 6, 4)
64 (1, 6, 4)
65 (1, 6, 4)
66 (1, 6, 4)
67 (1, 6, 4)
68 (1, 6, 4)
69 (1, 6, 4)
70 (1, 6, 4)
71 (1, 6, 4)
72 (1, 6, 4)
73 (1, 6, 4)
74 (1, 6, 4)
75 (1, 6, 4)
76 (1, 6, 4)
77 (1, 6, 4)
78 (1, 6, 4)
79 (1, 6, 4)
80 (1, 6, 4)
81 (1, 6, 4)
82 (1, 6, 4)
83 (1, 6, 4)
84 (1, 6, 4)
85 (1, 6, 4)
86 (1, 6, 4)
87 (1, 6, 4)
88 (1, 6, 4)
89 (1, 6, 4)
90 (1, 6, 4)
91 (1, 6, 4)
92 (1, 6, 4)
93 (1, 6, 4)
94 (1, 6, 4)
95 (1, 6, 4)
96 (1, 6, 4)
97 (1, 6, 4)
98 (1, 6, 4)
99 (1, 6, 4)
100 (1, 6, 4)
101 (1, 6, 4)
102 (1, 6, 4)
103 (1, 6, 4)
104 (1, 6, 4)
105 (1, 6, 4)
106 (1, 6, 4)
107 (1, 6, 4)
108 (1, 6, 4)
109 (1, 6, 4)
110 (1, 6, 4)
111 (1, 6, 4)
112 (1, 6, 4)
113 (1, 6, 4)
114 (1, 6, 4)
115 (1, 6, 4)
116 (1, 6, 4)
117 (1, 6, 4)
118 (1, 6, 4)
119 (1, 6, 4)
120 (1, 6, 4)

---- array ------------------------------------------------------------
(1, 46, 4) -- S0 & S1
(1, 121, 6, 4) -- joint

---- dict:list ------------------------------------------------------------

S0
0 (1, 1, 4)

S1
0 (1, 1, 4)
1 (1, 1, 4)
2 (1, 1, 4)
3 (1, 1, 4)
4 (1, 1, 4)
5 (1, 1, 4)
6 (1, 1, 4)
7 (1, 1, 4)
8 (1, 1, 4)
9 (1, 1, 4)
10 (1, 1, 4)
11 (1, 1, 4)
12 (1, 1, 4)
13 (1, 1, 4)
14 (1, 1, 4)
15 (1, 1, 4)
16 (1, 1, 4)
17 (1, 1, 4)
18 (1, 1, 4)
19 (1, 1, 4)
20 (1, 1, 4)
21 (1, 1, 4)
22 (1, 1, 4)
23 (1, 1, 4)
24 (1, 1, 4)
25 (1, 1, 4)
26 (1, 1, 4)
27 (1, 1, 4)
28 (1, 1, 4)
29 (1, 1, 4)
30 (1, 1, 4)
31 (1, 1, 4)
32 (1, 1, 4)
33 (1, 1, 4)
34 (1, 1, 4)
35 (1, 1, 4)
36 (1, 1, 4)
37 (1, 1, 4)
38 (1, 1, 4)
39 (1, 1, 4)
40 (1, 1, 4)
41 (1, 1, 4)
42 (1, 1, 4)
43 (1, 1, 4)
44 (1, 1, 4)

phi_t * phi_f
0 (1, 6, 4)

phi_t * psi_f
0 (1, 6, 4)
1 (1, 6, 4)
2 (1, 6, 4)
3 (1, 6, 4)
4 (1, 6, 4)
5 (1, 6, 4)
6 (1, 6, 4)
7 (1, 6, 4)
8 (1, 6, 4)

psi_t * phi_f
0 (1, 6, 4)
1 (1, 6, 4)
2 (1, 6, 4)
3 (1, 6, 4)
4 (1, 6, 4)
5 (1, 6, 4)
6 (1, 6, 4)

psi_t * psi_f_up
0 (1, 6, 4)
1 (1, 6, 4)
2 (1, 6, 4)
3 (1, 6, 4)
4 (1, 6, 4)
5 (1, 6, 4)
6 (1, 6, 4)
7 (1, 6, 4)
8 (1, 6, 4)
9 (1, 6, 4)
10 (1, 6, 4)
11 (1, 6, 4)
12 (1, 6, 4)
13 (1, 6, 4)
14 (1, 6, 4)
15 (1, 6, 4)
16 (1, 6, 4)
17 (1, 6, 4)
18 (1, 6, 4)
19 (1, 6, 4)
20 (1, 6, 4)
21 (1, 6, 4)
22 (1, 6, 4)
23 (1, 6, 4)
24 (1, 6, 4)
25 (1, 6, 4)
26 (1, 6, 4)
27 (1, 6, 4)
28 (1, 6, 4)
29 (1, 6, 4)
30 (1, 6, 4)
31 (1, 6, 4)
32 (1, 6, 4)
33 (1, 6, 4)
34 (1, 6, 4)
35 (1, 6, 4)
36 (1, 6, 4)
37 (1, 6, 4)
38 (1, 6, 4)
39 (1, 6, 4)
40 (1, 6, 4)
41 (1, 6, 4)
42 (1, 6, 4)
43 (1, 6, 4)
44 (1, 6, 4)
45 (1, 6, 4)
46 (1, 6, 4)
47 (1, 6, 4)
48 (1, 6, 4)
49 (1, 6, 4)
50 (1, 6, 4)
51 (1, 6, 4)

psi_t * psi_f_dn
0 (1, 6, 4)
1 (1, 6, 4)
2 (1, 6, 4)
3 (1, 6, 4)
4 (1, 6, 4)
5 (1, 6, 4)
6 (1, 6, 4)
7 (1, 6, 4)
8 (1, 6, 4)
9 (1, 6, 4)
10 (1, 6, 4)
11 (1, 6, 4)
12 (1, 6, 4)
13 (1, 6, 4)
14 (1, 6, 4)
15 (1, 6, 4)
16 (1, 6, 4)
17 (1, 6, 4)
18 (1, 6, 4)
19 (1, 6, 4)
20 (1, 6, 4)
21 (1, 6, 4)
22 (1, 6, 4)
23 (1, 6, 4)
24 (1, 6, 4)
25 (1, 6, 4)
26 (1, 6, 4)
27 (1, 6, 4)
28 (1, 6, 4)
29 (1, 6, 4)
30 (1, 6, 4)
31 (1, 6, 4)
32 (1, 6, 4)
33 (1, 6, 4)
34 (1, 6, 4)
35 (1, 6, 4)
36 (1, 6, 4)
37 (1, 6, 4)
38 (1, 6, 4)
39 (1, 6, 4)
40 (1, 6, 4)
41 (1, 6, 4)
42 (1, 6, 4)
43 (1, 6, 4)
44 (1, 6, 4)
45 (1, 6, 4)
46 (1, 6, 4)
47 (1, 6, 4)
48 (1, 6, 4)
49 (1, 6, 4)
50 (1, 6, 4)
51 (1, 6, 4)

---- dict:array ------------------------------------------------------------
(1, 1, 4) -- S0
(1, 45, 4) -- S1
(1, 1, 6, 4) -- phi_t * phi_f
(1, 9, 6, 4) -- phi_t * psi_f
(1, 7, 6, 4) -- psi_t * phi_f
(1, 52, 6, 4) -- psi_t * psi_f_up
(1, 52, 6, 4) -- psi_t * psi_f_dn
"""
