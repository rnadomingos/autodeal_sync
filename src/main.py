from data.infra.database import engine, Base, PostgresSessionLocal as SessionLocal
from modules.companies.use_case.get_companies import get_all_companies

Base.metadata.create_all(bind=engine)

db = SessionLocal()


def main():
    companies = get_all_companies(db)

    for cp in companies:
        print(f'ID: {cp.id}, Empresa: {cp.name}')

    
if __name__ == "__main__":
    main()