import codewars_test as test
# from solution import sum_two_smallest_numbers

def sum_two_smallest_numbers(numlist):
    numlist.sort()
    sum_two_small_nums = numlist[0] + numlist[1]
    # print(numlist)
    return sum_two_small_nums

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)
        test.assert_equals(sum_two_smallest_numbers([7, 15, 12, 18, 22]), 19)
        test.assert_equals(sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)
        test.assert_equals(sum_two_smallest_numbers([18, 2, 930, 8373738, 38362627]), 20)