def normalize_testimonial(testimonial_data):
    """
    Function for normalizing testimonial data according to frontend
    :param testimonial_data:
    :return: Normalized testimonial data
    """

    normalized_testimonial_data = []
    for data in range(0, len(testimonial_data), 2):
        normalized_testimonial_data.append(
            [testimonial_data[data], testimonial_data[data + 1]]
        )
    return normalized_testimonial_data
