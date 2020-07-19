"""












"""

class PowerColorCalculator:
	def __init__(self):

		# 威力彩
		self.Table = {
			"1":{"#":1,"$":0},
			"2":{"#":7,"$":0},
			"3":{"#":192,"$":150000},
			"4":{"#":1344,"$":20000},
			"5":{"#":7440,"$":4000},
			"6":{"#":52080,"$":800},
			"7":{"#":99200,"$":400},
			"8":{"#":539400,"$":200},
			"9":{"#":694400,"$":100},
			"10":{"#":1208256,"$":100},
			"ALL":{"#":22085448}
		}

	def run(self,gain1,gain2,bet=100):
		self.Table["1"]["$"] = gain1
		self.Table["2"]["$"] = gain2
		op = 0.0
		for k in self.Table:
			if k not in "ALL":
				p = self.Table[k]["#"]/self.Table["ALL"]["#"]
				op += p*self.Table[k]["$"]
		print("RTP >= {:10f} % , EG >= {:10f}".format(100*op/bet,op-bet))


if __name__ == '__main__':
	PowerColorCalculator().run(gain1=89000000,gain2=11000000)
	PowerColorCalculator().run(gain1=1844988896/2,gain2=11000000)


