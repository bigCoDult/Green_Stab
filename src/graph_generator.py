import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 데이터 정의
data = {
    'Year': ['1', '2', '3', '4', '5'],
    'Revenue': [58800, 294000, 882000, 2058000, 4998000],
    'COGS': [15600, 78000, 234000, 546000, 1326000],
    'SGSA': [11760, 56800, 176400, 411600, 999600],
    'EBITA': [31440, 157200, 471600, 1100400, 2672400],
    'Users': [1000, 5000, 15000, 35000, 85000]
}

# DataFrame 생성
df = pd.DataFrame(data)

# Users 스케일 조정 (5년차 85000이 6M 스케일에서 적절한 높이가 되도록)
# 5년차 Users가 대략 4M 정도가 되도록 조정
users_scale_factor = 4000000 / 85000
df['Users_scaled'] = df['Users'] * users_scale_factor

# COGS + SG&A 계산
df['COGS_SGSA'] = df['COGS'] + df['SGSA']

# 그래프 설정
fig, ax = plt.subplots(figsize=(14, 10))

# x축 위치 설정
x = np.arange(len(df['Year']))
width = 0.2  # 막대 너비

# 각 막대의 x 위치 계산
x1 = x - 1.5 * width  # Users (첫 번째 막대)
x2 = x - 0.5 * width  # Revenue (두 번째 막대)
x3 = x + 0.5 * width  # COGS + SG&A (세 번째 막대)
x4 = x + 1.5 * width  # EBITA (네 번째 막대)

# 1번째 막대: Users (초록색)
bars1 = ax.bar(x1, df['Users_scaled'], width, label='Users', color='green', alpha=0.8)

# 2번째 막대: Revenue (빨간색)
bars2 = ax.bar(x2, df['Revenue'], width, label='Revenue', color='red', alpha=0.8)

# 3번째 막대: COGS + SG&A (하늘색과 파란색으로 구분)
# 먼저 COGS (하늘색, 아래쪽)
bars3_cogs = ax.bar(x3, df['COGS'], width, label='COGS', color='skyblue', alpha=0.8)
# 그 위에 SG&A (파란색, 위쪽)
bars3_sgsa = ax.bar(x3, df['SGSA'], width, bottom=df['COGS'], label='SG&A', color='blue', alpha=0.8)

# 4번째 막대: EBITA (분홍색)
bars4 = ax.bar(x4, df['EBITA'], width, label='EBITA', color='yellow', alpha=0.8)

# 그래프 설정
ax.set_xlabel('Year', fontsize=14, fontweight='bold')
ax.set_ylabel('US $', fontsize=14, fontweight='bold')
ax.set_title('5-Year Growth & Performance', fontsize=16, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(df['Year'], fontsize=12)

# y축 설정 (6M까지)
ax.set_ylim(0, 6000000)

# y축 눈금을 더 읽기 쉽게 설정
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000000:.1f}M'))

# 범례 설정 (그래프 아래에 위치)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=5, fontsize=12)

# 격자 추가
ax.grid(True, alpha=0.3, axis='y')

# 레이아웃 조정
plt.tight_layout()

# 그래프 저장
plt.savefig('../img/financial_graph.png', dpi=300, bbox_inches='tight')
plt.show()

# 데이터 요약 출력
print("Data Summary:")
print("=" * 50)
for i, year in enumerate(df['Year']):
    print(f"\n{year}:")
    print(f"  Users: {df['Users'].iloc[i]:,}")
    print(f"  Revenue: ${df['Revenue'].iloc[i]:,}")
    print(f"  COGS: ${df['COGS'].iloc[i]:,}")
    print(f"  SG&A: ${df['SGSA'].iloc[i]:,}")
    print(f"  COGS + SG&A: ${df['COGS_SGSA'].iloc[i]:,}")
    print(f"  EBITA: ${df['EBITA'].iloc[i]:,}")
