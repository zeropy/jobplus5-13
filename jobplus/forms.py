from falsk_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, SelectField, SelectMultipleField, RadioField
from wtforms import DateField, DateTimeField
from wtforms.validators import Length, Email, EqualTo, Required, URL, NumberRange, DataRequired
from wforms import ValidationError
from flask import flash
from models import db, User

class Register(FlaskForm):
    # 个人注册表单

    email = StringField('邮箱',validators=[Required(),Email()])
    username = StringField('用户名',validators=[Required(),Length(6,24)])
    password = PasswordField('密码',validators=[Required(),Length(8,30)])
    repeat_password = PasswordField('重复密码', validators=[Required(),EqualTo('password')])
    agreement = BooleanField('我同意',validators=[DataRequired()])
    submit = SubmitField('注册')

class CompanyRegister(FlaskForm):
    # 企业注册
    company_name = StringField('企业名称',validators=[Required(),Length(2,64)])
    location = StringField('所在地', validators=[Required()])
    linkman = StringField('联系人',validators=[Required(),Length(2,30)])
    phone = StringField('联系电话',validators=[Required(),Length(6,20))
    email = StringField('邮箱', validators=[Required(),Email()])
    username = StringField('用户名',validators=[Required(),Length(6,24)])
    password = PasswordField('密码',validators=[Required(),Length(8,30)])
    repeat_password = PasswordField('重复密码', validators=[Required(),EqualTo('password')])
    agreement = BooleanField('我同意',validators=[DataRequired()])
    submit = SubmitField('注册')


class Login(FlaskForm):
    # 登录表单
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码', validators=[Required(),Length(8,30)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')

    def validate_email(self,field):
        id = db.session.query(User.id).filter_by(email=field.data).first()
        if not id:
            raise ValidationError('邮箱不存在或密码错误')

    def validate_password(self, field):
        user = User.query.filter_by(email=field.email.data)
        if user and not user.check_password(field.data):
            raise ValidationError('邮箱不存在或密码错误')

class Job(FlaskForm):
    # 职位表单

    name = StringField('职位名称',validators=[Required()])
    salay = SelectField('薪资范围',validators=[Required()])
    location = StringField('工作地点',validators=[Required()])
    work_exp = SelectField('工作经验',validators=[Required()])
    education = SelectField('学历',validators=[Required()])
    count = IntegerField('招聘人数',validators=[Required())
    welfare = SelectMultipleField('员工福利', validators=[Required()])
    job_info = TextAreaField('职位信息',validators=[Required(),Length(50,1000)])
    categorys = SelectMultipleField('职能类别',validators=[Required()])
    submit = SubmitField('保存')

class Resume_info(FlaskForm):
    # 简历 基础信息部分

    real_name = StringField('姓名',validators=[Required()])
    sex = RadioField('性别',validators=[Required())
    brithdate = DateField('出身日期',validators=[Required()])
    work_started = DateField('开始工作年份',validators=[Required()])
    phone = StringField('手机号码',validators=[Required()])
    status = RadioField('求职状态',validators=[Required()])
    email = StringField('电子邮箱',validators=[Required(),Email()])
    location = StringField('现居地',validators=[Required()])
    submit = SubmitField('保存')

class Resume_purpose(FlaskForm):
    # 简历 求职意向

    salay_range = SelectField('薪资范围',validators=[Required()])
    work_location = StringField('工作地点',validators=[Required()])
    job = StringField('职位',validators=[Required()])
    evaluation = TextAreaField('自我评价',validators[Required(),Length(50,200)])
    available_time = SelectField('到岗时间',validators=[Required()])
    type = RadioField('工作类型',validators=[Required())
    submit = SubmitField('保存')

class Resume_experiment(FlaskForm):
    # 简历 工作经验

    company_name = StringField('公司名称',validators=[Required()])
    time = StringField('时间',validators=[Required()])
    job = StringField('职位',validators=[Required()])
    department = StringField('部门',validators=[Required()])
    industry = SelectField('行业',validators=[Required()])
    company_sized = SelectField('公司规模',validators=[Required()])
    compamy_type = SelectField('公司性质')
    description = TextAreaField('工作描述',validators=[Required(),Length(50,500)])
    evaluation = TextAreaField('自我评价',validators[Required(),Length(50,200)])
    submit = SubmitField('保存')


class Resume_project(FlaskForm):
    # 简历  项目经验

    name  = StringField('项目名称',validators=[Required()])
    time = StringField('时间',validators=[Required()])
    description = TextAreaField('项目描述',validators=[Required()])
    duty = TextAreaField('职责描述',validators=[Required()])
    submit = SubmitField('保存')

class Resume_education(FlaskForm):
    # 简历 受教育经验

    time = StringField('时间',validators=[Required()])
    school_name = StringField('学校名称',validators=[Required()])
    degree = StringField('学位',validators=[Required()])
    profression = StringField('专业',validators=[Required()])
    description = TextAreaField('专业描述')
    submit = SubmitField('保存')

class Resume_train(FlaskForm):
    # 简历  培训经历

    time = StringField('时间',validators=[Required()])
    course = StringField('课程',validators=[Required()])
    organization = StringField('培训机构名称',validators=[Required()])
    description = TextAreaField('培训描述',validators=[Required()])
    submit = SubmitField('保存')

class Resume_skill(FlaskForm):
    # 简历 专业技能

    description = TextAreaField('专业技能')
    submit = SubmitField('保存')

class Companyinfo(FlaskForm):
    # 企业信息
    name = StringField('公司名称',validators=[Required()])
    slogan = StringField('标语')
    description = TextAreaField('公司简介',validators=[Required()])
    submit = SubmitField('保存')

class Userinfo(FlaskForm):
    # 个人信息
    real_name = StringField('姓名',validators=[Required()])
    sex = RadioField('性别',validators=[Required())
    brithdate = DateField('出身日期',validators=[Required()])
    work_started = DateField('开始工作年份',validators=[Required()])
    phone = StringField('手机号码',validators=[Required()])
    status = RadioField('求职状态',validators=[Required()])
    email = StringField('电子邮箱',validators=[Required(),Email()])
    location = StringField('现居地',validators=[Required()])
    submit = SubmitField('保存')
