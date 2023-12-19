import React from "react";
import { FaCircleDot } from "react-icons/fa6";

const DashboardTable = (props) => {
  const listCampaigns = props.listCampaigns;

  return (
    <div className="camp-table-data">
      <table>
        <thead>
          <tr>
            <th>Campaign Name</th>
            <th>Status</th>
            <th>Used Amount</th>
            <th>Usage Rate</th>
            <th>Budget</th>
            <th>Start date</th>
            <th>End date</th>
          </tr>
        </thead>
        <tbody>
          {
            listCampaigns?.map((campaign, index = campaign.campaign_id) => {
              return (
                <React.Fragment key={index}>
                  <tr>
                    <td>{campaign.name}</td>
                    <td>
                      <FaCircleDot
                        className="fa-duotone"
                        icon="fa-duotone fa-circle"
                        style={{
                          color: campaign.status === true ? "green" : "red",
                        }}
                      />
                    </td>
                    <td>{campaign.used_amount}</td>
                    <td>{campaign.usage_rate}</td>
                    <td>{campaign.budget}</td>
                    <td>{campaign.start_date}</td>
                    <td>{campaign.end_date}</td>
                  </tr>
                </React.Fragment>
              );
            })}
        </tbody>
      </table>
    </div>
  );
};

export default DashboardTable;
