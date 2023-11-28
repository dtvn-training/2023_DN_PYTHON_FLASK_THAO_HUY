import  './SideBar.scss';
import { OPEN_ACCOUNT, OPEN_CAMPAIGN,OPEN_DASHBOARD } from '../../containers/menuContainer';
import React from "react";
import { RiFundsLine } from 'react-icons/ri';
const logo = require('../../assest/user.png');


const SideBar = (props) =>{
    function clickChange(value) {
        props.clickSideBar(value)
    }

    return (
        <div className={`${'side-bar'} 
            ${props.show ? '' : 'hidden'
        }`}>
            <item className= 'user-info'>
                <div className='logo-user'>
                    <img src={logo}/>
                </div>
                <div className={'name-user'}>
                    <text>User name</text>
                </div>
            </item>
            <item className = 'item-side' onClick = {() => clickChange(OPEN_DASHBOARD)}>
                <RiFundsLine className='icon-side-bar'/>
                Dashboard
            </item>
            <item className = 'item-side' onClick = {() => clickChange(OPEN_CAMPAIGN)}>
                <RiFundsLine className='icon-side-bar'/>
                Campaign
            </item>
            <item className = 'item-side' onClick = {() => clickChange(OPEN_ACCOUNT)}>
                <RiFundsLine className='icon-side-bar'/>
                Account
            </item>
        </div>
    )
}

export default SideBar;
