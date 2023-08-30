import React from "react";
import '../styles/base.scss'

const Base = (props) => {

    const { children } = props;

    return (
        <div className="container-fluid">
            <div className="row">
                <div className="col-6 mx-auto">
                    {children}
                </div>
            </div>
        </div>
    );
};

export default Base;
