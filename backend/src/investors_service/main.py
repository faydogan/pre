from investors_service.dbservice import SessionDep
from investors_service.models import (
    Investor,
    InvestorListResponse,
    InvestorResponse,
)
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import select


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/investors/", response_model=InvestorListResponse)
def get_investors_paginated(
    session: SessionDep,
    skip: int = Query(0, description="Number of items to skip", ge=0),
    limit: int = Query(
        10, description="Number of items to return", ge=1, le=100
    ),
    sort: str = Query("id", description="Sort by column"),
) -> InvestorListResponse:
    "Get all commitments for a given investor."

    investors = session.exec(
        select(Investor).offset(skip).limit(limit).order_by(sort)
    ).all()
    response = InvestorListResponse(
        investors=[
            InvestorResponse(
                id=investor.id,
                name=investor.name,
                investor_type=investor.investor_type.name,
                country=investor.country.name,
                date_added=investor.date_added,
                last_updated=investor.last_updated,
                total_commitment=0,
            )
            for investor in investors
        ]
    )

    return response
