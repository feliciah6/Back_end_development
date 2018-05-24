from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/grader')
def mark(marks="0"):
  marks=int(request.args.get('marks',marks))
  total_marks = int(marks)
  if marks>71:
    return "for marks {} the grade  is A".format(marks,total_marks)
  elif marks>61:
    return "for marks {} the grade  is B".format(marks,total_marks)
  elif marks>51:
    return "for marks {} the grade  is C".format(marks,total_marks)
  else:
    return "for marks {} the grade  is D".format(marks,total_marks)
  
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

