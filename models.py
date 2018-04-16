from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# 用户表定义

class UserBase(db):
    __abstract__ = True

    created_at = db.Column(db.Datetime,default=datetime.utcnow)
    updated_at = db.Column(db.Datetime,default=datetime.utcnow,onupdate=datetime.utcnow)


class User(UserBase):
    __tablename__ = 'user'

    ROLE_ADMIN = 30
    ROLE_CP = 20 # 企业角色
    ROLE_USER = 10

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(256),nullable=True)
    role = db.Column(db.Integer,default=ROLE_USER,nullable=False)
    available = db.Column(db.Boolean,default=True) # 是否启用

class UserDetail(UserBase):
    # 用户信息
    __tablename__ = 'user_detail'

    id = db.Column(db.Integer,primary_key=True)
    user = db.relationship('User',uselist=False)
    user_id = db.Column(db.Integer,db.ForeginKey('user.id'))
    real_name = db.Column(db.String(64),nullable=False)\
    sex = db.Column(db.SmallInteger,default=0) # 性别: 0:男 1: 女
    brithdate = db.Column(db.Date)
    phone = db.Column(db.String(20),index=True, nullable=True)
    marriage_status = db.Column(db.Integer) # 婚姻状况, 0: 未婚, 1: 已婚, 2: 离异
    census_register = db.Column(db.String(64)) # 户籍


class CompanyDetail(UserBase):
    # 企业信息
    __tablename__ = 'enterprise_detail'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeginKey('user.id'))
    user = db.relationship('User',uselist=False)
    name = db.Column(db.String(128),unique=True, index=True)
    scale = db.Column(db.SmallInteger, nullable=True) # 规模
    industry = db.Column(db.String(64),nullable=True) #  行业
    location = db.Column(db.String(256),nullable=False) # 地址
    sologan = db.Column(db.String(256)) # 标语
    logo_url = db.Column(db.String(256))
    web_url = db.Column(db.String(256)) # 企业网站
    description = db.relationship('CompanyDescription',lazy='dynamic')

class CompanyDescription(UserBase):
    # 企业详细介绍
    __tablename__ = 'company_description'

    id = db.Column(db.Integer,primary_key=True)
    company_id = db.Column(db.Integer,db.ForeginKey('enterprise_detail.id'))
    description = db.Column(db.Text,nullable=False)


class Jobs(db.Model):
    # 职位信息表
    __tablename__ = 'jobs'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),nullable=True)
    company_id = db.Column(db.Integer,db.ForeginKey('user.id'))
    salay = db.Column(db.String(64), nullable=False) # 薪水
    location = db.Column(db.String(128),nullable=False) # 工作地点
    description = db.relationship('Job_info',uselist=False,lazy='dynamic')
    required = db.Column(db.Integer,nullable=True) # 招聘人数
    available =  db.Column(db.Boolean,default=True)

class Job_info(db.Model):
    # 职位描述
    __tablename__ = 'job_info'

    id = db.Column(db.Integer,primary_key=True)
    job_id = db.Column(db.Integer,db.ForeginKey('job.id'))
    description = db.Column(db.Text,nullable=False)

class Resume(db.Model):
    # 简历
    __tablename__ = 'resume'

    id = db.Column(db.Integer,primary_key=True)
    user = db.relationship('User')
    user_id = db.Column(db.Integer,db.ForeginKey('user.id'))
    store_url = db.Column(db.String(256),nullable=False)
