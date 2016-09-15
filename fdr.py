#!/home/yar2/default/bin/python -u
from __future__ import print_function, division
import numpy as np
from scipy import stats
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-z', action='store_true', default=False,
        help='treat input numbers as Z scores for a one-sided test')
parser.add_argument('-h', action='store_true', default=False,
        help='treat first line of each input stream as header')
parser.add_argument('--threshold', type=float, default = 0.05)
parser.add_argument('files', nargs='*', default=['/dev/stdin'])
#TODO. will require a parameter to specify p-value column
# parser.add_argument('-l', action='store_true', default=False,
#         help='print all lines that pass significance, rather than just the threshold')
args = parser.parse_args()

for name in args.files:
    f = open(name):
        for line in f.readlines():
            print(line)
# if args.zscores is not None:
#     z = np.array(map(float, open(args.zscores).readlines()))
#     p = stats.norm.sf(z)
# else:
#     p = np.array(map(float, open(args.pvals).readlines()))
# p.sort()
# c = np.arange(1,len(p)+1)*args.threshold/len(p)
# cutoff_fdr = np.inf
# for i in range(len(p)):
#     if p[i] < c[i]:
#         cutoff_fdr = stats.norm.isf(p[i])
# print(cutoff_fdr)
