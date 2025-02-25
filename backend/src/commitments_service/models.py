"""SQLModel classes for the Commitments Service."""

from decimal import Decimal
from typing import Optional, List
from pydantic import BaseModel
from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Column, Numeric


class AssetClass(SQLModel, table=True):
    """AssetClass model - simple Enum table"""

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    commitments: List["Commitment"] = Relationship(back_populates="asset_class")


class Commitment(SQLModel, table=True):
    """Commitment model - 3NF table to hold investor commitments by asset types
    #TODO (JIRA-####): Add support for multiple currencies
    """

    id: int | None = Field(default=None, primary_key=True)
    investor_id: int = Field(index=True)
    asset_class_id: int = Field(foreign_key="assetclass.id")
    amount: Decimal = Field(sa_column=Column(Numeric(18, 2)))
    currency: str = Field(default="GBP")
    asset_class: Optional[AssetClass] = Relationship(
        back_populates="commitments"
    )


class CommitmentResponse(BaseModel):
    """Contactual - Pydantic model for Commitment response"""

    id: int
    investor_id: int
    asset_class_name: str
    amount: Decimal
    currency: str


class CommitmentListResponse(BaseModel):
    """Pydantic model for Commitment list response"""

    commitments: List[CommitmentResponse]


class InvestorTotalCommitmentRequest(BaseModel):
    """Pydantic model for Total Commitment request"""

    investor_ids: List[int]


class InvestorTotalCommitmentResponse(BaseModel):
    """Pydantic model for Total Commitment response"""

    total: int
    currency: str
    investor_id: int


class InvestorTotalCommitmentListResponse(BaseModel):
    """Pydantic model for Total Commitment list response"""

    total_commitments: List[InvestorTotalCommitmentResponse]
