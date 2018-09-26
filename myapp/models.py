from django.db import models

from django.utils.html import format_html

class Vmms(models.Model):
    # 车型
    carModel = models.CharField(max_length=255,verbose_name="车型")
    # 试验用途
    useTests = (
        (0, "请选择试验用途"),
        (1, "排放油耗试验"),
        (2, "温度场试验"),
        (3, "冷却试验"),
        (4, "空调试验"),
    )
    useTest = models.IntegerField(choices=useTests, default=0,verbose_name="试验用途")
    #试验进度
    testProgresss = (
        (0, "进行中"),
        (1, "完成"),
    )
    testProgress = models.IntegerField(choices=testProgresss,default=0,verbose_name="试验进度")
    # VIN码
    VIN = models.CharField(max_length=17,verbose_name="VIN码")
    #发动机号
    engineNumber = models.CharField(max_length=17,verbose_name="发动机号")
    #里程(KM)
    mileage = models.IntegerField(verbose_name="里程(KM)")
    #接样人
    recipient = models.CharField(max_length=5,verbose_name="接车人")
    # 接车时间
    sampleDate = models.DateTimeField(verbose_name="接车时间")
    # 还车时间
    returnDate = models.DateTimeField(verbose_name="还车时间")
    # 运输
    transports = (
        (0,"不可拖运"),
        (1, "可拖回")
    )
    transport = models.IntegerField(choices=transports,default=0,verbose_name="是否可运输")
    #车辆停放位置
    parkingLocations = (
        (0, "试验室"),
        (1, "停车场"),
    )
    parkingLocation = models.IntegerField(choices=parkingLocations,default=0,verbose_name="停放地")

    # 备注
    remarks = models.TextField(verbose_name="备注")

    class Meta:
        db_table = 'vmms'
        verbose_name = "车辆管理"
        verbose_name_plural = verbose_name

    # 列表显示名称
    def __str__(self):
        return self.carModel

    # ordering = ('-sampleDate')排序方式

    #
    def testProgresss(self):
       if self.testProgress == 0:
           color_code = 'green'
       else:
           color_code = 'red'
       return format_html(
            '<span style="color: #{};">{} {}</span>',
           color_code,
           self.testProgress
       )