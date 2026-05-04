import json
import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from data.infra.database import Base, PostgresSessionLocal as SessionLocal, engine
from data.schemas.company import CompanyModel

dotenv_path = Path.cwd() / '.env'
load_dotenv(dotenv_path=dotenv_path)

CONFIG_FILE = Path(os.getenv("COMPANIES_CONFIG_PATH"))


def load_companies_config() -> list[dict]:
    if not CONFIG_FILE.exists():
        raise FileNotFoundError(f"Config file not found: {CONFIG_FILE}")

    with CONFIG_FILE.open("r", encoding="utf-8") as config_file:
        companies = json.load(config_file)

    if not isinstance(companies, list):
        raise ValueError("companies.config must contain a JSON array of companies")

    return companies


def is_companies_table_empty(db: Session) -> bool:
    return db.query(CompanyModel).count() == 0


def seed_companies() -> None:
    companies = load_companies_config()

    Base.metadata.create_all(bind=engine)

    with SessionLocal() as db:
        if not is_companies_table_empty(db):
            print("A tabela companies já possui registros. Nenhuma seed foi aplicada.")
            return

        db.add_all([CompanyModel(id=company["id"], name=company["name"]) for company in companies])
        db.commit()

    print(f"{len(companies)} empresas inseridas na tabela companies.")


if __name__ == "__main__":
    seed_companies()
