R1 = [(1,1), (1,4), (2,1), (2,2), (2,4), (3,1), (3,2), (3,3), (4,4)]
R2 = [(1,1), (1,4), (2,2), (2,3), (3,4), (3,1), (3,2), (3,3), (4,4)]

R1_inverse = [(b, a) for (a, b) in R1]
R2_inverse = [(b, a) for (a, b) in R2]

print("R1 Inverse:", (R1_inverse))
print("R2 Inverse:", (R2_inverse))

def compose_relations(R1_inverse, R2_inverse):
  result = set()
  for a, b in R2_inverse:
    for c, d in R1_inverse:
      if b == c:
        result.add((a, d))
  return result

print("R1 o R2:", compose_relations(R1_inverse, R2_inverse))