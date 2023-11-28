import { React, useEffect, useState } from "react";
import NavBar from '../../components/Navbar/Navbar';
import Banner from '../../components/Banner/Banner';
import SideBar from '../../components/SideBar/SideBar';
import './HomePage.scss';
import { useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import { OPEN_CAMPAIGN, OPEN_ACCOUNT, OPEN_DASHBOARD } from '../../containers/menuContainer';
import Account from "../../components/Account/Account";


const HomePage = () => {
    const navigate = useNavigate();
    const [openMenu, setOpenMenu] = useState(OPEN_DASHBOARD);
    const [isOpenSideBar, setIsOpenSideBar] = useState(true);
    const isAuth = useSelector(state => state.isAuthenticated);
    useEffect(() => {
        function checkPermission() {
            if (!isAuth) {
                alert('Login before using, please!')
                navigate('/')
            }
        }
        checkPermission();
    }, [isAuth]);
    function openSideBar() {
        return setIsOpenSideBar(!isOpenSideBar);
    }

    function clickSideBar(changeValue) {
        return setOpenMenu(changeValue)
    }

    return (
        <div className='home-page'>
            <Banner />
            <NavBar openSideBar={openSideBar} />
            <div className='main-page'>
                <SideBar show={isOpenSideBar} clickSideBar={clickSideBar} />
                {openMenu === OPEN_ACCOUNT && <Account />}
            </div>
        </div>
    )
};

export default HomePage;

