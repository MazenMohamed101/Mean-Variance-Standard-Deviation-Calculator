from mean_var_std import calculation

def test_calculate():
    data = [0,1,2,3,4,5,6,7,8]
    result = calculation(data)

    # test some elements
    assert result['Sum'][2] == 36, "Sum of all elements should be 36"
    assert result['Mean'][2] == 4, "Mean of all elements should be 4.0"
    assert result['Max'][2] == 8, "Max of all elements should be 8"
    assert result['Min'][2] == 0, "Min of all elements should be 0"

    print("All tests passed!")


if __name__ == "__main__":
    test_calculate()
