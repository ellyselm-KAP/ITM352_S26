def test_determine_progress(progress_function):
    # "Get going!" cases
    assert progress_function(10, 0) == "Get going!", "spins=0 should be Get going!"
    assert progress_function(0, 10) == "Get going!", "hits/spins = 0 should be Get going!"
    assert progress_function(-1, 10) == "Get going!", "negative ratio should be Get going!"

    # "On your way!" case (ratio > 0 but < 0.25)
    assert progress_function(1, 10) == "On your way!", "0 < ratio < 0.25 should be On your way!"

    # "Almost there!" case (ratio >= 0.25 but not a win)
    assert progress_function(3, 10) == "Almost there!", "0.25 <= ratio < 0.5 should be Almost there!"

    # "You win!" case (ratio >= 0.5 AND hits < spins)
    assert progress_function(6, 10) == "You win!", "ratio>=0.5 and hits<spins should be You win!"

    print("All tests passed!")

# Run tests on determine_progress1
test_determine_progress(determine_progress1)


def determine_progress1(hits, spins):
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins

    if hits_spins_ratio > 0:
        progress = "On your way!"
        if hits_spins_ratio >= 0.25:
            progress = "Almost there!"
            if hits_spins_ratio >= 0.5:
                if hits < spins:
                    progress = "You win!"
    else:
        progress = "Get going!"

    return progress


def determine_progress2(hits, spins):
    if spins == 0:
        return "Get going!"

    ratio = hits / spins
    progress = "Get going!"

    if ratio > 0:
        progress = "On your way!"
    if ratio >= 0.25:
        progress = "Almost there!"
    if ratio >= 0.5 and hits < spins:
        progress = "You win!"

    return progress


test_determine_progress(determine_progress2)

def determine_progress3(hits, spins):
    if spins == 0:
        return "Get going!"

    ratio = hits / spins

    if ratio <= 0:
        return "Get going!"
    elif ratio < 0.25:
        return "On your way!"
    elif ratio < 0.5:
        return "Almost there!"
    elif hits < spins:
        return "You win!"
    else:
        return "Almost there!"


test_determine_progress(determine_progress3)


def determine_progress_no_ifs(hits, spins):
    # spins==0 is handled by short-circuiting: (spins and hits/spins) avoids division by zero
    ratio = (spins and (hits / spins)) or 0

    messages = ["Get going!", "On your way!", "Almost there!", "You win!"]

    idx = 0
    idx += int(spins != 0 and ratio > 0)
    idx += int(spins != 0 and ratio >= 0.25)
    idx += int(spins != 0 and ratio >= 0.5 and hits < spins)

    return messages[idx]

