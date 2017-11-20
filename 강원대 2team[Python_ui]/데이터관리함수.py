#============================================================
# 작성자 : 김영진
# 작성시작일 : 2016/12/27
# 최종 업데이트 일 : 2017/07/23
# 기능 : 데이터분석 캠프에서 활용하기 위하여 만듦
#     : 데이터를 빠르게 관찰할 수 있도록 만든 UI Demo와 연동
#     : 파일 입출력 및 데이터 처리에 관한 기능을 기술
#============================================================

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

import matplotlib.pyplot as plt
from matplotlib import style
import random as rd
#import numpy as np


#------------------------------------------------------------
# 데이터 처리 함수
#------------------------------------------------------------
# csv 파일로부터 데이터 로드

def 테이블_생성(파일명, 구분자=','):
    파일 = open(파일명, 'r')
    속성목록 = []
    인스턴스목록 = []
    i = 0
    for line in 파일:
        i = i + 1
        if i == 1: 속성목록 = line.strip().split(구분자)
        else: 인스턴스목록.append(line.strip().split(구분자))
    파일.close()
    return 속성목록, 인스턴스목록

#------------------------------------------------------------
# 속성사전 생성 : 속성목록과 인스턴스목록을 가지고 속성사전 생성

def 속성사전_생성(속성목록, 인스턴스목록):
    속성사전 = {}
    for i in range(0, len(속성목록)):
        리스트 = []
        for 인스턴스 in 인스턴스목록:
            리스트.append(인스턴스[i])
        속성사전[속성목록[i]] = 리스트
    return 속성사전

#------------------------------------------------------------
# 1차원 리스트의 문자열을 파일로 출력
def 리스트파일출력(파일명, 단일리스트):
    파일 = open(파일명, 'w')
    for each in 단일리스트:
        print(each, file=파일)
    파일.close()
    return 1

# 2차원 리스트 형태의 테이블을 csv 유형의 파일로 출력
def 데이터파일출력(파일명, 이중리스트, 구분자=','):
    파일 = open(파일명, 'w')
    for 단일리스트 in 이중리스트:
        크기 = len(단일리스트)
        for i in range(0, 크기):
            if i != 0: print(구분자, end='', file=파일)
            print(단일리스트[i], end='', file=파일)
        print(file=파일)
    파일.close()
    return 1
# 속성의 색인을 찾는 함수
def 속성색인찾기(속성목록, 선택속성명):
   index = 999999
   i=0
   for each in 속성목록:
      if 선택속성명 == each:
         index =i
         break
      i = i+1
   return index






