import cmath


def quadratic_formula(a, b, c):
    result = {}
    # validate that inputs are integers
    try:
        a = int(a) 
        b = int(b) 
        c = int(c)
    except ValueError:
        result = {
            "error": True,
            "errorMessage": "Invalid Input: function did not get Integers"
        }
        return result
    result['answer_array'] = [(b**2)]
    result['answer_array'].append(-4*a*c)
    result['answer_array'].append(
        result['answer_array'][0] + result['answer_array'][1])
    result['answer_array'].append(cmath.sqrt(result['answer_array'][2]))
    result['answer_array'].append((-b) + result['answer_array'][3])
    result['answer_array'].append(2 * a)
    result['answer_array'].append(
        -b / result['answer_array'][5])
    result['answer_array'].append(result['answer_array'][3] / result['answer_array'][5])
    result['answer_array'].append(result['answer_array'][6] + result['answer_array'][7])
    result['answer_array'].append(result['answer_array'][6] - result['answer_array'][7])
    result['answer'] = []
    result['answer'].extend([result['answer_array'][-1],result['answer_array'][-2]])
    result['error'] = False
    return result


if __name__ == "__main__":
    a, b, c = input("enter qaudratic values a, b and c ").split()
    result = quadratic_formula(a, b, c)
    # i figured you were asked to go through the steps. Note that this is an overengineered way of doing this with a lot of boilerplate if you do not need the 'steps' later. Removing unnecessary code is just as important as adding code and so my challenge to you is to remove what you don't need.
    print("your first x is " + result['errorMessage']
          if result['error'] else result['answer'][0])
    for index, element in enumerate(result['answer_array']):
        print("step", index,":", element)