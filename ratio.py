import cPickle as pickle


data_dir = "/Volumes/Transcend/database/"
g = pickle.load(open(data_dir + "G.pk", "rb"))

totaltrip=0
tripfromi=0
for i in range(75):
    for j in range(75):
        totaltrip=totaltrip+g[10][i][j][0]


for j in range(75):
    tripfromi=tripfromi+g[10][6][j][0]


print totaltrip,tripfromi

ratio=float(tripfromi)/float(totaltrip)
refnum=float(1)/float(75)

print "ratio:",ratio
print "refnum:",refnum
