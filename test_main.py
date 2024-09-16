from mylib.lib import load_dataset, calculate_summaries


def test_add(dataset):
    """Tewting the add function"""
    assert dataset is not None
    assert dataset.shape == (73280, 8)


def test_countries(dataset):
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


if __name__ == "__main__":
    dataset = load_dataset()
    test_add(dataset)
    test_countries(dataset)
    print("Test completed successfully")
