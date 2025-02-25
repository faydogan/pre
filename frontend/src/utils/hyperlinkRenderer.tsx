import React from 'react';
import { useNavigate } from 'react-router-dom';
import { formatNumber } from './amountFormatter';

// Define the props for the custom cell renderer
interface InternalLinkCellRendererProps {
  value: any; // The cell value
  data: any; // The row data
}

const InternalLinkCellRenderer: React.FC<InternalLinkCellRendererProps> = (props) => {
  const { value, data } = props;
  const navigate = useNavigate();

  // Handle click event
  const handleClick = () => {
    navigate(`/details?id=${data.id}&name=${data.name}`);
  };

  return (
    <span style={{ color: 'blue', textDecoration: 'underline', cursor: 'pointer' }} onClick={handleClick}>
      {formatNumber(value)}
    </span>
  );
};

export default InternalLinkCellRenderer;