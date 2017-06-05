import math


class TextJustifier(object):
    """
    Justifies text for best fit on a line of specified with in no.of
    characters
    """
    def __init__(self, text, line_width):

        if type(text) is not str:
            error_message = "ERROR: input not a string"
            print(error_message)
            raise TypeError(error_message)

        if type(line_width) is not int:
            error_message = "ERROR: line width not an integer"
            print(error_message)
            raise TypeError(error_message)

        if line_width < 0:
            error_message = "ERROR: line width is less than 0"
            print(error_message)
            exit(1)



        self.text = text
        self.line_width = line_width
        self.minimum_penalty_dict = {}
        self.minimum_penalty_trace_dict = {}

        minimum_line_width = max(len(word) for word in self.words_list)
        if line_width < minimum_line_width:
            error_message = (
                "ERROR: line width is shorter than longest word in text")
            print(error_message)
            exit(1)

    @property
    def words_list(self):
        return self.text.split()

    def penalty(self, start_word_index, stop_word_index):
        character_length = sum(
            len(self.words_list[index]) for index in range(
                start_word_index,
                stop_word_index + 1))
        spaces = stop_word_index - start_word_index
        character_length += spaces
        # print(character_length)

        if character_length > self.line_width:
            return math.inf
        else:
            return (
                (len(self.words_list) - character_length) ** 2)

    def get_min_penalty(self, start_word_index):

        # print("Start word index: " + str(start_word_index))
        # print("Length: " + str(len(self.words_list)))
        minimum_penalty = math.inf
        minimum_penalty_stop_word_index = -1


        if start_word_index in self.minimum_penalty_trace_dict:
            minimum_penalty_stop_word_index_computed = (
                self.minimum_penalty_trace_dict[start_word_index])
            return (
                self.minimum_penalty_dict[
                    (start_word_index,
                     minimum_penalty_stop_word_index_computed)])

        if start_word_index > len(self.words_list) - 1:
            minimum_penalty = 0
            minimum_penalty_stop_word_index = start_word_index
            # return minimum_penalty



        for stop_word_index in range(start_word_index, len(self.words_list)):

            current_penalty = (
                self.penalty(start_word_index, stop_word_index) +
                self.get_min_penalty(stop_word_index + 1))

            if current_penalty < minimum_penalty:
                # print("*"*100, current_penalty, start_word_index, stop_word_index)
                minimum_penalty = current_penalty
                minimum_penalty_stop_word_index = stop_word_index

        self.minimum_penalty_trace_dict[start_word_index] = (
            minimum_penalty_stop_word_index)
        self.minimum_penalty_dict[
            (start_word_index, minimum_penalty_stop_word_index)] = (
            minimum_penalty)


        return minimum_penalty

    def print_justified(self, start_word_index=0):
        print("\n\nOriginal text:")
        print(self.text)
        print("\n\nJustification width: %s" % str(self.line_width))
        print("\n\nJustified text:")
        print("=" * self.line_width)
        index_start = start_word_index
        while index_start < len(self.words_list):
            index_end = self.minimum_penalty_trace_dict[index_start]
            print(' '.join(self.words_list[index_start: index_end + 1]))
            index_start = index_end + 1
        print("=" * self.line_width)








def main():
    text = "Technology is the practical use of science, including the making, modification or improvement, applied activity or behavior, use and knowledge of tools, machines, techniques, crafts, systems, methods of organization, or environmental modifications or arrangement in order to solve a problem, improve a preexisting solution to a problem, achieve a goal or perform a specific function. It can also refer to the collection of such tools, machinery, modifications, environmental arrangement and procedures. Technologies significantly affect human as well as other animal species' ability to control and adapt to their natural environments. The word technology comes from Greek τεχνολογία (technología); from τέχνη (téchnē), meaning 'art, skill, craft', and -λογία (-logía), meaning 'study of-'. The term can be applied either generally or to many specific areas, examples of which include construction technology, medical technology and information technology."


    line_width = 30

    justifier = TextJustifier(text, line_width)

    # print(justifier.words_list)
    print(justifier.penalty(1, 2))

    print(justifier.get_min_penalty(0))

    # print(justifier.minimum_penalty_trace_dict)
    # print(justifier.minimum_penalty_dict)

    justifier.print_justified()




if __name__ == "__main__":
    main()
