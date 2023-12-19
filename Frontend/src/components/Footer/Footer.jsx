import React, {useEffect} from "react";
import './Footer.scss';

const Footer = ({range, setPage, page, slice}) => {
    useEffect(() => {
        if (slice.length < 1 && page !== 1) {
            setPage(page - 1);
        }
    }, [slice, page, setPage]);

    return (
        <div className='tableFooter'>
            {range.map((el) => (
                <button
                    key={el}
                    className={`${
                        page === el ? 'button activeButton' : 'button inactiveButton'
                    }`}
                    onClick={() => setPage(el)}
                >
                    {el}
                </button>
            ))}
        </div>
    );
};

export default Footer;