import FinanceDataReader as fdr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

# 데이터 시각화 Tools - seaborn : matplotlib 을 simply하게 구현해 둔  패키지.
# fig, axes, plt.subplots 로 구성.

fig, axes = plt.subplots(ncols=2)  # ,nrows = 2
plt.show()

# 파이썬 초기화 용 - 사용하지 않기 바람 =======

# def pltconfig_default():
#     sns.reset_defaults()

#     # %matplotlib inline
# pltconfig_default()

# 한글 폰트 설정 =================================================
Han_font = 'Malgun Gothic'

plt.rc('font', family=Han_font)  # 한글폰트 해결.
plt.rc('axes', unicode_minus=False)  # 축에 - 값 적용
plt.style.use('ggplot')  # 원하는 표의 style을 지정.
pd.Series([1, 3, -5, 15, 9]).plot(title='한글제목{}'.format(Han_font))
plt.show()

# 데이터 시각화 Visualization ==============================================
df = fdr.StockListing('KRX')
df_krx = df
# KRX market별 빈도수 구하기와 시각화 =======================================
# Series별 시각화는 Series.value_counts()를 사용

# Unique 한 Market column의 값을 확인
df_krx['Market'].unique
df_krx['Market'].value_counts()

# pd 사용 ==========================
df_krx['Market'].value_counts().plot(kind='barh')  # 기본은 선형, kind = bar / barh
plt.show()

# seaborn 사용 ==========================
sns.countplot(data=df_krx, x='Market')  # 가로형 막대
plt.show()
sns.countplot(data=df_krx, y='Market')  # 세로형 막대
plt.show()

# Sector 상위 30개 시각화 =====================================
# 옵션은 pd, sns, plt 마다 다르므로 확인필요
# pd : .head(30).sort_values(), figsize( , ), fontsize =
# sns : sort_values(), order =

# pd ====================================================================
sector_count_top = df_krx['Sector'].value_counts().head(30)
sector_count_top.plot.barh(title='Sector 빈도수', figsize=(19, 8), fontsize=6)
plt.show()

# SNS ====================================================================
sns.countplot(data=df_krx, y='Sector')
plt.show()

# df_krx_sector = df_krx[df_krx['Sector'].isin(sector_count_top.index)]
# sns.countplot(data=df_krx_sector, y='Sector', order=sector_count_top.index, palette='Blues_r')
# plt.show()

sns.countplot(data=df_krx, y='Sector', order=df_krx['Sector'].value_counts(
).head(30).index, palette='Blues_r')
plt.show()

# , order = sector_count_top.index, palette = 'Blues' / 'Blues_r' )

# 최빈도 Sector data 만 추출
df_krx[df_krx['Sector'] == '특수 목적용 기계 제조업']

# Industry 상위 30개 시각화 =====================================
# pd로
df_krx['Industry'].value_counts().head(30).plot.barh()
plt.show()
df_krx['Industry'].value_counts().head(30).sort_values().plot.barh()
plt.show()

# sns로
sns.countplot(data=df_krx, y='Industry', palette='Reds_r',
              order=df_krx['Industry'].value_counts().head(10).index).set_title('산업구분별 종목수')
plt.show()

# Region 시각화 =====================================
# pd로
df_krx_region = df_krx['Region'].value_counts().sort_values().plot.barh()
plt.show()

# sns로
sns.countplot(data=df_krx, y='Region', palette='Reds_r',
              order=df_krx['Region'].value_counts().index).set_title('소개지별 종목수')
plt.show()

sns.countplot(data=df_krx.sort_values(by='Region'), y='Region',
              palette='Greens').set_title('소개지별 종목수')
plt.show()

# 두개의 변수 빈도수 구하고 시각화 =====================================
# crosstab data값이 0 일때도 표현됨.
# group by or pivot_table : group으로 aggregation하므로 0인 값은 제외.
# crosstab으로 빈도수 구하기 Cross table 의 약자
# crosstab (index항목, 변수컬럼들[1,2...], dropna = False)
# sns.countplot 으로 시각화
# pd.lineplot(연속형) , barplot (범주형), hist (연속된 수치데이터 범주화)

pd.crosstab(df_krx['Market'], df_krx['Region'])
sns.countplot(data=df_krx, y='Market')
sns.countplot(data=df_krx, y='Region')
sns.countplot(data=df_krx, y='Market', hue='Region')  # 보기 어려움.
# hue에 빈도수 적은 것을 넣어주는 것이 좋다.
sns.countplot(data=df_krx, y='Region', hue='Market')
plt.show()

# 연도별 상장 종목 빈도수 분석
# pd로
m_vs_y = pd.crosstab(df['Market'], df['ListingYear'])

plt.figure(figsize=(15, 4))
plt.xticks(rotation=90)

sns.countplot(data=df, x="ListingYear", hue='Market')
plt.show()

m_vs_y
m_vs_y.plot()
m_vs_y.T  # T : Transfeser 가로형(float) --> 세로형(int)
m_vs_y.T.plot()
m_vs_y.T.plot(subplots=True)
m_vs_y.T.plot.bar(subplots=True)
m_vs_y.T.plot.bar()
m_vs_y.T.plot.bar(figsize=(15, 4))
m_vs_y.T.plot.bar(subplots=True)
plt.show()

# relplot(data= , x = , y = , col or row = )# , kind = line) 과 비교할 것.

# Group by 가 리소스 적고, 빠르다 =======================
# df.groupby([index 1 , index 2, .... ])['counting되는 변수/컬럼명'].aggregation funtion
df_krx.groupby('Market').count()
df_krx.groupby('Market')['Symbol'].count()
df_krx.groupby(['Market', 'ListingYear'])['Symbol'].count()
df_krx.groupby(['ListingYear', 'Market'])['Symbol'].count()

df_year_market = df_krx.groupby(['ListingYear', 'Market'])['Symbol'].count()
#  Series형태 -> DataFrame으로 전환.
df_year_market = df_year_market.reset_index()
df_year_market = df_year_market.rename(columns={'Symbol': 'count'})

# Pivot_table =================================
# Pivot은 data 모양만 변경,
# Pivot_table은 data 모양 변경+ aggregation funtion
# Pivot_table(data= , index= , aggfunc =)
pd.pivot_table(data=df, index='ListingYear', aggfunc='count').head(5)
df_year_market = pd.pivot_table(data=df_krx, index=['ListingYear', 'Market'],
                                values='Symbol', aggfunc='count')

# df_year_market = df_year_market.reset_index() # index를 추가하여 datatable로 활용.
df_year_market = df_year_market.rename(columns={'Symbol': 'count'})

# scatterplot 시각화 (x,y 축 모두 수치형 일때 분포)=================================
plt.figure(figsize=(15, 4))
sns.scatterplot(data=df_year_market, x='ListingYear',
                y='count', hue='Market', size='count')
plt.show()

# lineplot 시각화 (x,y 축 모두 수치형 일때 분포)=================================
plt.figure(figsize=(15, 4))
sns.lineplot(data=df_year_market, x='ListingYear', y='count')
sns.lineplot(data=df_year_market, x='ListingYear',
             y='count', ci=None)  # 95% 신뢰구간 생략
sns.lineplot(data=df_year_market, x='ListingYear', y='count', hue='Market')
plt.show()

# relplot 시각화 (여러 가지를 구분하여 같은 x, y로 분포도를 그릴때.
# relationplot
# relplot(data= , x = , y = , col or row = )# , kind = )

sns.relplot(data=df_year_market, x='ListingYear', y='count',
            col='Market', hue='Market')  # , row = 'Market'
sns.relplot(data=df_year_market, x='ListingYear', y='count',
            col='Market', hue='Market', kind='line')  # , row = 'Market'
plt.show()

# 도수분포, 히스토그램 histogram 시각화
# 연속형 수치데이터를 구간 기준으로 데이터 분포 확인
# df['컬럼명'].plot.hist(bins=XX, ) ## bins = 구간 갯수

df['ListingYear'].plot.hist(bins=5, figsize=(10, 4), title='상장연도')
plt.show()

# 데이터 색인 ==============================================
df['ListingYear'] == 2020 & df['Region'] == '서울특별시' & df['Market'] == 'KOSPI'
# [object] array and scalar of type [bool] 오류.
# type 오류 발생- 다른 타입들을 연결한 연산의 경우,
# 연산은 묶어 줄 것.

df[(df['ListingYear'] == 2020) &
   (df['Region'] == '서울특별시') &
   (df['Market'] == 'KOSPI')]

### 시각화 ##########################################
corp_name1 = '한솔홈데코'
corp_name2 = '엠에스오토텍'

df.plot()
df2 = df[[corp_name1, corp_name2]]
df2.plot(secondary_y=corp_name2, title='주가그래프')
plt.show()

### 표준화 standardization ##################################
### Z-score표준화 = (측정값 - 평균) / (표준편차) ############
df_std = (df2-df2.mean()) / (df2.std())
df_std.plot()
plt.axhline(1, color='red', linestyle=':')
plt.show()

### 정규화 normalization ####################################
### (측정값-최소값) / (최대값-최소값) ########################
df_nor = (df2-df2.min())/(df2.max() - df2.min())
df_nor.plot()
plt.axhline(1, color='red', linestyle=':')
plt.show()

### 시작일 대비 현재 성장율 비교 ############################
df_gr = (df2/df2.iloc[0] - 1)
df_gr.plot()
plt.axhline(1, color='red', linestyle=':')
plt.show()

### 여러개 그래프를 한번에 보여주기 ############################
fig, axes = plt.subplots(1, 4, figsize=(15, 10))
df2.plot(secondary_y=corp_name2, ax=axes[0], title='주가그래프')
df_std.plot(ax=axes[1], title='주가표준화')
df_nor.plot(ax=axes[2], title='Z-score 주가')
df_gr.plot(ax=axes[3], title='시작일 대비 성장')
plt.show()

g = df_nor.hist(figsize=(10, 5), bins=20)
plt.show()


# Anatomy of a figure
# This figure shows the name of several matplotlib elements composing a figure

np.random.seed(19680801)

X = np.linspace(0.5, 3.5, 100)
Y1 = 3+np.cos(X)
Y2 = 1+np.cos(1+X/0.75)/2
Y3 = np.random.uniform(Y1, Y2, len(X))

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1, aspect=1)


def minor_tick(x, pos):
    if not x % 1.0:
        return ""
    return f"{x:.2f}"


ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(4))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(4))
# FuncFormatter is created and used automatically
ax.xaxis.set_minor_formatter(minor_tick)

ax.set_xlim(0, 4)
ax.set_ylim(0, 4)

ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=10)
ax.tick_params(which='minor', width=1.0, labelsize=10)
ax.tick_params(which='minor', length=5, labelsize=10, labelcolor='0.25')

ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)

ax.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Blue signal", zorder=10)
ax.plot(X, Y2, c=(1.00, 0.25, 0.25), lw=2, label="Red signal")
ax.plot(X, Y3, linewidth=0,
        marker='o', markerfacecolor='w', markeredgecolor='k')

ax.set_title("Anatomy of a figure", fontsize=20, verticalalignment='bottom')
ax.set_xlabel("X axis label")
ax.set_ylabel("Y axis label")

ax.legend()


def circle(x, y, radius=0.15):
    from matplotlib.patches import Circle
    from matplotlib.patheffects import withStroke
    circle = Circle((x, y), radius, clip_on=False, zorder=10, linewidth=1,
                    edgecolor='black', facecolor=(0, 0, 0, .0125),
                    path_effects=[withStroke(linewidth=5, foreground='w')])
    ax.add_artist(circle)


def text(x, y, text):
    ax.text(x, y, text, backgroundcolor="white",
            ha='center', va='top', weight='bold', color='blue')


# Minor tick
circle(0.50, -0.10)
text(0.50, -0.32, "Minor tick label")

# Major tick
circle(-0.03, 4.00)
text(0.03, 3.80, "Major tick")

# Minor tick
circle(0.00, 3.50)
text(0.00, 3.30, "Minor tick")

# Major tick label
circle(-0.15, 3.00)
text(-0.15, 2.80, "Major tick label")

# X Label
circle(1.80, -0.27)
text(1.80, -0.45, "X axis label")

# Y Label
circle(-0.27, 1.80)
text(-0.27, 1.6, "Y axis label")

# Title
circle(1.60, 4.13)
text(1.60, 3.93, "Title")

# Blue plot
circle(1.75, 2.80)
text(1.75, 2.60, "Line\n(line plot)")

# Red plot
circle(1.20, 0.60)
text(1.20, 0.40, "Line\n(line plot)")

# Scatter plot
circle(3.20, 1.75)
text(3.20, 1.55, "Markers\n(scatter plot)")

# Grid
circle(3.00, 3.00)
text(3.00, 2.80, "Grid")

# Legend
circle(3.70, 3.80)
text(3.70, 3.60, "Legend")

# Axes
circle(0.5, 0.5)
text(0.5, 0.3, "Axes")

# Figure
circle(-0.3, 0.65)
text(-0.3, 0.45, "Figure")

color = 'blue'
ax.annotate('Spines', xy=(4.0, 0.35), xytext=(3.3, 0.5),
            weight='bold', color=color,
            arrowprops=dict(arrowstyle='->',
                            connectionstyle="arc3",
                            color=color))

ax.annotate('', xy=(3.15, 0.0), xytext=(3.45, 0.45),
            weight='bold', color=color,
            arrowprops=dict(arrowstyle='->',
                            connectionstyle="arc3",
                            color=color))

ax.text(4.0, -0.4, "Made with https://matplotlib.org",
        fontsize=10, ha="right", color='.5')

plt.show()
