def data_smoothing(data, size):
    """
    Applies moving average smoothing to a time series using specified filter size.
    :param data: (list of float) the time series data to be smoothed.
    :param size: (int) the size of the smoothing filter.
    :return: a list in which each element is the smoothed value at that index, or None if there is insufficient data to calculate average.
    """
    if size < 1 or size > len(data): # Check that size is within the valid range
        raise ValueError("Invalid size: must be greater than or equal to 1, and less than or equal to length of data ")

    smoothed_data = []
    for d in range(len(data)): # Empty list to store smoothed output
        if d < size - 1: # Append none as not enough previous values to compute average
            smoothed_data.append(None)
        else:
            total = 0.0 # Total initialised for averaging
            for s in range(size): # Sum current and previous values
                total += data[d-s]
            smoothed_data.append(total/size) # Append the calculated average to result

    return smoothed_data