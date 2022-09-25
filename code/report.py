import csv
import matplotlib.pyplot as plt
from itertools import compress

doGANIndices = []
with open("GAN_probability_report_exp_Elena_4.5_duration.csv", "r") as f:
	reader = csv.reader(f, delimiter=",")
	
	# Skip header
	next(reader, None)

	# gtAndTrue = 0
	# gtAndFalse = 0
	# ltAndTrue = 0
	# ltAndFalse = 0


	sids = []
	pDoGANs = []
	# isRBs = []
	durations = []
	doGANs = []

	# header = ['Sentence_id', 'DoGAN probability', 'Sentence Duration', 'Do GAN']
	for i, row in enumerate(reader):
		sid, pDoGAN, duration, doGAN = row

		# Cast values
		sid = int(sid)
		pDoGAN = float(pDoGAN)
		# isRB = bool(isRB)
		duration = float(duration)
		if doGAN == "True":
			doGAN = True
		else:
			doGAN = False

		# if pDoGAN >= 0.5 and doGAN:
		# 	gtAndTrue = gtAndTrue + 1
		# elif pDoGAN >= 0.5 and not doGAN:
		# 	gtAndFalse = gtAndFalse + 1
		# elif pDoGAN < 0.5 and doGAN:
		# 	ltAndTrue = ltAndTrue + 1
		# elif pDoGAN < 0.5 and not doGAN:
		# 	ltAndFalse = ltAndFalse + 1

		sids.append(sid)
		pDoGANs.append(pDoGAN)
		# isRBs.append(isRB)
		durations.append(duration)
		doGANs.append(doGAN)

		# if pDoGAN <= 0.25:
		# 	print("TODO")

		# elif pDoGAN > 0.25 and pDoGAN <= 0.5:
		# 	print("TODO")
		
		# elif pDoGAN > 0.5 and pDoGAN <= 0.75:
		# 	print("TODO")

		# elif pDoGAN > 0.75 and pDoGAN <=1:
		# 	print("TODO")

# print("Greater and True: %d.\nGreater and False: %d.\nLower and True: %d.\nLower and False: %d" % (gtAndTrue, gtAndFalse, ltAndTrue, ltAndFalse))

# Probabilities of True values

pTrue = list(compress(pDoGANs, doGANs))
pFalse = list(compress(pDoGANs, [not x for x in doGANs]))

# print(pTrue)
plt.subplot(2, 1, 1)
plt.ylim((0, 500))
plt.title("Histogram of probabilites of True cases")
tHist = plt.hist(pTrue, 20)
plt.subplot(2, 1, 2)
plt.ylim((0, 500))
plt.title("Histogram of probabilites of False cases")
fHist = plt.hist(pFalse, 20)

plt.show()