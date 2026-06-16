EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.


#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.

def bake_time_remaining(elapsed_bake_time):
    """calculate the bake time remaining."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """calculate the total preparation time based on he number of layers.
       Each layer is assumed to take 2 minutes."""
    return number_of_layers * 2
#TODO (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.



#TODO (student): define the 'elapsed_time_in_minutes()' function below.



# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """calculate the totalelapsed cooking time."""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time