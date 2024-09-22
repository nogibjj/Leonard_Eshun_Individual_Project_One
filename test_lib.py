from mylib.lib import load_dataset, calculate_summaries
from script import save_bar_chart, save_histogram
import os

# Data
dataset_path = "https://raw.githubusercontent.com/fivethirtyeight/data/master/urbanization-index/urbanization-census-tract.csv"


def test_data_loading():
    """Testing data loading"""
    dataset = load_dataset(dataset_path)
    assert dataset is not None
    assert dataset.shape == (73280, 8)
    return dataset


def test_summaries(dataset):
    my_calculated_summaries = calculate_summaries(
        dataset, "population", "Population", "urbanindex", "Urban Index", True
    )
    pandas_summaries = dataset.describe()
    assert (
        pandas_summaries.loc["mean", "population"]
        == my_calculated_summaries.loc["Mean", "Population"]
    )
    assert (
        pandas_summaries.loc["std", "population"]
        == my_calculated_summaries.loc["Standard Deviation", "Population"]
    )
    assert (
        pandas_summaries.loc["min", "population"]
        == my_calculated_summaries.loc["Min", "Population"]
    )
    assert (
        pandas_summaries.loc["max", "population"]
        == my_calculated_summaries.loc["Max", "Population"]
    )


def test_file_creation(data, cleanup=True):
    # Remove existing ones
    if os.path.exists("population_bar.png"):
        os.remove("population_bar.png")
    if os.path.exists("population_histogram.png"):
        os.remove("population_histogram.png")

    # Test and create new ones
    assert os.path.exists("population_bar.png") == False
    assert os.path.exists("population_histogram.png") == False

    save_bar_chart(data)
    save_histogram(data)

    assert os.path.exists("population_bar.png") == True
    assert os.path.exists("population_histogram.png") == True

    # Clean up
    if cleanup:
        if os.path.exists("population_bar.png"):
            os.remove("population_bar.png")
        if os.path.exists("population_histogram.png"):
            os.remove("population_histogram.png")


if __name__ == "__main__":
    dataset = test_data_loading()
    test_summaries(dataset)
    test_file_creation(dataset)
    print("Test completed successfully")
