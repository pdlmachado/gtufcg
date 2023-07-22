from emoji import emojize

right_answer = emojize(":check_mark_button:")
wrong_answer = emojize(":cross_mark:")
wait_answer = emojize(":white_question_mark:")

def check_answer_int(R,E):
  if R == 0:
    return wait_answer 
  elif R==E:
    return right_answer
  else:
    return wrong_answer

def check_boxes(R,E):
  out = []
  for i in range(len(R)):
    if R[i] == E[i]:
      out.append(right_answer)
    else:
      out.append(wrong_answer)
  return out
