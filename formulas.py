def strassen_estimate(n):
  if n == 1:
    return 1
  else:
    return 7*(strassen_estimate(n/2)) + pow(n,2)  