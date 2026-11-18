WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)
def insert():
  file=input("Insert filename:")
  print(f'Reading file {file}.')
  filehandler=open(file,"r")
  filehandler.readline()
  listtimestamp=[]
  for line in filehandler:
    line=line.rstrip("\n")
    if line != "":
      index=line.split(";")
      timestamp={}
      timestamp["weekday"]=index[0]
      timestamp["hour"]=float(index[1])
      timestamp["consumption"]=float(index[2])
      timestamp["price"]=float(index[3])
      timestamp["total"] = timestamp["price"]*timestamp["consumption"]
      listtimestamp.append(timestamp)
  filehandler.close() 
  return listtimestamp
def analyse(listt):
  usage=[0,0,0,0,0,0,0]
  cost=[0,0,0,0,0,0,0]
  results=[]
  print("Analysing timestamps.")
  for line in listt:
    for i in range(len(WEEKDAYS)):
      if line["weekday"]==WEEKDAYS[i]:
        usage[i]+= line["consumption"]
        cost[i]+= line["total"]
  for i in range (7):
    results.append(F" - {WEEKDAYS[i]} usage {usage[i]} kWh, cost {cost[i]} ")      
  return results  
def display(result):
  print("### Electricity consumption summary ###")
  for i in range (7):
    print(result[i])
  print("### Electricity consumption summary ###")


def main():
  print("Program starting.")
  file=insert()
  analysed=analyse(file)
  displayy=display(analysed)
  print("Program ending.")
main()  