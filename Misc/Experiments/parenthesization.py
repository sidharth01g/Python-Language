import math


class Parenthesize(object):
    def __init__(self, matrices_dimensions_list):
        self.matrices_dimensions_list = matrices_dimensions_list
        list_length = len(self.matrices_dimensions_list)
        self.min_cost_inter_array = [
            [(None, None) for y in range(list_length)] for x in range(list_length)
        ]

    def show_min_cost_inter_array(self):
        for i in range(len(self.min_cost_inter_array)):
            print(self.min_cost_inter_array[i])

    def cost(self, start_index, inter_index, stop_index):
        return (
            self.matrices_dimensions_list[start_index][0] *
            self.matrices_dimensions_list[inter_index][1] *
            self.matrices_dimensions_list[stop_index][1]
        )

    def get_min_cost(self, start_index=None, stop_index=None):

        if not start_index:
            start_index = 0
        if not stop_index:
            stop_index = len(self.matrices_dimensions_list) - 1
        print("Start index:", start_index, " Stop index: ", stop_index)
        print("asdfadfadsf")
        if self.min_cost_inter_array[start_index][stop_index][1]:
            return self.min_cost_inter_array[start_index][stop_index][1]


        # Base case
        if start_index >= stop_index:
            min_cost = 0
            min_cost_inter_index = None
            self.min_cost_inter_array[start_index][stop_index] = (
                min_cost_inter_index, min_cost
            )
        elif start_index == stop_index - 1:
            min_cost = (
                self.matrices_dimensions_list[start_index][0] *
                self.matrices_dimensions_list[start_index][1] *
                self.matrices_dimensions_list[stop_index][1]
            )
            min_cost_inter_index = None
            self.min_cost_inter_array[start_index][stop_index] = (
                min_cost_inter_index, min_cost
            )
        else:
            min_cost = math.inf
            min_cost_inter_index = None

            for inter_index in range(start_index + 1, stop_index):
                print("#" * 20,self.cost(start_index, inter_index, stop_index))
                current_min_cost = (
                    self.cost(start_index, inter_index, stop_index) +
                    self.get_min_cost(start_index, inter_index) +
                    self.get_min_cost(inter_index + 1, stop_index)
                )
                if current_min_cost < min_cost:
                    min_cost = current_min_cost
                    min_cost_inter_index = inter_index

            self.min_cost_inter_array[start_index][stop_index] = (
                min_cost_inter_index, min_cost
            )

        return min_cost

    def locate_parentheses(self):
        pass







def main():
    matrices_dimensions_list = [
        (20, 11), (11, 33), (33, 5), (5, 215), (215, 901), (901, 75)]

    print("Matrices dimensions:\n %s" % str(matrices_dimensions_list))
    p = Parenthesize(matrices_dimensions_list)
    print("Initital min_cost_inter_array:")
    p.show_min_cost_inter_array()

    min_cost = p.get_min_cost()

    print("Minimum cost of parenthesization: %s" % str(min_cost))

    print("Final min_cost_inter_array:")
    p.show_min_cost_inter_array()




if __name__ == "__main__":
    main()
