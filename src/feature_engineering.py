def calculate_statistics(data):
    """Calculate basic statistics for dataset."""
    return {
        'mean': data.mean(),
        'std': data.std(),
        'count':len(data)
    }