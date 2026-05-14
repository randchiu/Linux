# 重装
安装nvidia驱动后，有时候会突然失效，使用`nvidia-smi`报错，显示GPU没有链接到正确的驱动程序，这有可能是因为更新了linux内核导致与nvidia驱动不兼容所致，因此，应首先注意：
- 非必要尽量不要使用`sudo apt upgrade`命令，该命令同样也会更新linux内核
- 禁用 Nouveau 开源驱动，可通过`lsmod | grep -i nouveau`查看nouveau驱动是否已被加载，如回显中存在nouveau，则说明nouveau驱动已被加载，否则说明nouveau驱动未被加载。
若出现这种情况，正确解决方法为：
1. 使用以下命令彻底卸载旧版nvidia驱动
```
sudo apt-get --purge remove "*cublas*" "cuda*" -y #如果安装了cuda需要卸载，但也可以不卸载
sudo apt --purge remove "*nvidia*" -y
sudo apt --purge remove "nvidia-*" -y
sudo apt purge "nvidia*" -y
sudo apt purge "libnvidia*" -y
sudo apt autoremove
```
2. 升级软件包及系统内核（可选，如果通过第一步卸载安装仍不可行，更新系统内核后再按第一步卸载nvidia驱动后，按第三步重新安装）
```
sudo apt update
sudo apt upgrade
sudo apt purge *nvidia*
```
3. 通过apt库安装推荐的nvidia driver
```
ubuntu-drivers devices # 列出支持的驱动版本
sudo apt install nvidia-driver-<version> # 安装标注有recommended的版本
```
4. 重启，重启后输入`nvidia-smi`就可以正常使用了。
```
sudo reboot
```
---
# 常用命令
- `lspci | grep -i nvidia` 查看当前显卡信息
- `lsmod | grep nvidia` 用于检查 NVIDIA 显卡驱动内核模块是否已加载的命令。如果输出包含 nvidia、nvidia_modeset、nvidia_uvm 等内容，说明驱动已加载并运行；如果输出为空，则表示驱动未安装或未加载
