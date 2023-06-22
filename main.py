import matplotlib.pyplot as plt
import re


def parse_talk_history(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    talk_data = []
    current_date = None
    current_count = 0

    for line in lines[1:]:
        line = line.strip()

        if re.match(r'\d{4}/\d{2}/\d{2}\(.+\)', line):
            if current_date:
                talk_data.append((current_date, current_count))
                current_count = 0
            current_date = line.split('(')[0]
        elif re.match(r'\d{2}:\d{2}\s+', line):
            if current_date:
                current_count += 1

    if current_date:
        talk_data.append((current_date, current_count))

    return talk_data


def plot_talk_counts(talk_data):
    dates = [data[0] for data in talk_data]
    counts = [data[1] for data in talk_data]

    fig, ax = plt.subplots()
    ax.plot(dates, counts, marker='o', linestyle='-', color='blue')
    ax.set(xlabel='Date', ylabel='Talk Count', title='LINE Talk Counter')
    ax.set_xticks(range(len(dates)))
    ax.set_xticklabels(dates, rotation=45)
    ax.grid(True)

    for i, count in enumerate(counts):
        ax.text(i, count, str(count), ha='center', va='bottom')

    plt.show()


file_path = 'data/sakumi.txt'
talk_data = parse_talk_history(file_path)
plot_talk_counts(talk_data)
