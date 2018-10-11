from sqlalchemy.orm import relationship, backref, joinedload
from sqlalchemy import Column, DateTime, String, Integer, Float, ForeignKey, func, UniqueConstraint
import uuid
from db.base import Base, inverse_relationship, create_tables 


class System_app(Base):
    __tablename__ = 'system_app'
    id = Column(String(36), primary_key=True)
    name = Column(String(100))
    api_key = Column(String(255))
    type = Column(String(50))
    status = Column(String(50))
    ip = Column(String(255)) #, nullable=False
    
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_json(self, data, mod):        
        if mod == 'create':
            self.id = uuid.uuid4()

        if 'name' in data:
            self.name = data['name']
        
        if 'api_key' in data:
            self.api_key = data['api_key']
        
        if 'type' in data:
            self.type = data['type']
        
        if 'status' in data:
            self.status = data['status']
        
        if 'ip' in data:
            self.ip = data['ip']

    def read_data(self, data_obj):
        data = {
            'name': data_obj.name,
            'api_key': data_obj.api_key,
            'type': data_obj.type,
            'status': data_obj.status,
            'ip': data_obj.ip
        }
        return data        




class System_config(Base):
    __tablename__ = 'system_config'
    id = Column(String(36), primary_key=True)
    key = Column(String(255))
    value = Column(String(255)) #Text
    
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_json(self, data, mod):
        
        if mod == 'create':
            self.id = uuid.uuid4()

        if 'key' in data:
            self.key = data['key']
        
        if 'value' in data:
            self.value = data['value']

    def read_data(self, data_obj):
        data = {
            'key': data_obj.key,
            'value': data_obj.value
        }
        return data  



if __name__ != '__main__':
    create_tables()