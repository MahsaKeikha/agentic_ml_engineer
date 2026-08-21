class ExperimentMemory:
 def __init__(self):self.records=[]
 def add(self,record):self.records.append(record)
 def snapshot(self):return list(self.records)
