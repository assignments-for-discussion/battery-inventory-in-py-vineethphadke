def count_batteries_by_health(present_capacities):
  rated_capacity = 120
  healthy_count, exchange_count, failed_count = 0,0,0
  SoH =  0 
  for i in present_capacities:
    if(i<0 or i>120):   #checking boundary conditions
        continue
    SoH = 100 * int(i) / rated_capacity
    if SoH >80 :
      healthy_count += 1
    elif SoH >63 and SoH <=80:
      exchange_count +=1
    else:
      failed_count += 1
      
  return {
    "healthy": healthy_count,
    "exchange": exchange_count,
    "failed": failed_count
  }


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [115, 118, 80, 95, 91, 72]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
