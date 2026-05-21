import pandas as pd
import os

# ========== 配置区域 ==========
INPUT_EXCEL = 'protein_sequences.xlsx'   # 输入Excel文件路径
OUTPUT_CSV = 'paired_sequences.csv'   # 输出文件路径，输出为csv格式文件

# Sheet名称
LIGHT_SHEET = '轻链'      # 轻链所在sheet名
HEAVY_SHEET = '重链'      # 重链所在sheet名

# 列名（根据你的实际表头修改）
SEQUENCE_COL = 'sequence'   # 序列所在列名
ID_COL = 'id'               # 编号列名（如果没有就注释掉这行）

# ========== 读取数据 ==========
# 读取轻链Sheet
df_light = pd.read_excel(INPUT_EXCEL, sheet_name=LIGHT_SHEET)
print(f"轻链Sheet列名: {df_light.columns.tolist()}")
print(f"轻链数量: {len(df_light)}")

# 读取重链Sheet
df_heavy = pd.read_excel(INPUT_EXCEL, sheet_name=HEAVY_SHEET)
print(f"重链Sheet列名: {df_heavy.columns.tolist()}")
print(f"重链数量: {len(df_heavy)}")

# ========== 提取序列 ==========
light_seqs = df_light[SEQUENCE_COL].astype(str).tolist()
heavy_seqs = df_heavy[SEQUENCE_COL].astype(str).tolist()

# 提取ID（如果有的话）
if ID_COL in df_light.columns and ID_COL in df_heavy.columns:
    light_ids = df_light[ID_COL].astype(str).tolist()
    heavy_ids = df_heavy[ID_COL].astype(str).tolist()
else:
    # 没有ID列，自动生成
    light_ids = [f'L{i+1}' for i in range(len(df_light))]
    heavy_ids = [f'H{i+1}' for i in range(len(df_heavy))]

# ========== 两两配对 ==========
pairs = []
pair_num = 1

for i, (l_seq, l_id) in enumerate(zip(light_seqs, light_ids)):
    for j, (h_seq, h_id) in enumerate(zip(heavy_seqs, heavy_ids)):
        pairs.append({
            'pair_id': f'Pair_{pair_num:04d}',
            'light_id': l_id,
            'light_chain': l_seq,
            'heavy_id': h_id,
            'heavy_chain': h_seq
        })
        pair_num += 1

# ========== 保存结果 ==========
df_result = pd.DataFrame(pairs)
df_result.to_csv(OUTPUT_CSV, index=False, encoding='utf-8-sig')

print(f"\n✓ 配对完成！")
print(f"✓ 轻链: {len(light_seqs)} 条")
print(f"✓ 重链: {len(heavy_seqs)} 条")
print(f"✓ 总配对数: {len(pairs)} 对")
print(f"✓ 输出文件: {os.path.abspath(OUTPUT_CSV)}")

# 显示前3行预览
print(f"\n前3行预览:")
print(df_result.head(3))
