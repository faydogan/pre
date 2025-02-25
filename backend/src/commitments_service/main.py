from typing import List
from commitments_service.dbservice import SessionDep
from commitments_service.models import (
    Commitment,
    CommitmentListResponse,
    CommitmentResponse,
    InvestorTotalCommitmentListResponse,
    InvestorTotalCommitmentRequest,
    InvestorTotalCommitmentResponse,
)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import select
from sqlalchemy import func


app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/commitments/{investor_id}", response_model=CommitmentListResponse)
def get_commitment_responses(
    investor_id: int, session: SessionDep
) -> CommitmentListResponse:
    """Get commitments for a given investor by asset class."""

    commitments = session.exec(
        select(Commitment).where(Commitment.investor_id == investor_id)
    ).all()

    if not commitments:
        return CommitmentListResponse(commitments=[])

    response_list = [
        CommitmentResponse(
            id=commitment.id,
            investor_id=commitment.investor_id,
            asset_class_name=(
                commitment.asset_class.name
                if commitment.asset_class
                else "Not Found"
            ),
            amount=commitment.amount,
            currency=commitment.currency,
        )
        for commitment in commitments
    ]

    return CommitmentListResponse(commitments=response_list)


@app.post(
    "/commitments/total/", response_model=InvestorTotalCommitmentListResponse
)
def get_list_of_total_commitments_by_investor(
    request: InvestorTotalCommitmentRequest,
    session: SessionDep,
) -> InvestorTotalCommitmentListResponse:
    """Get all commitments for a given investor."""

    # pylint: disable=no-member
    if not request.investor_ids:
        total_commitments_by_investors = session.exec(
            select(
                Commitment.investor_id,
                Commitment.currency,
                func.sum(Commitment.amount).label("total"),
            ).group_by(Commitment.investor_id, Commitment.currency)
        ).all()
    else:

        total_commitments_by_investors = session.exec(
            select(
                Commitment.investor_id,
                Commitment.currency,
                func.sum(Commitment.amount).label("total"),
            )
            .where(Commitment.investor_id.in_(request.investor_ids))
            .group_by(Commitment.investor_id, Commitment.currency)
        ).all()
    # pylint: enable=no-member

    if not total_commitments_by_investors:
        return InvestorTotalCommitmentListResponse(total_commitments=[])

    response_list = [
        InvestorTotalCommitmentResponse(
            total=int(result.total),
            currency=result.currency,
            investor_id=result.investor_id,
        )
        for result in total_commitments_by_investors
    ]

    return InvestorTotalCommitmentListResponse(total_commitments=response_list)
