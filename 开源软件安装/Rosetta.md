# 安装依赖包
```
sudo apt update
sudo apt install -y gcc g++ gfortran build-essential libhdf5-dev libgmp-dev
```
---
# 软件下载
进入网站https://downloads.rosettacommons.org/software/academic/ 选择相应版本下载，可只下载源码,可使用`wget -c`命令（3.15版本源码约5G）
1. 解压（解压后会生成一个新的文件夹，里面包含main目录，原来压缩包可以删除）（解压后约13G）
```
tar -jxvf rosetta_source_3.15_bundle.tar.bz2
```
2. 移动到apps目录（例如将解压后的软件文件夹防置在软件目录，并重命名）
```
mv rosetta.source.release-408 ~/apps/rosetta3.15
```
---
# 安装
1. 进入源码目录
```
cd apps/rosetta3.15/main/source/
```
2. 编译前需要先将安装的依赖包hdf5添加环境变量，不然会编译报错
```
export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/hdf5/serial:$LD_LIBRARY_PATH
export INCLUDE=usr/include/hdf5/serial:$INCLUDE
```
2. 编译全部二进制文件
```
./scons.py -j$(nproc) mode=release bin
```
- -j$(nproc)：使用所有 CPU 核心并行编译
- mode=release：生成优化版本（速度快，适合生产运行）
- bin：编译所有可执行文件（包括 rosetta_scripts、relax、mpi_msd 等）

# 貌似下载linux版本可以不用编译
下载后加载环境变量(好像不是)
```
export ROSETTA=$HOME/Apps/rosetta/main/source
export ROSETTA3_DB=$ROSETTA/../database
export ROSETTA_BIN=$ROSETTA/bin
export PATH=$ROSETTA_BIN:$PATH
```

