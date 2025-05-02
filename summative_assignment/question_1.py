def data_smoothing(data, size):
    if size < 1 or size > len(data):
        raise ValueError("Invalid size: must be greater than or equal to 1, and less than or equal to length of data ")

    smoothed_data = []
    for d in range(len(data)):
        if d < size - 1:
            smoothed_data.append(None)
        else:
            total = 0.0
            for s in range(size):
                total += data[d-s]
            smoothed_data.append(total/size)

    return smoothed_data