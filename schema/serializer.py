from pydantic import BaseModel



class PostCreateSerailizer(BaseModel):
    
    title       : str
    content     : str 
    is_published: bool 
    
    
    
    