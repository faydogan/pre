import axios from 'axios';

/* TODO (JIRA-####): Create a app config to hold backend URLs.*/
/* TODO (JIRA-####): Implement pagination and sorting for the investors data.*/
/* TODO (JIRA-####): Create Types for API responses.*/
const INVESTORS_API_URL = 'http://localhost:3001/investors/?skip=0&limit=100&sort=id';

export const fetchInvestorsData = async () => {
    try {
        const response = await axios.get(INVESTORS_API_URL);
        return response.data?.investors || [];
    } catch (error) {
        console.error('Error fetching investors data:', error);
        throw error;
    }
};


const COMMITMENT_API_URL = 'http://localhost:3002/commitments/total/';

export const fetchTotalCommitmentsData = async () => {
    try {
        const response = await axios.post(COMMITMENT_API_URL, {investor_ids: []});
        return response.data?.total_commitments || [];
    } catch (error) {
        console.error('Error fetching total commitments data:', error);
        throw error;
    }
};


export const fetchCombinedInvestorData = async () => {
    try {
        const investors = await fetchInvestorsData();
        const commitments = await fetchTotalCommitmentsData();
        const commitmentMap = new Map();

        commitments.forEach((commitment: { investor_id: any; }) => {
            commitmentMap.set(commitment.investor_id, commitment);
        });
        const combinedData = investors.map((investor: { id: any; }) => {
            const commitment = commitmentMap.get(investor.id);
            return {
                ...investor,
                total: commitment ? commitment.total : null
            };
        });
        console.log('Combined data:', combinedData);
        return combinedData;
    } catch (error) {
        console.error('Error fetching combined investor data:', error);
        throw error;
    }
};


const COMMITMENTS_BY_INVESTIR_API_URL = 'http://localhost:3002/commitments/';

export const fetchCommitmentsDataForInvestor = async (id: number) => {
    console.log('Fetching commitments data for investor:', id);
    try {
        const response = await axios.get(COMMITMENTS_BY_INVESTIR_API_URL + id.toString());
        return response.data?.commitments || [];
    } catch (error) {
        console.error('Error fetching commitments data:', error);
        throw error;
    }
};