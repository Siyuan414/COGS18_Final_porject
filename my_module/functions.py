# this is an example module file
# put stuff in here (or make your own file)
# that you will import into your notebook
# classes, functions, variables, etc

import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pytest

# fucntion to select the top album and return as a df 
def find_album(df,artist):
    '''
    assert check the inputs
    '''
    assert isinstance(df,pd.DataFrame)
    assert isinstance(artist,str)
    df = df.loc[lambda df: df['artist_name'] == artist]
    return df

# function to plot the top track use barplot 
def plot_pop_track(df,c1,c2):
    '''
    assert check the inputs
    '''
    assert isinstance(c1,str)
    assert isinstance(c2,str)
    assert isinstance(df,pd.DataFrame)
    
    plt.figure(figsize=(20,6))
    sns.barplot(data=df[[c1, c2]], x= c1,y= c2)
    plt.ylabel('Popularity')
    plt.xlabel('Track_name')

    plt.show()

# function to plot the top artist use barplot 
def plot_pop_art(df,c1,c2):
    '''
    assert check the inputs
    '''
    assert isinstance(c1,str)
    assert isinstance(c2,str)
    assert isinstance(df,pd.DataFrame)
    
    plt.figure(figsize=(15,6))
    sns.barplot(data=df[[c1, c2]], x= c1,y= c2)
    plt.ylabel('Popularity')
    plt.xlabel('Artist')

    plt.show()
    
# function to filter the dataframe with specific column
def get_curr_df(df,c1,array,name1):
    '''
    assert check the inputs
    '''
    
    assert isinstance(df,pd.DataFrame)
    assert isinstance(c1,str)
    assert len(array)!=0
    assert isinstance(name1,str)
    
    df.loc[~df[c1].isin(array),c1] = name1
    df1 = df
    return df1

#show the heatmap with df 
def show_heatmap(df):
    '''
    assert check the inputs
    '''
    assert isinstance(df,pd.DataFrame)
    palette = sns.diverging_palette(299, 192, s=75, l=50, as_cmap = True, sep = 20,center = 'dark')
    sns.heatmap(df.corr(), annot = True,
               cmap = palette, square = True, linewidth = .5, linecolor="#09101F",
               vmin = -1, vmax = 1, fmt = ".2f")

    return 

# scatter plot 
def plot_scatter(df,x,y,color1,color2,ax):
    '''
    assert check the inputs
    '''
    
    assert isinstance(df,pd.DataFrame)
    assert isinstance(x,str)
    assert isinstance(y,str)
    assert isinstance(color1,str)
    assert isinstance(color2,str)
    
    sns.regplot(data = df, x = x, y = y,ax = ax, scatter_kws = {'color':color1}, line_kws = {'color':color2, 'linewidth': 3})
          


# scatter plot to show all the column and included subplot 
def scatter_plot_all_col(df):
    '''
    assert check the inputs
    '''
    
    assert isinstance(df,pd.DataFrame)
    
    all_cols = ['danceability', 'energy', 'loudness', 'speechiness','acousticness',
                'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms']
    fig, axs = plt.subplots(4,3, figsize=(20, 20))
    for i in range(10):
        plot_scatter(df,'track_pop',all_cols[i],'#1db5d0','#ca7fc9',axs[i//3][i%3])
    fig.delaxes(axs[3][2])
    fig.delaxes(axs[3][1])
    plt.show()


# history plot 
def hist_plot(df,cols):
    '''
    assert check the inputs
    '''
    
    assert isinstance(df,pd.DataFrame)
    assert isinstance(cols,list)
    
    fig, ax = plt.subplots(3,4, figsize=(35, 25))
    for i in range(len(cols)):
            sns.histplot(data = df, x = cols[i], bins = 20, ax = ax[i // 4][i % 4],kde=True)
    plt.show()
    
    
# box plot 
def box_plot(df,cols):
    '''
    assert check the inputs
    '''
    
    assert isinstance(df,pd.DataFrame)
    assert isinstance(cols,list)
    
    fig, ax = plt.subplots(3,4, figsize=(35, 25))
    for i in range(len(cols)):
            sns.boxplot(x = df[cols[i]], ax = ax[i // 4][i % 4])
    plt.show()


# linear regression module and plots   
def linear_reg(df):
    '''
    assert check the inputs
    '''
    
    assert isinstance(df,pd.DataFrame)
    
    all_cols = ['danceability', 'energy', 'loudness', 'speechiness','acousticness',
                'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms']
    fig = plt.figure(figsize=(30, 20))
    for i,c in enumerate(all_cols):
        
        Model = LinearRegression()
        X = df['track_pop'].values.reshape(-1,1)
        Y = df[c].values.reshape(-1,1)
        Model.fit(X,Y)
        y_pred = Model.predict(X)
        ax = fig.add_subplot(3, 4, i+1)
        plt.scatter(X,Y)
        plt.plot(X,y_pred,color='red')
        plt.xlabel('track_pop')
        plt.ylabel(c) 
        rsq = 'coef: ' + str(Model.score(X, Y)) 
        plt.title(rsq)
        





    