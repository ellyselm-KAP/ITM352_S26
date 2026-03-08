responses = [5, 7, 3, 8]
respondent_ids = (1012, 1035, 1021, 1053)

responses.append(respondent_ids)
print(responses)


responses = [5, 7, 3, 8]

responses.append(0)      # add 0 to the end of the list
responses.insert(2, 6)   # insert 6 between 7 and 3

print(responses)


responses = [5, 7, 3, 8]

responses = responses + [0]                 # add 0 to the end
responses = responses[:2] + [6] + responses[2:]  # insert 6 at index 2

print(responses)

respondent_ids = (1012, 1035, 1021, 1053)
respondent_ids = respondent_ids + (1011,)
print(respondent_ids)


