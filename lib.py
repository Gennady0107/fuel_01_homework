def fuel_calc(litr_in_tank, l_100km):
    """
    >>>fuel_calc(10,5)
    200
    """
    distance_for_refueling = litr_in_tank / l_100km * 100
    return distance_for_refueling
