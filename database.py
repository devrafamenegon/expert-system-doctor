BD=[
  {"DOENCA":"GRIPE","SINTOMAS": {"TOSSE":5,"FEBRE":7,"DOR GARGANTA":8,"CORIZA":6,"FADIGA":3},"OCORRENCIAS": 0,"PERCENTUAL":0},
  {"DOENCA":"DENGUE","SINTOMAS": {"FEBRE":9,"DOR CORPO":8,"MANCHAS CORPO":5},"OCORRENCIAS": 0,"PERCENTUAL":0},   
  {"DOENCA":"COVID","SINTOMAS": {"FEBRE":9,"TOSSE":9,"CORIZA":4,"CANSACO":8,"PERDA PALADAR":7},"OCORRENCIAS": 0,"PERCENTUAL":0},
  {"DOENCA":"DIABETES","SINTOMAS": {"DOR CORPO":5,"MANCHAS CORPO":3,"PERDA PESO":6,"SEDE":9,"FADIGA":8},"OCORRENCIAS": 0,"PERCENTUAL":0}
]

def zerar_ocorrencias():
  for i in BD:
    i["OCORRENCIAS"]=0
    i["PERCENTUAL"]=0