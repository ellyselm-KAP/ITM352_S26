emotions = ("sad", "fear", "surprise", "happy")

condition = (len(emotions) > 3) and (emotions[-1] == "happy")

# No if-statement, no ternary:
print({True: "true", False: "false"}[condition])





emotions = ("sad", "fear", "surprise", "happy")

if len(emotions) > 3 and emotions[-1] == "happy":
    print("true")
else:
    print("false")
