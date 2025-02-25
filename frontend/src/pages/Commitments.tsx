import React from 'react';
import { AgGridReact } from 'ag-grid-react';
import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-alpine.css';
import { ColDef } from 'ag-grid-community';
import { useSearchParams } from 'react-router-dom';
import { formatNumber } from '../utils/amountFormatter';
import { fetchCommitmentsDataForInvestor } from '../services/BackendService';

const Commitments: React.FC = () => {
  const [searchParams] = useSearchParams();
  const id = searchParams.get('id');
  const investorName = searchParams.get('name');

  const colDefs: ColDef[] = [
    { headerName: 'Id', field: 'id' },
    { headerName: 'Asset Class', field: 'asset_class_name' },
    { headerName: 'Currency', field: 'currency' },
    { headerName: 'Amount', field: 'amount', valueFormatter: (params: any) => formatNumber(params.value) }
    ];

    const [rowData, setRowData]: [any, any] = React.useState(null);
    const [assetTypes, setAssetTypes] = React.useState([]);
    const [selectedAssetType, setSelectedAssetType] = React.useState('');
    const [rowSum, setRowSum] = React.useState('');


    React.useEffect(() => {
        if (!id) return;
        const fetchData = async () => {
            try {
                const data = await fetchCommitmentsDataForInvestor(Number(id));
                setRowData(data);
                const uniqueAssetTypes: any = Array.from(new Set(data.map((item: any) => item.asset_class_name)));
                setAssetTypes(uniqueAssetTypes);
            } catch (error) {
                console.error('Error:', error);
            }
        };

        fetchData();
    }, [id]);

    const handleAssetTypeChange = (event: any) => {
        setSelectedAssetType(event.target.value);
        setRowSum(getRowSum());
    };

    const filteredRowData = selectedAssetType && rowData
        ? rowData.filter((item: any) => item.asset_class_name === selectedAssetType)
        : rowData || [];

    const getRowSum = (): any => filteredRowData.reduce((acc: any, item: any) => ({ asset_class_name: "Total", currency: "GBP", amount: acc.amount + Number(item.amount) }), { asset_class_name: "Total", currency: "GBP", amount: 0});


    return (
        <div style={{ width: '100%', height: '100vh' }}>
            {/* Header */}
            <div style={{ width: '100%', height: '5vh', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <h1>Commitments</h1>
            </div>

            {/* Sub-Header */}
            <div style={{ width: '100%', height: '20px', display: 'flex', alignItems: 'left', justifyContent: 'space-between' }}>
                <span> Investor: <b>{ investorName }</b></span>
                <select id="assetTypeFilter" value={selectedAssetType} onChange={handleAssetTypeChange}>
                    <option value="">All</option>
                        {assetTypes.map((assetType, index) => (
                            <option key={index} value={assetType}>{assetType}</option>
                        ))}
                </select>
            </div>

            {/* ag-Grid */}
            <div className="ag-theme-alpine" style={{ flexGrow: 1, width:'100%', height:'600px', margin: '3em 0 0 0' }}>
                <AgGridReact
                    columnDefs={colDefs}
                    rowData={filteredRowData}
                    pinnedBottomRowData={[getRowSum()]}
                />
            </div>
        </div>
    );
};

export default Commitments;