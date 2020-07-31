"""
Power Consumption Plots --- PWC
===============================
"""

from matplotlib import pyplot as plt 

MOTE_ID_LOCATION = 0
DATA_TYPE_LOCATION = 1
TIME_STAMP_LOCATION = 2
DATA_LOCATION = 2

ALL_MOTES = [
        "Z1_1",
        "Z1_2",
        "Z1_3",
        "Z1_4",
        "Z1_5",
        "Z1_9"
        ]

DATA_TYPE = [
        "ON",
        "RX",
        "TX",
        ]

def read_data(location, delimiter):
    """@brief funcion para leer data de un archivo
    @param location es la ubicacion del archivo
    @param cols tupla que indica las columnas que se quieren leer
    @param delim es el delimitador
    @return s los datos leidos
    """
    data = []

    file = open(location, 'r')

    for line in file:
        try:
            data += [line.split(delimiter)]
        except:
            pass

    return data



def process_data(data, mote, data_type):

    filtered_data = []

    for line in data:

        if(line[MOTE_ID_LOCATION] == mote and
                line[DATA_TYPE_LOCATION] == data_type):
            filtered_data.append(line[DATA_LOCATION])

    return filtered_data


def get_time_stamp(data):

    data_type = "MONITORED"

    filtered_data = []

    for line in data:
        ## Todos los motes tienen el mismo timestamp
        ## agarro el del Z1_1
        if(line[MOTE_ID_LOCATION] == "Z1_1" and
                line[DATA_TYPE_LOCATION] == data_type):
            filtered_data.append(line[TIME_STAMP_LOCATION])

    return filtered_data

def get_tx_data(motes, mote):
    return process_data(motes, mote, DATA_TYPE[2])

def get_rx_data(motes, mote):
    return process_data(motes, mote, DATA_TYPE[1])

def get_on_data(motes, mote):
    return process_data(motes, mote, DATA_TYPE[0])

def get_rx_avg(motes):
    return process_data(motes, "AVG", "RX")

def main():

    # motes es una matriz donde cada fila son las
    # lineas del archivo y cada columna los datos
    # separados por el delimitador
    data = read_data("./COOJA_POWER.md", ",")

    motes_rx = []
    motes_tx = []
    motes_on = []
    
    t = get_time_stamp(data)
    t = [float(x)*1e-6 for x in t]
    
    for mote in ALL_MOTES:
        motes_rx.append([float(x)*1e-6 for x in get_rx_data(data, mote)])
        motes_tx.append([float(x)*1e-6 for x in get_tx_data(data, mote)])
        motes_on.append([float(x)*1e-6 for x in get_on_data(data, mote)])

    motes_rx_avg = ([float(x)*1e-6 for x in get_rx_avg(data)])

    fig = plt.figure()
    plt.plot(t, motes_rx[0], linewidth=2, color='b', label="Nodo 1")
    plt.plot(t, motes_rx[1], linewidth=2, color='r', label="Nodo 2")
    plt.plot(t, motes_rx[2], linewidth=2, color='m', label="Nodo 3")
    plt.plot(t, motes_rx[3], linewidth=2, color='g', label="Nodo 4")
    plt.plot(t, motes_rx[4], linewidth=2, color='C1', label="Nodo 5")
    plt.plot(t, motes_rx[5], linewidth=2, color='C5', label="Nodo 9")
    #plt.ylim((0, 10))
    plt.legend()
    plt.xlabel(r't[us]')
    plt.ylabel(r'RX[us]')
    plt.grid()
    plt.show()
    fig.savefig("rx_flood_attack.png", dpi=200)

    fig = plt.figure()
    plt.plot(t, motes_tx[0], linewidth=2, color='b', label="Nodo 1")
    plt.plot(t, motes_tx[1], linewidth=2, color='r', label="Nodo 2")
    plt.plot(t, motes_tx[2], linewidth=2, color='m', label="Nodo 3")
    plt.plot(t, motes_tx[3], linewidth=2, color='g', label="Nodo 4")
    plt.plot(t, motes_tx[4], linewidth=2, color='C1', label="Nodo 5")
    plt.plot(t, motes_tx[5], linewidth=2, color='C5', label="Nodo 9")
    #plt.ylim((0, 10))
    plt.legend()
    plt.xlabel(r't[us]')
    plt.ylabel(r'TX[us]')
    plt.grid()
    plt.show()
    fig.savefig("tx_flood_attack.png", dpi=200)

    fig = plt.figure()
    plt.plot(t, motes_on[0], linewidth=2, color='b', label="Nodo 1")
    plt.plot(t, motes_on[1], linewidth=2, color='r', label="Nodo 2")
    plt.plot(t, motes_on[2], linewidth=2, color='m', label="Nodo 3")
    plt.plot(t, motes_on[3], linewidth=2, color='g', label="Nodo 4")
    plt.plot(t, motes_on[4], linewidth=2, color='C1', label="Nodo 5")
    plt.plot(t, motes_on[5], linewidth=2, color='C5', label="Nodo 9")
    #plt.ylim((0, 10))
    plt.legend()
    plt.xlabel(r't[us]')
    plt.ylabel(r'ON[us]')
    plt.grid()
    plt.show()
    fig.savefig("on_flood_attack.png", dpi=200)

    fig = plt.figure()
    plt.plot(t, motes_rx_avg, linewidth=2, color='b', label="Nodo 1")
    #plt.ylim((0, 10))
    plt.legend()
    plt.xlabel(r't[us]')
    plt.ylabel(r'ON[us]')
    plt.grid()
    plt.show()
    #fig.savefig("tx_flood_attack.png", dpi=200)


if __name__ == "__main__":
    main()


