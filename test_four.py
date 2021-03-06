import pytest

def extract_position(line):
    if not line:
        pos = None
    else:
        if 'debug' in line or 'error' in line:
            pos = None
        else:
            if 'x:' in line:
                start_index = line.find('x:') + 2
                pos = line[start_index:] # from start_index to the end.
            else: 
                pos = None
    return pos

if __name__ == "__main__":
    result1 = extract_position('|error| numerical calculations could not converge.')
    print(result1)
    result2 = extract_position('|update| the positron location in the particle accelerator is x:21.432')
    print(result2)

@pytest.fixture
def error():
    return '|error| something went wrong'

@pytest.fixture
def average():
    return '|update| the positron location in the particle accelerator is x:21.432'

def test_extract_position_null_case(error):
    assert extract_position(error) == None

def test_average_input(average):
    assert extract_position(average) == "21.432"




