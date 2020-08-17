# 통계 import
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pylab as plt
import csv
from pandas import DataFrame
import os


def draw(team1, team2):
    file = 'static/team_project/function/possession.png'
    if os.path.isfile(file):
        os.remove(file)

    # csv 가져오기
    df = pd.read_csv('static/team_project/all_team.csv')

    # 1팀 경기만 추출
    df1 = df[df['Team'].isin([team1])]

    # 1팀 시즌별로 분류
    df_team1_1920 = df1[df['Matchyear'].isin(['2019/20'])]
    df_team1_1819 = df1[df['Matchyear'].isin(['2018/19'])]
    df_team1_1718 = df1[df['Matchyear'].isin(['2017/18'])]
    df_team1_1617 = df1[df['Matchyear'].isin(['2016/17'])]
    df_team1_1516 = df1[df['Matchyear'].isin(['2015/16'])]
    # 1팀 시즌별 평균
    df_team1_1920_mean = df_team1_1920.mean(axis=0)
    df_team1_1819_mean = df_team1_1819.mean(axis=0)
    df_team1_1718_mean = df_team1_1718.mean(axis=0)
    df_team1_1617_mean = df_team1_1617.mean(axis=0)
    df_team1_1516_mean = df_team1_1516.mean(axis=0)
    # 1팀 시즌별 평균 df
    df1 = DataFrame([df_team1_1516_mean.fillna(0), df_team1_1617_mean.fillna(0), df_team1_1718_mean.fillna(0),
                     df_team1_1819_mean.fillna(0), df_team1_1920_mean.fillna(0)])


    # 2팀 경기만 추출
    df2 = df[df['Team'].isin([team2])]

    # 2팀 시즌별로 분류
    df_team2_1920 = df2[df['Matchyear'].isin(['2019/20'])]
    df_team2_1819 = df2[df['Matchyear'].isin(['2018/19'])]
    df_team2_1718 = df2[df['Matchyear'].isin(['2017/18'])]
    df_team2_1617 = df2[df['Matchyear'].isin(['2016/17'])]
    df_team2_1516 = df2[df['Matchyear'].isin(['2015/16'])]

    # 2팀 시즌별 평균
    df_team2_1920_mean = df_team2_1920.mean(axis=0)
    df_team2_1819_mean = df_team2_1819.mean(axis=0)
    df_team2_1718_mean = df_team2_1718.mean(axis=0)
    df_team2_1617_mean = df_team2_1617.mean(axis=0)
    df_team2_1516_mean = df_team2_1516.mean(axis=0)

    # 2팀 시즌별 평균 df
    df2 = DataFrame([df_team2_1516_mean.fillna(0), df_team2_1617_mean.fillna(0), df_team2_1718_mean.fillna(0),
                     df_team2_1819_mean.fillna(0), df_team2_1920_mean.fillna(0)])

    ##############
    # Possession #
    ##############
    df1_list = []
    df2_list = []
    for item in df1['Possession']:
        df1_list.append(item)
    for item in df2['Possession']:
        df2_list.append(item)

    matplotlib.use('Agg')
    x_values = ['2015/16', '2016/17', '2017/18', '2018/19', '2019/20', ]
    plt.plot(x_values, df1_list, marker='o')
    plt.plot(x_values, df2_list, marker='o')

    plt.xlabel('Season')
    plt.ylabel('Possession')
    plt.legend([team1, team2])
    plt.title('Possession')
    plt.grid()
    plt.draw()

    fig = plt.gcf()
    fig.savefig('static/team_project/function/possession.png', dpi=fig.dpi)
    plt.switch_backend('agg')
    plt.close()

    ##############
    # Shots #
    ##############
    df1_list = []
    df2_list = []
    for item in df1['Shots']:
        df1_list.append(item)
    for item in df2['Shots']:
        df2_list.append(item)

    matplotlib.use('Agg')
    plt.plot(x_values, df1_list, marker='o')
    plt.plot(x_values, df2_list, marker='o')

    plt.xlabel('Season')
    plt.ylabel('Shots')
    plt.legend([team1, team2])
    # plt.title(team1,'과',team2,'의 Possession')
    plt.title('Shots')
    plt.grid()
    plt.draw()

    fig = plt.gcf()
    fig.savefig('static/team_project/function/Shots.png', dpi=fig.dpi)
    plt.switch_backend('agg')
    plt.close()


    ##############
    # Shots_on_Target #
    ##############
    df1_list = []
    df2_list = []
    for item in df1['Shots_on_Target']:
        df1_list.append(item)
    for item in df2['Shots_on_Target']:
        df2_list.append(item)

    matplotlib.use('Agg')
    plt.plot(x_values, df1_list, marker='o')
    plt.plot(x_values, df2_list, marker='o')

    plt.xlabel('Season')
    plt.ylabel('Shots_on_Target')
    plt.legend([team1, team2])
    # plt.title(team1,'과',team2,'의 Possession')
    plt.title('Shots_on_Target')
    plt.grid()
    plt.draw()

    fig = plt.gcf()
    fig.savefig('static/team_project/function/Shots_on_Target.png', dpi=fig.dpi)
    plt.switch_backend('agg')
    plt.close()


    ##############
    # Touches #
    ##############
    df1_list = []
    df2_list = []
    for item in df1['Touches']:
        df1_list.append(item)
    for item in df2['Touches']:
        df2_list.append(item)

    matplotlib.use('Agg')
    plt.plot(x_values, df1_list, marker='o')
    plt.plot(x_values, df2_list, marker='o')

    plt.xlabel('Season')
    plt.ylabel('Touches')
    plt.legend([team1, team2])
    plt.title('Touches')
    plt.grid()
    plt.draw()

    fig = plt.gcf()
    fig.savefig('static/team_project/function/Touches.png', dpi=fig.dpi)
    plt.switch_backend('agg')
    plt.close()


    ##############
    # Passes #
    ##############
    df1_list = []
    df2_list = []
    for item in df1['Passes']:
        df1_list.append(item)
    for item in df2['Passes']:
        df2_list.append(item)

    matplotlib.use('Agg')
    plt.plot(x_values, df1_list, marker='o')
    plt.plot(x_values, df2_list, marker='o')

    plt.xlabel('Season')
    plt.ylabel('Passes')
    plt.legend([team1, team2])
    # plt.title(team1,'과',team2,'의 Possession')
    plt.title('Passes')
    plt.grid()
    plt.draw()

    fig = plt.gcf()
    fig.savefig('static/team_project/function/Passes.png', dpi=fig.dpi)
    plt.switch_backend('agg')
    plt.close()

    ##############
    # Tackles #
    ##############
    df1_list = []
    df2_list = []
    for item in df1['Tackles']:
        df1_list.append(item)
    for item in df2['Tackles']:
        df2_list.append(item)

    matplotlib.use('Agg')
    plt.plot(x_values, df1_list, marker='o')
    plt.plot(x_values, df2_list, marker='o')

    plt.xlabel('Season')
    plt.ylabel('Tackles')
    plt.legend([team1, team2])
    plt.title('Tackles')
    plt.grid()
    plt.draw()

    fig = plt.gcf()
    fig.savefig('static/team_project/function/Tackles.png', dpi=fig.dpi)
    plt.switch_backend('agg')
    plt.close()

    ##############
    # Clearances #
    ##############
    df1_list = []
    df2_list = []
    for item in df1['Clearances']:
        df1_list.append(item)
    for item in df2['Clearances']:
        df2_list.append(item)

    matplotlib.use('Agg')
    plt.plot(x_values, df1_list, marker='o')
    plt.plot(x_values, df2_list, marker='o')

    plt.xlabel('Season')
    plt.ylabel('Clearances')
    plt.legend([team1, team2])
    plt.title('Clearances')
    plt.grid()
    plt.draw()

    fig = plt.gcf()
    fig.savefig('static/team_project/function/Clearances.png', dpi=fig.dpi)
    plt.switch_backend('agg')
    plt.close()

    ##############
    # Corners #
    ##############
    df1_list = []
    df2_list = []
    for item in df1['Corners']:
        df1_list.append(item)
    for item in df2['Corners']:
        df2_list.append(item)

    matplotlib.use('Agg')
    plt.plot(x_values, df1_list, marker='o')
    plt.plot(x_values, df2_list, marker='o')

    plt.xlabel('Season')
    plt.ylabel('Corners')
    plt.legend([team1, team2])
    plt.title('Corners')
    plt.grid()

    plt.draw()

    fig = plt.gcf()
    fig.savefig('static/team_project/function/Corners.png', dpi=fig.dpi)
    plt.switch_backend('agg')
    plt.close()

    ##############
    # Offsides #
    ##############
    df1_list = []
    df2_list = []
    for item in df1['Offsides']:
        df1_list.append(item)
    for item in df2['Offsides']:
        df2_list.append(item)

    matplotlib.use('Agg')
    plt.plot(x_values, df1_list, marker='o')
    plt.plot(x_values, df2_list, marker='o')

    plt.xlabel('Season')
    plt.ylabel('Offsides')
    plt.legend([team1, team2])
    plt.title('Offsides')
    plt.grid()
    plt.draw()

    fig = plt.gcf()
    fig.savefig('static/team_project/function/Offsides.png', dpi=fig.dpi)
    plt.switch_backend('agg')
    plt.close()

    ##############
    # Yellow_cards #
    ##############
    df1_list = []
    df2_list = []
    for item in df1['Yellow_cards']:
        df1_list.append(item)
    for item in df2['Yellow_cards']:
        df2_list.append(item)

    matplotlib.use('Agg')
    plt.plot(x_values, df1_list, marker='o')
    plt.plot(x_values, df2_list, marker='o')

    plt.xlabel('Season')
    plt.ylabel('Yellow_cards')
    plt.legend([team1, team2])
    plt.title('Yellow_cards')
    plt.grid()
    plt.draw()

    fig = plt.gcf()
    fig.savefig('static/team_project/function/Yellow_cards.png', dpi=fig.dpi)
    plt.switch_backend('agg')
    plt.close()



    ##############
    # Red_cards #
    ##############
    df1_list = []
    df2_list = []
    for item in df1['Red_cards']:
        df1_list.append(item)
    for item in df2['Red_cards']:
        df2_list.append(item)

    matplotlib.use('Agg')
    plt.plot(x_values, df1_list, marker='o')
    plt.plot(x_values, df2_list, marker='o')

    plt.xlabel('Season')
    plt.ylabel('Red_cards')
    plt.legend([team1, team2])
    plt.title('Red_cards')
    plt.grid()
    plt.draw()

    fig = plt.gcf()
    fig.savefig('static/team_project/function/Red_cards.png', dpi=fig.dpi)
    plt.switch_backend('agg')
    plt.close()



    ##############
    # Fouls_conceded #
    ##############
    df1_list = []
    df2_list = []
    for item in df1['Fouls_conceded']:
        df1_list.append(item)
    for item in df2['Fouls_conceded']:
        df2_list.append(item)

    matplotlib.use('Agg')
    plt.plot(x_values, df1_list, marker='o')
    plt.plot(x_values, df2_list, marker='o')

    plt.xlabel('Season')
    plt.ylabel('Fouls_conceded')
    plt.legend([team1, team2])
    plt.title('Fouls_conceded')
    plt.grid()
    plt.draw()

    fig = plt.gcf()
    fig.savefig('static/team_project/function/Fouls_conceded.png', dpi=fig.dpi)
    plt.switch_backend('agg')
    plt.close()

    return