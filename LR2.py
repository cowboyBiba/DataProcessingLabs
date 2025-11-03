import matplotlib
import numpy as np


def generate_data(dimensions, min_v, max_v, dtype=float):
    if dtype == int:
        data_array = np.random.randint(min_v, max_v, size=dimensions)
    elif dtype == float:
        data_int_array = np.ones(dimensions) * (max_v - min_v)
        data_array = np.random.rand(*dimensions)
        data_array *= data_int_array
        data_array += min_v
    else:
        return None
    print(data_array)
    return data_array
def prepare_data(data):
    data = np.array(data)
    data = data.ravel()
    for i in range(len(data)):
        if data[i] is None:
            data[i] = 0

def generate_linear_graph(data):
    pass
def generate_scatter_graph(data):
    pass
def plt_draw(data):
    pass
def main():
    data = generate_data([2,5,3], 10, 15, float)
    prepare_data(data)
    # plt и его настройка ниже

    plt.show()