#============================================================
# 작성자 : 김영진
# 작성시작일 : 2017/01/18
# 최종 업데이트 일 : 2017/07/24
# 기능 : 데이터분석 캠프에서 활용하기 위하여 만듦
#     : 데이터를 빠르게 관찰할 수 있도록 만든 UI Demo
#============================================================

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

import 데이터관리함수 as dmf
import 그래프함수 as gmf

import matplotlib.pyplot as plt
from matplotlib import style
import random as rd

from tkinter import *
from tkinter import ttk
import easygui as eg

#import kmeansDef
#from sklearn import tree

#from IPython.display import Image

#import pydotplus


#<Main>============================================================

# --------------------------------------------------------------------------------
# Global 변수 설정 및 옵션
# --------------------------------------------------------------------------------

파일이름 = ''
출력파일이름 = ''

속성리스트 = []
데이터리스트 = []
속성사전 = {}

선택속성 = []
선택속성색인 = []
출력리스트 = []

입력구분자 = ','
출력구분자 = ','
빈크기 = 10
목적속성 = ''
군집수 = 3


# --------------------------------------------------------------------------------
# 창 생성
# --------------------------------------------------------------------------------

창 = Tk()
창.title('Data Analysis User interface')
창.config(width=1024, height=768, bg='gray')



# --------------------------------------------------------------------------------
# 파일 매뉴 화면 구성
# --------------------------------------------------------------------------------
# File Menu Frame 생성
파일메뉴화면 = ttk.Frame(창, padding=(5, 5))
파일메뉴화면.place(height=82, width=150, x=2, y=2) 

# 파일 레이블 
파일레이블 = ttk.Label(파일메뉴화면, text='파일관리', width=20)
파일레이블.grid(row=0, sticky=W)

# 출력 리스트 생성
def 이중리스트출력(이중리스트):
    데이터보기.delete('1.0',END)
    for line in 이중리스트:
        문자열 = ''
        for each in line: 문자열 = 문자열 + each + '\t'
        데이터보기.insert('end', 문자열 + '\n')

# 선택 속성 리스트에 속성 추가
def 속성리스트_생성(속성):
    속성리스트박스.delete(0, 'end')
    for each in 속성리스트: 속성리스트박스.insert('end', each)

# 파일 오픈 버튼
def 파일선택():
    global 파일이름, 입력구분자, 속성리스트, 데이터리스트, 속성사전, 출력리스트, 선택속성, 빈크기, 목적속성
    파일이름 = ''
    입력구분자 = 입력구분자입력공간.get()
    속성리스트 = []
    데이터리스트 = []
    속성사전 = {}
    출력리스트 = []
    선택속성 = []
    빈크기 = 10
    목적속성 = ''
    파일이름입력공간.delete(0,'end')
    데이터보기.delete('1.0', END)

    파일이름 = eg.fileopenbox(msg='파일열기', title='파일열기', default='*', filetypes=None, multiple=False)
    if 파일이름 == None: eg.msgbox('파일이 선택되지 않았습니다.', title='오류')
    else: 
        파일이름입력공간.insert(0, 파일이름)
        속성리스트, 데이터리스트 = dmf.테이블_생성(파일이름, 입력구분자)
        속성사전 = dmf.속성사전_생성(속성리스트, 데이터리스트)
        
        출력리스트 = 데이터리스트.copy()
        출력리스트.insert(0, 속성리스트)
        이중리스트출력(출력리스트)
        
        선택속성 = 속성리스트.copy()
        속성리스트_생성(속성리스트)

파일열기 = ttk.Button(파일메뉴화면, text='파일불러오기', width=18, command=파일선택)
파일열기.grid(row=1, sticky=(W,N))

# 파일 저장 버튼
def file_save():
    global 출력파일이름, 출력구분자, 속성리스트, 데이터리스트, 속성사전, 출력리스트, 선택속성, 빈크기, 목적속성
    출력파일이름 = 출력파일이름입력공간.get()
    출력구분자 = 출력구분자입력공간.get()
    if 출력파일이름 == '': eg.msgbox('저장할 파일명을 입력해주세요.', title='오류')
    else :
        in_split = 파일이름.split('\\')
        out_split = 출력파일이름.split('\\')
        if in_split[-1] == out_split[-1]: eg.msgbox('원본 파일과 다른 이름으로 입력해주세요.', title='오류')
        else:
            print(out_split)
            dmf.데이터파일출력(출력파일이름, 출력리스트, 출력구분자) # 출력 데이터 리스트명을 수정해야 함

파일저장 = ttk.Button(파일메뉴화면, text='파일저장하기', width=18, command=file_save)
파일저장.grid(row=2, sticky=(W,N))



# --------------------------------------------------------------------------------
# 파일 상태 화면 구성
# --------------------------------------------------------------------------------
# File 상태 frame 생성
파일상태화면 = ttk.Frame(창, padding=(5, 5))
파일상태화면.place(height=82, width=868, x=154, y=2) 
ttk.Label(파일상태화면, width=10).grid(column=0, row=0, sticky=W) # 공백출력

# 불러온 파일 위치 레이블
파일역할레이블 = ttk.Label(파일상태화면, text='불러온 파일 위치', width=14)
파일역할레이블.grid(column=0, row=1, sticky=(W,N))

# 파일 명 입력 공간
파일이름입력공간 = ttk.Entry(파일상태화면, width=70, textvariable=파일이름)
파일이름입력공간.grid(column=1, row=1)

# 입력 구분자 레이블
ttk.Label(파일상태화면, width=2).grid(column=2, row=1, sticky=W) # 공백출력
입력구분자레이블 = ttk.Label(파일상태화면, text='입력 구분자', width=10)
입력구분자레이블.grid(column=3, row=1, sticky=W)

# 입력 구분자 입력 공간
입력파일구분자 = StringVar()
입력구분자입력공간 = ttk.Entry(파일상태화면, width=5, textvariable=입력파일구분자, justify='center')
입력구분자입력공간.insert(0, 입력구분자)
입력구분자입력공간.grid(column=4, row=1, sticky=(W,N))

# 구분자 적용 버튼
def 입력구분자적용():
    global 입력구분자
    입력구분자 = 입력구분자입력공간.get()
    #print(입력구분자)
    if '\\t' in 입력구분자: 입력구분자 = '\t'; 입력구분자입력공간
    elif '\\n' in 입력구분자: 입력구분자 = '\n'

ttk.Label(파일상태화면, width=1).grid(column=5, row=1, sticky=W) # 공백출력
입력구분자적용버튼 = ttk.Button(파일상태화면, text='입력 구분자 적용', width=14, command=입력구분자적용)
입력구분자적용버튼.grid(column=6, row=1, sticky=(W,N))

# 저장 파일 이름 레이블
파일역할레이블 = ttk.Label(파일상태화면, text='저장 파일 이름', width=14)
파일역할레이블.grid(column=0, row=2, sticky=(W,N))

# 출력 파일 명 입력 공간
출력파일이름입력공간 = ttk.Entry(파일상태화면, width=70, textvariable=출력파일이름)
출력파일이름입력공간.grid(column=1, row=2)

# 출력 구분자 레이블
출력구분자레이블 = ttk.Label(파일상태화면, text='출력 구분자', width=10)
출력구분자레이블.grid(column=3, row=2, sticky=W)

# 출력 구분자 입력 공간
출력파일구분자 = StringVar()
출력구분자입력공간 = ttk.Entry(파일상태화면, width=5, textvariable=출력파일구분자, justify='center')
출력구분자입력공간.insert(0, 출력구분자)
출력구분자입력공간.grid(column=4, row=2, sticky=(W,N))

# 구분자 적용 버튼
def 출력구분자적용():
    global 출력구분자
    출력구분자 = 출력구분자입력공간.get()
    #print(출력구분자)
    if '\\t' in 출력구분자:
        출력구분자 = '\t'
        출력구분자입력공간
    elif '\\n' in 출력구분자:
        출력구분자 = '\n'

ttk.Label(파일상태화면, width=1).grid(column=5, row=2, sticky=W) # 공백출력
출력구분자적용버튼 = ttk.Button(파일상태화면, text='출력 구분자 적용', width=14, command=출력구분자적용)
출력구분자적용버튼.grid(column=6, row=2, sticky=(W,N))



# --------------------------------------------------------------------------------
# 데이터 살펴보기 Frame 구성
# --------------------------------------------------------------------------------


# --------------------------------------------------------------------------------
# 시군구  목록 Frame 구성
# --------------------------------------------------------------------------------
# 여분 frame 생성
속성화면 = ttk.Frame(창, padding=(5, 5))
속성화면.place(height=680, width=150, x=2, y=86)

속성화면2 = ttk.Frame(창, padding=(5, 5))
속성화면2.place(height=680, width=150, x=154, y=86)

속성레이블 = ttk.Label(속성화면, text='시/도 목록', width=13)
속성레이블.grid(column=0, row=0, sticky=W)

# 속성 목록 레이블
속성레이블 = ttk.Label(속성화면2, text='시/군/구 목록', width=13)
속성레이블.grid(column=0, row=0, sticky=W)

# 선택 속성 적용 버튼
def 선택속성적용하기():
    global 속성리스트, 데이터리스트, 출력리스트, 선택속성, 선택속성색인
    크기 = len(속성리스트)
    if 크기 > 0:
        i = 0; tf = 0
        while i < 크기:
            print(속성리스트박스.selection_includes(i))
            if 속성리스트박스.selection_includes(i) == 1: 
                tf = 1; break
            i = i + 1
        if tf == 1:
            출력리스트 = []; 선택속성 = []; 선택속성색인 = []
            선택속성 = 속성리스트박스.selection_get().strip().split('\n')
            for each in 선택속성: 선택속성색인.append(속성리스트.index(each))
            i = 0
            크기 = len(데이터리스트)
            while i < 크기:
                buf = []
                for each_i in 선택속성색인: buf.append(데이터리스트[i][each_i])
                출력리스트.append(buf)
                i = i + 1
            출력리스트.insert(0, 선택속성)
            이중리스트출력(출력리스트)

속성적용버튼 = ttk.Button(속성화면, text='선택 속성 적용', width=16, command=선택속성적용하기)
속성적용버튼.grid(column=0, row=1, sticky=E)

속성적용버튼 = ttk.Button(속성화면2, text='선택 속성 적용', width=16, command=선택속성적용하기)
속성적용버튼.grid(column=0, row=1, sticky=E)

# 속성 목록 리스트 박스
속성리스트박스 = Listbox(속성화면, height=35, width=16, selectmode=MULTIPLE)
속성리스트박스.grid(column=0, row=2, sticky=(N,W,E,S))

속성리스트박스 = Listbox(속성화면2, height=35, width=16, selectmode=MULTIPLE)
속성리스트박스.grid(column=0, row=2, sticky=(N,W,E,S))

# 속성 목록 리스트 박스 스크롤
속성목록스크롤 = ttk.Scrollbar(속성화면, orient=VERTICAL, command=속성리스트박스.yview)
속성목록스크롤.grid(column=1, row=2, sticky=(N,S))
속성리스트박스['yscrollcommand'] = 속성목록스크롤.set
속성리스트박스.insert(0, '#없음#')

속성목록스크롤1 = ttk.Scrollbar(속성화면2, orient=VERTICAL, command=속성리스트박스.yview)
속성목록스크롤1.grid(column=1, row=2, sticky=(N,S))
속성리스트박스['yscrollcommand'] = 속성목록스크롤1.set
속성리스트박스.insert(0, '#없음#')

# 속성 전체 선택 버튼
def 모든속성선택하기():
    속성리스트박스.selection_set(0, 'end')

속성전체선택버튼 = ttk.Button(속성화면, text='속성 전체 선택', width=16, command=모든속성선택하기)
속성전체선택버튼.grid(column=0, row=3, sticky=E)

속성전체선택버튼 = ttk.Button(속성화면2, text='속성 전체 선택', width=16, command=모든속성선택하기)
속성전체선택버튼.grid(column=0, row=3, sticky=E)

# 모든 속성 해제 버튼
def 모든속성해제하기():
    속성리스트박스.selection_clear(0, 'end')

속성전체해제버튼 = ttk.Button(속성화면, text='속성 전체 해제', width=16, command=모든속성해제하기)
속성전체해제버튼.grid(column=0, row=4, sticky=E)

속성전체해제버튼 = ttk.Button(속성화면2, text='속성 전체 해제', width=16, command=모든속성해제하기)
속성전체해제버튼.grid(column=0, row=4, sticky=E)



# --------------------------------------------------------------------------------
# 데이터분석 Frame 구성
# --------------------------------------------------------------------------------


# --------------------------------------------------------------------------------
# 데이터 결과 Frame 구성
# --------------------------------------------------------------------------------
# 데이터 결과 Frame 생성
데이터결과화면 = ttk.Frame(창, padding=(5, 5))
데이터결과화면.place(height=480, width=868, x=300, y=128) 

# 데이터 결과 레이블
데이터결과레이블 = ttk.Label(데이터결과화면, text='데이터 화면', width=20).grid(column=0, row=0, sticky=W)

# 데이터 표현 공간 : 리스트 박스
데이터보기 = Text(데이터결과화면, height=31, width=119, wrap=NONE) 
데이터보기.grid(column=0, row=1, sticky=(N,W,E,S))

# 데이터 보기 스크롤
데이터보기세로스크롤 = ttk.Scrollbar(데이터결과화면, orient=VERTICAL, command=데이터보기.yview)
데이터보기세로스크롤.grid(column=1, row=1, sticky=(N,S))
데이터보기가로스크롤 = ttk.Scrollbar(데이터결과화면, orient=HORIZONTAL, command=데이터보기.xview)
데이터보기가로스크롤.grid(column=0, row=2, sticky=(W,E))
데이터보기['yscrollcommand'] = 데이터보기세로스크롤.set
데이터보기['xscrollcommand'] = 데이터보기가로스크롤.set

# Clear 버튼
def 데이터초기화():
    global 파일이름, 속성리스트, 데이터리스트, 목적속성
    파일이름 = ''
    속성리스트 = ''
    데이터리스트 = ''
    목적속성 = ''
    파일이름입력공간.delete(0,'end')
    출력파일이름입력공간.delete(0,'end')
    데이터보기.delete('1.0',END)
    속성리스트박스.delete(0, 'end')
    속성리스트박스.insert(0, '#없음#')

전체초기화버튼 = ttk.Button(데이터결과화면, text='Clear', width=18, command=데이터초기화)
전체초기화버튼.grid(column=0, row=4, sticky=E)



# --------------------------------------------------------------------------------
# 종료
# --------------------------------------------------------------------------------

#창.mainloop()


# ================================================================================
# < END >
# ================================================================================










