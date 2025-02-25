"""Investor service database models - Transformed into 3NF """

from datetime import date
from sqlmodel import Field, SQLModel
from typing import List
from pydantic import BaseModel


from datetime import date
from sqlmodel import SQLModel, Field, Relationship


class InvestorType(SQLModel, table=True):
    """InvestorType model - simple Enum table"""

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    investors: list["Investor"] = Relationship(back_populates="investor_type")


class Country(SQLModel, table=True):
    """Country model - simple Enum table"""

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    investors: list["Investor"] = Relationship(back_populates="country")


class Investor(SQLModel, table=True):
    """Investor model - 3NF table to hold investor details"""

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    investor_type_id: int = Field(foreign_key="investortype.id")
    country_id: int = Field(foreign_key="country.id")
    date_added: date
    last_updated: date
    investor_type: InvestorType = Relationship(back_populates="investors")
    country: Country = Relationship(back_populates="investors")


class InvestorResponse(BaseModel):
    """Contactual - Pydantic model for Investor response"""

    id: int
    name: str
    investor_type: str
    country: str
    date_added: date
    last_updated: date
    total_commitment: int


class InvestorListResponse(BaseModel):
    """Pydantic model for Investor list response"""

    investors: List[InvestorResponse]
