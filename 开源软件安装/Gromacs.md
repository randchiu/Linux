(http://sobereva.com/457)
- **提前检查编译环境及系统信息，如 cuda 版本、gpu 驱动版本 、SIMD 等，**
- Check system information in advance, such as the cuda version, gpu driver version, and SIMD
```
mpirun --version
cmake --version
gcc --version
nvcc --version
fftw-wisdom --version           #It can be installed by Gromacs itself
nvidia-smi                      # check nvidia driver and cuda
```
# 安装NVIDIA驱动

# 安装CUDA
1. 在安装nvidia驱动后，输入'nvidia-smi'确定与驱动相适应的CUDA版本，百度搜索相应版本并按照官网提示进行安装。（推荐使用deb(network)，WSL子系统也同样适用）
2. 安装后输入以下命令将cuda添加到环境变量,里面的版本号根据安装的版本进行相应更改
```
echo -e "export PATH=/usr/local/cuda-12.4/bin:\$PATH\nexport LD_LIBRARY_PATH=/usr/local/cuda-12.4/lib64:\$LD_LIBRARY_PATH" >> ~/.bashrc
source ~/.bashrc
nvcc --version
```

## 安装GCC与G++（安装前先查看版本，系统一般默认安装好）
```
sudo apt install gcc
gcc --version

sudo apt install g++
g++ --version
```
## 安装cmake
**不用追求最新版本，可直接运行`sudo apt install cmake`**

（**未验证**）官网https://cmake.org/download/ 下载相应版本源码进行编译安装，解压并进入文件夹，执行`./bootstrap`以及后续步骤
```
tar -zxvf cmake-3.29.6.tar.gz
cd cmake-3.29.6
```
```
./bootstrap
make 
sudo make install
```
若在执行`./bootstrap`出现
CMake Error at Utilities/cmcurl/CMakeLists.txt:772 (message):
  Could not find OpenSSL.  Install an OpenSSL development package or
  configure CMake with -DCMAKE_USE_OPENSSL=OFF to build without OpenSSL.
  是因为缺少ssl库，执行以下命令解决
```
sudo apt-get install libssl-dev
```
# 安装Open MPI
进入官网https://www.open-mpi.org/software/ompi/v5.0/ 下载相应版本进行编译安装，解压并进入文件夹，执行`./configure`，并指定安装位置`--prefix=/home/username/software/openmpi`
```
tar -xvzf openmpi-5.0.1.tar.gz
cd openmpi-5.0.1
```
```
./configure --prefix=/home/username/software/openmpi 
make
sudo make install
echo 'export PATH=/home/username/software/openmpi/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/home/username/software/openmpi/lib:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
```
```
mpirun --version
ompi_info
```
# 安装FFTW
进入官网https://fftw.org/download.html 下载相应版本进行编译安装，解压并进入文件夹，执行`./configure`，并指定安装位置`--prefix=/home/username/software/fftw-3310`
```
tar -xvf fftw-3.3.10.tar.gz 
cd fftw-3.3.10
```
```
./configure --enable-float --enable-sse2 --enable-avx2 --enable-shared --prefix=/home/username/software/fftw-3310
make 
sudo make install
echo "export LD_LIBRARY_PATH=/home/username/software/fftw-3310/lib:\$LD_LIBRARY_PATH" >> ~/.bashrc  # 如果安装到了非标准路径，更新环境变量，将 FFTW 的库路径添加到 LD_LIBRARY_PATH
source ~/.bashrc
```

# 安装Gromacs
官网下载对应版本，安装到/home/hp/software/gmx24.2路径
```
tar -xvzf gromacs-2024.2.tar.gz
cd gromacs-2024.2/
mkdir build
cd build
```
```
cmake .. -DCMAKE_INSTALL_PREFIX=/home/hp/software/gmx24.2 \
  -DCMAKE_PREFIX_PATH=/home/hp/software/fftw3310 \
  -DGMX_GPU=CUDA \
  -DCUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda-12.8 \
  -DGMX_MPI=ON \
  -DREGRESSIONTEST_DOWNLOAD=ON \
  -DCMAKE_CUDA_COMPILER=/usr/local/cuda-12.8/bin/nvcc \
  -DCMAKE_C_COMPILER=/home/hp/software/openmpi/bin/mpicc \
  -DCMAKE_CXX_COMPILER=/home/hp/software/openmpi/bin/mpic++
```
```
make
make check
sudo make install
```
环境变量添加（以实际安装目录为准），`vim ~/.bashrc`添加以下两行，并`source ~/.bashrc`：

export PATH=/home/hp/software/gmx24.2/bin:$PATH

source /home/hp/software/gmx24.2/bin/GMXRC

若输入`gmx --version`无效，可输入`gmx_mpi --version`,也可将`gmx_mpi`链接到`gmx`
```
sudo ln -s /home/hp/software/gmx24.2/bin/gmx_mpi /home/hp/software/gmx24.2/bin/gmx
```

https://blog.csdn.net/qq_41854911/article/details/122700898

https://blog.csdn.net/m0_54634272/article/details/142392644?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522026f6005204f2a709edff3a005541ce5%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=026f6005204f2a709edff3a005541ce5&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-142392644-null-null.142^v102^pc_search_result_base7&utm_term=gromacs%E5%AE%89%E8%A3%85&spm=1018.2226.3001.4187
