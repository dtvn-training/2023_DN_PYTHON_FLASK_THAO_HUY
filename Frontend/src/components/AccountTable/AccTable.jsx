import React, { useState } from "react";
import './AccTable.scss';
import useTable from "../../store/useTable";
import Footer from "../Footer/Footer";
import { AiFillEdit, AiFillDelete } from "react-icons/ai";
import AccPopup from "../AccountPopup/AccPopup";
import AccUpdatePopup from "../AccountPopup/AccUpdatePopup";

const AccTable = (props) => {
    const [selectedRecord, setSelectedRecord] = useState(null);
    const handleEditClick = (record) => {
        setSelectedRecord(record);
    }
    const handleFormClose = () => {
        setSelectedRecord(null);
    }
    const [isOpenPopup, setOpenPopup] = useState(false);

    const changePopup = () => {
        setOpenPopup(!isOpenPopup);
    }

    const rowsPerPage = 10;
    const [page, setPage] = useState(1);
    const { pageData: slice, pages: range } = useTable(props.data, page, rowsPerPage);

    function renderTable() {
        return (
            slice.map((val, key) => {
                return (
                    <tr key={key}>
                        <td>{val.id}</td>
                        <td>{`${val.last_name} ${val.first_name}`}</td>
                        <td>{val.email}</td>
                        <td>{val.address}</td>
                        <td>{val.phone}</td>
                        <td>{val.role ? 'Admin' : 'DAC'}</td>
                        <td>
                            <AiFillEdit className='edit-btn' onClick={() => handleEditClick(val)} />
                            <AiFillDelete className='del-btn' />
                        </td>
                    </tr>
                );
            })
        )
    }

    return (
        <div className="acc-table-data">
            <table>
                <tr>
                    <th>ID</th>
                    <th>User Name</th>
                    <th>Email</th>
                    <th>Address</th>
                    <th>Phone</th>
                    <th>Role</th>
                    <th>Actions</th>
                </tr>
                {props.data && renderTable(props.data)}
            </table>
            <Footer range={range} slice={slice} setPage={setPage} page={page} />
            {isOpenPopup && <AccPopup changePopup={changePopup} />}
            {selectedRecord && <AccUpdatePopup record={selectedRecord} onClose={handleFormClose} />}
        </div>
    )
}

export default AccTable;
