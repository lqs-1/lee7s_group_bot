from datetime import datetime

from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, create_engine

# 基础类
BaseDB = declarative_base()

# User表
class User(BaseDB):
    """必须继承BASE"""

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    sex = Column(String, nullable=False)
    createTime = Column(DateTime, default=datetime.now, nullable=False)
    loginTime = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    email = Column(String)
    isDelete = Column(Integer, default=0)

    def __str__(self):
        return f"{self.id},{self.username},{self.password},{self.sex},{self.createTime},{self.loginTime},{self.email},{self.isDelete}"



# UserFile表
class UserFile(BaseDB):
    """必须继承Base"""

    __tablename__  = "user_file"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    userId = Column(Integer, nullable=False)
    file = Column(String, nullable=False)
    fileType = Column(String, nullable=False)
    isDelete = Column(Integer, default=0)
    uploadTime = Column(DateTime, default=datetime.now, nullable=False)
    fileName = Column(String, nullable=False)
    deleteTime = Column(DateTime)

    def __str__(self):
        return f"{self.id},{self.userId},{self.file},{self.fileType},{self.isDelete},{self.uploadTime},{self.fileName},{self.deleteTime}"

# 用户角色关系表
class UserRole(BaseDB):
    """必须继承Base"""

    __tablename__ = "user_role"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    userId = Column(Integer, nullable=False)
    roleId = Column(Integer, nullable=False)


# 用户权限关系表
class UserPermission(BaseDB):
    """必须继承Base"""

    __tablename__ = "user_permission"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    userId = Column(Integer, nullable=False)
    permissionId = Column(Integer, nullable=False)


# 用户菜单关系表
class UserMenu(BaseDB):
    """必须继承Base"""

    __tablename__ = "user_menu"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    userId = Column(Integer, nullable=False)
    menuId = Column(Integer, nullable=False)





