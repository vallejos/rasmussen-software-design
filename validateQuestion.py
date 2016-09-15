# filename validateQuestion.py

# The validateQuestion module takes "data" as an argument and "valid" as an 
# argument by reference. This modules validates if "data" is a correct answer
# to a "yes" or "no" question, returning in "valid" the result.

def validateQuestion(data, valid):
  
  if ((data.lower() == "yes") or (data.lower() == "no")):
    valid = True
  else:
    valid = False

  return valid

#End module
