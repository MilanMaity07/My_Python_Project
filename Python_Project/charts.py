import pandas as pd
import matplotlib.pyplot as plt


# ==============================
# LOAD DATA
# ==============================

def load_data():

    try:

        df = pd.read_csv("students.csv")

        if df.empty:

            print("No data available for graph.")

            return None

        return df

    except FileNotFoundError:

        print("students.csv not found.")

        return None

    except pd.errors.EmptyDataError:

        print("students.csv is empty.")

        return None


# ==============================
# BAR CHART
# ==============================

def show_bar_chart():

    df = load_data()

    if df is None:
        return

    plt.figure(figsize=(8, 5))

    plt.bar(
        df["Name"],
        df["Total"]
    )

    plt.xlabel("Students")

    plt.ylabel("Total Marks")

    plt.title("Student Total Marks")

    plt.xticks(rotation=30)

    plt.tight_layout()

    plt.show()


# ==============================
# LINE GRAPH
# ==============================

def show_line_graph():

    df = load_data()

    if df is None:
        return

    plt.figure(figsize=(8, 5))

    plt.plot(
        df["Name"],
        df["Average"],
        marker="o"
    )

    plt.xlabel("Students")

    plt.ylabel("Average Marks")

    plt.title("Student Average Marks")

    plt.xticks(rotation=30)

    plt.tight_layout()

    plt.show()


# ==============================
# HISTOGRAM
# ==============================

def show_histogram():

    df = load_data()

    if df is None:
        return

    plt.figure(figsize=(8, 5))

    plt.hist(
        df["Percentage"],
        bins=5
    )

    plt.xlabel("Percentage")

    plt.ylabel("Number of Students")

    plt.title("Student Percentage Distribution")

    plt.tight_layout()

    plt.show()