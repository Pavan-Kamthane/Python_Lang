def toh(n,source,helper,destination):
  if(n==1):
    print("the disk will move from ",source," to ",destination)
    return
  toh(n-1,source,helper,destination)
  print("the disk ", n, " will move from ",source," to ",destination)
  toh(n-1,helper,destination,source)
n=4
toh(n,source,helper,destination)
