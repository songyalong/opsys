# coding:utf-8
from django.db import models


class Machine(models.Model):
    physical_host_name = models.CharField(max_length=200, null=True, verbose_name="物理机主机名")
    physical_host_IP = models.GenericIPAddressField(null=True, verbose_name="物理机IP")
    machine_hostname = models.CharField(max_length=200, null=True, verbose_name="虚拟主机名")
    cpu_count = models.SmallIntegerField(null=True, verbose_name="CPU核数")
    memory_size = models.SmallIntegerField(null=True, verbose_name="内存大小")
    disk_size = models.SmallIntegerField(null=True, verbose_name="磁盘大小")
    os = models.CharField(max_length=100, null=True, verbose_name="操作系统")
    machine_IP = models.GenericIPAddressField(null=True, verbose_name="虚拟主机IP")
    allocate_time = models.DateField(null=True, verbose_name="分配时间")
    is_running = models.SmallIntegerField(null=True, verbose_name="状态")
    allocate_time = models.CharField(max_length=100, null=True, verbose_name="申请人")
    allocate_time = models.CharField(max_length=100, null=True, verbose_name="申请部门")
    machine_password = models.CharField(max_length=200, null=True, verbose_name="机器密码")
