# this is an example test file
# put stuff in here to test your module
# all functions should begin with test_

# test find_album
def test_find_album():
    '''
    Test the input and output on different function call
    '''
    df = pd.read_csv("TikTok_songs_2022.csv")
    assert callable(find_album)
    assert find_album(df,1) == "Invalid Operation"
    assert find_album(sdas,'sdsa') == "Invalid Operation"
    assert isinstance(get_curr_df(df),pd.DataFrame)
    
# test plot_pop_track
def test_plot_pop_track():
    '''
    Test the input and output on different function call
    '''
    assert callable(plot_pop_track)
    df = pd.read_csv("TikTok_songs_2022.csv")
    assert plot_pop_track(222,'sdsa','sdsa') == "Invalid Operation"
    assert plot_pop_track(df,1,'sdsa') == "Invalid Operation"
    assert plot_pop_track(df,'sdsa',22) == "Invalid Operation"

# test plot_pop_art
def test_plot_pop_art():
    '''
    Test the input and output on different function call
    '''
    assert callable(plot_pop_art)
    df = pd.read_csv("TikTok_songs_2022.csv")
    assert plot_pop_art(222,'sdsa','sdsa') == "Invalid Operation"
    assert plot_pop_art(df,1,'sdsa') == "Invalid Operation"
    assert plot_pop_art(df,'sdsa',22) == "Invalid Operation"
    

# test get_curr_df    
def test_get_curr_df():
    '''
    Test the input and output on different function call
    '''
    df = pd.read_csv("TikTok_songs_2022.csv")
    assert callable(get_curr_df)
    assert get_curr_df(222,'sdsa',['sds'],'sds') == "Invalid Operation"
    assert get_curr_df(df,1,['dsd'],'sdsa') == "Invalid Operation"
    assert get_curr_df(df,1,[],'sds') == "Invalid Operation"
    assert get_curr_df(df,1,['sdsa'],22) == "Invalid Operation"
    assert isinstance(get_curr_df(df),pd.DataFrame) 
    
# test show_heatmap    
def test_show_heatmap():
    '''
    Test the input and output on different function call
    '''
    assert callable(plot_pop_track)
    assert show_heatmap(22) == "Invalid Operation"

# test plot_scatter
def test_plot_scatter():
    '''
    Test the input and output on different function call
    '''
    df = pd.read_csv("TikTok_songs_2022.csv")
    assert callable(plot_pop_track)
    assert plot_scatter(1,'dsds','sds','sdsd','sds',ax) == "Invalid Operation"
    assert plot_scatter(df,1,'sds','sdsd','sds',ax) == "Invalid Operation"
    assert plot_scatter(df,'dsds',2,'sdsd','sds',ax) == "Invalid Operation"
    assert plot_scatter(df,'dsds','sds',3,'sds',ax) == "Invalid Operation"
    assert plot_scatter(df,'dsds','sds','sds',3,ax) == "Invalid Operation"

# test scatter_plot_all_col    
def test_scatter_plot_all_col():
    '''
    Test the input and output on different function call
    '''
    assert callable(plot_pop_track)
    assert scatter_plot_all_col(22) == "Invalid Operation"
    
# test hist_plot    
def test_hist_plot():
    '''
    Test the input and output on different function call
    '''
    assert callable(hist_plot)
    assert hist_plot(df,22) == "Invalid Operation"
    assert hist_plot('dsa',[]) == "Invalid Operation"
    
# test box_plot   
def test_box_plot():
    '''
    Test the input and output on different function call
    '''
    df = pd.read_csv("TikTok_songs_2022.csv")
    assert callable(box_plot)
    assert box_plot(df,22) == "Invalid Operation"
    assert box_plot('dsa',[]) == "Invalid Operation"
    
# test linear_reg   
def test_linear_reg():
    '''
    Test the input and output on different function call
    '''
    assert callable(linear_reg)
    assert linear_reg(22) == "Invalid Operation"
