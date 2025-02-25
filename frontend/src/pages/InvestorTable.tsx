import React from 'react';
import { AgGridReact } from 'ag-grid-react';
import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-alpine.css';
import { ColDef } from 'ag-grid-community';
import { AllCommunityModule, ModuleRegistry, provideGlobalGridOptions } from 'ag-grid-community';
import { fetchCombinedInvestorData } from '../services/BackendService';

import InternalLinkCellRenderer from '../utils/hyperlinkRenderer';


ModuleRegistry.registerModules([AllCommunityModule]);
provideGlobalGridOptions({ theme: "legacy" });

const InvestorTable: React.FC = () => {

    const colDefs: ColDef[] = [
        { headerName: 'Id', field: 'id' },
        { headerName: 'Investor Name', field: 'name' },
        { headerName: 'Investor Type', field: 'investor_type' },
        { headerName: 'Investor Country', field: 'country' },
        { headerName: 'Total Commitments', field: 'total', cellRenderer: InternalLinkCellRenderer},
    ];

    const [rowData, setRowData] = React.useState(null);

    React.useEffect(() => {
        const fetchData = async () => {
            try {
                const data = await fetchCombinedInvestorData();
                setRowData(data);
            } catch (error) {
                console.error('Error:', error);
            }
        };

        fetchData();
    }, []);

    return (
    <div style={{ width: '100%', height: '100vh' }}>
        {/* Header */}
        <div style={{ width: '100%', height: '5vh', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <h1>Investors</h1>
        </div>

        {/* ag-Grid */}
        <div className="ag-theme-alpine" style={{ height: 400, width: '100%', margin: '3em 0 0 0' }}>
            <AgGridReact
                columnDefs={colDefs}
                rowData={rowData}
            />
        </div>
    </div>
    );
};

export default InvestorTable;