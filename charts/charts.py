import matplotlib.pyplot as pylot

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 35, 120]

    fig, ax = pylot.subplots()
    ax.pie(values, labels = labels)
    pylot.savefig('pie2.png')
    pylot.close()