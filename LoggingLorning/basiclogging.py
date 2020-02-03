import logging

logging.basicConfig(level=logging.INFO)


def hypotenus(a, b):
    """compute the hypotenuses"""
    c = (a**2 + b**2)**0.5
    logging.info("hypotenus of {} and {} is {}".format(a, b, c))


hypotenus(3, 4)


