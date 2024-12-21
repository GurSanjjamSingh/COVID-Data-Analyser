import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def display_menu():
    print("Reading data from a file")
    menu = """
    1. Display the data
    2. Display data of a particular state
    3. Display the mean confirmed cases, mean recovered, mean deaths
    4. Display the state having the maximum number of cases
    5. Display a line chart showing confirmed cases of the first ten states
    6. Display a bar chart comparing the data of any two states
    7. Display a histogram of the recovered cases of all the states
    8. Display the confirmed cases and death cases of all the states
    9. Display the line plot of five states having the most recovered cases
    10. Sort the entire data in descending order of deaths and plot a line chart
    0. EXIT
    """
    print(menu)


def display_data():
    data = pd.read_csv("state_wise.csv", skiprows=1,
                       names=["State", "Confirmed", "Recovered", "Deaths", "Active", "Last_Updated_Time"])
    print(data)


def display_data_by_state():
    data = pd.read_csv("state_wise.csv", skiprows=1,
                       names=["State", "Confirmed", "Recovered", "Deaths", "Active", "Last_Updated_Time"])
    states = eval(input("Enter the state(s) to display (e.g., ['State1', 'State2']): "))
    for state in states:
        state_data = data[data['State'] == state]
        print(state_data)


def display_mean_cases():
    data = pd.read_csv("state_wise.csv", skiprows=1,
                       names=["State", "Confirmed", "Recovered", "Deaths", "Active", "Last_Updated_Time"])
    print("\nMean cases in each category:\n", data[["Confirmed", "Recovered", "Deaths"]].mean())


def display_max_cases():
    data = pd.read_csv("state_wise.csv", skiprows=1,
                       names=["State", "Confirmed", "Recovered", "Deaths", "Active", "Last_Updated_Time"])
    print("State with maximum confirmed cases:", data.iloc[data['Confirmed'].idxmax()]['State'])
    print("State with maximum recovered cases:", data.iloc[data['Recovered'].idxmax()]['State'])
    print("State with maximum deaths:", data.iloc[data['Deaths'].idxmax()]['State'])
    print("State with maximum active cases:", data.iloc[data['Active'].idxmax()]['State'])


def plot_line_chart_first_ten_states():
    data = pd.read_csv("state_wise.csv", skiprows=1,
                       names=["State", "Confirmed", "Recovered", "Deaths", "Active", "Last_Updated_Time"])
    plt.plot(data["State"][:10], data["Confirmed"][:10])
    plt.title("Confirmed Cases of the First Ten States")
    plt.xlabel("States")
    plt.ylabel("Confirmed Cases")
    plt.xticks(rotation=45)
    plt.show()


def plot_bar_chart_two_states():
    data = pd.read_csv("state_wise.csv", skiprows=1,
                       names=["State", "Confirmed", "Recovered", "Deaths", "Active", "Last_Updated_Time"])
    states = eval(input("Enter the names of two states in list format (e.g., ['State1', 'State2']): "))
    state1 = data[data["State"] == states[0]].iloc[0]
    state2 = data[data["State"] == states[1]].iloc[0]

    x = np.arange(4)
    y1 = [state1["Confirmed"], state1["Recovered"], state1["Deaths"], state1["Active"]]
    y2 = [state2["Confirmed"], state2["Recovered"], state2["Deaths"], state2["Active"]]

    plt.bar(x - 0.2, y1, width=0.4, label=states[0])
    plt.bar(x + 0.2, y2, width=0.4, label=states[1])
    plt.xticks(x, ["Confirmed", "Recovered", "Deaths", "Active"])
    plt.title("Comparison of Two States")
    plt.ylabel("Number of Cases")
    plt.legend()
    plt.show()


def plot_histogram_recovered_cases():
    data = pd.read_csv("state_wise.csv", skiprows=1,
                       names=["State", "Confirmed", "Recovered", "Deaths", "Active", "Last_Updated_Time"])
    plt.hist(data["Recovered"], bins=20, color='blue', edgecolor='black')
    plt.title("Histogram of Recovered Cases")
    plt.xlabel("Recovered Cases")
    plt.ylabel("Frequency")
    plt.show()


def display_confirmed_and_death_cases():
    data = pd.read_csv("state_wise.csv", skiprows=1,
                       names=["State", "Confirmed", "Recovered", "Deaths", "Active", "Last_Updated_Time"])
    print(data[["State", "Confirmed", "Deaths"]])


def plot_line_chart_top_recovered():
    data = pd.read_csv("state_wise.csv", skiprows=1,
                       names=["State", "Confirmed", "Recovered", "Deaths", "Active", "Last_Updated_Time"])
    top_five = data.nlargest(5, "Recovered")
    plt.plot(top_five["State"], top_five["Recovered"], marker='o')
    plt.title("Top Five States by Recovered Cases")
    plt.xlabel("States")
    plt.ylabel("Recovered Cases")
    plt.xticks(rotation=45)
    plt.show()


def plot_line_chart_sorted_deaths():
    data = pd.read_csv("state_wise.csv", skiprows=1,
                       names=["State", "Confirmed", "Recovered", "Deaths", "Active", "Last_Updated_Time"])
    sorted_data = data.sort_values(by="Deaths", ascending=False)
    plt.plot(sorted_data["State"], sorted_data["Deaths"], marker='o', linestyle='--')
    plt.title("States Sorted by Deaths")
    plt.xlabel("States")
    plt.ylabel("Deaths")
    plt.xticks(rotation=45)
    plt.show()


def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice from the above menu: "))
            if choice == 1:
                display_data()
            elif choice == 2:
                display_data_by_state()
            elif choice == 3:
                display_mean_cases()
            elif choice == 4:
                display_max_cases()
            elif choice == 5:
                plot_line_chart_first_ten_states()
            elif choice == 6:
                plot_bar_chart_two_states()
            elif choice == 7:
                plot_histogram_recovered_cases()
            elif choice == 8:
                display_confirmed_and_death_cases()
            elif choice == 9:
                plot_line_chart_top_recovered()
            elif choice == 10:
                plot_line_chart_sorted_deaths()
            elif choice == 0:
                print("Thank you for using the COVID DATA SYSTEM.")
                print("Please visit again!")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print("An error occurred:", e)


if __name__ == "__main__":
    main()
