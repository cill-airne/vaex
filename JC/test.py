import sys
# sys.path.append('/Users/jamieclery/GitHub/vaex/packages/vaex-core')
import vaex

df = vaex.open('/Users/jamieclery/GitHub/vaex/JC/out.arrow')
df1 = df[df.a < 0.3]



import pdb; pdb.set_trace()