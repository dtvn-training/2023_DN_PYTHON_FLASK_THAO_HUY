import React, { useRef, useState, useEffect } from "react";
import AccTable from "../AccountTable/AccTable";
import AccPopup from "../AccountPopup/AccPopup";
import './Account.scss';
import AccountServices from "../../services/AccountServices";
import { useSelector } from "react-redux";
import { CSVLink } from 'react-csv';

const Account = () => {
    const searchRef = useRef();
    const [data, setData] = useState([]);
    const [dataSearch, setDataSearch] = useState({ 'search': null });
    const [isOpenPopup, setOpenPopup] = useState(false);
    const [isReload, setReload] = useState(true);

    useEffect(() => {
        function searchData() {
            AccountServices.searchAccount(dataSearch).then((res) => {
                if (res.data.result === 'success') {
                    setData(res.data.data);
                }
            })
        }
        searchData();
    }, [isReload])

    function changePopup() {
        setOpenPopup(!isOpenPopup);
        setReload(!isReload);
    }

    function handleSearch() {
        let search = searchRef.current.value;
        setDataSearch({ 'search': search });
        setReload(!isReload);
    }

    return (
        <div className='account'>
            <div className='acc-filter-bar'>
                <div className='acc-search-container'>
                    <input type='text' id='search-bar' onBlur={handleSearch} ref={searchRef} placeholder='Search' />
                </div>
                <div className='acc-func-btn'>
                    <CSVLink className={'acc-export-btn'} data={data}>Export CSV</CSVLink>
                    <button onClick={changePopup}>Create Account</button>
                </div>
            </div>
            {data && <AccTable data={data} />}
            {!data && <div className='acc-nodata-text'>NO DATA</div>}
            {isOpenPopup && <AccPopup changePopup={changePopup} />}
        </div>
    )
}

export default Account;
