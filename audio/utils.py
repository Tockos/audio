

def wave_sum(waves: list):
    """
    Sum the waves in list

    :param waves: List of waves
    :return: Wave
    """

    if len(waves) == 0:
        raise ValueError("No waves was specified")
    elif len(waves) == 1:
        return waves[0]

    return sum(waves[1:], start=waves[0])
