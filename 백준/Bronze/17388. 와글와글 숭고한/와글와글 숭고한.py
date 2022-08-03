S, K, H = map(int, input().split())

if S + K + H >= 100:
  print('OK')
else:
  univ = min([S, K, H])
  if univ == S:
    print('Soongsil')
  elif univ == K:
    print('Korea')
  else:
    print('Hanyang')