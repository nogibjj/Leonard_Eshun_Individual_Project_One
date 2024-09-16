from mylib.lib import *


# saving markdown
def save_to_markdown(data):
    with open("population_summary.md", "w") as file:
        file.write("Population Summaries:\n")
        file.write(
            calculate_summaries(
                data, "population", "Population", "urbanindex", "Urban Index"
            ).to_markdown()
        )
        file.write("\n\n")
        file.write("![population_histogram](population_histogram.png)")
        file.write("\n\n")
        file.write("![population_bar](population_bar.png)")


if __name__ == "__main__":
    df = load_dataset()
    create_histogram(df, "population", "Population across areas in the U.S.", True)
    create_bar_chart(df, True)
    save_to_markdown(df)
