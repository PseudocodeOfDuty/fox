from csp_n import exec
        
N = 20
best_fcsp = None
for n in range(N):
    t = 6.172 + 0.42 * n
    fcsp = exec(n,t)
    best_fcsp = fcsp.keep_if_higher_score_than(best_fcsp)
    print(best_fcsp)
