!pip install emoji
import emoji

def check_answer_int(R,E):
  if R == 0:
    return ""
  elif R==E:
    return emoji.emojize(":check_mark_button:")
  else:
    return emoji.emojize(":cross_mark:")

def check_boxes(R,E):
  out = []
  for i in range(len(R)):
    if R[i] == E[i]:
      out.append(True)
    else:
      out.append(False)
  return out

# Gabarito
E1 = 1
E2 = 1
E6 = 4
E7 = 1
E8 = [True, False, True, False]
