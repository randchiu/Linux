# 基础环境配置
---
# 软件下载
进入网站https://downloads.rosettacommons.org/software/academic/ 选择相应版本下载，可只下载源码,可使用`wget`命令（3.15版本源码约5G）
1. 解压（解压后会生成一个新的文件夹，里面包含main目录，原来压缩包可以删除）（解压后约13G）
```
tar -jxvf rosetta_source_3.15_bundle.tar.bz2
```
2. 移动到工作目录（例如将解压后的软件文件夹防置在软件目录，并重命名）
```
mv rosetta.source.release-408 ~/software/rosetta3.15
```
---
# 安装
1. 进入源码目录
```
cd software/rosetta3.15/main/source/
```
2. 编译全部二进制文件
```
./scons.py -j$(nproc) mode=release bin
```
- -j$(nproc)：使用所有 CPU 核心并行编译
- mode=release：生成优化版本（速度快，适合生产运行）
- bin：编译所有可执行文件（包括 rosetta_scripts、relax、mpi_msd 等）

