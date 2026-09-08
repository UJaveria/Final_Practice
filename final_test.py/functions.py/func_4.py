# Write summarize_scores(scores) that returns a dictionary with keys "min", "max", "average".

def summarize_scores(scores) :
    minimum = min(scores)
    maximum = max(scores)
    average = sum(scores) / len(scores)
    return {"min" : minimum, "max" : maximum, "average" : average}

scores = [12,43,95,11,10]
print(summarize_scores(scores))