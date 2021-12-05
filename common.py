# функция проверки и преобразования строки в число

def chislo(str_1, num=1):
  """ 
  num = 1 целое положительное
  num = 2 целое
  num = 3 дробное положительное
  num = 4 дробное
  
  """
  if num == 1:
    try:
      return int(str_1) if int(str_1)>=0 else -int(str_1)
    except:
      return None
  elif num == 2:
    try:
      return int(str_1)
    except:
      return None
  elif num == 3:
    try:
      return float(str_1) if float(str_1)>=0 else -float(str_1)
    except:
      return None  
  elif num == 4:
    try:
      return float(str_1)
    except:
      return None
 
    
    