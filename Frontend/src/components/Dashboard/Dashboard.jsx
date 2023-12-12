import React, { useRef, useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import Pagination from "react-pagination-library";
import "react-pagination-library/build/css/index.css";
import "./Dashboard.scss";
import moment from "moment";
import DashboardTable from "./DashboardTable/DashboardTable";
import { fetchListCampaignAction } from "../../store/actions/campaignActions";
import useAxios from "../../utils/useAxios";

const Dashboard = (props) => {
  const typingTimeoutRef = useRef(null);
  const [startTime, setStartTime] = useState("2023-01-01 23:59:59");
  const [endTime, setEndTime] = useState("2023-12-12 23:59:59");
  const [pageNumber, setPageNumber] = useState(1);
  const [keyWord, setkeyWord] = useState("ALL");
  const api = useAxios();
  const dispatch = useDispatch();
  const listCampaigns = useSelector((state) => state.campaign.listCampaigns);
  const totalRecords = useSelector((state) => state.campaign.totalRecords);
  const pageCount = Math.ceil(totalRecords / 3);

  const handlePageClick = (event) => {
    setPageNumber(event);
  };
  const handleChangeSearchByKeyWord = (e) => {
    const value = e.target.value;
    if (typingTimeoutRef.current) {
      clearTimeout(typingTimeoutRef.current);
    }
    typingTimeoutRef.current = setTimeout(() => {
      setkeyWord(value);
    }, 600);
  };

  function handleStartTimeChange(event) {
    const selectedStartTime = event.target.value;
    if (moment(selectedStartTime).isAfter(endTime)) {
      return;
    }
    setStartTime(moment(selectedStartTime).format("YYYY-MM-DD HH:mm:ss"));
  }

  function handleEndTimeChange(event) {
    const selectedEndTime = event.target.value;
    const minDateTime = moment(startTime)
      .add(1, "days")
      .format("YYYY-MM-DD HH:mm:ss");
    if (moment(selectedEndTime).isBefore(minDateTime)) {
      return;
    }
    if (moment(selectedEndTime).isBefore(startTime)) {
      return;
    }
    setEndTime(moment(selectedEndTime).format("YYYY-MM-DD HH:mm:ss"));
  }

  useEffect(() => {
    dispatch(
      fetchListCampaignAction(
        {
          key_word: keyWord,
          page_number: pageNumber,
          start_time: startTime,
          end_time: endTime,
        },
        api
      )
    );
  }, [pageNumber, keyWord, startTime, endTime]);

  const handleChangeCurrentPage = () => {
    setPageNumber(1);
  };

  return (
    <div className="dash-grid">
      <div className="dash-filter-bar">
        <div className="dash-search-container">
          <input
            type="text"
            id="search-bar"
            onBlur={(e) => handleChangeSearchByKeyWord(e)}
            placeholder="Search"
          />
          <div className="dash-datetime">
            <div className="starttime-container">
              <label htmlFor="startDateTimePicker">Start Time:</label>
              <input
                type="datetime-local"
                id="startDateTimePicker"
                name="start_date"
                value={startTime}
                onChange={handleStartTimeChange}
              ></input>
            </div>
            <div className="endtime-container">
              <label htmlFor="endDateTimePicker">End Time:</label>
              <input
                className="endtime"
                type="datetime-local"
                id="endDateTimePicker"
                name="end_date"
                value={endTime}
                onChange={handleEndTimeChange}
              ></input>
            </div>
          </div>
        </div>
      </div>
      {listCampaigns && listCampaigns.length > 0 ? (
        <DashboardTable
          listCampaigns={listCampaigns}
          startTime={startTime}
          endTime={endTime}
          keyWord={keyWord}
          pageNumber={pageNumber}
          handleChangeCurrentPage={handleChangeCurrentPage}
        />
      ) : (
        <div className="camp-nodata-text">NO CAMPAIGN FOUND</div>
      )}
      {listCampaigns && totalRecords > 3 && (
        <Pagination
          // key={pageNumber}
          currentPage={pageNumber}
          totalPages={pageCount}
          changeCurrentPage={handlePageClick}
          theme="square-fill"
        />
      )}
    </div>
  );
};

export default Dashboard;
