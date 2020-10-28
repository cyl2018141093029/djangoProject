from django.db import models


# Create your models here.


class People(models.Model):
    # 用户
    STU_SEX = [('F', 'female'),
               ('M', 'male')]
    stu_num = models.IntegerField(primary_key=True)
    stu_name = models.CharField(max_length=8, )
    password = models.CharField(max_length=12,)
    stu_sex = models.CharField(max_length=1, choices=STU_SEX)
    stu_phone = models.CharField(max_length=11)
    stu_qq = models.CharField(max_length=20, blank=True)
    stu_email = models.EmailField(blank=True)
    stu_major = models.CharField(max_length=15)
    stu_class = models.IntegerField()
    stu_college = models.CharField(max_length=30)


class Department(models.Model):
    # 部门
    dp_num = models.CharField(max_length=2, primary_key=True)
    dp_name = models.CharField(max_length=10)
    dp_presentetion = models.CharField(max_length=500)
 

class ActivityInfo(models.Model):
    # 活动信息
    act_num = models.IntegerField(primary_key=True)  # 活动编号
    stu_num = models.OneToOneField(to='People', to_field='stu_num', on_delete=models.PROTECT,)  # 活动负责人
    dp_num = models.ForeignKey(to='Department', to_field='dp_num', on_delete=models.CASCADE,)  # 举办部门
    act_type = models.CharField(max_length=10)  # 活动类型
    act_name = models.CharField(max_length=50)  # 活动名称
    act_held_timerange = models.DurationField(null=True)  # 活动举办时间段
    act_release_time = models.DateTimeField(auto_created=True)  # 活动发布时间
    act_held_loca = models.CharField(max_length=100)  # 活动举办地点
    act_details = models.CharField(max_length=200)  # 活动详细信息
    act_participant = models.CharField(max_length=20)  # 活动参与对象
    numberofp_limit = models.IntegerField()  # 人数限制
    act_appendix = models.FileField(upload_to="ActivityInfo_appendix")  # 附件路径（路经保存在数据库中，文件上传到指定目录）
    act_image = models.ImageField(null=True)


class DpMembers(models.Model):
    # 部门成员
    # 部门编号
    dp_num = models.OneToOneField(to='Department', to_field='dp_num', on_delete=models.CASCADE,
                                  )
    # 部门成员学号
    stu_num = models.OneToOneField(to='People', to_field='stu_num', on_delete=models.CASCADE)
    # 部门成员职务
    stu_post = models.CharField(max_length=6)


class ActivityFeedback(models.Model):
    IF_ANONYMOUS = [('Y', '匿名'), ('N', '不匿名')]
    # 活动反馈
    fb_num = models.AutoField(primary_key=True)  # 反馈编号
    act_num = models.ForeignKey(to='ActivityInfo', to_field='act_num', on_delete=models.CASCADE,)  # 活动编号
    stu_num = models.ForeignKey(to='DpMembers', to_field='stu_num', on_delete=models.DO_NOTHING,)  # 评论人学号
    restu_num = models.ForeignKey(to='People', to_field='stu_num', on_delete=models.DO_NOTHING, null=True)  # 活动负责人学号
    feedback = models.CharField(max_length=400)  # 活动评论
    refeedback = models.CharField(max_length=400, null=True)   # 活动反馈
    feedback_time = models.DateTimeField(auto_now_add=True)  # 活动评论时间
    refeedback_time = models.DateTimeField(auto_now_add=True, null=True)  # 活动反馈时间
    if_anonymous = models.CharField(max_length=6, choices=IF_ANONYMOUS, blank=True, null=True)


class FundRecord(models.Model):
    # 资金记录
    # 资金记录编号
    fund_num = models.AutoField(primary_key=True)
    # 使用资金的部门编号
    fund_for_dp = models.ForeignKey(to='Department', to_field='dp_num', on_delete=models.PROTECT)
    # 资金用于的活动编号
    fund_for_act = models.ForeignKey(to='ActivityInfo', to_field='act_num', on_delete=models.PROTECT)
    # 资金预使用事项
    fund_for_matt = models.CharField(max_length=500)
    # 资金数目
    fund_amount = models.FloatField(blank=True, null=True)
    # 报账编号
    reim_num = models.ForeignKey(to='Reimbursement', to_field='reim_num', on_delete=models.PROTECT, null=True)


class Reimbursement(models.Model):
    # 预先使用资金报账
    # 报账编号
    reim_num = models.IntegerField(primary_key=True)
    # 审核报账部门
    reim_to = models.ForeignKey(to='Department', to_field='dp_num', max_length=2, on_delete=models.PROTECT)
    # 发票链接
    invo_appendix = models.CharField(max_length=50)
    # 申请时间
    apply_time = models.DateTimeField(auto_now_add=True)
    # 申请通过时间
    allow_time = models.DateTimeField(auto_now=True)
    # 配置auto_now_add=True，创建数据记录的时候会把当前时间添加到数据库
    # 配置auto_now=True，每次更新数据记录的时候会更新该字段
    # 负责申请的人
    fund_pinchrage = models.BigIntegerField()
    # 申请状态
    reim_state = models.CharField(max_length=6)


class MatterialRecord(models.Model):
    # 物资记录
    m_num = models.IntegerField(primary_key=True)
    m_name = models.CharField(max_length=20)
    m_stock = models.CharField(max_length=3)
    m_pincharge = models.ForeignKey(to='DpMembers', to_field='stu_num', on_delete=models.PROTECT,)
    m_borrow_sta = models.CharField(max_length=6)


class ClassroomRecord(models.Model):
    # 教室信息
    classroom_num = models.CharField(max_length=10, primary_key=True)
    classroom_cap = models.IntegerField()
    classroom_pincharge = models.ForeignKey(to='DpMembers', to_field='stu_num', on_delete=models.PROTECT,)
    classroom_borrowif = models.IntegerField()


class BorrowRecord(models.Model):
    # 借用记录
    BorrowType = [('place', '场地'), ('matterial', '物资')]
    borrow_num = models.IntegerField(primary_key=True)
    borrow_type = models.CharField(max_length=20, choices=BorrowType)
    object_num = models.ForeignKey(to='MatterialRecord', to_field='m_num', on_delete=models.CASCADE)
    borrow_name = models.CharField(max_length=20)
    borrow_amount = models.IntegerField(default=1)
    lent_to_dp = models.ForeignKey(to='Department', to_field='dp_num', on_delete=models.CASCADE)
    lent_for = models.CharField(max_length=200)
    lent_time_range = models.DurationField(null=True)
    return_time = models.DateTimeField(auto_created=True)


class ActivityFile(models.Model):
    # 活动文案
    actfile_num = models.IntegerField(primary_key=True)
    act_dp = models.ForeignKey(to='Department', to_field='dp_num', on_delete=models.CASCADE)
    act_name = models.CharField(max_length=50)
    actfile_name = models.CharField(max_length=50)
    actfile_appendix = models.FileField(upload_to="ActivityFile")
    check_if = models.IntegerField()


class CheckYesActfile(models.Model):
    # 审核活动文案
    check_num = models.IntegerField(primary_key=True)
    actfile_num = models.ForeignKey(to='ActivityFile', to_field='actfile_num', on_delete=models.CASCADE)
    check_dpmember_num = models.ForeignKey(to="DpMembers", to_field="stu_num", on_delete=models.PROTECT, blank=True)
    check_state = models.CharField(max_length=6)


class Cooperation(models.Model):
    # 部门对接
    coo_num = models.IntegerField(primary_key=True)
    taskname = models.CharField(max_length=20)
    adp_num = models.OneToOneField(to='Department', verbose_name='任务发布部门', on_delete=models.CASCADE)
    astu_num = models.ForeignKey(to='DpMembers', verbose_name='任务发布负责人', on_delete=models.PROTECT)
    bdp_num = models.ForeignKey(to='Department', verbose_name='任务接收部门', related_name='Department_bdp_num',
                                on_delete=models.CASCADE)
    bstu_num = models.OneToOneField(to='DpMembers', verbose_name='任务接收负责人', related_name='Department_bdp_num',
                                    on_delete=models.PROTECT)
    contact_if = models.IntegerField()
    release_date = models.DateTimeField(auto_now_add=True)
    ddl = models.DateTimeField()
    task_details = models.CharField(max_length=200)
    task_note = models.CharField(max_length=200)
    aappendix = models.FileField(upload_to="a_Cooperation", blank=True)
    bappendix = models.FileField(upload_to="b_Cooperation", blank=True)
    task_state = models.CharField(max_length=6)
