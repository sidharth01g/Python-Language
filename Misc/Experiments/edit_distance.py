class EditMinimize(object):
    def __init__(self, from_string, to_string):
        if type(from_string) is not str or type(to_string) is not str:
            error_message = "ERROR: Inputs are not strings"
            raise TypeError(error_message)
        self.from_string = from_string
        self.to_string = to_string
        self.min_cost_dict = {}

    def insert_cost(self, character):
        if type(character) is not str:
            error_message = (
                "ERROR: Cannot compute insert cost for non-string types")
            raise TypeError(error_message)
        if len(character) != 1:
            error_message = (
                "ERROR: Length not equal to 1. Cannot compute insert cost")
            raise Exception(error_message)
        cost = 1.0
        return cost

    def delete_cost(self, character):

        if type(character) is not str:
            error_message = (
                "ERROR: Cannot compute delete cost for non-string types")
            raise TypeError(error_message)
        if len(character) != 1:
            error_message = (
                "ERROR: Length not equal to 1. Cannot compute delete cost")
            raise Exception(error_message)

        cost = 1.0
        return cost

    def replace_cost(self, from_character, to_character):
        if type(from_character) is not str:
            error_message = (
                "ERROR: Cannot compute replace cost for non-string types")
            raise TypeError(error_message)
        if len(from_character) != 1:
            error_message = (
                "ERROR: Length not equal to 1. Cannot compute replace cost")
            raise Exception(error_message)
        if type(to_character) is not str:
            error_message = (
                "ERROR: Cannot compute replace cost for non-string types")
            raise TypeError(error_message)
        if len(to_character) != 1:
            error_message = (
                "ERROR: Length not equal to 1. Cannot compute replace cost")
            raise Exception(error_message)
        if from_character == to_character:
            cost = 0.0
        else:
            cost = 1.0
        return cost

    def get_min_cost(self, start_index_first, start_index_second):
        # print(start_index_first, start_index_second)
        # print(self.min_cost_dict)
        if (start_index_first, start_index_second) in self.min_cost_dict:
            return self.min_cost_dict[(start_index_first, start_index_second)]

        min_cost = None

        # Base case
        if start_index_first >= len(self.from_string):
            try:
                min_cost = sum(
                    [self.delete_cost(character) for character in self.to_string[
                        start_index_second:]])
            except Exception as error:
                print("Error occured at first base case")

        elif start_index_second >= len(self.to_string):
            try:
                min_cost = sum(
                    [self.delete_cost(character) for character in self.from_string[
                        start_index_first:]])
            except Excpetion as error:
                print("Error occured at second base case")

        else:
            try:
                cost_ins = (
                    self.insert_cost(self.from_string[start_index_first]) +
                    self.get_min_cost(start_index_first,
                                      start_index_second + 1))
                cost_del = (
                    self.delete_cost(self.from_string[start_index_first]) +
                    self.get_min_cost(start_index_first + 1,
                                      start_index_second))
                cost_rep = (
                    self.replace_cost(self.from_string[start_index_first],
                                      self.to_string[start_index_second]) +
                    self.get_min_cost(start_index_first + 1,
                                      start_index_second + 1))
                costs_list = [cost_ins, cost_del, cost_rep]
                min_cost = min(costs_list)
            except Exception as error:
                print("Error occurred in general case: ", error)
                raise error

        self.min_cost_dict[(start_index_first, start_index_second)] = min_cost
        return min_cost


def main():
    from_string = "kitten"
    to_string = "knitting"
    print("From: " + str(from_string))
    print("To: " + str(to_string))
    try:
        em = EditMinimize(from_string, to_string)
    except Exception as error:
        print("Error instantiating edit minimization: " + str(error))
        exit(1)

    try:
        min_cost = em.get_min_cost(0, 0)
        print("Minimum edit distance: " + str(min_cost))
    except Exception as error:
        print("Error occurred: " + str(error))
        exit(1)



if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("Error occurred in main method: " + str(error))
