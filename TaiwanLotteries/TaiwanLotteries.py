"""












"""
from color_cmd import *
import pandas as pd
import json
import codecs
from pprint import pprint

class PowerColorCalculator:
	def __init__(self):
		#============================================
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
		#==============================================
		self.compute("XXX.json")


	def run(self,gain1,gain2,bet=100):
		self.Table["1"]["$"] = gain1
		self.Table["2"]["$"] = gain2
		op = 0.0
		for k in self.Table:
			if k not in "ALL":
				p = self.Table[k]["#"]/self.Table["ALL"]["#"]
				op += p*self.Table[k]["$"]
		print("RTP >= {:10f} % , EG >= {:10f}".format(100*op/bet,op-bet))

	def compute(self,jsonfile):
		self.P = {}
		self.totalP = {}
		with codecs.open(jsonfile, encoding='utf8') as f:
			j = json.load(f)["PowerColor6+1"]
			for k in j:
				for i in range(len(j[k])):
					pos = i+1
					if pos not in self.P:
						self.P[pos] = {}
					num = j[k][i]
					if num not in self.P[pos]:
						self.P[pos][num] = 0
					self.P[pos][num] += 1 
					if num not in self.totalP:
						self.totalP[num] = 0
					self.totalP[num] += 1

		# normalize 
		for pos in self.P:
			_sum = 0
			for num in self.P[pos]:
				_sum += self.P[pos][num]
			for num in self.P[pos]:
				self.P[pos][num] = self.P[pos][num]*100/_sum

		

	def show(self):
		pprint(self.totalP)
		for pos in range(1,7):
			print("======================================")
			print("第 {} 個位置, 理論:{:.4f} %".format(pos,100/(39-pos)))
			print("======================================")
			for num in range(1,39):
				if num in self.P[pos]:
					printGreen("({}):{:.4f} %".format(num,self.P[pos][num]),True)
				else:
					printRed("({}):{:.4f} %".format(num,0),True)
		print("======================================")
		print("特別區 , 理論:{:.4f}%".format(100/8))
		print("======================================")
		
		for i in range(1,9):
			print("({}):{:.4f}%".format(i,self.P[7][i]))

if __name__ == '__main__':
	machine = PowerColorCalculator()
	machine.show()
	
	