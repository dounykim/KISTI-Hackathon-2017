#============================================================
# 작성자 : 김영진
# 작성시작일 : 2016/12/27
# 최종 업데이트 일 : 2017/07/24
# 기능 : 데이터분석 캠프에서 활용하기 위하여 만듦
#     : 데이터를 빠르게 관찰할 수 있도록 만든 UI Demo와 연동
#     : 다양한 그래프에 대한 기능 기술
#============================================================

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

import matplotlib.pyplot as plt
from matplotlib import style
import random as rd
#import numpy as np



#------------------------------------------------------------
# 그래프 함수 : 단일 속성
#------------------------------------------------------------

#그래프 값 표현
def autolabel_x(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%.2f' % float(height),
                ha='center', va='bottom')

def autolabel_y(rects):
    for rect in rects:
        height = rect.get_height()
        #button = rect.
        plt.text(rect.get_x() + rect.get_width()/2., rect.get_y()+(height/2),
                '%.2f' %float(height),
                ha='center', va='bottom')



#선형 그래프
def 선형그래프(ylist, ytitle='', color='b'):
    result = False
    if len(ylist) > 1:
        x_v = [x for x in range(0,len(ylist))]
        plt.figure('선형 그래프', figsize=(6,6), facecolor=(1.0,1.0,0.8))
        plt.subplots_adjust(top=0.95, bottom=0.08, left=0.15, right=0.95, wspace=0.2, hspace=0.1)
        plt.plot(x_v, ylist, color+'-', linewidth=3.0, alpha=0.3)
        plt.ylabel(ytitle, fontsize=15)
        plt.show()
        result = True
    return result


#히스토그램
def 히스토그램(d_list, bins=10, a_name='', color='b'):
    result = False
    if len(d_list) != 0:
        plt.figure('히스토그램', figsize=(6,6), facecolor=(1.0,1.0,0.8))
        plt.subplots_adjust(top=0.95, bottom=0.125, left=0.1, right=0.95, wspace=0.2, hspace=0.1)
        his_plt = plt.hist(d_list, bins, normed=True, facecolor=color)
        plt.xlabel(a_name, fontsize=15)
        plt.grid(True)
        plt.show()
        result = True
    return result


def 히스토그램_선형(d_list, bins=10, a_name='', color='b'):
    result = False
    if len(d_list) > 1:
        plt.figure('히스토그램 및 선형 그래프', figsize=(15,5), facecolor=(1.0,1.0,0.8))
        plt.subplots_adjust(top=0.95, bottom=0.125, left=0.08, right=0.95, wspace=0.25, hspace=0.1)

        plt.subplot(1,3,1)
        his_plt = plt.hist(d_list, bins, normed=True, facecolor=color)
        plt.xlabel(a_name, fontsize=15)
        plt.grid(True)

        plt.subplot(1,3,2)
        x_v = [x for x in range(0,len(d_list))]
        plt.plot(x_v, d_list, color+'-', linewidth=3.0, alpha=0.3)
        plt.ylabel(a_name, fontsize=15)
        plt.grid(True)

        plt.subplot(1,3,3)
        plt.axis('off')
        plt.text(0.1, 0.9, '데이터수 : %d' %len(d_list), size=16)
        plt.text(0.1, 0.8, '최 소 값 : %.4f' %min(d_list), size=16)
        plt.text(0.1, 0.7, '최 대 값 : %.4f' %max(d_list), size=16)
        plt.text(0.1, 0.6, '총    합 : %.4f' %sum(d_list), size=16)
        평균 = sum(d_list) / len(d_list)
        plt.text(0.1, 0.5, '평    균 : %.4f' %평균, size=16)
        분산 = 0
        for each in d_list: 분산 += ((each - 평균) ** 2)
        분산 = 분산 / len(d_list)
        plt.text(0.1, 0.4, '분    산 : %.4f' %분산, size=16)
        표준편차 = 분산 ** (1/2)
        plt.text(0.1, 0.3, '표준편차 : %.4f' %표준편차, size=16)

        plt.show()        
        result = True
    return result



# 막대 그래프
def 도수그래프(d_list, a_name='', select_color='b'):
    result = False
    if len(d_list) > 1:
        a_value = list(set(d_list))
        frequency = []
        for i in range(len(a_value)):
            frequency.append(d_list.count(a_value[i]))
        position = range(1, len(frequency) + 1)

        plt.figure('막대 그래프', figsize=(8,6), facecolor=(1.0,1.0,0.8))
        plt.subplots_adjust(left=0.23, right=0.95)
        bar_plt = plt.barh(position, frequency, align='center', color=select_color, edgecolor=select_color, alpha=0.5)

        plt.yticks(position, a_value)
        #style.use('ggplot') 
        plt.xlabel('빈도수')
        plt.title(a_name+'\n')
        plt.grid()
        
        for rec in bar_plt:
            height = rec.get_height()
            width = rec.get_width()
            plt.text(width, rec.get_y(), width, ha='left', va='bottom')

        plt.show()
        result = True
    return result



# 원 그래프
def 원그래프(d_list, a_name='', select_color='b'):
    result = False
    if len(d_list) > 0:
        a_value = list(set(d_list))
        rate = []
        for i in range(len(a_value)):
            rate.append(d_list.count(a_value[i])/len(d_list))
            
        explode = [ 0.01*len(a_value) ] * len(a_value)
        plt.figure('원 그래프', figsize=(6,6), facecolor=(1.0,1.0,0.8))
        plt.pie(rate, explode=explode, labels=a_value, autopct='%0.1f%%', shadow=True, startangle=90)
        plt.show()
        
        result = True
    return result



# 도수_원 그래프
def 도수_원(d_list, a_name='', select_color='b'):
    result = False
    if len(d_list) > 0:
        a_value = list(set(d_list))

        frequency = []
        for i in range(len(a_value)):
            frequency.append(d_list.count(a_value[i]))
        position = range(1, len(frequency) + 1)

        rate = []
        for i in range(len(a_value)):
            rate.append(d_list.count(a_value[i])/len(d_list))
        explode = [ 0.01*len(a_value) ] * len(a_value)

        plt.figure('도수 및 원 그래프', figsize=(14,6), facecolor=(1.0,1.0,0.8))
        plt.subplots_adjust(left=0.15, right=0.9)

        plt.subplot(1,2,1)
        bar_plt = plt.barh(position, frequency, align='center', color=select_color, edgecolor=select_color, alpha=0.5)
        plt.yticks(position, a_value)
        #style.use('ggplot') 
        plt.xlabel('빈도수')
        plt.title(a_name+'\n')
        plt.grid()
        for rec in bar_plt:
            height = rec.get_height()
            width = rec.get_width()
            plt.text(width, rec.get_y(), width, ha='left', va='bottom')

        plt.subplot(1,2,2)
        plt.pie(rate, explode=explode, labels=a_value, autopct='%0.1f%%', shadow=True, startangle=90)
        
        plt.show()
        result = True
    return result




#------------------------------------------------------------
# 그래프 함수 : 두 속성 이상
#------------------------------------------------------------

#xy plot
def xy그래프(xlist, ylist, xtitle='', ytitle='', color='b'):
    result = False
    if len(xlist) == len(ylist):
        plt.figure('xy그래프', figsize=(6,6), facecolor=(1.0,1.0,0.8))
        plt.subplots_adjust(top=0.95, bottom=0.1, left=0.15, right=0.95, wspace=0.2, hspace=0.1)
        plt.plot(xlist, ylist, color+'o', alpha=0.3)
        plt.xlabel(xtitle, fontsize=15)
        plt.ylabel(ytitle, fontsize=15)
        plt.show()
        result = True
    return result



#xy plot 멀티
def xy그래프_멀티(d_list, name_list):
    result = False
    if len(d_list) == len(name_list):
        plt.figure('속성 교차 그래프', figsize=(10,9), facecolor=(1.0,1.0,0.8))
        plt.subplots_adjust(top=0.95, bottom=0.08, left=0.1, right=0.95, wspace=0.2, hspace=0.1)

        plt.subplot(3,3,1)
        plt.ylabel(name_list[0], fontsize=15)
        plt.plot(d_list[0], d_list[0], 'ro', alpha=0.5)

        plt.subplot(332)
        plt.plot(d_list[1], d_list[0], 'ro', alpha=0.5)

        plt.subplot(333)
        plt.plot(d_list[2], d_list[0], 'ro', alpha=0.5)


        plt.subplot(334)
        plt.ylabel(name_list[1], fontsize=15)
        plt.plot(d_list[0], d_list[1], 'ro', alpha=0.5)

        plt.subplot(335)
        plt.plot(d_list[1], d_list[1], 'ro', alpha=0.5)

        plt.subplot(336)
        plt.plot(d_list[2], d_list[1], 'ro', alpha=0.5)


        plt.subplot(337)
        plt.ylabel(name_list[2], fontsize=15)
        plt.xlabel(name_list[0], fontsize=15)
        plt.plot(d_list[0], d_list[2], 'ro', alpha=0.5)

        plt.subplot(338)
        plt.xlabel(name_list[1], fontsize=15)
        plt.plot(d_list[1], d_list[2], 'ro', alpha=0.5)

        plt.subplot(339)
        plt.xlabel(name_list[2], fontsize=15)
        plt.plot(d_list[2], d_list[2], 'ro', alpha=0.5)

        plt.show()
        result = True
    return result



def 비율그래프(d_list, t_list, d_name='', t_name='', color='b'):
    result = False
    if len(d_list) > 0 and len(t_list) > 0:

        d_value = list(set(d_list))
        d_rate = []
        for i in range(len(d_value)): d_rate.append(d_list.count(d_value[i])/len(d_list))
        d_position = range(0, len(d_value))

        plt.figure('막대 그래프', figsize=(12,6), facecolor=(1.0,1.0,0.8))
        plt.subplots_adjust(top=0.90, bottom=0.1, left=0.1, right=0.95, wspace=0.2, hspace=0.1)

        plt.subplot(1,2,1)
        gr_plt=plt.bar(d_position, d_rate, align='center', color=color, edgecolor=color, alpha=0.5)
        plt.xticks(d_position, d_value)
        plt.ylabel('비율', fontsize=12)
        plt.title(d_name+'\n')
        plt.grid()
        autolabel_x(gr_plt)

        plt.subplot(1,2,2)
        t_value = list(set(t_list))
        
        t_rate_pare = [0] * len(d_value)
        for i in range(len(d_value)): t_rate_pare[i] = [0] * len(t_value)
        for i in range(len(d_list)):
            d_ind = d_value.index(d_list[i])
            t_ind = t_value.index(t_list[i])
            t_rate_pare[d_ind][t_ind] += 1

        plot_list = []
        p_ind = [x for x in range(0,len(d_value))]
        width = 0.8

        bottom_list = []
        bottom_list.append([0]*len(d_value))

        for j in range(len(t_value)):
            rate_list = []
            for each in t_rate_pare: rate_list.append(each[j] / sum(each))

            buf = rate_list.copy()
            for i in range(len(buf)): buf[i] += bottom_list[-1][i]
            bottom_list.append(buf)

            g_col = rd.random()
            b_col = rd.random()
            plot_list.append(plt.bar(left=p_ind, height=rate_list,
                                     width=width, bottom=bottom_list[j],
                                     align='center',
                                     color=(1.0,g_col,b_col), edgecolor=color, alpha=0.5))

        plt.ylim(ymin=0.0, ymax=1.2)
        plt.xticks(d_position, d_value)
        plt.title(d_name+'-'+t_name+'\n')
        plt.grid()
        plt.legend(plot_list, t_value, fontsize=10) #지표
        for each in plot_list: autolabel_y(each)
        plt.show()
        result = True
    return result








