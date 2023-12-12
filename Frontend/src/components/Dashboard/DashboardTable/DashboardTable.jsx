import React, { useState } from "react";
import { useDispatch } from "react-redux";
import "./DashboardTable.scss";
import { FaCircleDot } from "react-icons/fa6";
import useAxios from "../../../utils/useAxios";

const DashboardTable = (props) => {
  const api = useAxios();
  const dispatch = useDispatch();
  const listCampaigns = props.listCampaigns;
  const startTime = props.startTime;
  const endTime = props.endTime;
  const keyWord = props.keyWord;
  const pageNumber = props.pageNumber;

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
          {listCampaigns &&
            listCampaigns.map((campaign, index = campaign.campaign_id) => {
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
