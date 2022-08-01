N, M, K = map(int, input().split())

if M == K:
  result = N
elif M < K:
  result = M + (N - K)
else:
  result = K + (N - M)

print(result)