def has_k_anonymity(data, target_k):
    """
    Check if the data satisfies k-anonymity.
    Parameters:
    data: a pandas dataframe
    k: the data should have atleast k-1 duplicates for each combination of features
    """
    # Count the frequency of each unique combination of quasi-identifiers
    k = k_anonymity(data)

    
    # Check if any combination occurs less than k times
    return k >= target_k

def k_anonymity(data):
    """
    Returns the k-anonymity of the data.
    Parameters:
    data: a pandas dataframe
    """
    # Count the frequency of each unique combination of features
    counts = data.value_counts()
    #print(counts)
    
    # Check if any combination occurs less than k times
    return min(counts)
