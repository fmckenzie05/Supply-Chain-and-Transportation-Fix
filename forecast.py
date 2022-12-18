def forecast_demand(history, period):
    """
    Forecast future demand based on a given history of demand data.
    
    Parameters:
        history (list): A list of demand data for a given time period.
        period (int): The length of time (in weeks) covered by the demand data.
    
    Returns:
        float: The forecasted demand for the next period.
    """
    # Calculate the average demand for the given period
    average_demand = sum(history) / len(history)
    
    # Adjust the forecast based on the trend in the data
    if history[-1] > history[0]:
        forecast = average_demand * 1.1
    elif history[-1] < history[0]:
        forecast = average_demand * 0.9
    else:
        forecast = average_demand
        
    return forecast