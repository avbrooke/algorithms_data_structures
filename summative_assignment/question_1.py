def data_smoothing(data, size):
    """
    Applies moving average smoothing to a time series using specified filter size.
    Args:
        data (list of float): The time series data to be smoothed.
        size (int): The size of the smoothing filter.
    Returns:
        list: A list in which each element is the smoothed value at that index, or None if there is
        insufficient data to calculate average.
    Raises:
        ValueError: If size is less than 1 or greater than the length of the data.
    """
    # Check that size is within the valid range
    if size < 1 or size > len(data):
        raise ValueError("Invalid size: must be greater than or equal to 1, and less than or equal to length of data.")

    smoothed_data = [] # Empty list to store smoothed output

    for d in range(len(data)):
        if d < size - 1:
            smoothed_data.append(None) # Append none as not enough previous values to compute average
        else:
            total = 0.0 # Total initialised for averaging
            for s in range(size):
                total += data[d-s] # Sum current and previous values
            smoothed_data.append(total/size) # Append the calculated average to result

    return smoothed_data