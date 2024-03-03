from riddle_solvers import solve_sec_hard


encryption_key = "266200199BBCDFF1"
plaintext = "0123456789ABCDEF"
inp = encryption_key,plaintext
encrypted_text = solve_sec_hard(inp)
print("Encrypted Text:", encrypted_text)
#Result: 4E0E6864B5E1CA52
