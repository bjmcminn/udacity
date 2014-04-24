
    

if __name__ == "__main__":

    filename = "combined_weather_mta_raw_data/turnstile_data_master_with_weather.csv"
    # This would be how ideally I create the dataframe to avoid having to delete the unnamed index column
    #thedata = pandas.read_csv(filename, index_col=0)

    thedata = pandas.read_csv(filename)
    print plot_weather_data(thedata)
