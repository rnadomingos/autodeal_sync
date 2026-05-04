from sqlalchemy.orm import Session
from data.schemas.company import CompanyModel

def get_all_companies(db: Session):
    '''
    Get all companies
    '''
    return db.query(CompanyModel).all()
