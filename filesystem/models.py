from django.db import models
from django import forms
import os, wmi
# Create your models here.


class Document(models.Model):
        docfile = models.FileField(upload_to = 'documents/%Y/%m/%d')

        def get_fs_info():
                tmplist = []
                c = wmi.WMI()
                for physical_disk in c.Win32_DiskDrive():
                        for partition in physical_disk.associators("Win32_DiskDriveToDiskPartition"):
                                for logical_disk in partition.associators("Win32_LogicalDiskToPartition"):
                                        if logical_disk.Caption == os.path.splitdrive(os.getcwd())[0]:
                                                FreeSpace=int(logical_disk.FreeSpace)/1024/1024/1024  
                return FreeSpace

	
class DocumentForm(forms.Form):
	docfile = forms.FileField(label = 'Select a file')
