from django.db import models
import time

from django.utils.html import format_html

class Vmms(models.Model):
    # 车型
    carModel = models.CharField(max_length=255,verbose_name="车型")
    # 发动机排量
    engineDisplacement = models.CharField(max_length=10,verbose_name="发动机排量",blank=True)
    #变速箱
    gearBox = models.CharField(max_length=100,verbose_name="变速箱",blank=True)
    # VIN码
    VIN = models.CharField(max_length=17,verbose_name="VIN码")
    #发动机号
    engineNumber = models.CharField(max_length=17,verbose_name="发动机号")
    #里程(KM)
    mileage = models.IntegerField(verbose_name="里程(KM)")
    #接样人
    recipient = models.CharField(max_length=5,verbose_name="接车人")
    # 接车时间
    sampleDate = models.DateField(verbose_name="接车时间")
    # 还车时间
    returnDate = models.DateField(verbose_name="还车时间",blank=True)
    # 试验用途
    useTest = models.CharField(max_length=100, verbose_name="试验用途")
    #车辆停放位置
    parkingLocations = (
        (0, "试验室"),
        (1, "停车场"),
    )
    parkingLocation = models.IntegerField(choices=parkingLocations,default=0,verbose_name="停放地")
    # 运输
    transports = (
        (0, "不可拖运"),
        (1, "可拖回")
    )
    transport = models.IntegerField(choices=transports, default=0, verbose_name="是否可运输")
    # 试验进度
    testProgresss = (
        (0, "进行中"),
        (1, "已拖回"),
    )
    testProgress = models.IntegerField(choices=testProgresss, default=0, verbose_name="试验进度")
    # 备注
    remarks = models.TextField(verbose_name="备注",blank=True)
    class Meta:
        db_table = 'vmms'
        verbose_name = "车辆管理"
        verbose_name_plural = verbose_name
    # 列表显示名称
    def __str__(self):
        return self.carModel

# 加班统计模型
class overTime(models.Model):
    # 加班日期
    overDate = models.DateField(verbose_name="加班日期")
    # 开始时间
    startTime = models.TimeField(verbose_name="开始时间")
    #结束时间
    endTime = models.TimeField(verbose_name="结束时间")
    # 加班时长
#    causeTime = models.IntegerField('')
    #加班事由（选填）
    overTimeCause = models.CharField(max_length=255,verbose_name="加班事由")

    class Meta:
        db_table = 'overtime'
        verbose_name = "加班统计"
        verbose_name_plural = verbose_name

    def duration(self):

        # 计算时长
        sTime = str(self.startTime)
        eTime = str(self.endTime)
        def t2s(t):
            h,m,s = t.strip().split(":")
            return int(h) * 3600 + int(m) * 60 + int(s)
        s1Time = t2s(sTime)
        e1Time = t2s(eTime)
        cTime = e1Time - s1Time
        print(cTime)
        dTime = time.strftime("%H:%M:%S", time.gmtime(cTime))
        return dTime
    duration.short_description = "加班时长"

#测试数据库
class test(models.Model):
	name = models.CharField(max_length=100,verbose_name="测试名称")
	age = models.IntegerField()

#	class Meta:
#        db_table = 'test'
#        verbose_name = "测试"
#        verbose_name_plural = verbose_name