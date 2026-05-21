# 该脚本可将csv表中不同抗体的轻重链批量提取出来，并将每一个抗体序列导入到一个新的txt或任意格式的文本文件中，运行前可能需要`pip install pandas openpyxl`
# 还需准备模板文件，模板文件中应含有占位符，用于批量替换

import pandas as pd   
import os

# 1. 读取csv文件，如果为excel文件，则将csv替换为excel
csv_path = 'sequence.csv'             # 替换为你的csv文件路径
df = pd.read_csv(csv_path)

# 如果CSV分隔符不是逗号，可选择性取消下列代码注释
# 制表符分隔（常见）
# df = pd.read_csv(csv_path, sep='\t')
# 分号分隔
# df = pd.read_csv(csv_path, sep=';')

# 2. 指定txt模板文件路径（包含占位符的文件）
template_path = 'tempplate.yaml'           # 替换为你的模板文件路径
output_folder = 'output_files'        # 输出文件夹路径

# 3. 创建输出文件夹（如果不存在）
os.makedirs(output_folder, exist_ok=True)

# 4. 读取模板文件内容
with open(template_path, 'r', encoding='utf-8') as f:
    template_content = f.read()

# 5. 遍历每一行数据
for index, row in df.iterrows():
    # 获取A列（文件名）、B列和C列的值
    file_name = str(row['NAME'])         # A列作为文件名
    b_value = str(row['VL'])             # B列数据
    c_value = str(row['VH'])             # C列数据
    
    # 6. 替换模板中的占位符
    # 假设模板中使用 {VL} 和 {VH}}作为占位符
    new_content = template_content.replace('{VL}', b_value).replace('{VH}', c_value)
    
    # 7. 生成txt文件（以A列值命名）
    output_file = os.path.join(output_folder, f"{file_name}.yaml")       #还可在输出文件名上批量加上后缀，如{file_name}_18oxof.yaml
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"已生成文件: {output_file}")

print("全部完成！")
