"""
	- 作者 : Plus & Minus 2020-05-09
	- 這是 Euler Squares - Numberphile  
		https://www.youtube.com/watch?v=qu04xLNrk94&t=1s
	
	- 使用 邏輯限制式建模(限制規劃) CP-Solver 4x4 窮舉結果 - 共 1152 組解

	(影片 3:47 的解)
	------------------------------
	solution [245]
	------------------------------
	C1,H13,S12,D11,
	D12,S11,H1,C13,
	H11,C12,D13,S1,
	S13,D1,C11,H12,  

		
	- pip 安裝指令 :  python3 -m pip install --upgrade --user ortools
"""

from ortools.constraint_solver import pywrapcp 



if __name__ == '__main__':

	_solver = pywrapcp.Solver("Euler_squares")
	#==============================================================================
	# 建立邏輯變數  位置 (i,j) 是撲克牌 (a1=花色,a2=數字) , n^4 種 {0,1} 
	_vars = {
		"{},{}={}{}".format(i,j,a1,a2):_solver.IntVar(0,1)
		for i in range(4) for j in range(4) for a1 in ["S","H","D","C"] for a2 in ["1","11","12","13"]
	}
	
	# ================================================================================
	# (1) 每個方格最多可以放一張牌
	for i in range(4):
		for j in range(4):
			_solver.Add(_solver.Sum(_vars["{},{}={}{}".format(i,j,a1,a2)] for a1 in ["S","H","D","C"] for a2 in ["1","11","12","13"] )==1)

	#===============================================================================
	# (2) 每張牌在所有方格上是唯一
	for a1 in ["S","H","D","C"]:
		for a2 in ["1","11","12","13"]:
			_solver.Add(_solver.Sum(_vars["{},{}={}{}".format(i,j,a1,a2)] for i in range(4) for j in range(4))==1)
	#===============================================================================
	# (3) 每一列 a1 唯一 , 每一列 a2 唯一
	for i in range(4):
		for a1 in ["S","H","D","C"]:
			_solver.Add(_solver.Sum(_vars["{},{}={}{}".format(i,j,a1,a2)] for j in range(4) for a2 in ["1","11","12","13"])==1)
		for a2 in ["1","11","12","13"]:
			_solver.Add(_solver.Sum(_vars["{},{}={}{}".format(i,j,a1,a2)] for j in range(4) for a1 in ["S","H","D","C"])==1)
	#===============================================================================
	# (4) 每一行 a1 唯一 , 每一行 a2 唯一
	for j in range(4):
		for a1 in ["S","H","D","C"]:
			_solver.Add(_solver.Sum(_vars["{},{}={}{}".format(i,j,a1,a2)] for i in range(4) for a2 in ["1","11","12","13"])==1)
		for a2 in ["1","11","12","13"]:	
			_solver.Add(_solver.Sum(_vars["{},{}={}{}".format(i,j,a1,a2)] for i in range(4) for a1 in ["S","H","D","C"])==1)


	#==================================================================================================================
	# (5) 對角線 (i,i) a1 唯一 , a2 唯一
	for a1 in ["S","H","D","C"]:	
		_solver.Add(_solver.Sum(_vars["{},{}={}{}".format(i,i,a1,a2)]  for i in range(4) for a2 in ["1","11","12","13"])==1)
	for a2 in ["1","11","12","13"]:	
		_solver.Add(_solver.Sum(_vars["{},{}={}{}".format(i,i,a1,a2)]  for i in range(4) for a1 in ["S","H","D","C"])==1)

	#===========================================================================================================
	# (6) 對角線 (i,n-i-1) a1 唯一 , a2 唯一
	for a1 in ["S","H","D","C"]:	
		_solver.Add(_solver.Sum(_vars["{},{}={}{}".format(i,4-i-1,a1,a2)]  for i in range(4) for a2 in ["1","11","12","13"])==1)
	for a2 in ["1","11","12","13"]:	
		_solver.Add(_solver.Sum(_vars["{},{}={}{}".format(i,4-i-1,a1,a2)]  for i in range(4) for a1 in ["S","H","D","C"])==1)
	#=============================================================================================
	

	# 窮舉初始設定 !!
	db = _solver.Phase(list(_vars.values()),_solver.INT_VAR_DEFAULT,_solver.INT_VALUE_DEFAULT)
	_solver.NewSearch(db)
	_count = 0
	while _solver.NextSolution():  #  開始窮舉下一個解
		_count +=1
		print("------------------------------")
		print("solution [{}]".format(_count))
		print("------------------------------")
		table = {}
		for name in _vars:
			# 只存 = 1 的解
			if(_vars[name].Value() == 1):
				pos,a = name.split("=")
				i , j =  pos.split(",")
				# 放到 table 上
				if int(i) not in table:
					table[int(i)] = {}
				table[int(i)][int(j)] = a
		# 列印解 !!
		for i in range(4):
			for j in range(4):
				print(table[i][j],end=",")
			print()
	



	
	